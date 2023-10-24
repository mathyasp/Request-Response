# import flask
from flask import Flask

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


# run the server
if __name__ == '__main__':
    app.run(debug=True)