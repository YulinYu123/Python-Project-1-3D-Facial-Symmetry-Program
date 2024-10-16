"""
CITS1401 Project1
Student Name: Yulin Yu
Student Number: 22743739
Python Version: 3.9.7
"""

# Set default values based on the sample dataset as global values.
adult_id = 0
point = 1
x = 2
y = 3
z = 4


# Calculate the average number
def mean(l):
    return round(sum(l) / len(l), 4)


# This is the function that used in std_calculate function.
# Calculate the standard deviation of a list.
def std_calculate(l):
    avg = sum(l) / len(l)
    tmp = 0
    for i in l:
        tmp += (i - avg) ** 2
    return round((tmp / len(l)) ** 0.5, 4)


# Calculate the asymmetry values of given point
def cal_asym3D(data):
    asymx = float(data[x])
    asymy = float(data[y])
    asymz = float(data[z])
    return (asymx * asymx + asymy * asymy + asymz * asymz) ** 0.5


# Calculate the minimum asymmetry values of lower and upper face
def cal_mn(asym):
    return [min(asym[:5]), min(asym[5:])]


# Calculate the maximum asymmetry values of lower and upper face
def cal_mx(asym):
    return [max(asym[:5]), max(asym[5:])]


# Calculate the average values of asymmetry values of lower and upper face
def cal_avg(asym):
    return [mean(asym[:5]), mean(asym[5:])]


# Calculate the standard deviation of asymmetry values of lower and upper face
def cal_std(asym):
    return [std_calculate(asym[:5]), std_calculate(asym[5:])]


# Transfer the data type from str to float and do the calibration
def calibration(data):
    for i in range(len(data)):
        data[i][x] = float(data[i][x])
        data[i][y] = float(data[i][y])
        data[i][z] = float(data[i][z])
    for i in range(len(data)):
        if data[i][point] == '10':
            if not (data[i][x] == 0 and data[i][y] == 0 and data[i][z] == 0):
                for j in range(len(data)):
                    data[j][x] -= data[i][x]
                    data[j][y] -= data[i][y]
                    data[j][z] -= data[i][z]
            data.remove(data[i])
            break
    return data


# Extract the data according to adults and type
def preprocess(data, adults, t):
    data_processed = []
    if t == 'corr':
        for row in data:
            if row[adult_id] == adults[0] or row[adult_id] == adults[1]:
                data_processed.append(row)
    elif t == 'stats':
        for row in data:
            if row[adult_id] == adults:
                data_processed.append(row)
    return data_processed


# Calculate the statistic values
def cal_stats(data):
    asym3D1 = [cal_asym3D(data[i]) for i in range(len(data))]
    asym3D = [round(asym3D1[i], 4) for i in range(len(asym3D1))]
    mn1 = cal_mn(asym3D)
    mx1 = cal_mx(asym3D)
    avg1 = cal_avg(asym3D1)
    std1 = cal_std(asym3D1)
    return asym3D, mn1, mx1, avg1, std1, asym3D1


# Used in cal_corr()
def _denominator_calculate(l):
    avg = sum(l) / len(l)
    tmp = 0
    for i in l:
        tmp += (i - avg) ** 2
    # If the denominator is 0, it will be replaced by 1, rather than raising an ZeroDivisionError.
    if tmp == 0:
        tmp = 1
    return tmp ** 0.5


# Used in cal_corr()
def _numerator_calculate(n1, n2):
    avgx = sum(n1) / len(n1)
    avgy = sum(n2) / len(n2)
    tmp = 0
    for i in range(len(n1)):
        tmp += (n1[i] - avgx) * (n2[i] - avgy)
    return tmp


# Calculate the correlation
def cal_corr(n1, n2):
    # Calculate the correlation
    denominator1 = _denominator_calculate(n1)
    denominator2 = _denominator_calculate(n2)
    numerator = _numerator_calculate(n1, n2)
    if denominator1 * denominator2 == 0:
        # If the denominator is 0, the correlation coefficient will be meaningless. The output will be replaced by a 0.
        return 0
    return round(numerator / (denominator1 * denominator2), 4)


def main(csvfile, adults, t):
    global adult_id, point, x, y, z
    filename = csvfile.strip()
    t = t.strip()
    # Open the data file and read the data
    facial_data = open(filename, 'r')
    data = facial_data.read()
    facial_data.close()

    data = data.strip().split('\n')  # Group the data by rows, and convert to list.
    for i in range(len(data)):
        data[i] = data[i].split(',')
    # Match the columns. Ensure that no matter how the column order changes (or add jamming headings),
    # the corresponding column can be found based on the headings.
    for item in range(len(data[0])):
        if data[0][item] == 'Adult ID':
            adult_id = item
        if data[0][item] == 'Point Number':
            point = item
        if data[0][item] == 'X':
            x = item
        if data[0][item] == 'Y':
            y = item
        if data[0][item] == 'Z':
            z = item

    if t == 'stats':
        data_cal = preprocess(data, adults, t)
        data_cal = calibration(data_cal)
        return cal_stats(data_cal)[:-1]
    elif t == 'corr':
        data0 = preprocess(data, adults[0], 'stats')
        data0 = calibration(data0)
        data1 = preprocess(data, adults[1], 'stats')
        data1 = calibration(data1)
        asym0 = cal_stats(data0)
        asym1 = cal_stats(data1)
        return cal_corr(asym0[-1], asym1[-1])

