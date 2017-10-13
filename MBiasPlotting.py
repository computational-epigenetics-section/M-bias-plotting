#!/usr/bin/env/python
import sys
from collections import defaultdict
import numpy as np
import matplotlib.pyplot as plt
# import seaborn as sns
# sns.set_style("darkgrid")

input_file = sys.argv[1]

def extract_m_bias(file_path):

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
    print(x)

    subplot = 211
    for key, line in zip(['R1', 'R2'], ['b--', 'r--']):
        y = data[key]

        plt.figure(1, figsize=(10,6))
        plt.subplot(subplot)
        plt.ylabel("Percent methylation")
        plt.plot(x, y, line)
        plt.grid(True)
        plt.minorticks_on()
        subplot += 1

    plt.xlabel("Base pair position")
    plt.show()

if __name__ == "__main__":
    extract_m_bias(input_file)
