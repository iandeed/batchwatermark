# batchwatermark
Simple script to watermark a folder of images in batch from the command line

Usage: python batch_watermark.py --root [Path to images folder] --watermark [path to watermark image] 

-This will copy each image in the folder adding the watermark image specified over the center of the new copy.  Output image filenames will be appended with: "-watermark".

Additional usage: python batch_watermark.py --root [Path to images folder] --watermark [path to watermark image] --name [Preffered appendix for files, replaces "-watermark"]
							--extension [Image extensions to look out for]  --position [Preferred position of watermark EG. north, south, east, west, center, southeast, etc]
							--resize [Percentage image copy should be to original image i.e 50 - half size]  --exclude [path content to exclude from watermarking]

Example usage:
$ python dev/batchWatermark/batch_watermark.py --root /home/ian/Pictures/Sports/03/rugbyimages/Converted/ --watermark /home/ian/Pictures/Sports/myWatermark.png -name rugbygame --extension .jpg --position south --resize 50

- This will produce a half size copy of all jpg files in the folder with a watermark on the bottom edge and '-rugbygame' appended to the filename ie IMG_2098.jpg  will become: IMG_2098-rugbygame.jpg and the watermark file will be over the image.

Transparency will be maintained after the conversion.