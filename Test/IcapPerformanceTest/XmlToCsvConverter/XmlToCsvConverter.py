import csv
import xml.etree.ElementTree as ET
import os

tree = ET.parse("C:/Git/file-rebuild-performance-tests/Test/FileRebuildPerformanceTest/Results/FileRebuildResults.xml")
root = tree.getroot()


WANTED_KEYS = [
    "x-amzn-RequestId",
    "gw-metric-upload",
    "gw-metric-detect",
    "gw-metric-download",
    "gw-metric-rebuild",
    "gw-version",
    "gw-metric-filesize",
]

with open("C:/Git/file-rebuild-performance-tests/Test/FileRebuildPerformanceTest/Results/gw_metrics.csv", "w", newline="") as f:
    csvwriter = csv.writer(f)

    data = []
    for http_sample_with_post in [item for item in root.findall("./httpSample") if item.attrib.get("lb").startswith("Post_")]:
        name = http_sample_with_post.attrib["lb"]
        text = http_sample_with_post.find("responseHeader").text
        responseTime = http_sample_with_post.attrib["t"]
        lines = [item.split(": ", 1) for item in text.splitlines()]
        lines[0] = lines[0][0].split(" ", 1)
        lines = [item for item in lines if item[0] in WANTED_KEYS]

        # if data is empty, add headers
        if not data:
            headers = ["name"] + [item[0] for item in lines] + ["responseTime"]
            data.append(headers)

        # add row
        row = [name] + [item[1] for item in lines] + [responseTime]
        data.append(row)

    csvwriter.writerows(data)


#import pandas as pd
#
#df = pd.read_csv("C:/Git/file-rebuild-performance-tests/Test/FileRebuildPerformanceTest/Results/gw_metrics.csv")
#print(df)
