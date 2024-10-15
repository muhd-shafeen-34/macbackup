def copyfile(sourcefile,destfile):
    try:
        with open(sourcefile,'r') as src:
            contents = src.read()
        print("sourcefile contents: \n",contents)
        with open(destfile,'w') as dst:
            dst.write(contents)
            print("File copied successfully!")
        with open(destfile,'r') as drc:
            contents2 = drc.read()
        print("destinationfile contents: \n",contents2)
        
    except FileNotFoundError:
        print("Source file not found.")
    except Exception as e:
        print(f"An error occurred:{e}")

sourcefile = input("enter source file name:")
destfile = input("enter destination file name:")
copyfile(sourcefile,destfile)
