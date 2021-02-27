from flask import Flask
import random

app = Flask(__name__)

@app.route('/')
def homepage():
    """Shows a greeting to the user."""
    return 'Are you there, world? It\'s me, Ducky!'

@app.route('/animal/<users_animal>')
def favorite_animal(users_animal):
    """Display a message to the user that changes based on their favorite animal."""
    return ("Wow, %s is my favorite animal, too!" % users_animal)

@app.route('/dessert/<users_dessert>')
def favorite_dessert(users_dessert):
    """Display a message to the user that changes based on their favorite dessert."""
    return ("How did you know I liked %s?" % users_dessert)

@app.route('/madlibs/<adjective>/<noun>')
def adjective_noun(adjective, noun):
    """Display a message to the user that changes based on their adjectives and nouns."""
    return ("The %s dog likes to play with his %s." % ((adjective), (noun)))

@app.route('/multiply/<number1>/<number2>')
def multiply(number1, number2):
    """Multiply 2 numbers together."""
    if number1.isdigit() == True & number2.isdigit() == True:
        result = int(number1) * int(number2)
        return ("%s times %s is %s" % ((number1), (number2), (result)))
    else:
        return "Invalid inputs. Please try again by entering 2 numbers!"

@app.route('/sayntimes/<word>/<n>')
def sayntimes(word, n):
    """Print a word n number of times."""
    words = ""
    for index in n:
        words = word + ' '
        
    return ('%s' % words)

@app.route('/dicegame')
def dicegame():
    """Dice Game - rolling a 6 wins"""
    random_num = random.randint(1, 6)

    if random_num == 6:
        return ("You rolled a %d. You won!" % random_num)
    else:
        return ("You rolled a %d. You lost!" % random_num)







if __name__ == '__main__':
    app.run(debug=True)
