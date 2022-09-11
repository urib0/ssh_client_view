#!/usr/bin/env python3
import os

try:
  with open(os.environ['HOME']+"/.ssh/authorized_keys", "r") as f:
    auth_key_list = f.readlines()
except Exception as e:
  print(e)
  exit(0)
