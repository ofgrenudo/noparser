
# noparser (nmap output parser)

noparser is a tool that allows for parsing of nmap output. Sometimes, you may run a netwide scan, and then wish to parse it into a csv or some other kind of portable
document. nmap-parser is hear to save the day. To create a nmap output file that nmap-parser can parse run the following command `nmap -sn -oN "file_name.txt" 10.10.10.10/24`

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
