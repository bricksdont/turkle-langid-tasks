#! /usr/bin/python3

import os
import csv
import random
import logging
import argparse

from collections import defaultdict


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--csv", type=str, help="File path to CSV with results.", required=True)

    args = parser.parse_args()

    return args


def main():

    args = parse_args()

    logging.basicConfig(level=logging.DEBUG)
    logging.debug(args)

    csv_handle = open(args.csv, "r")

    reader = csv.DictReader(csv_handle)

    files = defaultdict(lambda: defaultdict(int))

    for row in reader:
        filename = row["Input.filename"]
        answer = row["Answer.language"]

        files[filename][answer] += 1

    for filename, answer_dict in files.items():

        total = sum(answer_dict.values())

        print(filename + ":\t", end='')

        for key in sorted(answer_dict.keys()):
            value = answer_dict[key]
            percentage = value / float(total) * 100
            print(f"'{key}': {percentage:.2f}% ({value}/{total}) ", end='')
        print()

    print()

    num_systems = len(files.keys())
    num_annotations = sum([sum(answer_dict.values()) for file, answer_dict in files.items()])

    print(f"OVERALL STATS: NUM SYSTEMS={num_systems}\tNUM_ANNOTATIONS={num_annotations}\tAVG NUM ANNOTATIONS={num_annotations / num_systems}")


if __name__ == '__main__':
    main()
