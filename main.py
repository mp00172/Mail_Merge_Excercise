with open(file="Input/Letters/starting_letter.txt", mode="r") as starting_letter:
	starting_letter = starting_letter.readlines()

with open(file="Input/Names/invited_names.txt", mode="r") as names:
	names = names.readlines()

names = [name.strip("\n") for name in names]

for name in names:
	with open(file="Output/ReadyToSend/letter_for_{}".format(name), mode="a") as new_file:
		for line in starting_letter:
			new_file.write(line.replace("[name]", name))
