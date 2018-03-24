#!/usr/bin/env python
# encoding: utf-8

import os
import argparse
import time

def main():
    parser = argparse.ArgumentParser(description='Add watermarks to images in path')
    parser.add_argument('--root', help='Root path for images', required=True, type=str)
    parser.add_argument('--watermark', help='Path to watermark image', required=True, type=str)
    parser.add_argument('--name', help='Name addition for watermark', default="-watermark", type=str)
    parser.add_argument('--extension', help='Image extensions to look for', default=".jpg", type=str)
    parser.add_argument('--position', help='Cardinal position to place the watermark', default="center", type=str)
    parser.add_argument('--resize', help='Percentage by which to resize the image', default="100", type str)
    parser.add_argument('--exclude', help='Path content to exclude', type=str)

    args = parser.parse_args()

    files_processed = 0
    files_watermarked = 0
    start_time = time.time()
    for dirName, subdirList, fileList in os.walk(args.root):
        if args.exclude is not None and args.exclude in dirName:
            continue
        #print('Walking directory: %s' % dirName)
        for fname in fileList:
            files_processed += 1
            #print('  Processing %s' % os.path.join(dirName, fname))
            if args.extension in fname and args.watermark not in fname and args.name not in fname:
                ext = '.'.join(os.path.basename(fname).split('.')[1:])
                orig = os.path.join(dirName, fname)
                new_name = os.path.join(dirName, '%s.%s' % (os.path.basename(fname).split('.')[0] + args.name, ext))
                if not os.path.exists(new_name):
                    files_watermarked += 1
                    print('    Convert %s to %s' % (orig, new_name))
                    os.system('composite -dissolve 70%% -gravity %s %s "%s" "%s"' % (args.position, args.watermark, orig, new_name))
                    if args.resize < 100:
                        #Scale down the image
                        os.system('convert -resize %s%% %s %s', args.resize, new_name, new_name)

    print("Files Processed: %s" % "{:,}".format(files_processed))
    print("Files Watermarked: %s" % "{:,}".format(files_watermarked))
    elapsed_time = time.Time() - start_time
    print("Time taken: %s", elapsed_time)

if __name__ == '__main__':
    main()