# Function to extract binary data from an image
from PIL import Image
def decode_image(image_path):
    img = Image.open(image_path)
    
    # Convert image to RGBA (in case it's in another format)
    img = img.convert("RGBA")
    
    img_data = img.getdata()
    binary_secret_text = ""
    
    # Iterate through each pixel
    for pixel in img_data:
        r, g, b, a = pixel  # Handle RGBA (Red, Green, Blue, Alpha)
        
        # Extract the LSB of each color channel
        binary_secret_text += format(r, '08b')[-1]  # LSB from red pixel
        binary_secret_text += format(g, '08b')[-1]  # LSB from green pixel
        binary_secret_text += format(b, '08b')[-1]  # LSB from blue pixel
        binary_secret_text += format(a, '08b')[-1]  # LSB from alpha pixel
    
    # Find the delimiter to determine the end of the secret message
    delimiter = '1111111111111110'  # The delimiter you added during encoding
    binary_secret_text = binary_secret_text[:binary_secret_text.find(delimiter)]

    # Convert binary data to text
    secret_text = ''.join(chr(int(binary_secret_text[i:i+8], 2)) for i in range(0, len(binary_secret_text), 8))
    return secret_text

# Example usage
decoded_message = decode_image('output_image.png')
print(f"Decoded Message: {decoded_message}")
