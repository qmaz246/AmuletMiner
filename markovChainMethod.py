import hashlib
import random
import sys
import os
import re

def save_amulet(poem, bits, rarity):
	
	for ques in poem.split(" "):
		if '\n' not in ques:
			word = re.sub(r'[^\w\s]','', ques)
			break
	files = os.listdir('amulets/')
	if files != []:
		for filename in files:
			# Check if word was already used
			if word == filename.split("_")[0]:
				# check if rarity was used or not
				if rarity == filename.split("_")[2]:
					title = "_".join([word, str(int(filename.split("_")[1]) + 1), rarity]) + ".txt"
				else:
					title = "_".join([word, str(int(filename.split("_")[1])), rarity]) + ".txt"
			else:
				title = "_".join([word, "0", rarity]) + ".txt"
	else:
		title = "_".join([word, "0", rarity]) + ".txt"

	filepath = "amulets/" + title
	print(filepath)
	# end for loop
	with open((filepath), "w") as file:
		file.writelines([poem, "\n", bits])

	return 0

if __name__ == '__main__':
	print("Finding Amulets: ")
	
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
	for i in range(10000000):
		word1 = random.choice(list(chain.keys())) #random first word
		message = word1.capitalize()
		
		count = random.randint(count_min, count_max)
		# Picks the next word over and over until word count achieved
		while len(message.split(' ')) < count:
			word2 = random.choice(chain[word1])
			word1 = word2
			message += ' ' + word2

		# # creates new file with output and prints it to the terminal
		# with open("output.txt", "w") as file:
		# 	file.write(message)
		# output = open("output.txt","r")
		# string = output.read()
		string = message
		text = bytes(string, 'utf-8')
		if len(text)<=64:
			hash_object = hashlib.sha256(text)
			hex_dig = hash_object.hexdigest()
			if('8888888888' in hex_dig):
				print(string)
				print(len(text))
				print(hex_dig)
				print("?????")
				save_amulet(string, hex_dig, "?????")
				print("")
			elif('888888888' in hex_dig):
				print(string)
				print(len(text))
				print(hex_dig)
				print("Mythic")
				save_amulet(string, hex_dig, "Mythic")
				print("")
			elif('88888888' in hex_dig):
				print(string)
				print(len(text))
				print(hex_dig)
				print("Legendary")
				save_amulet(string, hex_dig, "Legendary")
				print("")
			elif('8888888' in hex_dig):
				print(string)
				print(len(text))
				print(hex_dig)
				print("Epic")
				save_amulet(string, hex_dig, "Epic")
				print("")
			# elif('888888' in hex_dig):
			# 	print(string)
			# 	print(len(text))
			# 	print(hex_dig)
			# 	print("Rare")
			# 	save_amulet(string, hex_dig, "Rare")		
			# 	print("")
			# elif('88888' in hex_dig):
			# 	print(string)
			# 	print(len(text))
			# 	print(hex_dig)
			# 	print("Uncommon")
			#	save_amulet(string, hex_dig, "Uncommon")
			# 	print("")
			# elif('8888' in hex_dig):
			# 	print(string)
			# 	print(len(text))
			# 	print(hex_dig)
			# 	print("Common")
			# 	save_amulet(string, hex_dig, "Common")
			# 	print("")
