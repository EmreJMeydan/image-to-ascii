from PIL import Image

# current testing image
img = Image.open("test.jpg")

# turn image to greyscale + save greyscale image for further work
gray = img.convert("L")
gray.save("gray.jpg")

# width + height variables collected from iamge size
in_width, in_height = img.size

# resized values for screen fitted output for the converter
out_width = 60
out_height = in_height / in_width

