# Harshil Rathod
def encode_password(password):
	string_password = ''
	for element in password:
		int_password = (int(element) + 3) % 10
		string_password += str(int_password)
	return string_password


def decode_password(password):
	pass


def main():
	global encoded_password
	program = True
	while program:
		print("Menu")
		print("-------------")
		print("1. Encode")
		print("2. Decode")
		print("3. Quit\n")

		user_input = input("Please enter an option: ")

		if user_input == '1':
			user_password = input("Please enter your password to encode: ")
			encoded_password = encode_password(user_password)
			print("Your password has been encoded and stored!\n")

		elif user_input == '2':
			decoded_password = decode_password(encoded_password)
			print(f"The encoded password is {encoded_password}, and the original password is {decoded_password}.")

		elif user_input == '3':
			program = False
			break


if __name__ == "__main__":
	main()
