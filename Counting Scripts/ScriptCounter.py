#! usr/bin/env Python3
import sys;
import os;

def get_number_of_interpeter_in_dir(directoryPath):
    scripts={}
    shebangExtensions={".py",".sh",".pl",".rb",".php"}
    for root,dirs,files in os.walk(directoryPath):
        for file in files:
            filename,extension= os.path.splitext(file)
            if (extension in shebangExtensions):
                with open(os.path.join(root,file), 'r') as readingFile:
                    interpreter= readingFile.readline()
                    if(interpreter.startswith('#!')):
                        if(interpreter not in scripts):
                                scripts[interpreter] = 0
                        scripts[interpreter] +=1
    return scripts

def set_to_report_file(data):
     with open(reportPath+'\data_report.txt','w') as file:
        file.write(data)

if(__name__ == "__main__"):
    directoryPath= sys.argv[1]
    reportPath=""
    if(sys.argv[2]):
        reportPath=sys.argv[2]

    scripts= get_number_of_interpeter_in_dir(directoryPath)
    data=""
    if(len(scripts)> 0):
        for name,count in scripts.items():
            tupleToString=f"{count} {name}\n"
            data.join(tupleToString)
            print(tupleToString)
        set_to_report_file(data)
    else:
        print("There are no files in this directory with the shebang interpreter")
    
    


                        
                

