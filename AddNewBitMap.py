
import math
import mmh3
from bitarray import bitarray
from pathlib import Path
import json
from bloomfilter import BloomFilter
import subprocess
import sys
n = int(subprocess.check_output(["wc", "-l", "{}".format(sys.argv[1])],universal_newlines=True).split(" ")[0])
p = 0.05
bloomf = BloomFilter(n, p)
f = open(sys.argv[1], "rb")
for line in f:
    bloomf.add(line)
Bit_Output = open("BitMaps/map_"+sys.argv[1].split("/")[-1], "wb")
bloomf.bit_array.tofile(Bit_Output)
Bit_Output.close()

data1 = {
    "{}".format(sys.argv[1].split("/")[-1]): {
        "BitMapRoute": "BitMaps/map_"+sys.argv[1].split("/")[-1],
        "lines": n
    }
}
path = Path('map.json')
data = json.loads(path.read_text(encoding='utf-8'))
data.append(data1)
path.write_text(json.dumps(data, indent=2), encoding='utf-8')