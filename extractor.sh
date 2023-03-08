VIDEO_ROOT=$1
FRAME_ROOT=$2
NUM_THREADS=$3


echo "Extracting frame from videos in folder: ${VIDEO_ROOT}"
python vid2img.py --NUM_THREADS ${NUM_THREADS} --VIDEO_ROOT ${VIDEO_ROOT} --FRAME_ROOT ${FRAME_ROOT}