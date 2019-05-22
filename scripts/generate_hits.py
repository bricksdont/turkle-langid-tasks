#! /usr/bin/python3

import os
import csv
import random
import logging
import argparse


def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument("--folder", type=str, help="folder with system output files (will be searched recursively).", required=True)
    parser.add_argument("--csv-output", type=str, help="File name where csv with HITs should be saved.", required=True)
    parser.add_argument("--num-per-system", type=int, help="Max number of lines from each system.", required=False, default=10000)

    args = parser.parse_args()

    return args


def get_csv_writer(args):

    # CSV writer
    csv_handle = open(args.csv_output, "w")

    writer = csv.writer(csv_handle, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONE)

    # write header to this new file
    writer.writerow(["segmentid", "filename", "text"])

    # then change quoting behaviour for all other columns
    writer = csv.writer(csv_handle, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)

    return writer


def main():

    args = parse_args()

    logging.basicConfig(level=logging.DEBUG)
    logging.debug(args)

    writer = get_csv_writer(args)

    tasks = []

    num_files = 0

    # walk all subfolders
    for dir_path, _, files in os.walk(args.folder):

        for file_name in files:

            num_files += 1

            logging.debug(f"Found file: {file_name}")

            file_path = os.path.join(dir_path, file_name)

            file_handle = open(file_path)

            for index, line in enumerate(file_handle):

                if index == args.num_per_system:
                    break

                line = line.strip()

                tasks.append([str(index), file_name, line])

    num_tasks = len(tasks)

    logging.debug(f"Number of files found: {num_files}")
    logging.debug(f"Number of tasks found: {num_tasks}")

    assert num_tasks / num_files <= args.num_per_system, "Number of tasks per system higher than number of allowed tasks."

    random.shuffle(tasks)

    for task in tasks:
        writer.writerow(task)


if __name__ == '__main__':
    main()
