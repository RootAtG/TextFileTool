import time #hello
import os
print()
print()

print("-----------------------------------------------------------------------------------------------")
print("[*] Welcome to the Text File Tool!")
print("[*] Providing easy ways to manage your text files in an easy to use console since July of 2019!")
print("-----------------------------------------------------------------------------------------------")
time.sleep(.5)
print("Enter help for a list of commands.")
print()
time.sleep(.5)

var = None
while var == None:
    tcon = input("tft > ")
    if tcon == "help":
        print()
        print("CONSOLE OPTIONS")
        time.sleep(.5)
        print("     -r --Read the file")
        time.sleep(.5)
        print("     -w --Write to the file")
        time.sleep(.5)
        print("     -c --Count number of lines in the file")
        time.sleep(.5)
        print("     -f --Find if a certain piece of text is in the file")
        time.sleep(.5)
        print("     -m --Make a new text file")
        time.sleep(.5)
        print("     -d --Delete a text file")
        time.sleep(.5)
        print("     help --Shows what you can do with the Text File Tool")
        time.sleep(.5)
        print("     quit --Quits the Text File Tool")
        print()
    elif tcon == "-r":
        print()
        fname = input("Enter the file name: ")
        try:
            fhand = open(fname, "r")
        except:
            print("This file does not exist")
            print()
            continue
        print(fhand.read())
        print()
    elif tcon == "-w":
        print()
        fname = input("Enter the file name: ")
        wi = input("Append or Overwrite?: ")
        wi = wi.lower()
        if "app" in wi:
            aw = input("What do you want to append?: ")
            try:
                fhand = open(fname, "a")
                fhand.write(aw)
                fhand.close()
            except:
                print("This file does not exist")
                print()
                continue
            print("File has been appended")
            print()
        elif "over" in wi:
            ow = input("What do you want to overwrite the file with?: ")
            try:
                fhand = open(fname, "w")
                fhand.write(ow)
                fhand.close()
            except:
                print("This file does not exist")
                print()
                continue
            print("File has been overwritten")
            print()
        else:
            print("Error")

    elif tcon == "-c":
        print()
        fname = input("Enter the file name: ")
        try:
            fhand = open(fname)
        except:
            print("This file does not exist")
            print()
            continue
        count = 0
        for line in fhand:
            count = count + 1
        print("There were " + count + " lines in the file.")
        print()

    elif tcon == "-f":
        print()
        fname = input("Enter the file name: ")
        try:
            fhand = open(fname)
        except:
            print("This file does not exist")
            print()
            continue
        find = input("What do you want to find? ")
        count = 0
        for line in fhand:
            if find in line:
                count = count + 1

        if count > 0:
            count = str(count)
            print(find + " appeared in the file " + count + " times.")
            print()
        else:
            print(find + " is not in the file")
            print()





    elif tcon == "-m":
        print()
        fc = input("Enter the filename you want to create: ")
        fhand = open(fc, "x")
        print("File has been created")
        print()
    elif tcon == "quit":
        print("See you soon!")
        print()
        quit()
    elif tcon == "-d":
        print()
        fc = input("Enter the filename you want to delete: ")
        if os.path.exists(fc):
          os.remove(fc)
          print("File has been deleted.")
          print()
        else:
          print("The file does not exist")
          print()
