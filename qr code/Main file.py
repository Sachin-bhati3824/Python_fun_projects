import numpy as np 
import random 
import os 
import time
import math 
import reedsolo 
from PIL import Image
import matplotlib.pyplot as plt



def hexcode(char):
    return(hex(ord(char))[2:])


def binary(char):
    ascii_val = ord(char)
    binary_val = bin(ascii_val)[2:].zfill(8) 
    return binary_val

def split_into_chunks(s, chunk_size=8):
    return [s[i:i+chunk_size] for i in range(0, len(s), chunk_size)]


def generate_ecc(data_codewords, num_ecc_codewords):
    rs = reedsolo.RSCodec(num_ecc_codewords)  
    ecc_codewords = rs.encode(data_codewords)[-num_ecc_codewords:]  
    return list(ecc_codewords)


def hex_to_bin(hex_string):
    return bin(int(hex_string, 16))[2:].zfill(8)



url = "place your url here"
url_char = list(url)
dict_1 = {}
list_main  = [] 
for i in range(len(url_char)):
    list_a = [] 
    list_a.append(url_char[i])
    list_a.append(hexcode(url_char[i]))
    list_a.append(binary(url_char[i]))
    list_main.append(list_a)
data_bits = ''
for i in range(len(list_main)):
    data_bits += str(list_main[i][2])
ECC_low_max_bits = [19  ,34  ,55  ,80  ,108  ,136  ,156  ,194  ,232  ,274  ,324  ,370  ,428  ,461  ,523  ,589  ,647  ,721  ,795  ,861  ,932  ,1006  ,1094  ,1174  ,1276  ,1370  ,1468  ,1531  ,1631  ,1735  ,1843  ,1955  ,2071  ,2191  ,2306  ,2434  ,2566  ,2702  ,2812  ,2956  ]
ECC_low_max_bits = list(map(lambda x: x*8 ,ECC_low_max_bits))
#select the veersion of the qr code in the ECC low only 
for i in range(len(ECC_low_max_bits)):
    if ECC_low_max_bits[i] >= len(data_bits):
        version = i 
        break

max_bits = ECC_low_max_bits[version] 
final_bitcode = "0100" + str(bin(int(len(data_bits)/8))[2:].zfill(8)) + data_bits 
x = 0 
while True:
    
    if len(final_bitcode) < max_bits:
        if x < 4:
            final_bitcode+= "0"
            x += 1 
        else:
            break
y = 0 
while True :
    if not len(final_bitcode)%8 == 0  :
        final_bitcode += "0"
        y +=1 
    else : 
        break
flag1 = True 
flag2 = False 
while True :
    if len(final_bitcode)< max_bits:
        if flag1 :
            final_bitcode+= "11101100"
            flag2 = True
            flag1 = False
    if len(final_bitcode)<max_bits:
        if flag2 :
            final_bitcode+= "00010001"
            flag2 = False
            flag1 = True 

    if len(final_bitcode) == max_bits:
        break



final_bitcode_divi = split_into_chunks(final_bitcode)
final_bitcode_divi_hex = list(map(lambda x: hex(int(x, 2))[2:].upper(), final_bitcode_divi))

final_bitcode_divi = list(map(lambda x : int(hex(int(x,2)).upper(),16),final_bitcode_divi))
ECC_low_codewords = [7, 10, 15, 20, 26, 34, 42, 52, 62, 74, 86, 98, 112, 126, 140, 154, 170, 186, 202, 220, 238, 258, 278, 298, 318, 338, 358, 378, 398, 418, 438, 458, 478, 498, 518, 538, 558, 578, 598, 618]
ECC_codewords = ECC_low_codewords[version]

ecc_code = list(map(lambda x : hex(x)[2:].upper(), generate_ecc(final_bitcode_divi,ECC_codewords)))
final_bitcode_divi_hex = list(map(lambda x :x.zfill(2),final_bitcode_divi_hex))
ecc_code = list(map(lambda x : x.zfill(2),ecc_code))
final = []

