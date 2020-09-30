import os
import subprocess

def username():
    cmd = "az ad signed-in-user show | grep displayName | awk '{print $2 $3}'"
    az = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    output = az.communicate()[0]
    dcode = output.decode("utf-8")
    strip = dcode.strip('"\n,')
    return strip
