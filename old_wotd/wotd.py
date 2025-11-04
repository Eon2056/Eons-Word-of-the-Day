
# terminal commands to compile this code:
#   cd '\OneDrive\Documents\Python\PycharmProjects\Word of the Day'
#   py -m PyInstaller -F wotd.py

import os
import time
import random
import urllib.request


def nl():
    print()


def lines(*num):
    if num:
        print("-" * num[0])
    else:
        print("-" * 30)


def print_string(*args):
    string = ""
    strlen = 0
    strlen2 = 0
    str_list = []
    lens = []

    if isinstance(args[0], str):

        string = args[0]
        strlen = len(string)

        if len(args) == 2:
            for strings in args[1]:
                lens.append(len(strings))
            lens.sort()
            strlen2 = lens[-1]
            str_list = list(map(lambda i: i.ljust(strlen2), args[1]))

    elif isinstance(args[0], list):
        lens = list(map(lambda i: len(i), args[0]))
        lens.sort()
        strlen = lens[-1]
        str_list = list(map(lambda i: i.ljust(strlen), args[0]))

    nl()
    lines(strlen+10)

    if string:
        print(f"{string:^{strlen+10}}")
    if str_list:
        for str_print in str_list:
            print(f"{str_print:^{strlen+10}}")

    lines(strlen+10)
    nl()


FileNames = ("Unused_Words.txt", "Used_Words.txt")

# BasePath = os.getenv("USERPROFILE") + "\\OneDrive\\Documents\\MATLAB\\Word of the Day"

if os.path.exists(FileNames[0] and FileNames[1]):
    Unused_Path = os.path.abspath(FileNames[0])
    Used_Path = os.path.abspath(FileNames[1])

    print("\nWord files located:\n")
    print(Unused_Path)
    print(Used_Path)
    nl()

# elif os.path.exists(BasePath + FileNames[0] and BasePath + FileNames[1]):
#
#     Unused_Path = BasePath + "\\Unused_Words.txt"
#     Used_Path = BasePath + "\\Used_Words.txt"

else:

    print_string("\nWord files not found!" + "\nClosing program.")

    time.sleep(2)
    quit()


with open(Unused_Path, 'r') as Unused_File:
    Unused_List = [word.lower() for word in Unused_File.read().split("\n")]

with open(Used_Path, 'r') as Used_File:
    Used_List = [word.lower() for word in Used_File.read().split("\n")]

time.sleep(.5)

new_word_list = []


def list_sort():
    Unused_List.sort()
    Used_List.sort()


def dict_check(word):

    word = word.replace(" ", "%20")

    url = "https://merriam-webster.com//dictionary//" + word

    try:
        urllib.request.urlopen(url)
    except urllib.error.HTTPError:
        return False
    else:
        return True


def write(write_list, path):
    if write_list:
        write_list = [word for word in write_list if word != ""]
        with open(path, 'w') as file:
            for index in range(len(write_list) - 1):
                file.write(write_list[index] + "\n")
            file.write(write_list[len(write_list) - 1])
    else:
        with open(path, 'w') as file:
            file.write("")


def randword(unused):
    word = random.choice(unused)
    print("Selected Word:" + " " * 5 + word + " " * 5)

    return word


def word_of_the_day(unused, used):
    rep_yn = ""
    reroll = True
    yn = ["y", "n"]

    if unused and unused != [""]:
        while rep_yn != yn[1]:

            if reroll:
                new_word = randword(unused)

            time.sleep(.25)
            nl()
            word_yn = input("Would you like to use this word? Y or N\n>>> ").lower()
            nl()

            if word_yn == yn[0]:

                unused.remove(new_word)

                if used != [""]:
                    used.append(new_word)
                else:
                    used = [new_word]

                nl()
                lines()
                print("\"{}\" has been used!".format(new_word))
                lines()
                nl()

                rep_yn = yn[1]

            elif word_yn == yn[1]:

                rep_yn = input("Would you like to choose another word? Y or N\n>>> ").lower()
                nl()

                if rep_yn == yn[0]:
                    reroll = True

                elif rep_yn == yn[1]:
                    reroll = False

                else:
                    nl()
                    lines()
                    print("{:^30}".format("Invalid Input!"))
                    print("{:^30}".format("Please use only Y or N."))
                    lines()
                    nl()
                    time.sleep(.5)

            else:
                nl()
                lines()
                print("{:^30}".format("Invalid Input!"))
                print("{:^30}".format("Please use only Y or N."))
                lines()
                nl()

                reroll = False
                time.sleep(.5)

    else:
        time.sleep(.1)
        nl()
        lines()
        print("The Unused List is Empty!")
        lines()
        nl()
        time.sleep(.1)

    return unused, used


def scan(word_list, list_name):

    time.sleep(.25)

    if list_name != "both":

        word_dict = dict.fromkeys(set(word_list), 0)

        for word in word_list:
            word_dict[word] = word_dict[word] + 1

        duplicates = {}

        for key in word_dict:
            if word_dict[key] > 1:
                duplicates[key] = word_dict[key]

        dup_keys = list(filter(lambda word_key: word_dict[word_key] > 1, word_dict))
        dup_vals = list(filter(lambda word_val: word_val > 1, word_dict.values()))

        duplicates = dict(map(lambda keys, vals: (keys, vals), dup_keys, dup_vals))

        if duplicates:

            rep_list = []
            for key in duplicates:
                rep_list.append(f"\t\t\"{key}\" repeated {duplicates[key]-1} time{"s" if duplicates[key] > 2 else ""}")

            print_string(f"Repetitions found in {list_name}!", rep_list)

            word_list = list(word_dict.keys())

        elif not duplicates:

            print_string(f"No repetitions found in {list_name}!")

        return word_list

    else:

        repeats = set(word_list[0]).intersection(set(word_list[1]))

        if repeats:

            temp_str = "Repetitions found between Unused and Used Lists!"
            temp_len = len(temp_str)

            nl()
            lines(temp_len)
            print(f"{temp_str:{temp_len}}")
            for word in repeats:
                print(f"\t\"{word}\"")
                word_list[0].remove(word)
            lines(temp_len)
            nl()

        else:

            print_string("No repetitions found between Unused and Used Lists!")

        return word_list[0]


