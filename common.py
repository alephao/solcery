from functools import reduce
import re
from web3 import Web3


def encode_signature(sig):
    return Web3.toHex(Web3.keccak(text=sig))[:10]


def error_sig_to_obj(err):
    # Get function name
    nameRegex = re.compile(r"\b(.+)\b\(")
    nameMatch = nameRegex.match(err)
    name = nameMatch.group(1)

    # Get function params
    paramsRegex = re.compile(r".+\((.*)\)")
    paramsMatch = paramsRegex.match(err)
    paramsGroup = paramsMatch.groups()[0].strip()
    if len(paramsGroup) == 0:
        return {"name": name, "args": []}

    params = map(lambda x: x.strip(), paramsGroup.split(","))
    params = map(lambda x: x.split(" "), params)
    params = map(lambda x: {"name": "", "type": x[0]} if len(
        x) == 1 else {"name": x[1], "type": x[0]}, params)
    params = list(params)

    return {
        "name": name,
        "args": params
    }


def errors_on_content(content):
    regex = re.compile(r"error\s+(\w+.+\))\;")
    return regex.findall(content)


def errors_on_file(path):
    file = open(path, mode='r')
    content = file.read()
    file.close()

    return errors_on_content(content)
