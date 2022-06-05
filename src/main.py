# -*- encoding: utf-8 -*-
# Date: 24/May/2022
# Author: Steven Huang, Auckland, NZ
# License: MIT License
"""
Description: Main
Usage: python main.py ./res/us-1.jpg
"""

import os
from alpr_class import OpenALPRClass
from argparse import ArgumentParser
from image_cv import loadImg, showImg, textImg, rectangleImg, writeImg

# please change to your opoeALPR binary path
binary_path = os.path.join(os.getcwd(), r"..\openalpr_64")

COUNTRY = 'us'
CONFIG = os.path.join(binary_path, 'openalpr.conf')
RUNTIME_DATA = os.path.join(binary_path, 'runtime_data')

os.add_dll_directory(binary_path)  # search dlls path


def create_params():
    parser = ArgumentParser(description='OpenALPR Python Program')

    parser.add_argument("-c", "--country", dest="country", action="store", default=COUNTRY,
                        help="License plate Country")

    parser.add_argument("--config", dest="config", action="store", default=CONFIG,
                        help="Path to openalpr.conf config file")

    parser.add_argument("--runtime_data", dest="runtime_data", action="store", default=RUNTIME_DATA,
                        help="Path to OpenALPR runtime_data directory")

    parser.add_argument('plate_image', help='License plate image file')

    return parser.parse_args()


def get_file_name(path):
    """get basename, 'name.exe' 'x.zip' """
    base_name = os.path.basename(path)

    """split base-name, 'name.exe'--> tuple('name', '.exe') """
    return os.path.splitext(base_name)


def recognize_image(alpr, file, show=True):
    results = alpr.recognize_img(file)
    alpr.print_results(results)
    res = alpr.get_results(results)
    if res is None:
        print("No car plate detected!")
        return

    if show:
        times, plate, confidence, coordinates = res
        img = loadImg(file)
        print('processing times: ', times)
        print('plate=', plate)
        print('confidence=', confidence)
        print('coordinates=', coordinates)

        str_out = "car plate: " + plate + " confidence: " + str(confidence)
        print(str_out)
        fontsize = 0.6

        startPt = (coordinates[0]['x'], coordinates[0]['y'])
        stopPt = (coordinates[2]['x'], coordinates[2]['y'])

        loc = [30, 30]
        img = textImg(img, str_out, loc, fontScale=fontsize)
        loc = [x + 1 for x in loc]  # draw a text shade
        img = textImg(img, str_out, loc, color=(0, 0, 0), fontScale=fontsize)

        img = rectangleImg(img, startPt, stopPt)

        dst = os.path.join('res', get_file_name(file)[0] + '_result.jpg')
        writeImg(img, dst)
        showImg(img)


def main():
    options = create_params()

    alpr = OpenALPRClass(options.country, options.config, options.runtime_data)

    # file = os.path.join(binary_path, 'samples', 'us-1.jpg')
    file = options.plate_image
    recognize_image(alpr, file)


if __name__ == "__main__":
    main()