def word_add(unused, used):
    new_word = ""
    check_bool = False

    while not (new_word and any(char.isdigit for char in new_word) and check_bool):

        new_word = input("\nInput new word:\n>>> ").lower()

        if not new_word:

            print_string("Please provide a word.")

        elif any(char.isdigit() for char in new_word):

            print_string("Words cannot contain numerals.")

        elif len(new_word) < 3:

            print_string("Please provide a word of at least 3 characters.")

        else:

            check_bool = dict_check(new_word)

            if check_bool:

                unused.append(new_word)

                time.sleep(.25)
                unused = scan([unused, used], "both")
                time.sleep(.25)
                unused = scan(unused, "Unused List")
                time.sleep(.25)

                if new_word in unused:
                    new_word_list.append(new_word)

            else:

                print_string("That's not a word!")

    return unused


def word_rem(word_list):
    opts = ["Remove last word", "Remove a specific word"]

    temp_str = "Pick an option:"
    temp_len = len(temp_str) + 10

    nl()
    lines(temp_len)
    print(temp_str)
    for opt in range(len(opts)):
        print(f"\t{opt + 1}: {opts[opt]}")
    lines(temp_len)
    nl()

    del temp_str, temp_len

    choice = ""
    choices = list(map(str, range(1, len(opts) + 1)))

    while choice not in choices:

        choice = input(">>> ")

        if choice == choices[0]:

            if new_word_list:
                last_word = new_word_list[len(new_word_list)-1]
                word_list.remove(last_word)

                print_string(f"\"{last_word}\" removed from list!")

            else:

                print_string("You haven't added a word!")

        elif choice == choices[1]:

            word_input = word_list[0]

            while word_input in word_list:

                word_input = input("\nWord to be removed?\n>>> ")

                if word_input in word_list:
                    word_list.remove(word_input)

                    time.sleep(.25)

                    print_string(f"\"{word_input}\" removed!")

                    time.sleep(.25)

                else:

                    print_string("Please provide a word already in the list.")

        else:

            print_string(f"Please input a number 1-{len(opts)}.")

    return word_list


def rem_choose(unused, used):

    opts = []

    if unused and unused != [""]:
        opts.append(FileNames[0].removesuffix(".txt").replace("_", " "))
    if used and used != [""]:
        opts.append(FileNames[1].removesuffix(".txt").replace("_", " "))

    if opts:

        nl()
        lines()
        print("Pick a list:")
        for opt in range(len(opts)):
            print(f"\t{opt + 1}: {opts[opt]}")
        lines()
        nl()

        list_choice = ""
        list_choices = list(map(str, range(1, len(opts) + 1)))

        while list_choice not in list_choices:

            try:
                list_choice = input(">>> ")

                if list_choice == list_choices[0]:

                    unused = word_rem(unused)

                elif list_choice == list_choices[1]:

                    used = word_rem(used)

            except IndexError:
                nl()
                lines()
                if len(opts) > 1:
                    print("{:^30}".format(f"Please input a number 1-{len(opts)}."))
                else:
                    print("Come on, man, there's only one option.")
                lines()
                nl()

    else:

        nl()
        lines()
        print("Both lists are currently empty!")
        lines()
        nl()

    return unused, used


menu_choice = ""
menu_opts = ["1: Word of the Day", "2: Add a Word", "3: Remove a Word", "4: Scan for Repetitions", "5: Quit"]
menu_len = len(menu_opts)

while menu_choice != menu_len:

    time.sleep(.5)

    menu_str = "What would you like to do?"
    menu_strlen = len(menu_str) + 10

    print_string(menu_str, menu_opts)

    menu_choice = input(">>> ")

    if not menu_choice.isnumeric() or not int(menu_choice) in range(1, menu_len + 1):

        time.sleep(.5)

        print_string(["Invalid Input!", f"Please input a number 1-{menu_len + 1}."])

        time.sleep(.5)

    else:
        menu_choice = int(menu_choice)

        if menu_choice == 1:

            Unused_List, Used_List = word_of_the_day(Unused_List, Used_List)

            list_sort()

            write(Unused_List, Unused_Path)
            write(Used_List, Used_Path)

        elif menu_choice == 2:

            Unused_List = word_add(Unused_List, Used_List)

            list_sort()

            write(Unused_List, Unused_Path)

        elif menu_choice == 3:

            Unused_List, Used_List = rem_choose(Unused_List, Used_List)

            list_sort()

            write(Unused_List, Unused_Path)
            write(Used_List, Used_Path)

        elif menu_choice == 4:

            Used_List = scan(Used_List, "Used List")
            Unused_List = scan(Unused_List, "Unused List")
            Unused_List = scan([Unused_List, Used_List], "both")

            list_sort()

            write(Unused_List, Unused_Path)
            write(Used_List, Used_Path)

        elif menu_choice == menu_len:

            print_string("Goodbye!")

            time.sleep(0.5)
