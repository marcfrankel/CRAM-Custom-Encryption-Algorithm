# CRAM Custom Ecryption Algorithm (© Marc Frankel 2018)
import sys
import base64
import random

def getArgs():
    try:
        command = sys.argv[1]
        file_to_encrypt = sys.argv[2]
    except:
        print("Missing or invalid params")
        sys.exit(0)

    if (command not in ['in', 'out']):
        print("Invalid command")
        sys.exit(0)

    return (command, file_to_encrypt)

def load_file(filename):
    try:
        file_handler = open(filename, "rb")
    except:
        print("Could not load file")
        sys.exit(0)
    return file_handler

def encrypt(contents):
    step_seed = random.random()
    subtract = random.randint(10, 128)
    key = [str(step_seed), str(subtract)]
    output = []
    step_count = 0
    random.seed(step_seed)
    current_step = random.randint(2,10)
    for code in list(contents):
        if (step_count == current_step):
            step_count = 0
            code = code - subtract
            current_step = random.randint(2,10)
            if (code < 0):
                key.append(1)
            else:
                key.append(0)
            output.append(code ** 2)
        else:
            key.append(0)
            output.append(code ** 2)
            step_count += 1

    return(key, output)

def decrypt(key, cram):
    step_seed = key[0]
    addition = key[1]
    step_count = 0
    output = []
    random.seed(float(step_seed))
    current_step = random.randint(2,10)
    for key, code in zip(key[2:],cram):

        code = int(int(code) ** (1/2))
        if (int(key) == 1):
            code = code * -1
        if (step_count == current_step):
            step_count = 0
            code = code + int(addition)
            current_step = random.randint(2,10)
        else:
            step_count += 1
        output.append(code)

    return output


args = getArgs()

if (args[0] == "in"):
    file_handler = load_file(args[1])
    contents = base64.b64encode(file_handler.read())
    encrypt_results = encrypt(contents)

    key_out = open(args[1].split(".")[0] + ".ckey", "w")
    key_out.write(','.join(str(e) for e in encrypt_results[0]))
    key_out.close()

    file_open = open(args[1].split(".")[0] + ".cram", "w")
    file_open.write(','.join(str(e) for e in encrypt_results[1]))
    file_open.close()

    print("File encrypted successfully!")

if (args[0] == "out"):
    key_file = open(args[1].split(".")[0] + ".ckey", "r")
    key = key_file.read().split(",")
    key_file.close()

    cram_file = open(args[1].split(".")[0] + ".cram", "r")
    cram_contents = cram_file.read().split(",")
    cram_file.close()

    decrypt_results = decrypt(key, cram_contents)
    decrypt_results_string = ''.join(chr(e) for e in decrypt_results)

    output_file = open("output." + args[1].split(".")[1], "wb")
    output_file.write(base64.b64decode(decrypt_results_string))
    output_file.close()

    print("File decrypted successfully!")

