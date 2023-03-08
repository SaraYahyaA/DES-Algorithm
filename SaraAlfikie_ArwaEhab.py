####################################################################################
##					Helper Functions Already Implemented For You				####
####################################################################################

# Hexadecimal to binary conversion
import numpy as np
def hex2bin(s):
	mp = {'0': "0000",
		'1': "0001",
		'2': "0010",
		'3': "0011",
		'4': "0100",
		'5': "0101",
		'6': "0110",
		'7': "0111",
		'8': "1000",
		'9': "1001",
		'A': "1010",
		'B': "1011",
		'C': "1100",
		'D': "1101",
		'E': "1110",
		'F': "1111"}
	bin = ""
	for i in range(len(s)):
		bin = bin + mp[s[i]]
	return bin

# Binary to hexadecimal conversion
def bin2hex(s):
	mp = {"0000": '0',
		"0001": '1',
		"0010": '2',
		"0011": '3',
		"0100": '4',
		"0101": '5',
		"0110": '6',
		"0111": '7',
		"1000": '8',
		"1001": '9',
		"1010": 'A',
		"1011": 'B',
		"1100": 'C',
		"1101": 'D',
		"1110": 'E',
		"1111": 'F'}
	hex = ""
	for i in range(0, len(s), 4):
		ch = ""
		ch = ch + s[i]
		ch = ch + s[i + 1]
		ch = ch + s[i + 2]
		ch = ch + s[i + 3]
		hex = hex + mp[ch]

	return hex

# Binary to decimal conversion
def bin2dec(binary):

	binary1 = binary
	decimal, i, n = 0, 0, 0
	while(binary != 0):
		dec = binary % 10
		decimal = decimal + dec * pow(2, i)
		binary = binary//10
		i += 1
	return decimal

# Decimal to binary conversion
def dec2bin(num):
	res = bin(num).replace("0b", "")
	if(len(res) % 4 != 0):
		div = len(res) / 4
		div = int(div)
		counter = (4 * (div + 1)) - len(res)
		for i in range(0, counter):
			res = '0' + res
	return res



####################################################################################
##					Permutations Tables found in the documentation				####
####################################################################################

# Table of Position of 64 bits at initial level: Initial Permutation Table
initial_permutation = [58, 50, 42, 34, 26, 18, 10, 2,
				60, 52, 44, 36, 28, 20, 12, 4,
				62, 54, 46, 38, 30, 22, 14, 6,
				64, 56, 48, 40, 32, 24, 16, 8,
				57, 49, 41, 33, 25, 17, 9, 1,
				59, 51, 43, 35, 27, 19, 11, 3,
				61, 53, 45, 37, 29, 21, 13, 5,
				63, 55, 47, 39, 31, 23, 15, 7]

# Expansion E-box Table
expansion_E_box = [32, 1, 2, 3, 4, 5, 4, 5,
		6, 7, 8, 9, 8, 9, 10, 11,
		12, 13, 12, 13, 14, 15, 16, 17,
		16, 17, 18, 19, 20, 21, 20, 21,
		22, 23, 24, 25, 24, 25, 26, 27,
		28, 29, 28, 29, 30, 31, 32, 1]

# Straight Permutation Table
straight_perumtation = [16, 7, 20, 21,
	29, 12, 28, 17,
	1, 15, 23, 26,
	5, 18, 31, 10,
	2, 8, 24, 14,
	32, 27, 3, 9,
	19, 13, 30, 6,
	22, 11, 4, 25]

