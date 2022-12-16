# maspy
A simple tool built around [matchering](https://github.com/sergree/matchering) and [pydub](https://pypi.org/project/pydub/) to automatically master multiple songs using a reference track. It returns the mastered tracks as 192kbps mp3 files. It's an easy way to improve recordings of your band's practise session!

## Installation
Use the environment.yml to set up a new Python environment. Using anaconda:

`conda env create -f environment.yaml`

Maspy depends on ffmpeg for i/o of compressed audio formats such as mp3 and m4a. Get the latest build of ffmpeg [here](https://ffmpeg.org/download.html#build-windows) and add it to Path following [this guide](https://blog.gregzaal.com/how-to-install-ffmpeg-on-windows/). Next install ffmpeg in your new Python environment:

`pip install ffmpeg`

Currently you have to edit the script in an IDE and run it there until 