for i in range(len(final_bitcode_divi_hex)):
    final.append(final_bitcode_divi_hex[i])
for i in range(len(ecc_code)):
    final.append(ecc_code[i])



final = list(map(lambda x : hex_to_bin(x),final))

ready_to_push = ''
for i in range(len(final)):
    ready_to_push+= final[i]


module_recq = 21 + 4*(version)
qr_matrix = np.full((module_recq,module_recq), 7)
 

def the_pattern(matrix,x,y,size):
    layers = [1, 0, 1]  
    layer_size = size  

    for layer in layers:
        for i in range(x, x + layer_size):
            for j in range(y, y + layer_size):
                matrix[i][j] = layer  
      
        x += 1
        y += 1
        layer_size -= 2 
    return matrix


def draw_the_line(matrix,x,size,orientation,int):
    if orientation == "x":
        if int == 0 :
            for i in range(size):
                matrix[i][x] = 0
        if int == 1 :
            for i in range(size):
                matrix[i][x] = 1
        if int == 7 :
            for i in range(size):
                matrix[i][x] = 7
        if int ==-11:
            flag_a = True
            for i in range(size):
                if flag_a :
                    matrix[i][x] = 1 
                    flag_a = False
                    continue
                if not flag_a:
                    matrix[i][x] = 0 
                    flag_a = True
                    continue
        if int ==-10:
            flag_b = True
            for i in range(size):
                if flag_b :
                    matrix[i][x] = 0 
                    flag_b = False
                    continue
                if not flag_b:
                    matrix[i][x] = 1
                    flag_b = True
                    continue
    if orientation == "y":
        if int == 0 :
            for i in range(size):
                matrix[x][i] = 0
        if int == 1 :
            for i in range(size):
                matrix[x][i] = 1
        if int == 7 :
            for i in range(size):
                matrix[x][i] = 7
        if int ==-11:
            flag_a = True
            for i in range(size):
                if flag_a :
                    matrix[x][i] = 1 
                    flag_a = False
                    continue
                if not flag_a:
                    matrix[x][i] = 0 
                    flag_a = True
                    continue
        if int ==-10:
            flag_b = True
            for i in range(size):
                if flag_b :
                    matrix[x][i] = 0 
                    flag_b = False
                    continue
                if not flag_b:
                    matrix[x][i] = 1
                    flag_b = True
                    continue       
    return matrix 

def proper_line(matrix: list , x: int , actual_x: int , size: int , orientation: str , int):

    draw_the_line(matrix,x,(size+actual_x),orientation,int)
    draw_the_line(matrix,x,actual_x,orientation,7)
    return(matrix)

def finder_patterns(matrix):
    qr_matrix = matrix
    #timing patterns 
    qr_matrix  = proper_line(qr_matrix,6,0,len(qr_matrix),"x",-11)
    qr_matrix  = proper_line(qr_matrix,6,0,len(qr_matrix),"y",-11)

    #finder patterns
    qr_matrix = the_pattern(qr_matrix,0,0,7)
    qr_matrix = the_pattern(qr_matrix,len(qr_matrix)-7,0,7)
    qr_matrix = the_pattern(qr_matrix,0,len(qr_matrix)-7,7)

    # #separators 
    qr_matrix  = proper_line(qr_matrix,7,0,8,"x",0)
    qr_matrix  = proper_line(qr_matrix,7,0,8,"y",0)
    qr_matrix  = proper_line(qr_matrix,7,len(qr_matrix)-8,8,"x",0)
    qr_matrix  = proper_line(qr_matrix,len(qr_matrix)-8,0,8,"y",0)
    qr_matrix  = proper_line(qr_matrix,len(qr_matrix)-8,0,8,"x",0)
    qr_matrix  = proper_line(qr_matrix,7,len(qr_matrix)-8,8,"y",0)
    return qr_matrix 


qr_matrix  = finder_patterns(qr_matrix)




