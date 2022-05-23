def swapFileData():
    file1 = '/Users/Justice/Desktop/Python Projects/sample1.txt'
    file2 = '/Users/Justice/Desktop/Python Projects/sample2.txt'

    with open(file1,'r') as a:
        data_a = a.read()
    with open(file2,'r') as b:
        data_b = b.read()
    with open(file1,'w') as a:
        a.write(data_b)
    with open(file2,'w') as b:
        b.write(data_a)
swapFileData()