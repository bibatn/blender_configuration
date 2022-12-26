import os
with open('sea_urchin.txt', 'r') as data:
  plaintext = data.read()

plaintext = plaintext.replace(',', ' ')
with open('sea_urchin_.txt', 'w') as f:
    f.write(plaintext)
