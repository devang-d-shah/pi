import json
import glob
import re

# function to replace - in json keys with _ so that they can be imported as valid bigquery column names
def underscored_key(match):
    return str.replace(f'"{match.group(1)}" :','-','_')

# This would normally be passed as a parameter
read_files = glob.glob("C:\\Users\\DevangShah\\Documents\\DE_test_data_sets\\policies\\Row*.json")

# single newline delimited json output file with combined policisies from all input files, to make it possible to import into BQ 
with open("policies.json", "w") as outfile:
    for f in read_files:
        with open(f, "r") as infile:
            for line in infile:
                # newline delimited needs removing newlines from within each policy
                line = line.rstrip("\n")
                # replace json keys with function output
                line = re.sub(r'"([\w\-]+)" :',underscored_key,line)
                # replace empty dicts with null
                line = line.replace('{ }','null')
                outfile.write(line)
        # newline delimiter between policies
        outfile.write("\n")
