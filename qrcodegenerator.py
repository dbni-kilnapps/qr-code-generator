from PIL import Image

# max characters for versions 1-40
# TODO: fix the max characters for kanji
max_characters = {
    'numeric': {
        'L': [41, 77, 127, 187, 255, 322, 370, 461, 552, 652, 772, 883, 1022, 1101, 1250, 1408, 1548, 1725, 1903, 2061, 2232, 2409, 2620, 2812, 3057, 3283, 3517, 3669, 3909, 4158, 4417, 4686, 4965, 5253, 5529, 5836, 6153, 6479, 6743, 7089],
        'M': [34, 63, 101, 149, 202, 255, 293, 365, 432, 513, 604, 691, 796, 871, 991, 1082, 1212, 1346, 1500, 1600, 1708, 1872, 2059, 2188, 2395, 2544, 2701, 2857, 3035, 3289, 3486, 3693, 3909, 4134, 4343, 4588, 4775, 5039, 5313, 5596],
        'Q': [27, 48, 77, 111, 144, 178, 207, 259, 312, 364, 427, 489, 580, 621, 703, 775, 876, 948, 1063, 1159, 1224, 1358, 1468, 1588, 1718, 1804, 1933, 2085, 2181, 2358, 2473, 2670, 2805, 2949, 3081, 3244, 3417, 3599, 3791, 3993],
        'H': [17, 34, 58, 82, 106, 139, 154, 202, 235, 288, 331, 374, 427, 468, 530, 602, 674, 746, 813, 919, 969, 1056, 1108, 1228, 1286, 1425, 1501, 1581, 1677, 1782, 1897, 2022, 2157, 2301, 2361, 2524, 2625, 2735, 2927, 3057]
    },
    'alphanumeric': {
        'L': [25, 47, 77, 114, 154, 195, 224, 279, 335, 395, 468, 535, 619, 667, 758, 854, 938, 1046, 1153, 1249, 1352, 1460, 1588, 1704, 1853, 1990, 2132, 2223, 2369, 2520, 2677, 2840, 3009, 3183, 3351, 3533, 3721, 3924, 4087, 4296],
        'M': [20, 38, 61, 90, 122, 154, 178, 221, 262, 311, 366, 419, 483, 528, 600, 656, 734, 816, 909, 970, 1035, 1134, 1248, 1326, 1451, 1542, 1637, 1732, 1839, 1994, 2113, 2238, 2369, 2506, 2632, 2780, 2894, 3054, 3220, 3391],
        'Q': [16, 29, 47, 67, 87, 108, 125, 157, 189, 221, 259, 296, 352, 376, 426, 470, 531, 574, 644, 702, 742, 823, 890, 963, 1022, 1101, 1167, 1222, 1316, 1429, 1499, 1618, 1700, 1787, 1867, 1966, 2071, 2181, 2298, 2420],
        'H': [10, 20, 35, 50, 64, 84, 93, 122, 143, 174, 200, 227, 259, 283, 321, 365, 408, 452, 493, 557, 587, 640, 672, 744, 779, 864, 910, 958, 1016, 1080, 1132, 1201, 1273, 1367, 1465, 1528, 1628, 1732, 1839, 1949]
    },
    'binary': {
        'L': [17, 32, 53, 78, 106, 134, 154, 192, 230, 271, 321, 367, 425, 458, 520, 586, 644, 718, 792, 858, 929, 1003, 1091, 1171, 1273, 1367, 1465, 1528, 1628, 1732, 1839, 1949, 2071, 2191, 2306, 2434, 2566, 2702, 2812, 2956],
        'M': [14, 26, 42, 62, 84, 106, 122, 152, 180, 213, 251, 287, 331, 362, 412, 450, 504, 560, 624, 666, 711, 779, 857, 911, 997, 1059, 1125, 1190, 1264, 1370, 1452, 1538, 1628, 1722, 1809, 1911, 1989, 2099, 2213, 2331],
        'Q': [11, 20, 32, 46, 60, 74, 86, 108, 130, 151, 177, 203, 241, 258, 292, 322, 364, 394, 442, 482, 509, 565, 611, 661, 715, 751, 805, 868, 908, 982, 1030, 1112, 1168, 1228, 1283, 1351, 1423, 1499, 1579, 1663],
        'H': [7, 14, 24, 34, 44, 58, 64, 84, 98, 119, 137, 155, 177, 194, 220, 250, 280, 310, 338, 382, 403, 439, 461, 511, 535, 593, 625, 658, 698, 742, 790, 842, 898, 958, 1016, 1080, 1150, 1226, 1306, 1393]
    },
    'kanji': {
        'L': [10, 20, 32, 48, 65, 82, 95, 118, 141, 167, 198, 226, 262, 282, 320, 361, 397, 442, 488, 528, 572, 618, 672, 721, 784, 842, 902, 940, 1002, 1066, 1132, 1201, 1273, 1347, 1417, 1496, 1577, 1661, 1729, 1817],
        'M': [8, 16, 26, 38, 52, 65, 75, 93, 111, 131, 155, 177, 204, 223, 254, 277, 310, 345, 384, 410, 438, 480, 528, 561, 614, 652, 692, 732, 778, 843, 894, 947, 1002, 1060, 1113, 1176, 1224, 1286, 1354, 1426],
        'Q': [7, 12, 20, 28, 37, 45, 53, 66, 80, 93, 109, 125, 149, 159, 181, 203, 233, 253, 283, 313, 341, 385, 406, 442, 464, 514, 538, 596, 628, 661, 701, 745, 793, 845, 901, 961, 986, 1054, 1096, 1142],
        'H': [4, 8, 15, 21, 27, 36, 39, 52, 60, 74, 85, 96, 109, 120, 136, 154, 172, 190, 206, 223, 240, 262, 282, 305, 328, 351, 366, 397, 442, 468, 496, 534, 559, 604, 634, 684, 719, 756, 790, 832]
                
    }
}

