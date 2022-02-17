from flask import Flask, render_template, url_for, request

app = Flask(__name__)

@app.route('/')
def my_home():                              # Keep all .html files in "Templates" folder
    return render_template('index.html')    # Keep all .css, .js & image files in "Static" folder

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        return 'Form Submitted Successfuly.'
    else:
        return 'Something went wrong, Try Again!'

# @app.route('/<username>')                                 # Variable
# def user(username=None):
#     return render_template('about.html', name=username)
#
# @app.route('/<username>/<int:user_id>')                   # Variable
# def user_id(username=None, user_id=None):
#     return render_template('about.html', name=username, user_id=user_id)

# @app.route('/about')
# def about():
#    return render_template('about.html')

# @app.route('/works')
# def works():
#    return render_template('works.html')

# @app.route('/contact')
# def contact():
#        return render_template('contact.html')


