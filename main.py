from PIL import Image

#general variables
tall_char_correction = 0.5
out_width = 60
chars = "@%#*+=-:. "

# current testing image
img = Image.open("test.jpg")

# turn image to greyscale + save greyscale image for further work
gray = img.convert("L")
gray.save("gray.jpg")

# width + height variables collected from iamge size
in_width, in_height = img.size

# resized values for screen fitted output for the converter
out_height = int(in_height / in_width * out_width * tall_char_correction)
small = gray.resize((out_width, out_height))

# debug tests
print(small.getpixel((out_width // 2, out_height // 2)))
print(small.size)



