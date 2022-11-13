import json
import glob
import re

def underscored_key(match):
    new_key = str.replace(f'"{match.group(1)}" :','-','_')
#    print(new_key)
    return new_key

read_files = glob.glob("C:\\Users\\DevangShah\\Documents\\DE_test_data_sets\\policies\\Row*.json")

with open("policies.json", "w") as outfile:
    for f in read_files:
        with open(f, "r") as infile:
            for line in infile:
                line = line.rstrip("\n")
                line = re.sub(r'"([\w\-]+)" :',underscored_key,line)
                line = line.replace('{ }','null')
                outfile.write(line)
        outfile.write("\n")
