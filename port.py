import os
import sys

with open(sys.argv[1], 'r') as data:
  plaintext = data.read()

plaintext = plaintext.replace(',', ' ')
with open(sys.argv[1][:-4]+'.pcd', 'w') as f:
    f.write(plaintext)