# transposes a 2D array to the target 2D array
def transpose_array(start_x, start_y, array, target_array):
    for i in range(len(array)):
        for j in range(len(array[i])):
            target_array[start_y + i][start_x + j] = array[i][j]
            
def draw_array(pixels, start_x, start_y, array):
    for i in range(len(array)):
        for j in range(len(array[i])):
            pixels[start_x + j, start_y + i] = (0, 0, 0) if array[i][j] == 1 else (255, 255, 255)

margin = 4

position_marking = [
    [1,1,1,1,1,1,1],
    [1,0,0,0,0,0,1],
    [1,0,1,1,1,0,1],
    [1,0,1,1,1,0,1],
    [1,0,1,1,1,0,1],
    [1,0,0,0,0,0,1],
    [1,1,1,1,1,1,1],
]

# alignment pattern
alignment_pattern = [
    [1,1,1,1,1],
    [1,0,0,0,1],
    [1,0,1,0,1],
    [1,0,0,0,1],
    [1,1,1,1,1],
]

format_information_pattern = [1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1]

def generate_qr(data, correction_level='M'):
    qr_version = get_version_number(data, correction_level)
    qr_width = 29  # Assuming Version 3 (29x29) for simplicity in this example
    
    # initialize a qr_width * qr_width 2D array
    final_array = [[0 for _ in range(qr_width)] for _ in range(qr_width)]

    image = Image.new('RGB', (qr_width, qr_width), color='white')
    pixels = image.load()
    
    # draw the position markers
    transpose_array(margin, margin, position_marking, final_array)
    transpose_array(qr_width - 7 - margin, margin, position_marking, final_array)
    transpose_array(margin, qr_width - 7 - margin, position_marking, final_array)

    # draw the alignment pattern
    alignment_positions = [(qr_width - 9, qr_width - 9)]
    transpose_array(alignment_positions[0][0] - 2, alignment_positions[0][1] - 2, alignment_pattern, final_array)

    # draw the timing pattern
    for i in range(8, qr_width - 8):
        final_array[i][6] = 1 if i % 2 == 0 else 0
        final_array[6][i] = 1 if i % 2 == 0 else 0

    # draw the format information
    draw_array(pixels, margin, margin, final_array)
    return image

def get_version_number(data, correction_level):
    # determine data type
    if data.isnumeric():
        data_type = 'numeric'
    elif data.isalnum():
        data_type = 'alphanumeric'
    elif all(ord(char) < 256 for char in data):
        data_type = 'binary'
    else:
        data_type = 'kanji'
        
    # determine the correction level
    correction_level = correction_level.upper()
    if correction_level not in ['L', 'M', 'Q', 'H']:
        raise ValueError('Invalid correction level')
    
    # determine the version number
    for i in range(1, 41):
        if len(data) <= max_characters[data_type][correction_level][i - 1]:
            return i
    
    raise ValueError('Data is too long for the given correction level')

# Step 4: Save or display the image
image = generate_qr('HELLO123', correction_level='M')
image.save('output_image.png')
image.show()
