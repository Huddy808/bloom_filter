from bitarray import bitarray
import json
from pathlib import Path
from bloomfilter import BloomFilter
import subprocess
import sys
path = Path('map.json')
data = json.loads(path.read_text(encoding='utf-8'))

for line in data:
    for key  in line:
        Bit_path = line[key]['BitMapRoute']
        oup = open(Bit_path, "rb")
        print(Bit_path)
        n = line[key]["lines"]
        bloomf = BloomFilter(n, 0.05)
        bloomf.bit_array = bitarray(0)
        bloomf.bit_array.fromfile(oup)
        new_breach = open(sys.argv[1], "rb")
        entry = 0
        no_entry = 0
        for field in new_breach:
            if bloomf.check(field):
                entry += 1
                #print("'{}' Полное совпадение".format(field))
            else:
                no_entry += 1
                #print("'{}' Точно нет".format(field))

        proc = no_entry/((no_entry + entry) / 100)
        print("Replic " + str(entry)+"\n" + "Uniq_Field " +str(no_entry)+ "    " + str(proc))
        if (proc < 20):
            print("Look here!")