# M-bias-plotting
Takes M-bias report files from bismark methylation extractor and generates plots

## Requirements
* Python3 (untested with 2.7)
* numpy
* matplotlib

## Usage
python MBiasPlotting.py /path/to/M-bias.txt

or (if python is on PATH)

MBiasPlotting.py /path/to/B-bias.txt

## Output
Generates a png file containing two plots showing the M-bias data for forward and reverse reads
