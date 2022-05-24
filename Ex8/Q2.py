import gspread
import numpy as np


def extract_val(sheet):
    matrix = []
    for i in sheet:
        temp_l = []
        for j in i:
            temp_l.append(int(j))
        matrix.append(temp_l)
    return matrix


def multiply_matrices_algorithm(A,B):
    account = gspread.service_account("multiply-matrices-3c860f58740b.json")
    spreadsheet = account.open("Multiply matrices")
    a_matrix = spreadsheet.worksheet(A)
    b_matrix = spreadsheet.worksheet(B)
    A_val = a_matrix.get_all_values()
    B_val = b_matrix.get_all_values()
    matrix_A = np.array(extract_val(A_val))
    matrix_B = np.array(extract_val(B_val))
    result = np.dot(matrix_A, matrix_B)
    title = A+"_times_"+B
    spreadsheet.add_worksheet(title=title, rows=result.shape[0], cols=result.shape[1])
    result_matrix = spreadsheet.worksheet(title)
    last_cell = chr(ord('A') + (result.shape[1] - 1)) + str(result.shape[0])
    sheet_to_write = "A1:" + last_cell
    result_matrix.update(sheet_to_write, result.tolist())

if __name__ == '__main__':
    multiply_matrices_algorithm("A","B")
    multiply_matrices_algorithm("C","D")

