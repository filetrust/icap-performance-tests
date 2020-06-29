import csv
import xml.etree.ElementTree as ET
import os

tree = ET.parse("../Results/FileRebuildResults.xml")
root = tree.getroot()


WANTED_ATTRIBUTES = [
    "t",
    "lt",
    "ct",
    "ts",
    "s",
    "lb",
    "rc",
    "rm",
    "tn",
    "by",
    "sc",
    "ec",
    "ng",
    "na"
]

with open("../Results/gw_metrics.csv", "w", newline="") as f:
    csvwriter = csv.writer(f)

    # Add column headers
    data = []
    data.append(WANTED_ATTRIBUTES)
    for http_sample_with_post in [item for item in root.findall("./httpSample") if item.attrib.get("lb").startswith("Post_")]:
        # add row
        row = [http_sample_with_post.attrib[attrib] for attrib in WANTED_ATTRIBUTES]
        data.append(row)

    csvwriter.writerows(data)