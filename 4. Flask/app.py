from flask import Flask, render_template, request

'''
This creates an instance of the Flask class,
which will be the WSGI (Web Server Gateway Interface) application
'''
# WSGI application
app = Flask(__name__)


@app.route("/")
def welcome():
    return "Welcome to introduction to flask"


'''
The render_templates will redirect to the provided html file name inside the templates folder.
So, it is important to place the required html files in templates folder before using render_templates
'''
@app.route("/index")
def welcome_index():
    return render_template('index.html')


@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/details",methods = ['GET','POST'])
def get_details():
    if request.method == 'POST':
        name = request.form.get('name', '')
        return f'Hello!! {name}'
    return render_template("form.html")
    

'''
Keeping debug as True will refresh server when there are any changes made.
This is useful during development
'''
if __name__ == "__main__":
    app.run(debug = True)