import sys;
import os;
def replace_string_in_directory_files(directoryPath, oldString, newString):
    for root,dirs,files in os.walk(directoryPath):
        for file in files:
            print()
            file_path=os.path.join(root,file)
            replace_string_in_file(file_path,oldString,newString)

def replace_string_in_file(filePath, oldString,newString):
    with open(filePath, 'r') as fileReader:
        data= fileReader.read()
    
    if(oldString in data):
        data= data.replace(oldString,newString)
        with open(filePath, 'w') as fileWriter:
            fileWriter.write(data)
        print(filePath + " has been replaced")
  
if(__name__ == '__main__'):
    directoryPath=sys.argv[1]
    oldString=sys.argv[2]
    newString=sys.argv[3]
    replace_string_in_directory_files(directoryPath,oldString,newString)
