"""
Stephen Montague
CPSC-20000 Intro to Computer Science
8 Mar 2019
Week 8 - Exam 2

Combines 3 student programs into 1 python file, as required in the design doc,
organized by function, with a user menu to navigate between each program.

Assignments - Pig Latin Translator, Turtle Island, & Student Grade Book.

The tkinter module is required to support the turtle module,
so that it is possible to close & re-open the window canvas.
See more info on this here--

https://stackoverflow.com/questions/46630254/
python-turtle-error-on-closing-screen-code-from-how-to-think-like-a-computer-s

"""

from statistics import mean
import turtle
import tkinter


def main_menu():
    run_main = True
    while run_main is True:
        print_main()
        run_main = main_user_choice()
    return


def print_main():
    print("\nMain Menu\n"
          "     1 - English to Pig Latin Translator\n"
          "     2 - Turtle Command Center\n"
          "     3 - Student Grade Book\n"
          "     4 - Exit\n"
          "Enter Your Selection: ", end='')
    return


def main_user_choice():
    user_input = input()
    if user_input == "1":
        return run_pig()
    elif user_input == "2":
        run_turtle()
    elif user_input == "3":
        run_grade_book()
    elif user_input == "4":  # to exit
        return False
    else:
        print("Please enter 1-4 only.\n")
    return True


def run_pig():
    """
    Description: English to Pig Latin Translator

    Takes English input from the user and prints it as Pig Latin.

    Most stripped punctuation and capitalization will be rebuilt, however,
    this feature is not perfect, so if you want only the base translation,
    remove the function calls for punctuation & capitalization.

    """

    def make_pig_latin(sentence):
        pig_sentence = ''
        for word in sentence.split(" "):
            last_char = word[-1]
            if last_char in (',', '!', '?', '.'):
                word = word[:-1]
            word = word.lower()
            first = word[0]
            if first in ('a', 'e', 'i', 'o', 'u'):
                pig_word = word + 'ay'
            else:
                ay_str = first + 'ay'
                rest = word[1:]
                pig_word = rest + ay_str
            pig_sentence += (pig_word + ' ')
        return pig_sentence

    def fix_punctuation(broken_string, template_string):
        broken_string_list = broken_string.split(" ")
        for index, word in enumerate(template_string[:].split(" ")):
            template_last_char = word[-1]
            if template_last_char in (',', '!', '?', '.'):
                broken_string_list[index] += template_last_char
        fixed_punctuation = ' '.join(broken_string_list)
        return fixed_punctuation

    def fix_case(broken_string, template_string):
        broken_string_words = broken_string.split(" ")
        for index, word in enumerate(template_string[:].split(" ")):
            if word.isupper():
                broken_string_words[index] = broken_string_words[index].upper()
            elif word[0].isupper():
                broken_string_words[index] = broken_string_words[index].capitalize()
        fixed_case = ' '.join(broken_string_words)
        return fixed_case

    print("\nWelcome to the English to Pig Latin translator!\n")

    run_loop = 'y'
    try:
        while run_loop == 'y':
            english_input = input("\nEnter a sentence: ")
            translation = make_pig_latin(english_input)
            translation = fix_punctuation(translation, english_input)
            translation = fix_case(translation, english_input)
            print("Pig Latin: ", translation)
            run_loop = input("\nRun again? (Y/N)").strip().lower()
        print("\nExiting translator...")
        return True
    except IndexError:
        print("\n\n\nNo input received. Exiting...\n\n")
        return True


