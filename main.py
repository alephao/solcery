#!/usr/bin/env python

import sys
import errors_gen
import error_sig_comment

def main(args):
  if len(args) < 2:
    print("Usage: solcery <command>")
    print("Valid commands: errgen, errsig")
    return

  command = args[1]

  if command == "errgen":
    errors_gen.main(args[1:])
    return

  if command == "errsig":
    error_sig_comment.main(args[1:])
    return

  print("Unknown command '{}'".format(command))
  print("Valid commands: errgen, errsig")

if __name__=="__main__":
  main(sys.argv)
