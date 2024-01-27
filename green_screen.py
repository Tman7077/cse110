from PIL import Image
fg_image = Image.open(input("Input the full foreground image filepath (e.g. C:/Users/user/...): "))
fg_pixels = fg_image.load()
bg_image = Image.open(input("Input the full background image filepath (e.g. C:/Users/user/...): "))
bg_w, bg_h = bg_image.size
bg_pixels = bg_image.load()
print("Would you like to paste the foreground on the background or blend the two? ")
inp = input('Input "paste" or "blend": ').lower()
if inp == "paste":
     for row in range(bg_h):
          for col in range(bg_w):
               if fg_pixels[col, row][1] < 192:
                    bg_pixels[col, row] = fg_pixels[col, row]
     bg_image.save("bg_and_fg_paste.jpg")
     bg_image.show()
elif inp == "blend":
     for row in range(bg_h):
          for col in range(bg_w):
               bg_pix_r = bg_pixels[col, row][0]
               bg_pix_g = bg_pixels[col, row][1]
               bg_pix_b = bg_pixels[col, row][2]
               fg_pix_r = fg_pixels[col, row][0]
               fg_pix_g = fg_pixels[col, row][1]
               fg_pix_b = fg_pixels[col, row][2]
               avg_r = round((bg_pix_r + fg_pix_r) / 2)
               avg_g = round((bg_pix_g + fg_pix_g) / 2)
               avg_b = round((bg_pix_b + fg_pix_b) / 2)
               bg_pixels[col, row] = (avg_r, avg_g, avg_b)
     bg_image.save("bg_and_fg_blend.jpg")
     bg_image.show()
else:
     print("That's not a valid answer.")