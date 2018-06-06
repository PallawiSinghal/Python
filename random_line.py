import os
import random

filename ='yourpath/2007_test.txt'
train_path = 'yourpath/n____2007_test.txt'
length = 3349
with open(filename, "rb") as source:
    lines = [line for line in source]

    random_choice = random.sample(lines, length)
    for text_in_list in random_choice:
        file_to_write = open(train_path,"a")
        file_to_write.write(text_in_list)
