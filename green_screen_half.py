from PIL import Image
cat_image = Image.open("cat_small.jpg")
cat_pixels = cat_image.load()
earth_image = Image.open("earth.jpg")
earth_w, earth_h = earth_image.size
earth_pixels = earth_image.load()
earth_image.show() # shows before changes
r, g, b = cat_pixels[100, 100]
print(f'RGB at 100, 100: {r}, {g}, {b}')
earth_pixels[100, 100] = cat_pixels[100, 100]
r, g, b = cat_pixels[200, 200]
print(f'RGB at 200, 200: {r}, {g}, {b}')
earth_pixels[200, 200] = cat_pixels[200, 200]
r, g, b = cat_pixels[300, 300]
print(f'RGB at 300, 300: {r}, {g}, {b}')
earth_pixels[300, 300] = cat_pixels[300, 300]
r, g, b = cat_pixels[400, 400]
print(f'RGB at 400, 400: {r}, {g}, {b}')
earth_pixels[400, 400] = cat_pixels[400, 400]
r, g, b = cat_pixels[500, 500]
print(f'RGB at 500, 500: {r}, {g}, {b}')
earth_pixels[500, 500] = cat_pixels[500, 500]
earth_image.show() # also shows  after changes. 
# It shows twice per the requirements, not because I don't know that it shows twice. 
# Also why is this program longer than changing the whole image...?