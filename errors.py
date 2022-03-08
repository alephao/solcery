template = """// SPDX-License-Identifier: Unlicense
pragma solidity >=0.8.4;

// The code in this file was generate. Do not modify!
// solhint-disable const-name-snakecase,func-name-mixedcase
library Errors {
<CONTENT>
}
// solhint-enalbe const-name-snakecase"""

def fnsig(err):
  fnparams = ""

  if len(err["args"]) > 0:
    fnparams = []
    for i, arg in enumerate(err["args"]):
      if arg["name"] == "":
        fnparams.append("{} p{}".format(arg["type"], i + 1))
      else:
        fnparams.append("{} {}".format(arg["type"], arg["name"]))
    
    fnparams = ", ".join(fnparams)

  return "{}({})".format(err["name"], fnparams)

def implsig(err):
  implparams = ",".join(map(lambda x: x["type"], err["args"]))
  sig = "\"{}({})\"".format(err["name"], implparams)

  if len(err["args"]) == 0:
    return sig
  
  fnparams = []
  for i, arg in enumerate(err["args"]):
    if arg["name"] == "":
      fnparams.append("p{}".format(i + 1))
    else:
      fnparams.append("{}".format(arg["name"]))
    
  fnparams = ", ".join(fnparams)

  return "{}, {}".format(sig, fnparams)

def gen_error_entry(err):
  return "function {} internal pure returns (bytes memory) {{ return abi.encodeWithSignature({}); }}".format(fnsig(err), implsig(err))

def gen_functions(errors):
  return list(map(lambda err: gen_error_entry(err), errors))

def gen_file_contents(errors):
  fns = gen_functions(errors)
  fns = "\n".join(map(lambda fn: "    {}".format(fn), fns))
  return template.replace("<CONTENT>", fns)
