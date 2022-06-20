import sys
import requests
import os
import argparse
import subprocess

link = "https://github.com/slackhq/nebula/releases/download/v1.5.2/nebula-linux-amd64.tar.gz"
program = "nebula-linux-amd64.tar.gz"


def runcmd(cmd, verbose=False, *args, **kwargs) -> str:
    process = subprocess.Popen(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        shell=True
    )
    
    std_out, std_err = process.communicate()
    if verbose:
        print(std_out.strip(), std_err)
    return std_err if(not verbose) else str(std_out + std_err)

def clean() -> None:
    runcmd('rm nebula*' , verbose=False)
    runcmd('rm config*' , verbose=False)

def file_to_str(filename:str) -> str:
    f = open(filename,"r")
    return ''.join(f.readlines())

def str_to_file(filename:str,data:str) -> None:
    f = open(filename,"w")
    f.write(data)
    f.close()

def create_pub_priv_key(username:str,path_nebula:str="./nebula-cert") -> str:
    return runcmd(f"{path_nebula} keygen -out-key {username}.priv -out-pub {username}.pub",verbose=False)

class MyParser(argparse.ArgumentParser):
    def error(self, message):
        sys.stderr.write('error: %s\n' % message)
        self.print_help()
        exit(1)

if __name__ == "__main__":
    try:
        # parser = argparse.ArgumentParser(description='Process some integers.')
        parser = MyParser()
        parser.add_argument('--user', metavar='UUID', type=str,required=True, help='The username for the client')
        args = parser.parse_args()
    except:
        exit(1)
    if not os.path.exists(args.nebula):
        runcmd('wget ' + link, verbose=False)
        runcmd('tar xvf ' + program, verbose=False)
    
    create_pub_priv_key(args.user)