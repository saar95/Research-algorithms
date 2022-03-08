import importlib

"""
The function gets the name of a Python file that contains a particular module and the name of an output file, 
creates an HTML file documenting the module - Doc,annotations and more.
"""


def get_doc(module_name, output_file):
    module = module_name[:-3]
    module = importlib.import_module(module)
    module_funcs = module.__dir__()[8:]
    with open(output_file, 'w') as file:
        file.write("<html>\n<head>\n<title>\n \
                    </title>\n</head> <body><h1>"
                   )
        file.write(str(module.__name__) + "\n")
        file.write("\n")
        file.write(str(module.__doc__) + "\n")
        file.write("\n")
        for func in module_funcs:
            file.write("function: "  + func+"\n")
            attr = getattr(module, func)
            module_documentation = attr.__doc__
            file.write("Documentation: "+str(module_documentation)+"\n")
            module_annotations = attr.__annotations__
            file.write("Annotations: " + str(module_annotations)+"\n")
            file.write("\n")
        file.write("</h1>\n \
                       </body></html>")


if __name__ == '__main__':
    get_doc("mymodule.py", "mydoc.html")
