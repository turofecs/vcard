<!-- omit in toc -->
vcard splitter
=

create single-person vcard files from a multi-person vcard file. Commandline tool.

(c) 2023 turofecs@filmkorn.de Stefan Waizmann

# introduction

Sometimes, contacts are disapperaing from your macOS address book. It is recommendable to have a backup ready then, a multi-person vcard file or contact archive. Best practice is a multi-person vcard file. For being able to retrieve single contacts, this tool will create single files from your contacts, easy to restore and re-import.

# install

Clone the [https://github.com/turofecs/vcard.git](https://github.com/turofecs/vcard.git) repository into a folder of your choice. On commandline, this works like this (you need git to be installed):

```sh
rookie@MBP python % git clone https://github.com/turofecs/vcard.git
Cloning into 'vcard'...
```
As an alternative, download th zip file and unzip it.

# usage

Help is provided with the -h parameter:

```sh
rookie@MBP % cd vcard
rookie@MBP vcard % python3 vcf_split.py -h
usage: vcf_split.py [-h] [-f] [-v] [--dir DIR] file

creates single-person vcard files from a multi-person vcard file

positional arguments:
  file           the multi-person VCARD file

options:
  -h, --help     show this help message and exit
  -f, --force    overwrite existing files
  -v, --verbose  get more info
  --dir DIR      specify target folder DIR
rookie@MBP vcard %
```

Operation is straightforward. Provided with an multi-person vcard file (here: 20230216.vcf) the script will:

- create a folder with name of the original file without file suffix
- create small single vcard files with full contact name as filenames

```sh
rookie@MBP vcard % python3 vcf_split.py 20230216.vcf
407 names written to 20230216
rookie@MBP vcard %
```

# license

GPL v 3.0
