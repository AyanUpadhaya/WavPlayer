# My custom module to create image object using PIL library easily


from PIL import Image, ImageTk

class Imageloader:
	"""
	loads image file by path with defined width and height
	makes creating image object in tkinter much easier.
	"""	
	def __init__(self):
		pass

	def loadImage(file, width, height):
	    image_file = Image.open(file)
	    image_file = image_file.resize((width, height), Image.ANTIALIAS)
	    image_data = ImageTk.PhotoImage(image_file)
	    return image_data

"""
Example

new_image = Imageloader.loadImage(path,width,height)
"""