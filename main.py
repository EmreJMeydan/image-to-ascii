from PIL import Image

#general variables
tall_char_correction = 0.5
out_width = 120
chars = "$@%&#*+=-:. "
max_brightness = 255
gamma = 1.5

# current testing image
img = Image.open("test.jpg")

# turn image to greyscale + save greyscale image for further work
gray = img.convert("L")
gray.save("gray.jpg")

# width + height variables collected from iamge size
in_width, in_height = img.size

# resized values for screen fitted output for the converter
out_height = int(in_height / in_width * out_width * tall_char_correction)
small = gray.resize((out_width, out_height), Image.Resampling.LANCZOS)

# centre coordinates
width_centre = out_width // 2
height_centre = out_height // 2

# brightness variable
#brightness = small.getpixel((width_centre, height_centre))

# single pixel index
#index = int((brightness / max_brightness) * (len(chars) - 1)) 

# the main loop
for y in range(out_height):
    row = ""
    for x in range(out_width):
        brightness = small.getpixel((x,y))
        index = int((brightness / max_brightness) ** gamma * (len(chars) - 1))
        row += chars[index]
    print(row)

# debug tests
#print(small.size)
#print(brightness)
#print(index)
#print(chars[index])




