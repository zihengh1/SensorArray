def split_string(msg):
    print(msg)
    values = {}
    data = msg.split("|")[1:]
    for sensor in data[0:-1]:
        temp_list = sensor.split(":")
        values[temp_list[0]] = temp_list[1]
        temp_list = []
    return values

def dec_to_binstr(data_dict):
    order = ['s1', 's2', 's3', 's4', 's5']
    T3_binstr = "0011"
    for s in order:
        if s in data_dict:
            data_dict[s] = str(bin(int(data_dict[s])).replace("0b", "")).zfill(10)
            T3_binstr += str(bin(int(s[1]))).replace("0b", "").zfill(4)
            T3_binstr += data_dict[s]
        else:
            T3_binstr += str(bin(int(s[1]))).replace("0b", "").zfill(4)
            T3_binstr += "0" * 10
    T3_binstr += (96 - len(T3_binstr)) * "0"
    return T3_binstr

def bin_to_hex(value):
    hex_map = {"0000": "0",
            "0001": "1",
            "0010": "2",
            "0011": "3",
            "0100": "4",
            "0101": "5",
            "0110": "6",
            "0111": "7",
            "1000": "8",
            "1001": "9",
            "1010": "A",
            "1011": "B",
            "1100": "C",
            "1101": "D",
            "1110": "E",
            "1111": "F"
            }
    i = 0
    output = ""
    while (i < len(value)):
        output = output + hex_map[value[i:i + 4]]
        i = i + 4
    return output
