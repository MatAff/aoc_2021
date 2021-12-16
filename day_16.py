import os

# Settings
path_data = "day_16.txt"

# Test Data
input = open(path_data).readlines()
input = [e.strip() for e in input]
print(input)

# Conversion
conv = open("day_16_conv.txt").readlines()
conv = [e.strip() for e in conv]
conv = {e.split(" = ")[0]: e.split(" = ")[1] for e in conv}
print(conv)

# Three
three_keys = [str(i) for i in range(8)]
three = {v[1:4]: k for k, v in conv.items() if k in three_keys}
four = {"0" + k: int(v) for k, v in three.items()}
four_plus = {"1" + k: int(v) + 8 for k, v in three.items()}
four = {**four, **four_plus}
print(four)

# Version
vers = {k: v[0:3] for k, v in conv.items()}
print(vers)

# Version val
vers_val = {k: three[v] for k, v in vers.items()}

types = {"4": 6 + 15 + 3}

# Convert input to binary
bin = "".join([conv[e] for e in input[0]])
len(bin)

def bin_to_dec(b):
    base = 2**0
    num = 0
    for i in b[::-1]:
        num = num + int(i) * base
        base = base * 2
    return num


# bin = "110100101111111000101000"
# bin = "00111000000000000110111101000101001010010001001000000000"
# bin = "".join([conv[e] for e in '8A004A801A8002F478'])

# 100 010 1 00000000001 # 18
# 001 010 1 00000000001 
# 101 010 0 000000000001011
# 110 100 01111000

bin = "".join([conv[e] for e in '620080001611562C8802118E34'])
print(bin)

# 011 000 1 00000000010
# 000 000 0 000000000010110
# 000 100 010101011000101100100010000 0000010000100011000111000110100

def parse(pos):
    print(f"pos: {pos}")
    bin_version = bin[pos:(pos + 3)]
    version = int(three[bin_version])
    bin_type = bin[(pos + 3):(pos + 6)]
    typee = int(three[bin_type])
    print(version, typee)
    if typee == 4:
        print("literal value")
        val = 1
        sub_pos = pos + 6
        while sub_pos == "1":
            val = four[bin[(sub_pos + 1):(sub_pos + 5)]]
            sub_pos = sub_pos + 4
        val = four[bin[(sub_pos + 1):(sub_pos + 5)]]
        sub_pos = sub_pos + 4
        while (sub_pos % 4) != 0:
            sub_pos = sub_pos + 1
        return version, typee, val, sub_pos
    else:
        print("operator")
        type_id = bin[pos+6]
        if type_id == '0':
            print("by bits")
            bin_number = bin[(pos + 7):(pos + 7 + 15)]
            # print(bin_number)
            number_bits = bin_to_dec(bin_number)
            nr_sub = int(number_bits / 11)
            # print(nr_sub)
            for s_nr in range(nr_sub):
                if s_nr != (nr_sub - 1):
                    print("not final")
                    sub_bin = bin[(pos + 7 + 15 + 11 * s_nr):(pos + 7 + 15 + 11 * s_nr + 11)]
                else:
                    print("final")
                    sub_bin = bin[(pos + 7 + 15 + 11 * s_nr):(pos + 7 + 15 + number_bits)]
                # print(sub_bin)
                sub_version, _, _, _ = parse(pos + 7 + 15 + 11 * s_nr)
                print(sub_version)
                version = version + sub_version
                pos_reached = pos + 7 + 15 + number_bits
        else:
            print("by number sub packages")
            bin_number = bin[(pos + 7):(pos + 7 + 11)]
            nr_sub  = bin_to_dec(bin_number)
            # print(nr_sub)
            for s_nr in range(nr_sub):
                sub_bin = bin[(pos + 7 + 11 + 11 * s_nr):(pos + 7 + 11 + 11 * s_nr + 11)]
                # print(sub_bin)
                # print(pos + 7 + 11 + 11 * s_nr)
                sub_version, _, _, _ = parse(pos + 7 + 11 + 11 * s_nr)
                print(sub_version)
                version = version + sub_version
            pos_reached = pos + 7 + 11 + nr_sub * 11
        # while (pos_reached % 4) != 0:
        #     pos_reached = pos_reached + 1
        # next_version_not_found = True
        # while next_version_not_found:
        #     if bin[pos_reached:(pos_reached + 4)] != "0000":
        #         return version, type, -1, pos_reached
        #     pos_reached = pos_reached + 4
        return version, type, -1, pos_reached

parse(0)

