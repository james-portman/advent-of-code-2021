def data_from_file():
    input = []
    for line in open("input").readlines():
        row = []
        for i in range(12):
            row.append(int(line[i]))
        input.append(row)
    return input


def data_into_cols(data):
    cols = []
    for i in range(12):
        cols.append([])
    for row in data:
        for i in range(12):
            cols[i].append(int(row[i]))
    return cols


def get_most_common(data, bit_index):
    cols = data_into_cols(data)
    col = cols[bit_index]
    ones = 0
    zeroes = 0
    for thing in col:
        if thing == 0:
            zeroes += 1
        else:
            ones += 1
    if zeroes > ones:
        return 0
    elif ones > zeroes:
        return 1
    else:
        return None

def get_least_common(data, bit_index):
    cols = data_into_cols(data)
    col = cols[bit_index]
    ones = 0
    zeroes = 0
    for thing in col:
        if thing == 0:
            zeroes += 1
        else:
            ones += 1
    if zeroes < ones:
        return 0
    elif ones < zeroes:
        return 1
    else:
        return None

def filter_data(data, bit_index, keep):
    output = []
    for row in data:
        if row[bit_index] == keep:
            output.append(row)
    return output


def get_oxygen(data):
    """
    To find oxygen generator rating,
    determine the most common value (0 or 1) in the current bit position,
    and keep only numbers with that bit in that position.
    If 0 and 1 are equally common, keep values with a 1 in the position being considered.
    """
    for i in range(12):
        most_common = get_most_common(data, i)
        if most_common == None:
            most_common = 1
        data = filter_data(data, i, most_common)
        if len(data) == 1:
            return data[0]
    raise Exception("bad")



def get_co2(data):
    """
    To find CO2 scrubber rating,
    determine the least common value (0 or 1) in the current bit position,
    and keep only numbers with that bit in that position.
    If 0 and 1 are equally common, keep values with a 0 in the position being considered.
    """
    for i in range(12):
        least_common = get_least_common(data, i)
        if least_common == None:
            least_common = 0
        data = filter_data(data, i, least_common)
        if len(data) == 1:
            return data[0]
    raise Exception("bad")

def to_int(bin_array):
    output = 0
    for i in range(12):
        output += bin_array[i] << (11-i)
    return output

def main():
    data = data_from_file()
    oxygen = get_oxygen(data)
    print(oxygen)
    co2 = get_co2(data)
    print(co2)

    print(to_int(oxygen)*to_int(co2))


if __name__ == "__main__":
    main()
