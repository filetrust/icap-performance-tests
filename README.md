# icap-performance-tests

Performance tests that drive web traffic containing documents that Glasswall can manage.

## Pre-requisites ##

JMeter is required to update and run these tests. This can be downloaded from http://jmeter.apache.org/download_jmeter.cgi
Python is required to run the XML to CSV converstion script.

## Running the tests

The tests should be run using JMeter's command line mode.
In a command console navigate to the folder containing the test specification file, `icap-performance-tests\Test\IcapPerformanceTest`
```
jmeter -n -t FileRebuildPerformanceTest.jmx
```

## Post-processing
Test result are written to the results folder, `icap-performance-tests\Test\IcapPerformanceTest\Results` in XML Format. To convert to CSV, run the conversion script `XmlToCsvConverter.py`, found in the folder `icap-performance-tests\Test\IcapPerformanceTest\XmlToCsvConverter`. This will produce a CSV version of the data in the `Results` folder.
```
python .\XmlToCsvConverter.py
```


