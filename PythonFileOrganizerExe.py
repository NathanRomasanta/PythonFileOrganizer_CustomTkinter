#python script that organizes folder contents into different subfolders, executable file
import os
import shutil
from pathlib import Path

from customtkinter import *
app = CTk()


def sortFiles(path):

    print(path)
    #creation of the folders
    os.mkdir(os.path.join(path, "Texts"))
    os.mkdir(os.path.join(path, "Videos"))
    os.mkdir(os.path.join(path, "Music"))
    os.mkdir(os.path.join(path, "SourceFiles"))
    os.mkdir(os.path.join(path, "Documents"))
    os.mkdir(os.path.join(path, "Images"))
    os.mkdir(os.path.join(path, "Others"))
    os.mkdir(os.path.join(path, "Texts & Scripts"))
    
    #sorting function
    for filename in os.listdir(path):

                f = os.path.join(path, filename)
                print(filename)
                new_path = ""
                # checking if it is a file
                if os.path.isfile(f):
                    try: 
                        if f.endswith('.mp3') or f.endswith(".wma") or f.endswith(".wav") or f.endswith(".aac"):
                            new_path =str(path) + '/Music/'

                            shutil.move(f, new_path)

                        elif f.endswith(".ai") or f.endswith(".psd") or f.endswith(".prproj") or f.endswith(".psb") or f.endswith(".xd") or f.endswith(".fig") or f.endswith(".sketch"):
                            new_path = str(path) + '/SourceFiles/' 

                            shutil.move(f, new_path)

                        elif f.endswith(".mp4") or f.endswith(".avi") or f.endswith(".mov") or f.endswith(".mkv"):
                            new_path = str(path) + '/Videos/' 

                            shutil.move(f, new_path)

                        elif f.endswith(".txt") or f.endswith(".sql") or f.endswith(".java") or f.endswith(".py") or f.endswith(".cpp") or f.endswith(".cs"):
                            new_path = str(path) + '/Texts & Scripts/' 

                            shutil.move(f, new_path)

                        elif f.endswith(".docx") or f.endswith(".pdf") or f.endswith(".ppt") or f.endswith(".xlsx")  or f.endswith(".doc") or f.endswith(".csv") or f.endswith(".xls"):
                            new_path = str(path) + '/Documents/' 

                            shutil.move(f, new_path)

                        elif f.endswith(".png") or f.endswith(".jpeg") or f.endswith(".webp") or f.endswith(".jpg")  or f.endswith(".gif"):
                            #needs to be typecasted otherwise will produce error
                            new_path = str(path) + '/Images/' 

                            shutil.move(f, new_path)

                        else:
                            new_path = str(path) + '/Others/' 
                            
                            shutil.move(f, new_path)


                    
                    except Exception as e:
                        print(f"Error: {e}")

    print("Files Organized!")
    x = input("")

def main():
    app = CTk()

    app.geometry("800x500")
    app.mainloop()

    title = CTkLabel(master=app, text="Python File Organizer", )
    title.place(relx=0.5, rely=0.5, anchor="center")


if __name__ == "__main__":
    main()