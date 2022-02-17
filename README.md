# slideshow-extractor
Python script to extract slideshow images from a video file and generate a pdf

## Installation
~~~
git clone https://github.com/sayantan01/slideshow-extractor.git
./install.sh
~~~

## Usage
~~~
python3 main.py <path to videofile>
~~~
This will extract all unique images from the video file and generate pdf.
The pdf will be stored as: slideshow-extractor/materials/mypdf.pdf

- You can optionally provide the duration of the video upto which you want images to be extracted.
~~~
python3 main.py <path to videofile> <hours> <minutes> <seconds>
~~~