alignment_patterns = [
    [],  # Version 1: No Alignment Pattern
    [[16, 16]],
    [[20, 20]],
    [[24, 24]],
    [[28, 28]],
    [[32, 32]],
    [[4, 20], [20, 20], [36, 20]],
    [[4, 24], [24, 24], [44, 24]],
    [[4, 28], [28, 28], [48, 28]],
    [[4, 32], [32, 32], [52, 32]],
    [[4, 28], [26, 28], [48, 28]],
    [[4, 30], [28, 30], [52, 30]],
    [[4, 32], [30, 32], [56, 32]],
    [[4, 24], [22, 24], [40, 24], [58, 24]],
    [[4, 24], [22, 24], [44, 24], [64, 24]],
    [[4, 24], [24, 24], [48, 24], [68, 24]],   
    [[4, 28], [26, 28], [52, 28], [72, 28]],
    [[4, 28], [24, 28], [50, 28], [76, 28]],
    [[4, 28], [26, 28], [54, 28], [80, 28]],
    [[4, 32], [30, 32], [58, 32], [84, 32]],
    [[4, 26], [22, 26], [42, 26], [62, 26], [82, 26]],
    [[4, 24], [22, 24], [40, 24], [58, 24], [86, 24]],
    [[4, 28], [26, 28], [48, 28], [70, 28], [92, 28]],
    [[4, 26], [24, 26], [46, 26], [68, 26], [90, 26]],
    [[4, 30], [28, 30], [52, 30], [76, 30], [100, 30]],
    [[4, 28], [26, 28], [50, 28], [74, 28], [98, 28]],
    [[4, 32], [30, 32], [56, 32], [82, 32], [108, 32]],
    [[4, 24], [22, 24], [40, 24], [58, 24], [76, 24], [94, 24]],
    [[4, 28], [26, 28], [48, 28], [70, 28], [92, 28], [114, 28]],
    [[4, 24], [22, 24], [40, 24], [58, 24], [76, 24], [94, 24], [112, 24]]
]

recq_alignment = alignment_patterns[version]

for i in range(len(recq_alignment)):
    qr_matrix = the_pattern(qr_matrix,recq_alignment[i][0],recq_alignment[i][1],5)

def dummy_format_bits(matrix):
    proper_line(matrix,8,len(qr_matrix)-8,8,"y",0)
    proper_line(matrix,8,len(matrix)-7,7,"x",0)
    matrix[len(matrix)-8][8] = 1
    proper_line(matrix,8,0,6,"y",0) 
    proper_line(matrix,7,0,9,"y",0)
    matrix[6][7] = 0
    matrix[6][8] = 1 
    matrix[8][6] = 1 
    matrix[8][7] = 0 
    matrix[8][8] = 0 
    proper_line(matrix,7,0,6,"x",0)
    proper_line(matrix,8,0,6,"x",0)
    return matrix 

qr_matrix  = dummy_format_bits(qr_matrix)


def just_mask_0_it(i,j,binary_bit):
    binary_bit = int(binary_bit)
    if (i + j) % 2 == 0:
        binary_bit ^= 1
    else:
        binary_bit = binary_bit 
    return binary_bit 


