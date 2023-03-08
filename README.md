## Frame extractor

To run the training and testing, we need to decompose the video into frames. These can be achieved with the script `extractor.sh`. The script has three arguments

- `VIDEO_ROOT` points to the folder where you put the video dataset
- `FRAME_ROOT` points to the root folder where the extracted frames will be put in
- `NUM_THREADS` specifies the number of threads to use in parallel for extraction, must be larger than 1

The command for running frame extraction is as follows

```
bash extractor.sh VIDEO_ROOT FRAME_ROOT NUM_THREADS
```

For frame extraction, you need [ffmpeg](https://www.ffmpeg.org/).

## Acknowledgements

This code repository is basically developed based on [TSM](https://github.com/mit-han-lab/temporal-shift-module). 
