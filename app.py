# import libraries
from flask import Flask
import random

# set up app variable
app = Flask(__name__)

# First route
@app.route('/')
def homepage():
    """Shows a greeting to the user."""
    return 'Are you there, world? It\'s me, Ducky!'

# Second route
@app.route('/animal/<users_animal>')
def favorite_animal(users_animal):
    """Display a message to the user that changes based on their favorite animal."""
    return f'Wow, {users_animal} is my favorite animal, too!'

# Third route (dessert)
@app.route('/dessert/<users_dessert>')
def favorite_dessert(users_dessert):
    """Display a message to the user that changes based on their favorite dessert."""
    return f'How did you know I liked {users_dessert}?'

# Fourth route (madlibs)
@app.route('/madlibs/<adjective>/<noun>')
def make_madlib(adjective, noun):
    """Display a madlib story based on the user's input adjective and noun"""
    return f'There once was a dog named Spot. His favorite toy was a {noun}. He loved his {adjective} {noun}.'

# Fifth route (Multiply 2 numbers)
@app.route('/multiply/<number1>/<number2>')
def multiply(number1, number2):
    """Validate input, display multiplication of 2 input numbers"""
    if not number1.isdigit() or not number2.isdigit():
        return 'Invalid inputs. Please try again by entering 2 numbers!'
    return f'{number1} times {number2} is {int(number1) * int(number2)}'

# Sixth route (Say N Times)
@app.route('/sayntimes/<word>/<n>')
def say_n_times(word, n):
    """Validate input, return string repeated n times"""
    if not n.isdigit():
        return 'Invalid input. Please try again by entering a word and a number!'
    n_string = ''
    for x in range(int(n)):
        n_string += f'{word} '
    return n_string

# Seventh routh (Dice Game)
@app.route('/dicegame')
def dice_game():
    """Choose random # from 1-6. If a 6, the user wins"""
    user_roll = random.randint(1, 6)
    user_message = f'You rolled a {user_roll}.'
    if user_roll == 6:
        return f'{user_message} You won!'
    return f'{user_message} You lost!'


# run the server
if __name__ == '__main__':
    app.run(debug=True)