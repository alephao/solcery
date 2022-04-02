import re
import sys
from web3 import Web3

# TODO: This was copy-pasted from one of my other projects,
#       need to refactor, add tests etc


regex = re.compile(r"error\s(\w+)\(.+\;")

def errors_on_file(path):
  file = open(path, mode='r')
  contents = file.read()
  file.close()

  return regex.findall(contents)

def add_error_sig_comments(path):
  file = open(path, mode='r')
  contents = file.read()
  file.close()
  errs = errors_on_file(path)

  for err in errs:
    sig = Web3.toHex(Web3.keccak(text="{}()".format(err)))[:10]
    old = re.compile("^(.*@dev\\s)0x.*(\\n\\s*error\\s{}\\(\\);)".format(err), flags=re.M)
    new = "\g<1>{}\g<2>".format(sig)
    contents = re.sub(old, new, contents)

  file = open(path, mode='w')
  file.write(contents)  
  file.close()

  print("Generated error sig comments on", path)

def main(args):
  if len(args) < 2:
    print("Usage: solcery errsig [<path_to_file_containing_error>]")
    return

  for path in sys.argv[2:]:
    add_error_sig_comments(path)

if __name__=="__main__":
  main(sys.argv)
