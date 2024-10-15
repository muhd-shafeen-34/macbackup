def linescount(s):
    try:
        with open(s,'r') as txt:
            contents = txt.read()
            lines = contents.count('\n')
            If lines == 0:
                print("number of lines: 1")
            else:
                print("number of lines: ",lines)
    except FileNotFoundError:
        print("file not found!")
    except Exception as e:
        print(f"An error occured:{e}")
file = input("enter file name: ")
linescount(file)

