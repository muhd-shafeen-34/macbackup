def captfile(s):
    try:
        with open(s,'r') as txt: 
            contents = txt.read().upper()
        with open(s,'w') as t:
            t.write(contents)
            print("capitalised successfully!\n")
            print(contents)
    except FileNotFoundError:
        print("file not found!")
    except Exception as e:
        print(f"An error occured:{e}")
file = input("enter file name: ")
captfile(file)
        
