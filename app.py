from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World from Corey Turner! I am adding my first code change.'

@app.route('/hello')
def hello():  # put application's code here
    return render_template('hello.html')

@app.route('/about')
def about():  # put application's code here
    return render_template('about.html')

@app.route('/favorite-course', methods = ['GET','POST'])
def favorite_course():  # put application's code here
     print('Subject Entered: ' + request.args.get('subject'))
     print('Course Number Entered: ' + request.args.get('course_number'))

     return render_template('favorite-course.html')

@app.route('/contact', methods = ['GET','POST'])
def favorite_course():  # put application's code here
     return render_template('contact.html')

if __name__ == '__main__':
    app.run()





