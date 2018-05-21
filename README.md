# CRAM Custom Encryption Algorithm
### © Marc Frankel 2018

----------

#### About:
CRAM is just a passion project I whipped together for custom encryption based off of random seeds and a mathematical principle of square roots. I make no promises this is actually secure. Use at own risk!

#### Install:
To install the encryption algorithm simple download cram.py

#### Usage:
To use CRAM to encrypt files simply use the following command:
```bash
python3 cram.py in [file_to_encrypt]
```
Running this command will produce the CRAM Key file (.ckey) and the CRAM output file (.cram)

The CRAM output file is the encrypted file that can be shared "securely." It can "only" (no promises) be decrypted with the corresponding CRAM Key file.

To decrypt a CRAM output file simply run the following command with the .ckey and the .cram file in the same folder. Also note, all files must have the same base name and the file name that should be passed into the command should be the original file name

```bash
python3 cram.py out [file_to_decrypt]
```