"""
chicken caesor salad
"""
import string

alpha_down = string.ascii_lowercase
alpha_up = string.ascii_uppercase

cipher_text = "qkbn{ePmv_lQL_kIMamZ_kQxpMZa_oMb_aW_pIZl}"
global plain_text, alpha_location
plain_text = ""
alpha_location = 0

print(f"Cipher text = {cipher_text}\n")
#find the shift value
one = "i"
two = "q"
shift = alpha_down.find(two) - alpha_down.find(one)
print(f"Shift Value = {shift}\n")


length = len(cipher_text)


for i in range(length):
	cipher_letter = cipher_text[i]
	if cipher_letter.islower() == True:
		alpha_location = alpha_down.find(cipher_letter)
		new_location = alpha_location - 8
		plain_text += alpha_down[new_location] 
	elif cipher_letter.isupper() == True:
		alpha_location = alpha_up.find(cipher_letter)
		new_location = alpha_location - 8
		plain_text += alpha_up[new_location]
	elif cipher_letter in ["{","_","}"]:
		plain_text += cipher_letter
print(f"Plain text = {plain_text}")