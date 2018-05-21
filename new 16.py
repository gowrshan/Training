from flask import Flask, render_template, request
from bot_function import *
import random
import os

greetings = ['hola', 'hello', 'hi', 'Hi', 'hey!','hey']
random_greeting = random.choice(greetings)

question = ['How are you?','How are you doing?']
responses = ["I am Good, Do you want to create an ORG or SPACE (if org input as ORG and if space input as SPACE "]

question2 = ['bye','Bye','good bye','Good Bye']

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def samplefunction():
    if request.method == 'GET':
        return render_template('new.html')
	if request.method == 'POST':
        while True:
            userInput = request.form['human']
            if userInput in greetings:
				return render_template('new.html', bot=random_greeting)
			elif userInput in question:
				return render_template('new.html', bot=responses)
			elif userInput == "ORG":
				return render_template('new.html', bot="Please input ORG name as ORG_NameOfORG (eg ORG_test if ORG name is test)")
			elif userInput == "SPACE":
				return render_template('new.html', bot="Please input SPACE with the ORG where it needs to be created as SPACE_NameOfSPACE_ORGName (example SPACE_test_Default if space name = test which needs to be created in ORG = Default)")
			
			
			elif userInput[0:4] == "ORG_":
				response1=create_org(userInput[4:])
				return render_template('new.html', bot=response1)
				
			elif userInput[0:6] == "SPACE_":
				response2=create_space(userInput)
				return render_template('new.html', bot=response2)	
			elif userInput in question2:
				return 	render_template('new.html', bot="Bye")	

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)			