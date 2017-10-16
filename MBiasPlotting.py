#!/usr/bin/env python
import sys
import os
from os.path import basename
from collections import defaultdict
import numpy as np
import matplotlib.pyplot as plt


def extract_m_bias(file_path, plot_title):

    start_reading = False

    # create dict to hold the values
    data = defaultdict(list)

    # Open file for reading and loop over lines
    with open(file_path, 'r') as f:
        for line in f:
            # Check if line designated a new M section
            if line.startswith('CpG'):
                start_reading = True
                read_id = line.split()[2].strip('(,)')
                print("Found read ID: {}".format(read_id))

            elif line.startswith('CH'):
                start_reading = False

            if start_reading == True:
                if line[0].isdigit():
                    pct = float(line.split()[3])
                    data[read_id].append(pct)

    print("CpG data extracted")

    x = np.arange(1, len(data['R1']) + 1, 1)

    subplot = 211
    for key, line in zip(['R1', 'R2'], ['b--', 'r--']):
        y = data[key]

        plt.figure(1, figsize=(10,6))
        plt.title(plot_title)
        plt.subplot(subplot)
        plt.ylabel("Percent methylation")
        plt.plot(x, y, line)
        plt.xlim(1,150)
        plt.grid(True)
        plt.minorticks_on()
        subplot += 1

    plt.xlabel("Base pair position")
    output_name = plot_title + "_m-bias_plot.png"
    plt.savefig(output_name)


if __name__ == "__main__":

    input_file = sys.argv[1]
    file_name = os.path.splitext(basename(input_file))[0]
    extract_m_bias(input_file, file_name)
