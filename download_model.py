#Download pretrained model

import os
import sys
import urllib2

def main(argv):
	OUTPUT_PATH="./pretrain/"
	if not os.path.isdir(OUTPUT_PATH):
		os.mkdir(OUTPUT_PATH)
	with open(OUTPUT_PATH+'yolov2_tiny-hand.h5','wb') as f:
		f.write(urllib2.urlopen("http://www.abars.biz/keras/yolov2_tiny-hand.h5").read())
		f.close()

if __name__=='__main__':
	main(sys.argv[1:])
