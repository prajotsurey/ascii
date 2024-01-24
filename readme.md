# Image-to-ASCII converter (WIP)

This script converts an image to a txt file cotaining ascii characters and outputs an image with those ascii characters.

This is a very naive implementaion and is not very optimized.

* [About](#about)
* [Installation](#user-content-installation)
* [Usage](#user-content-usage)

## About
This project is an implementation of the following tutorial:

https://youtu.be/v_raWlX7tZY

Apart from outputting a text file, it also outputs a image.

## Prerequisites

You need to create a python3 virtualenv and clone this project into it.

## Installation

1. Clone project into src folder inside your virtualenv

```bash
git clone https://github.com/prajotsurey/image-to-ascii.git src
```
2. Activate virtualenv

3. Install dependencies

```bash
pip install -r requirements.txt
```

## Usage

1. Place your png image in the input folder.
2. Rename it to image.png.
3. Run script.py in the activated virtualenv.

```bash
python script.py
```
4. The output image and text file is saved in the 'output' folder.
