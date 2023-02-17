#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# soll bilder von VCF files (OSX) zur groessenreduktion entfernen
import argparse

parser = argparse.ArgumentParser(description="VCF image remove cmd interface")
parser.add_argument("file", help="vcf original file")
args = parser.parse_args()

with open(args.file) as f:
	for line in f.readlines():
		if len(line) == 0 or line[0:5] == 'PHOTO' or line[0] == " ":
			continue
		print(line.strip())