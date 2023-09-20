
# noparser (nmap output parser)

noparser is a tool that allows for parsing of nmap output. Sometimes, you may run a netwide scan, and then wish to parse it into a csv or some other kind of portable
document. nmap-parser is hear to save the day. To create a nmap output file that nmap-parser can parse run the following command `nmap -sn -oN "file_name.txt" 10.10.10.10/24`

## Installing

To install, please download the latest release from the releases page (https://github.com/ofgrenudo/noparser/releases/)[https://github.com/ofgrenudo/noparser/releases/] and extract it to a folder on your desktop. You can either run it from the terminal there, or add it to your system path and run it from anywhere on your device.

### Example Command Usage

```text
usage: noparser.py [-h] [-i sample_input.txt] [-o output_file.csv] [-d]

options:
  -h, --help            show this help message and exit

  -i sample_input.txt, --input sample_input.txt
                        File Input
 
 -o output_file.csv, --output output_file.csv
                        File Output

  -d, --debug           Debugging Mode
```

## Building

`pyinstaller noparser.py`
