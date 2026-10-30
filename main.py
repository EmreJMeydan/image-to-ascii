from PIL import Image

#general variables
tall_char_correction = 0.5
out_width = 120
chars = " .:-=+*#%@"
max_brightness = 255
gamma = 0.7

# current testing image
img = Image.open("test.jpg")

# rgb split
r, g, b = img.split()
r.save("r.png")

# width + height variables collected from iamge size
in_width, in_height = img.size

# resized values for screen fitted output for the converter
out_height = int(in_height / in_width * out_width * tall_char_correction)
small = r.resize((out_width, out_height), Image.Resampling.LANCZOS)

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




