try:
    import sys
except:
    print("Could not import librarys `sys`. please try again")

try: 
    import plac
except:
    print("Could not import plac. Pleas trying installing the library using `pip install plac` then run the program again.")

scanned_hosts = [] # Will contain an array of an array that consists of a max of 2 values. Example [ ["hostname", "ip_address"], ... ]

@plac.opt('input', help="File Input", type=None)
@plac.opt('output', help="File Output", type=None)
@plac.flg('debug', help="Debugging Mode")
def main(input="sample_input.txt", output="output_file.csv", debug=False):
    """
    noparser is a tool that allows for parsing of nmap output. Sometimes, you may run a netwide scan, and then wish to parse it into a csv or some other kind of portable
    document. nmap-parser is hear to save the day. To create a nmap output file that nmap-parser can parse run the following command `nmap -sn -oN "file_name.txt" 10.10.10.10/24`
    """
    if debug: print("Received Input: \n\tinput  = {}\n\toutput = {}\n\tdebug  = {}\n\t".format(input, output, debug))
    if input != "sample_input.txt":
       parse_input_file(input, debug)
       
    if output != "output_file.csv":
        write_output_file(output, debug)        
        
    if input != "sample_input.txt" and output == "output_file.csv":
        for device in scanned_hosts:
            print("IP Address: {}  \tHostname: {}\t".format(device[1], device[0])) 
        

def parse_input_file(input_file, debug):
    file = open(input_file, 'r')
    all_lines = file.readlines()
    #print(all_lines)
    for line in all_lines:
        parsed_line = line.split()
        # print(parsed_line[0])
        # if parsed_line[0] == "Nmap": 
            # if debug: print(parsed_line)

        if len(parsed_line) == 5 and parsed_line[0] == "Nmap":
            # Device does not have hostname
            # if debug: print("Parsing {} \t Parsed {} ".format(parsed_line, parsed_line[4]))
            scanned_hosts.append(["None", parsed_line[4]])

        if len(parsed_line) == 6 and parsed_line[0] == "Nmap":
            # if debug: print("Parsing {} \t Parsed {} and {}".format(parsed_line, parsed_line[4], parsed_line[5].strip("()")))
            scanned_hosts.append( [parsed_line[4], parsed_line[5].strip("()")] )      
        
        if parsed_line[0] == "Host":
            pass

def write_output_file(output_file, debug):
    file = open(output_file, "w")
    file.write("Ip Address,Hostname\n")
    for device in scanned_hosts:
        file.write("{},{}\n".format(device[1], device[0]))

if __name__ == '__main__':
    plac.call(main)

