#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""creates single-person vcard files from a multi-person vcard file"""
# works OK with apple contacts

import argparse, logging, sys
from pathlib import Path

LOGGING_DEFAULT = logging.WARNING
LOGGING_FORMAT = '%(levelname)s: %(message)s'

class VCFsplitter:
	"""der vcf splitter"""
	filename = None
	filepath = None
	linestart = None
	lineend = None
	fullfile = None

	def __init__(self, wholefile) -> None:
		"übergebe die multi name vcf"
		self.set_target_dir( Path(args.file).stem)
		## read the original file
		with open(wholefile) as f:
			self.fullfile = f.readlines()
			logger.info(F"{len(self.fullfile)} Zeilen")

	def set_target_dir(self, targetdir) -> None:
		"manuelles Setzen eine Zieldirectories"
		self.filepath = Path(targetdir)

	def writeFile(self, overwrite=False ) -> None:
		"speichert den Zeilenabschnitt als eigenes File"
		assert self.lineend - self.linestart > 1, "invalid length of VCARD"
		assert self.filepath.is_dir(), F"target dir {self.filepath} not existing (try --dir)"
		newfile = self.filepath / Path(self.filename).with_suffix(".vcf")
		samenamecount = 0
		while not overwrite:
			if newfile.exists():
				logging.warning(F"{newfile} already existing")
				# if file exists, rename with number
				samenamecount += 1
				newfile = self.filepath / Path(self.filename.stem + F" ({samenamecount}).vcf")
			else:
				break
		with open(newfile, 'w') as f:
			logging.debug(newfile)
			# write the lines for certain name from full file to a new file
			for i in range(self.linestart, self.lineend+1):
				f.write(self.fullfile[i])

	def split(self, overwrite=False ):
		"split the fullfile into small files"
		# analyze the full file
		countername = 0	# let's count vcard names
		for idx, line in enumerate(self.fullfile):
			if line.startswith("FN:"):
				self.filename = Path(line[3:].strip() + '.vcf')
				countername += 1
			if line.strip() == "END:VCARD":
				self.lineend = idx
				# vcard end, so let's write this as a file
				assert None not in [self.lineend, self.linestart, self.filename], "vcard parsing error"
				self.writeFile(overwrite=overwrite)
				self.lineend = self.linestart = None
			if line.strip() == "BEGIN:VCARD":
				self.linestart = idx
		return countername


if __name__ == "__main__":
	
	parser = argparse.ArgumentParser(description=__doc__)
	parser.add_argument("file", help="the multi-person VCARD file")
	parser.add_argument('-f', '--force', action='store_true', help='overwrite existing files')
	parser.add_argument('-v', '--verbose', action='count', default=0, help='get more info')
	parser.add_argument('--dir', action='store', help='specify target folder')
	args = parser.parse_args()

	logging.basicConfig(level=max(LOGGING_DEFAULT - 10 * args.verbose, 1), format=LOGGING_FORMAT)
	logger = logging.getLogger(__file__)

	# SingleVCF gets correct path and creates it
	try:
		assert sys.version_info.major > 2, "ERROR - This program needs python3"
		svcf = VCFsplitter(args.file)
		if args.dir:
			svcf.set_target_dir(args.dir)
		Path(Path(args.file).stem).mkdir()
		logger.debug(F"created folder: {svcf.filepath}")
	except (FileExistsError) as e:
		logger.warning(F"folder {svcf.filepath} already exists")
	except (FileNotFoundError, OSError, AssertionError) as e:
		raise SystemExit(e)

	# analyze the full file and write the parts
	countername = svcf.split(overwrite=args.force)
	print(F"{countername} names written to {svcf.filepath}")
