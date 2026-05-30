import random
import string

length = int(input("Enter Password Length: "))

if length < 4:
    print("Password length should be at least 4")

else:
    pass_list = []

    pass_list.append(random.choice(string.ascii_uppercase))
    pass_list.append(random.choice(string.ascii_lowercase))
    pass_list.append(random.choice(string.digits))
    pass_list.append(random.choice(string.punctuation))

    all_characters = string.ascii_letters + string.digits + string.punctuation

    for i in range(length - 4):
        random_char = random.choice(all_characters)
        pass_list.append(random_char)

    random.shuffle(pass_list)

    final_password = ""

    for i in pass_list:
        final_password = final_password + i

    print("Generated Password:", final_password)