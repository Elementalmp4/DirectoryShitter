from os import walk

supportedFileTypes = ["js", "html", "css", "xml", "java", "py", "json", "gd"]
files = []

open("output.txt", "w").close()
output = open("output.txt", "a")

path = input("Enter a path to be directory shitted: ")

def traverse(path):
    for (dirpath, dirnames, filenames) in walk(path):
        for filename in filenames:
            files.append(dirpath + "\\" + filename)
        if dirnames is not []:
            for directory in dirnames:
                traverse(directory)

traverse(path)

print("Found " + str(len(files)) + " files")

for file in files:
    fileExtension = file.split(".")[1]
    fileName = file.split("\\")[-1]
    if (fileExtension in supportedFileTypes):
        print("Loading file of type " + fileExtension + " - " + file)
        content = ""
        with open(file, "r") as textFile:
            content = textFile.read()
            lines = content.split("\n")
            textFile.close()
            output.write("# # # # # " + fileName + " # # # # # \n\n")
            count = 1
            for line in lines:
                output.write(str(count) + ". " + line + "\n")
                count += 1
            output.write("\n\n")
        
    else:
        print("Ignoring file of type " + fileExtension + " - " + file)

print("Completed. Shitted " + str(len(files)) + " files")