def run_turtle(print_welcome=True):
    """
    Prompts the user to select a shape,
    Prompts for size and color,
    Draws the shape or gives feedback.
    """

    def draw_circle(size, color):
        myturtle.pencolor(color)
        myturtle.circle(size)
        return

    def draw_square(size, color):
        myturtle.pencolor(color)
        for side in range(4):
            myturtle.forward(size*2)
            myturtle.left(90)
        return

    def draw_triangle(size, color):
        myturtle.pencolor(color)
        for side in range(3):
            myturtle.forward(size*2)
            myturtle.left(120)
        return

    def draw_pentagon(size, color):
        myturtle.pencolor(color)
        for side in range(5):
            myturtle.forward(size*2)
            myturtle.left(72)

    def print_turtle_menu():
        print("\nTurtle Command Center\n"
              "    C = Circle       S = Square\n"
              "    T = Triangle     P = Pentagon\n"
              "    L = Left         R = Right\n\n"
              "    E = Erase        Q = Quit\n"
              "Awaiting your order: ", end='')
        return

    def turtle_command():
        try:
            user_input = input().lower().strip()
            if user_input == 'q':
                print("\nExiting Command Center...")
                return False
            if (user_input not in "cstplre") or (user_input == ''):
                print("\nTransmission garbled. Say again.")
                return True
            if user_input == 'l':
                myturtle.left(45)
                return True
            if user_input == 'r':
                myturtle.right(45)
                return True
            if user_input == 'e':
                myturtle.clear()
                return True
            shape_size = int(input("Choose size (0-100): "))
            shape_color = input("Choose color (Enter 'red', 'blue', 'green', etc.): ").lower()
            if user_input == 'c':
                print("%s Circle. Aye, Captain." % shape_color.title())
                draw_circle(shape_size, shape_color)
            elif user_input == 's':
                print("%s Square. Copy, Sir." % shape_color.title())
                draw_square(shape_size, shape_color)
            elif user_input == 't':
                print("%s Triangle. Roger that." % shape_color.title())
                draw_triangle(shape_size, shape_color)
            elif user_input == 'p':
                print("%s Pentagon. Right away." % shape_color.title())
                draw_pentagon(shape_size, shape_color)
            myturtle.pencolor("green")  # makes turtle's pen-color outline unnoticeable
            return True
        except (ValueError, turtle.TurtleGraphicsError):
            print("\nError: Turtle over-heated. Please confirm order.")
            window.withdraw()  # use withdraw(), not destroy()
            set_welcome = False
            run_turtle(set_welcome)

    window = tkinter.Tk()
    window.geometry("500x500+0+0")
    window.title("Turtle Island")
    window.configure(background="blue")
    canvas = turtle.Canvas(window)
    canvas.pack(expand=True)
    myturtle = turtle.RawTurtle(canvas, shape="turtle")
    myturtle.color("green")
    myturtle.screen.bgcolor("peach puff")

    if print_welcome is True:
        print("\nWelcome to Turtle Island. What can I do for you today?\n"
              "I can draw, and I can swim, but I can't draw on water.")

    run = True
    while run is True:
        print_turtle_menu()
        run = turtle_command()
    window.destroy()
    return True


def run_grade_book():
    """
    Updates a dictionary to hold names and test scores with possible values 0-100.
    Allows user to add / delete data as desired.
    Finds the high, low, and average score.
    Prints a report like...

    Grade Report
    -------------
    Sarah: 97
    Bob: 96
    Jim: 95
    more...

    High Score: 97
    Low Score: 95
    Average Score: 96

    """

    def print_gb_menu():
        print("\nGrade Book Menu\n"
              "     1 to Add Data\n"
              "     2 to Print Stats\n"
              "     3 to Remove Data\n"
              "     4 to Exit\n"
              "Enter Your Selection: ", end='')
        return

    def gb_user_choice():
        try:
            user_input = input()
            if user_input == "1":
                input_data()
                return True
            elif user_input == "2":
                if len(grade_book) == 0:
                    raise RuntimeError
                else:
                    make_stats()
                    print_stats()
                    return True
            elif user_input == "3":
                if len(grade_book) == 0:
                    raise RuntimeError
                else:
                    delete_data()
                    return True
            elif user_input == "4":  # to exit
                return False
            else:
                print("Error: Please Enter a Number")
                return True
        except RuntimeError:
            print("Error: Grade Book is Empty")
            return True

    def input_data():
        try:
            num_students = int(input("How many students?: ").strip())
            for student in range(num_students):
                name = input("Student Name: ").lower().strip()
                if name.isnumeric():
                    raise TypeError
                grade = float(input("Student Grade: "))
                if not 0 <= grade <= 100:
                    raise ValueError
                grade_book.update({name: grade})

        except ValueError:
            print("Error: Valid Numbers Only. Please Re-Enter Data")
            input_data()
        except TypeError:
            print("Error: Alphabetical Only. Please Re-Enter Data")
            input_data()
        return

    def delete_data():
        unwanted_name = input("Enter Name to Remove: ").strip().lower()
        if unwanted_name in grade_book:
            del grade_book[unwanted_name]
            print(unwanted_name.title(), "Removed from Grade Book")
        else:
            print("Error: '%s' not found in the Grade Book" % unwanted_name.title())
        return

    def make_stats():
        nonlocal high_score
        nonlocal low_score
        nonlocal avg_score
        high_score = max(grade_book.values())
        low_score = min(grade_book.values())
        avg_score = mean(grade_book.values())
        return

    def print_stats():
        print("\nGrade Report:")
        print("----------------")
        for student, grade in grade_book.items():
            print("%s: %.1f" % (student.title(), grade))
        print("\nHighest Score:", high_score)
        print("Lowest Score:", low_score)
        print("Average Score: %.1f" % avg_score)
        input("\nPress Enter to Continue")  # pause
        return

    grade_book = {}
    high_score = 0.0
    low_score = 0.0
    avg_score = 0.0

    run = True
    while run is True:
        print_gb_menu()
        run = gb_user_choice()
    print("\nExiting Grade Book...")
    return


main_menu()
print("\nGoodbye")
