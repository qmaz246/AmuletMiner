import hashlib
import random
import sys

if __name__ == '__main__':
	print("Finding Amulets: ")
	

	for i in range(100000):
		poems = open("stray_birds.txt", "r").read()
		poems = ''.join([i for i in poems if not i.isdigit()]).replace("\n\n", " ").split(' ')
		# This process the list of poems. Double line breaks separate poems, so they are removed.
		# Splitting along spaces creates a list of all words.

		index = 1
		chain = {}
		count_min = 8 # Desired word count of output
		count_max = 15
		# This loop creates a dicitonary called "chain". Each key is a word, and the value of each key
		# is an array of the words that immediately followed it.
		for word in poems[index:]: 
			key = poems[index - 1]
			if key in chain:
				chain[key].append(word)
			else:
				chain[key] = [word]
			index += 1

		word1 = random.choice(list(chain.keys())) #random first word
		message = word1.capitalize()
		
		count = random.randint(count_min, count_max)
		# Picks the next word over and over until word count achieved
		while len(message.split(' ')) < count:
			word2 = random.choice(chain[word1])
			word1 = word2
			message += ' ' + word2

		# creates new file with output and prints it to the terminal
		with open("output.txt", "w") as file:
			file.write(message)
		output = open("output.txt","r")
		string = output.read()
		text = bytes(string, 'utf-8')
		if len(text)<=64:
			hash_object = hashlib.sha256(text)
			hex_dig = hash_object.hexdigest()
			if('8888888888' in hex_dig):
				print(string)
				print(len(text))
				print(hex_dig)
				print("?????")
				print("")
			elif('888888888' in hex_dig):
				print(string)
				print(len(text))
				print(hex_dig)
				print("Mythic")
				print("")
			elif('88888888' in hex_dig):
				print(string)
				print(len(text))
				print(hex_dig)
				print("Legendary")
				print("")
			elif('8888888' in hex_dig):
				print(string)
				print(len(text))
				print(hex_dig)
				print("Epic")
				print("")
			elif('888888' in hex_dig):
				print(string)
				print(len(text))
				print(hex_dig)
				print("Rare")		
				print("")
			elif('88888' in hex_dig):
				print(string)
				print(len(text))
				print(hex_dig)
				print("Uncommon")
				print("")
			# ~ elif('8888' in hex_dig):
				# ~ print(string)
				# ~ print(len(text))
				# ~ print(hex_dig)
				# ~ print("Common")
				# ~ print("")
