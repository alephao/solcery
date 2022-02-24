#!/usr/bin/env python

import sys
import errors_gen

def main(args):
  if len(args) < 2:
    print("Usage: solcery <command>")
    return

  command = args[1]

  if command == "errgen":
    errors_gen.main(args[1:])
    return

  print("Unknown command '{}'".format(command))
  print("Valid commands: errgen")

if __name__=="__main__":
  main(sys.argv)
