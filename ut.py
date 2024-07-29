from PIL import Image

# Open an image file
with Image.open('path/to/image.png') as img:
    img = img.convert("RGBA")
    data = img.getdata()
    
    new_data = []
    for item in data:
        # Change all opaque (alpha = 255) pixels to white
        if item[3] == 255:  # Check alpha channel
            new_data.append((255, 255, 255, 255))  # New color
        else:
            new_data.append(item)

    img.putdata(new_data)
    img.save('path/to/new_image.png')