def zigzag(matrix,binary_data):
    indicator_i  =len(matrix) - 1
    indicator_j = len(matrix) -1    

    flag_1 = True
    flag_2 = False
    flag_3 = True
    flag_4 = True
    border = 0 
    count =  0 
    a = 0 
    b = 0 
    c =0 
    count_max = 0 
    while True:
        count_max+=1 
        if count > len(ready_to_push) -1  :
            break 
        if flag_1 :
            if flag_4  :
                if matrix[indicator_i][indicator_j] == 7:
                    matrix[indicator_i][indicator_j] = just_mask_0_it(indicator_i,indicator_j,binary_data[a])
                    a +=1
                    count+=1 
                flag_4 = False 

            indicator_j -=1 
            if matrix[indicator_i][indicator_j] == 7:
                matrix[indicator_i][indicator_j] = just_mask_0_it(indicator_i,indicator_j,binary_data[a])
                a+=1
                count+=1 

            
            
        


            if indicator_i == 0   :
                indicator_i = len(matrix) - 1 
                indicator_j -=1 
            
            
            indicator_i -=1
            indicator_j +=1
            if matrix[indicator_i][indicator_j] == 7:
                matrix[indicator_i][indicator_j] = just_mask_0_it(indicator_i,indicator_j,binary_data[a])
                a+=1
                count+=1 
            if indicator_j == 6:
                indicator_j -= 1

        if flag_2 :
            if flag_3 :
                indicator_j-=2
                if matrix[indicator_i][indicator_j] == 7:
                    matrix[indicator_i][indicator_j] =just_mask_0_it(indicator_i,indicator_j,binary_data[a])
                    a+=1 
                    count+=1 
                flag_3 = False
            indicator_j-=1
            if matrix[indicator_i][indicator_j] == 7: 
                matrix[indicator_i][indicator_j] =just_mask_0_it(indicator_i,indicator_j,binary_data[a])
                a+=1 
                count+=1 
            indicator_i +=1 
            indicator_j +=1
            if matrix[indicator_i][indicator_j] == 7: 
                matrix[indicator_i][indicator_j] = just_mask_0_it(indicator_i,indicator_j,binary_data[a])
                a+=1 
                count+=1 
            if indicator_j == 6:
                indicator_j -= 1

        

        if indicator_i == 0   :
            
            flag_1  = False

            flag_2 = True

            if b >= 1: 
                indicator_j -=1
                if matrix[indicator_i][indicator_j] == 7:
                    matrix[indicator_i][indicator_j] = just_mask_0_it(indicator_i,indicator_j,binary_data[a])
                    a+=1 
                    count+=1 
                indicator_j-=1
                if matrix[indicator_i][indicator_j] == 7: 
                    matrix[indicator_i][indicator_j] = just_mask_0_it(indicator_i,indicator_j,binary_data[a])
                    a+=1 
                    count+=1 
            b+=1 
            

        if indicator_i == len(matrix) -1 :
            indicator_j -=1 
            if matrix[indicator_i][indicator_j] == 7:
                matrix[indicator_i][indicator_j] = just_mask_0_it(indicator_i,indicator_j,binary_data[a])
                a+=1 
                count+=1 
            indicator_j -=1
            if matrix[indicator_i][indicator_j] == 7: 
                matrix[indicator_i][indicator_j] = just_mask_0_it(indicator_i,indicator_j,binary_data[a])
                a+=1 
                count+=1
            flag_1 = True
            flag_2 = False 


    return matrix 

qr_matrix = zigzag(qr_matrix,ready_to_push)

for i in range(len(qr_matrix)):
    for j in range(len(qr_matrix[i])):
        if qr_matrix[i][j] ==7  :
            qr_matrix[i][j] = just_mask_0_it(i,j,0)


format_bits = "111011111000100"

def insert_format_bits(matrix, format_bits):
    size = len(matrix)
    bits = [int(b) for b in format_bits]

    positions_primary = [
        
        (8, 0), (8, 1), (8, 2), (8, 3), (8, 4), (8, 5), (8, 7),
        (8,8) ,  (7,8),(5,8),(4,8),(3,8),(2,8),(1,8),(0,8)
        
    ]

    positions_mirrored = [
        
        (size - 1, 8), (size - 2, 8), (size - 3, 8), (size - 4, 8),
        (size - 5, 8), (size - 6, 8), (size - 7, 8) , 
        (8, size - 8), (8, size - 7), (8, size - 6), (8, size - 5),
        (8, size - 4), (8, size - 3), (8, size - 2), (8, size - 1)
    ]

    for i in range(len(bits)):
        matrix[positions_primary[i][0]][positions_primary[i][1]] = bits[i] 
        matrix[positions_mirrored[i][0]][positions_mirrored[i][1]] = bits[i] 

    return matrix

qr_matrix = insert_format_bits(qr_matrix,format_bits)

plt.figure(figsize=(6, 6))
plt.imshow(qr_matrix, cmap="binary", interpolation="nearest")
plt.axis('off')
plt.show()
