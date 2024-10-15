def replacefile(s,n,x):
    try:
        with open(s,'r') as txt: 
            contents = txt.read()
            print("before replace:\n",contents)
            if n in contents:
                contents = contents.replace(n,x)
        with open(s,'w') as t:
            t.write(contents)
            print("replaced successfully!\n")
            print("after replace:\n",contents)
    except FileNotFoundError:
        print("file not found!")
    except Exception as e:
        print(f"An error occured:{e}")
file = input("enter file name: ")
n = input("which word: ")
x = input("what word: ")
replacefile(file,n,x)
        
