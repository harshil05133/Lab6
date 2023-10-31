# Harshil Rathod

#Encode Function
def encode_password(password):
	string_password = ''
	#Iterates through characters in string. Adds 3, modulo 10.
	for element in password:
		int_password = (int(element) + 3) % 10
		string_password += str(int_password)
	return string_password

#Decode Function
def decode_password(password):
	string_password = ""
	#Iterates through characters in string. Subtracts 3, modulo 10.
	for element in password:
		int_password = (int(element) - 3)%10
		string_password += str(int_password)
	return string_password

#Main Function
def main():
	global encoded_password
	program = True
	#Keep showing menu until user has exited.
	while program:
		print("Menu")
		print("-------------")
		print("1. Encode")
		print("2. Decode")
		print("3. Quit\n")

		#Ask for user input
		user_input = input("Please enter an option: ")

		#Encode the password if user selected 1
		if user_input == '1':
			user_password = input("Please enter your password to encode: ")
			encoded_password = encode_password(user_password)
			print("Your password has been encoded and stored!\n")

		#Decode the password if user selected 2
		elif user_input == '2':
			decoded_password = decode_password(encoded_password)
			print(f"The encoded password is {encoded_password}, and the original password is {decoded_password}.")

		#Exit the program if user selected 3
		elif user_input == '3':
			program = False
			break

#Run Main
if __name__ == "__main__":
	main()
