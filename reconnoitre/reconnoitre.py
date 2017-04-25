#!/usr/bin/python
from argparse import ArgumentParser
import sys
from ping_sweeper import ping_sweeper
from find_dns import find_dns


def print_banner():
    print("  __")
    print("|\"\"\"\-=  RECONNOITRE")
    print("(____)      An OSCP scanner\n")

def main():
    parser = ArgumentParser()
    parser.add_argument("-t", dest="target_hosts", required=True, help="Set a target range of addresses to target. Ex 10.11.1.1-255" )
    parser.add_argument("-o", dest="output_directory", required=True, help="Set the output directory.")
    parser.add_argument("-pS", dest="ping_sweep", action="store_true", help="Write a new target.txt by performing a ping sweep and discovering live hosts.", default=False)
    parser.add_argument("-pD", dest="find_dns_servers", action="store_true", help="Find DNS servers from a list of targets.", default=False)
    parser.add_argument("--quiet", dest="quiet",  action="store_true", help="Supress banner and headers to limit to comma dilimeted results only.", default=False)
    arguments = parser.parse_args()

    if len(sys.argv) == 1:
        print_banner()
        parser.error("No arguments given.")
        parser.print_usage
        sys.exit()

    if arguments.quiet is not True:
        print_banner()
    if arguments.ping_sweep is True:
        print("[+] Performing ping sweep")
        ping_sweeper(arguments.target_hosts, arguments.output_directory, arguments.quiet)
    if arguments.find_dns_servers is True:
        print("[+] Identifying DNS Servers")
        find_dns(arguments.target_hosts, arguments.output_directory, arguments.quiet)
   

if __name__ == "__main__":
    main()