# S-box Table
sbox = [[[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
		[0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
		[4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
		[15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]],

		[[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
		[3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
		[0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
		[13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]],

		[[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
		[13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
		[13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
		[1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]],

		[[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
		[13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
		[10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
		[3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]],

		[[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
		[14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
		[4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
		[11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]],

		[[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
		[10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
		[9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
		[4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]],

		[[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
		[13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
		[1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
		[6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]],

		[[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
		[1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
		[7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
		[2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]]

# Final/invers Permutation Table
final_permutation = [40, 8, 48, 16, 56, 24, 64, 32,
			39, 7, 47, 15, 55, 23, 63, 31,
			38, 6, 46, 14, 54, 22, 62, 30,
			37, 5, 45, 13, 53, 21, 61, 29,
			36, 4, 44, 12, 52, 20, 60, 28,
			35, 3, 43, 11, 51, 19, 59, 27,
			34, 2, 42, 10, 50, 18, 58, 26,
			33, 1, 41, 9, 49, 17, 57, 25]

# Permuted Choice 1 Table : Compression of key from 64 bits to 56 bits
permuted_choice1 = [57, 49, 41, 33, 25, 17, 9,
		1, 58, 50, 42, 34, 26, 18,
		10, 2, 59, 51, 43, 35, 27,
		19, 11, 3, 60, 52, 44, 36,
		63, 55, 47, 39, 31, 23, 15,
		7, 62, 54, 46, 38, 30, 22,
		14, 6, 61, 53, 45, 37, 29,
		21, 13, 5, 28, 20, 12, 4]

# Permuted Choice 2 Table : Compression of key from 56 bits to 48 bits
permuted_choice2 = [14, 17, 11, 24, 1, 5,
			3, 28, 15, 6, 21, 10,
			23, 19, 12, 4, 26, 8,
			16, 7, 27, 20, 13, 2,
			41, 52, 31, 37, 47, 55,
			30, 40, 51, 45, 33, 48,
			44, 49, 39, 56, 34, 53,
			46, 42, 50, 36, 29, 32]

# Number of bit shifts for each round Table
shift_table = [1, 1, 2, 2,
			2, 2, 2, 2,
			1, 2, 2, 2,
			2, 2, 2, 1]


####################################################################################
##					Actual function to impelement the DES algorithm				####
####################################################################################


# Permute function to rearrange the bits
def permute(string, table):
 permutation = ""
 for i in range(0, len(table)):
  
  permutation=permutation+string[table[i]-1]
 return permutation

# shifting the bits towards left by nth shifts
def shift_left(k, nth_shifts):
	#TODO #2  Complete the function to make circular left shift (rotating) of the string s by n bits.
 string=""
 string = k[nth_shifts:]+k[0:nth_shifts]
 return string
         
     
# calculating xor of two strings of binary number a and b
def xor(a, b):
 ans = ""
	#TODO #3  Complete the function to return the XOR result for two strings a and b.
#  a=bin2dec(int(a))
#  b=bin2dec(int(b))
#  ans=np.bitwise_xor(a,b)
#  ans=dec2bin(ans)
 for i in range(len(a)):
     if a[i]==b[i]:
         ans+="0"
     else:
         ans+="1"

 return ans

# Precompute the keys for all the 16 rounds of the algorithm to be used later.
def keyPreparation(key):

	# TODO #4 Convert the hex key into binary
 key = hex2bin(key)
 


	# TODO #5 get 56 bit key from 64 bit. Which function should we use from the above functions ?
 key = permute(key, permuted_choice1)

	# TODO #6 Split the key to two equal halves.
 left = key[0:int(len(key)/2)]  
 right = key[int(len(key)/2):len(key)] 


 rounds_keys = [] 	# An array to presave each round key to be used later --> len(rounds_keys) = 16
 
 for i in range(0, 16):

		# TODO #7 Shift left each half of the key. Which function will we use ? And How ?
    left = shift_left(left,shift_table[i])
    right = shift_left(right,shift_table[i])
    

		# TODO #8 Go to the lab document, figure out which operation should be done here and do it :). 
    com_key=left+ right
	
		# TODO #9 get 48 bit key from 56 bit. Which function should we use from the above functions ?
    print(len(com_key))
    round_key = permute(com_key, permuted_choice2)
    

		# Finally save this round key in the array to be used in the encryption function.
    rounds_keys.append(round_key)

 return rounds_keys

# Encryption/ Decryption function
def encrypt(pt, RoundKey):
	# TODO #10 Convert the hex text into binary
 pt = hex2bin(pt)

	# TODO #11 What is the first step in the encryption algorithm ? Do it :)
 pt = permute(pt,initial_permutation) 

	# TODO #12 Split the palint text into to equal halfs
 left = pt[0:int(len(pt)/2)] 
 right = pt[int(len(pt)/2):len(pt)] 


 
	# Start the 16 rounds

 for i in range(0, 16):
        
		# TODO #13 Expansion D-box: Expanding the 32 bits data into 48 bits. I think you got the point :D.
		# Hint: Go to the document. do we expand both halves ? which half that we expand ?
        
         right_expanded = permute(right,expansion_E_box) 

		# TODO #14 XOR RoundKey[i] and right_expanded
         xor_x = xor(right_expanded, RoundKey[i]) 
         

		# S-boxex: substituting the value from s-box table by calculating row and column
         sbox_str = ""
		# TODO #15 Impelement the S-Box substitution logic.
		# Hint : Do you deal with binary or decimal numbers ?
         for j in range(0,8):
            row=bin2dec(int(xor_x[j*6]+xor_x[j*6 +5]))
            col=bin2dec(int(xor_x[j*6+1]+xor_x[j*6 +2]+xor_x[j*6 +3]+xor_x[j*6 +4]))
            sbox_str+=dec2bin(sbox[j][row][col])


		# TODO #16 Update the S-Box output by doing Straight Permutation. 
         sbox_str = permute(sbox_str,straight_perumtation)
         # TODO #17 Go to the lab document, figure out which operation should be done here and do it :).
         result = xor(left,sbox_str)
         left = result
         # TODO #18 According to the lab document We need to swap the two halves at the end of each round.
		  
    
        # Hint : Is there an exception ?!
         if(i!=15):
             temp=right
             right=left
             left=temp
    # Combination of the two halves at the end of the rou 
 combine = left + right

	# TODO #19 Final permutation: final rearranging of bits to get cipher text
 cipher_text = permute(combine, final_permutation) 
 return cipher_text



def decrypt(cipher_text, rkb):
	# TODO #20 Impelement the decryption algorithm and return the original message
	# Hint : What is the differences between encryption and decryption algorithms ?!
	original_message = encrypt(cipher_text, rkb[::-1])
 
	return bin2hex(original_message)
####################################################################################
##					Our program starts here (Main Function)						####
####################################################################################

# Algorithm Inputs
plaint_text = "123456ABCD132536"
key = "AABB09182736CCDD"

# Key generation
rounds_keys = keyPreparation(key)
print("HI")
print("Encryption")
cipher_text = bin2hex(encrypt(plaint_text, rounds_keys))
print("Cipher Text : ", cipher_text)

print("Decryption")
original_message = decrypt(cipher_text,rounds_keys)
print("Plain Text : ", original_message)
