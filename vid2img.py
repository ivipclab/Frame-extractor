# Code for "TSM: Temporal Shift Module for Efficient Video Understanding"
# arXiv:1811.08383
# Ji Lin*, Chuang Gan, Song Han
# {jilin, songhan}@mit.edu, ganchuang@csail.mit.edu

import os
import threading
from opts import parser


def split_get(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n]


def extract(video, cato):
    cmd = 'ffmpeg -i \"{}/{}\" -threads 1 -vf scale=-1:256 -q:v 0 \"{}/{}/%06d.jpg\"'.format(os.path.join(VIDEO_ROOT,cato), video,
                                                                                             os.path.join(FRAME_ROOT,cato), video.replace(".mp4", ""))
    os.system(cmd)


def target(video_list,cato):
    for video in video_list:
        if not os.path.exists(os.path.join(os.path.join(FRAME_ROOT,cato), video.replace(".mp4", ""))):
            os.makedirs(os.path.join(os.path.join(FRAME_ROOT,cato), video.replace(".mp4", "")))
        extract(video,cato)

if __name__ == '__main__':
    args = parser.parse_args()
    VIDEO_ROOT = args.VIDEO_ROOT
    NUM_THREADS = args.NUM_THREADS
    FRAME_ROOT = args.FRAME_ROOT
    if not os.path.exists(VIDEO_ROOT):
        raise ValueError('Please download videos and set VIDEO_ROOT variable.')
    if not os.path.exists(FRAME_ROOT):
        os.makedirs(FRAME_ROOT)


    video_dir_list = os.listdir(VIDEO_ROOT)
    for cato in video_dir_list:
        video_this = os.path.join(VIDEO_ROOT,cato)

        video_list = os.listdir(video_this)
        temp = split_get(video_list, NUM_THREADS)
        splits = list(temp)



        threads = []
        for i, split in enumerate(splits):
            thread = threading.Thread(target=target, args=(split,cato,))
            thread.start()
            threads.append(thread)

        for thread in threads:
            thread.join()