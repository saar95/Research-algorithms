import requests
import sqlite3
import xmltodict



def cursor_print(cursor):
    cursor.execute(''' 
        SELECT * FROM KNS_Committee
        ''')
    for c in cursor:
        print(c)
    cursor.execute("DROP TABLE KNS_Committee")

def help_function(val):
    if type(val) is str:
        return val
    else:
        try:
            val['@m:null']
        except:
            val = val['#text']
            if val == '@null':
                return None
            else:
                return val


if __name__ == '__main__':
    final_committee = []
    committee = []
    locations_list = ['d:CommitteeID', 'd:Name', 'd:CategoryID', 'd:CategoryDesc', 'd:KnessetNum', 'd:CommitteeTypeID',
                      'd:CommitteeTypeDesc', 'd:Email', 'd:StartDate', 'd:FinishDate', 'd:AdditionalTypeID',
                      'd:AdditionalTypeDesc', 'd:ParentCommitteeID', 'd:CommitteeParentName',
                      'd:IsCurrent', 'd:LastUpdatedDate']

    response = requests.get('https://knesset.gov.il/Odata/ParliamentInfo.svc/KNS_Committee()')
    xml_response = xmltodict.parse(response.content)
    db = sqlite3.connect('my_database.db')
    cursor = db.cursor()

    for values in xml_response['feed']['entry']:
        content_properties = values['content']['m:properties']

        CommitteeID = help_function(content_properties[locations_list[0]])
        Name = help_function(content_properties[locations_list[1]])
        CategoryID = help_function(content_properties[locations_list[2]])
        CategoryDesc = help_function(content_properties[locations_list[3]])
        KnessetNum = help_function(content_properties[locations_list[4]])
        CommitteeTypeID = help_function(content_properties[locations_list[5]])
        CommitteeTypeDesc = help_function(content_properties[locations_list[6]])
        Email = help_function(content_properties[locations_list[7]])
        StartDate = help_function(content_properties[locations_list[8]])
        FinishDate = help_function(content_properties[locations_list[9]])
        AdditionalTypeID = help_function(content_properties[locations_list[10]])
        AdditionalTypeDesc = help_function(content_properties[locations_list[11]])
        ParentCommitteeID = help_function(content_properties[locations_list[12]])
        CommitteeParentName = help_function(content_properties[locations_list[13]])
        IsCurrent = help_function(content_properties[locations_list[14]])
        LastUpdatedDate = help_function(content_properties[locations_list[15]])

        committee = [CommitteeID, Name, CategoryID, CategoryDesc, KnessetNum, CommitteeTypeID, CommitteeTypeDesc,
                     Email, StartDate, FinishDate, AdditionalTypeID, AdditionalTypeDesc, ParentCommitteeID,
                     CommitteeParentName, IsCurrent, LastUpdatedDate]

        final_committee.append(committee)
        committee = []


    cursor.execute(''' CREATE TABLE KNS_Committee(
                CommitteeID INTEGER PRIMARY KEY, Name VARCHAR(250), CategoryID INTEGER, CategoryDesc VARCHAR(150),
                KnessetNum INTEGER, CommitteeTypeID INTEGER, CommitteeTypeDesc VARCHAR(125), Email VARCHAR(254),
                StartDate DATETIME2, FinishDate DATETIME2, AdditionalTypeID INTEGER, AdditionalTypeDesc VARCHAR(125), 
                ParentCommitteeID INTEGER, CommitteeParentName VARCHAR(250), IsCurrent BIT, LastUpdatedDate DATETIME2)
                ''')

    cursor.executemany(''' INSERT INTO KNS_Committee(
    CommitteeID, Name, CategoryID, CategoryDesc, KnessetNum, CommitteeTypeID,
    CommitteeTypeDesc, Email, StartDate, FinishDate, AdditionalTypeID, AdditionalTypeDesc, 
    ParentCommitteeID, CommitteeParentName, IsCurrent, LastUpdatedDate)
    VALUES(
            ?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''', final_committee)
    db.commit()

    cursor_print(cursor)