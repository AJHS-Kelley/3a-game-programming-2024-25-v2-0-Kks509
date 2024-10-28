# Functions Practice, Ryan Kelley, v0.0

import random

def helloWorldMulti(): # FUNCTION SIGNATURE
    """This function will output Hello, World! in a language the user choose. """ # DOCSTRING \
    # print a list of languages to the screen, at least three but no more than five.
    print("""
        Welcome to the Hello, World! Translator
          The following languages are available.
          [E]nglish
          [S]panish
          [J]apanese
          """)
    # allow the user to select(input) a choice for the language.
    language = input("What language do you want?\n")
    # print "Hello, World!" to the screen in that language.
    if language == "English":
        print(f"you chose English")
    if language == "Spanish":
        print(f"Hola Mundo")
    if language == "Japanese":
        print(f"Kon'nichiwa sekai")

helloWorldMulti()
