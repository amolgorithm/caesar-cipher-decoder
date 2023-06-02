code = str(input("Enter a common English word encoded with Caesar cipher: "))

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def rotate_word(given_code: str, rotations:int = 1) -> str:
	global alphabet
	
	rotated_code = list(given_code.lower())
	
	for i in range(len(rotated_code)):
		rotated_code[i] = alphabet[alphabet.index(rotated_code[i]) - rotations]
		
	return "".join(rotated_code)



eng_com_file = open("./english_dict/eng_com.dic", "r")
center_file = open("./english_dict/center.dic", "r")
color_file = open("./english_dict/color.dic", "r")
labeled_file = open("./english_dict/labeled.dic", "r")
ize_file = open("./english_dict/ize.dic", "r")
yze_file = open("./english_dict/yze.dic", "r")

eng_words_list = eng_com_file.read().split("\n") + center_file.read().split("\n") + color_file.read().split("\n") + labeled_file.read().split("\n") + ize_file.read().split("\n") + yze_file.read().split("\n")

eng_com_file.close()
center_file.close()
color_file.close()
labeled_file.close()
ize_file.close()
yze_file.close()



def decode():
	global alphabet, code
	
	if not code.isalpha():
		raise ValueError("code contains nonalpha characters!")
	
	
	rotating_code: str = code
	rotnum: int = 0
	error_found: bool = False
	
	suggestion_found: bool = False
	rotating_code_again: str = code + " "
	rotnum_again: int = 0
	suggestion_rotnum: int = 0
	
	while rotating_code not in eng_words_list:
		if rotnum > 25:
			print("\nNo decoded version of ", code, " was found in our dictionary :(", sep = "")
			error_found = True
			
			
			for a in alphabet:
				rotnum_again: int = 0
				
				while rotating_code_again not in eng_words_list and rotnum_again <= 25:
					rotating_code_again = rotate_word(rotating_code_again[:-1]) + a
					rotnum_again += 1
					
				if rotating_code_again in eng_words_list:
					suggestion_found = True
					suggestion_rotnum = rotnum_again
					break
					
			if not suggestion_found:
				rotating_code_again = " " + code
				rotnum_again = 0
				suggestion_rotnum = 0
				
				for a in alphabet:
					rotnum_again: int = 0
					
					while rotating_code_again not in eng_words_list and rotnum_again <= 25:
						rotating_code_again = a + rotate_word(rotating_code_again[1:])
						rotnum_again += 1
						
					if rotating_code_again in eng_words_list:
						suggestion_found = True
						suggestion_rotnum = rotnum_again
						break
			
			break
			
		print(rotnum, "rotations:", rotating_code)
		rotating_code = rotate_word(rotating_code)
		rotnum += 1
	
	print(rotnum, "rotations:", rotating_code)
		
	if not error_found:
		print("\nDecoded: ", rotating_code, sep = "")
		print(rotnum, " rotation", "" if rotnum == 1 else "s", " from '", rotating_code, "'", sep = "")
		
		
	if suggestion_found:
		if rotate_word(rotating_code_again, len(alphabet) - suggestion_rotnum)[len(rotating_code_again) - 1] != code[len(code) - 1]:
			print("Perhaps you meant '", code + rotate_word(rotating_code_again[len(rotating_code_again) - 1], len(alphabet) - suggestion_rotnum), "', the encoded version of '", rotating_code_again, "'?", sep = "")
		else:
			print("Perhaps you meant '", rotate_word(rotating_code_again[0], len(alphabet) - suggestion_rotnum) + code, "', the encoded version of '", rotating_code_again, "'?", sep = "")



decode()
