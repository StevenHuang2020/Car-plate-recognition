# -*- encoding: utf-8 -*-
# Date: 24/May/2022
# Author: Steven Huang, Auckland, NZ
# License: MIT License
"""
Description: OpenALPR
"""

from openalpr import Alpr


class OpenALPRClass:
    """OpenALPR class"""

    def __init__(self, country, config, runtime_data):
        self.alpr = None

        alpr = Alpr(country, config, runtime_data)
        if not alpr.is_loaded():
            print("Error loading OpenALPR")
        else:
            print("Using OpenALPR " + alpr.get_version())
            self.alpr = alpr
            self.alpr.set_top_n(7)
            self.alpr.set_default_region("wa")
            self.alpr.set_detect_region(False)

    def recognize_img(self, img_file):
        if self.alpr:
            jpeg_bytes = open(img_file, "rb").read()
            return self.alpr.recognize_array(jpeg_bytes)

    def print_results(self, results):
        print("results=\n", results)
        print("Image size: %dx%d" % (results['img_width'], results['img_height']))
        print("Processing Time: %f" % results['processing_time_ms'])

        for i, plate in enumerate(results['results']):
            print("Plate #%d" % i)
            print("   %12s %12s" % ("Plate", "Confidence"))
            for candidate in plate['candidates']:
                prefix = "-"
                if candidate['matches_template']:
                    prefix = "*"

                print("  %s %12s%12f" % (prefix, candidate['plate'], candidate['confidence']))

    def get_results(self, results):
        if results is None:
            return None

        processing_time_total = results['processing_time_ms']
        plates = results['results']
        if len(plates) <= 0:
            return None

        # print(plates, type(plates), len(plates))
        plate_dict = plates[0]
        # print(plate_dict, type(plate_dict))

        plate = plate_dict['plate']
        confidence = plate_dict['confidence']
        matches_template = plate_dict['matches_template']
        plate_index = plate_dict['plate_index']

        region = plate_dict['region']
        region_confidence = plate_dict['region_confidence']
        processing_time_ms = plate_dict['processing_time_ms']
        requested_topn = plate_dict['requested_topn']
        coordinates = plate_dict['coordinates']
        candidates = plate_dict['candidates']
        return (processing_time_total, plate, confidence, coordinates)

    def __del__(self):
        if self.alpr:
            self.alpr.unload()
