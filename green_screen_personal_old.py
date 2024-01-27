from PIL import Image
cat_image = Image.open("C:/Users/tman/VS Code Projects/CSE110/example_images/cat_small.jpg")
cat_pixels = cat_image.load()
earth_image = Image.open("C:/Users/tman/VS Code Projects/CSE110/example_images/earth.jpg")
earth_w, earth_h = earth_image.size
earth_pixels = earth_image.load()
for row in range(earth_h):
     for col in range(earth_w):
          cat_pix_r = cat_pixels[col, row][0]
          cat_pix_g = cat_pixels[col, row][1]
          cat_pix_b = cat_pixels[col, row][2]
          if cat_pix_g < 192:
               earth_pixels[col, row] = cat_pixels[col, row]
earth_image.save("C:/Users/tman/VS Code Projects/CSE110/example_images/earth_and_cat_small.jpg")