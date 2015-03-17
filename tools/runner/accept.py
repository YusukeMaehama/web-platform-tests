# -*- coding: utf-8 -*-

import imp
import json
import os
import sys

here = os.path.dirname(__file__)
localpaths = imp.load_source("localpaths", os.path.abspath(os.path.join(here, os.pardir, "localpaths.py")))

root = localpaths.repo_root

def main(request, response):
    path = os.path.join(root, "dump", "result.json")
    f = open(path, 'w')
    f.write(request.body)
    f.close

    return [("Content-Type", "application/json")], ""
