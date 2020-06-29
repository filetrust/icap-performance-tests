import csv
import xml.etree.ElementTree as ET
import os

tree = ET.parse("../Results/FileRebuildResults.xml")
root = tree.getroot()


RECORDED_ATTRIBUTES = [
    ["t", "Elapsed time (milliseconds)"],
    ["lt", "Latency"],
    ["ct", "ct"],
    ["ts", "timeStamp"],
    ["s", "Success flag"],
    ["lb", "Label"],
    ["rc", "Response Code"],
    ["rm", "Response Message"],
    ["tn", "Thread Name"],
    ["by", "Bytes"],
    ["sc", "Sample count"],
    ["ec", "Error count"],
    ["ng", "Number of active threads in this group"],
    ["na", "	Number of active threads for all thread groups"],
]

attribute_store = dict(RECORDED_ATTRIBUTES)

with open("../Results/gw_metrics.csv", "w", newline="") as f:
    csvwriter = csv.writer(f)

    # Add column headers
    data = []
    data.append(attribute_store.values())
    for http_sample_with_post in [item for item in root.findall("./httpSample") if item.attrib.get("lb").startswith("Post_")]:
        # add row
        row = [http_sample_with_post.attrib[attrib] for attrib in attribute_store.keys()]
        data.append(row)

    csvwriter.writerows(data)