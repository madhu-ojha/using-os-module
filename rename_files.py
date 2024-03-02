#importing os module
import os

def main():
    # In this case my_folder has my images in jpg format
    folder_name ="my_folder" 
    directories = os.listdir(folder_name)

    for count, filename in enumerate(directories):
        new_name = f"msojha {str(count)}.jpg"
        source = f"{folder_name}/{filename}"
        new_name = f"{folder_name}/{new_name}"

        # rename function of os module. renames all the files 
        os.rename(source, new_name)
        
if __name__ == '__main__':
    main()