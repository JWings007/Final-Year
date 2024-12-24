from PIL import Image
import binascii

# Function to convert text to binary
def text_to_bin(text):
    binary = ''.join(format(ord(i), '08b') for i in text)
    return binary

# Function to encode text into an image
def encode_image(image_path, secret_text, output_image_path):
    # Open the image
    img = Image.open(image_path)
    
    # Convert image to RGB (in case it's RGBA or any other format)
    img = img.convert("RGBA")
    
    # Convert secret message to binary and add delimiter
    binary_secret_text = text_to_bin(secret_text) + '1111111111111110'  # Add delimiter to indicate end of secret text
    binary_secret_len = len(binary_secret_text)
    
    img_data = img.getdata()
    new_img_data = []
    data_index = 0

    # Iterate through each pixel
    for pixel in img_data:
        r, g, b, a = pixel  # Handle RGBA (Red, Green, Blue, Alpha)
        
        # Modify each pixel's least significant bit to hide the secret data
        if data_index < binary_secret_len:
            r = int(format(r, '08b')[:-1] + binary_secret_text[data_index], 2)
            data_index += 1
        if data_index < binary_secret_len:
            g = int(format(g, '08b')[:-1] + binary_secret_text[data_index], 2)
            data_index += 1
        if data_index < binary_secret_len:
            b = int(format(b, '08b')[:-1] + binary_secret_text[data_index], 2)
            data_index += 1
        if data_index < binary_secret_len:
            a = int(format(a, '08b')[:-1] + binary_secret_text[data_index], 2)
            data_index += 1

        new_img_data.append((r, g, b, a))  # Keep alpha channel as is

        if data_index >= binary_secret_len:
            break

    # Save the modified image
    img.putdata(new_img_data)
    img.save(output_image_path)
    print(f"Encoded image saved as {output_image_path}")

# Example usage
encode_image('scarlet.png', 'I love kim jisoo', 'output_image.png')
