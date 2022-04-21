import os ;import shutil;import sys;
import re 

#------------------------------


def check_dir(Dir, path):
    while Dir not in map(lambda x: x.lower(), os.listdir(path)):
        Dir = input("unfound directory . please enter a valid one: ")
    return Dir


def go_to_directory():
    pDir = "C:\\"
    os.chdir(pDir)
    while True:
        os.system("cls");sys.stdout.flush()
        for dir in os.listdir(os.getcwd()):
            if os.path.isdir(dir):
                print("- ", dir)
        print()
        todir = input(f"PS  {pDir}") 
        if todir == "":
            if pDir == 'C:\\':
                print("quitted the program")
                quit()
            else:
                break
        else:
            if "\\" in todir:
                todir = todir.replace("\\", "", todir.count("\\"))
            pDir +=  check_dir(todir, pDir) + "\\" 
            os.chdir(pDir)

    return pDir


def renamed_same_file(file, nfile):
    file_list = re.split(pattern = r"[()]", string= file)
    if  nfile > 1:
        if len(file_list) > 1:
            file_name , file_ext = file_list[0], file_list[-1]
        else:
            file_name, file_ext = file.split(".")[0], "." + file.split(".")[-1]
        return file_name + (f'({nfile})') + file_ext
        
    return file

def move_file(file, pDir, folder):
    nfile = 1
    while  renamed_same_file(file, nfile) in os.listdir(pDir + "\\" + folder):
        nfile += 1
    else:
        os.rename(file, renamed_same_file(file, nfile))
        shutil.move(pDir + '\\' + renamed_same_file(file, nfile), pDir + "\\" + folder)
        print("Moving --- " + renamed_same_file(file, nfile))

def manage_files(pDir):
    os.chdir(pDir)
    for file in os.listdir():
        if os.path.isfile(file):
            folder = file.split(".")[-1].lower()
            if folder not in os.listdir():
                os.mkdir(folder)
    
            move_file(file, pDir, folder)

