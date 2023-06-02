import math
import random


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def rotate_word(given_code: str, rotations:int = 1) -> str:
	global alphabet
	
	rotated_code = list(given_code.lower())
	
	for i in range(len(rotated_code)):
		rotated_code[i] = alphabet[alphabet.index(rotated_code[i]) - rotations]
		
	return "".join(rotated_code)



while True:
	word = input("Enter an English word or anything using only the English alphabet: ")
	if not word.isalpha():
		raise ValueError("code contains nonalpha characters!")
		

	num_of_rotations = random.randint(1, 25)
	encoded_form: str = rotate_word(word, num_of_rotations)
		
	print("Encoded form: ", encoded_form, end = "\n\n", sep = "")
