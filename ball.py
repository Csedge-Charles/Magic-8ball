from flask import Flask, render_template, request, url_for
import random

answer_list = ['Yes', 'Definitely', 'Hundred percent going to happen',
               'Definitely not', 'No', 'Not possible',
               'Maybe', "I don't know"]

app = Flask(__name__)

@app.route('/', methods= ['GET', 'POST'])
def hello():
    if request.method == 'POST':
        print('POST')
        return render_template('8ball.html', eightball=random.choice(answer_list))
    return render_template('index.html')



    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
