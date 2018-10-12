import argparse

ap = argparse.ArgumentParser(description = "Perspective transform")
ap.add_argument("--image_path",required = True,help = "path of the image")
ap.add_argument("--save_image",required = True,help = "path of the result image")
args = vars(ap.parse_args())
print "Dictionary of all the arguments passed",args
