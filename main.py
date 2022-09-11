#!/usr/bin/env python3
import os
import pprint
import subprocess

try:
  with open(os.environ['HOME']+"/.ssh/authorized_keys", "r") as f:
    auth_key_list = f.readlines()
except Exception as e:
  print(e)
  exit(0)

# #permitlisten=127.0.0.1:{port} {host} を抜き出す
comment_list = [i[:-1] for i in auth_key_list if i[:2] == "#p"]

# port:hostの辞書を作る
port_host_dic = {i.split(" ")[0].split(":")[1]:i.split(" ")[1] for i in comment_list if 1 < len(i.split(" "))}

pprint.pprint(port_host_dic)

cmd = 'ss -altn|grep -oE [0-9]{5}'
port_list = subprocess.Popen(cmd, stdout=subprocess.PIPE,shell=True).communicate()[0].decode("utf-8").split("\n")[:-1]
print(port_list)