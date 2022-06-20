import sys
import requests
import argparse
import subprocess

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

if __name__ == "__main__":
    try:
        # parser = argparse.ArgumentParser(description='Process some integers.')
        parser = MyParser()
        parser.add_argument('--user', metavar='UUID', type=str,required=True, help='The username for the client')
        parser.add_argument('--nebula', metavar='nebula_path',default="nebula",type=str,required=False, help='The username for the client')
        args = parser.parse_args()
    except:
        exit(1)
    runcmd(f"./{args.nebula} -config {args.user}.yaml", verbose=True)