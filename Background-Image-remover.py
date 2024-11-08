# Background remover in Python
from rembg import remove
from PIL import Image

input_path = input("Enter the input image path (e.g., 'pic.jpeg'): ")
output_path = input("Enter the output image path (e.g., 'pic.png'): ")

with open(input_path, 'rb') as f:
    input_data = f.read()


output_data = remove(input_data)

with open(output_path, 'wb') as out_f:
    out_f.write(output_data)

# Open and display the output image
output_img = Image.open(output_path)
output_img.show()

print(f"Background removed and saved as {output_path}")