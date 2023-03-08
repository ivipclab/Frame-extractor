# Code for "TSM: Temporal Shift Module for Efficient Video Understanding"
# arXiv:1811.08383
# Ji Lin*, Chuang Gan, Song Han
# {jilin, songhan}@mit.edu, ganchuang@csail.mit.edu

import argparse
parser = argparse.ArgumentParser(description="Frame extractor")
parser.add_argument('--VIDEO_ROOT', type=str)
parser.add_argument('--FRAME_ROOT', type=str)
parser.add_argument('--NUM_THREADS', type=int)