#script to test all the modules in the package

#from docsnac import DocType, DocChange, DocSearch



with open('something.txt', 'r') as input_file:
    for word in input_file.read().split(" "):
        print(word)
