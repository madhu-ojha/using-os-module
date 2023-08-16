import os
from PIL import Image

def resize_images(input_dir, output_dir, new_width, new_height):
    # Create the output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # List all files in the input directory
    files = os.listdir(input_dir)
    
    for file in files:
        # Check if the file is an image
        if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            try:
                # Open the image
                image_path = os.path.join(input_dir, file)
                img = Image.open(image_path)
                
                # Resize the image
                resized_img = img.resize((new_width, new_height))
                
                # Save the resized image to the output directory
                output_path = os.path.join(output_dir, file)
                resized_img.save(output_path)
                
                print(f"Resized {file} successfully.")
                
            except Exception as e:
                print(f"Error resizing {file}: {str(e)}")

# Specify input and output directories, as well as the new width and height
input_directory = "./"
output_directory = "./hello"
new_width = 800
new_height = 600

resize_images(input_directory, output_directory, new_width, new_height)
