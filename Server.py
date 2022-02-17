from flask import Flask, render_template, url_for, request, redirect
import csv

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
        return redirect('/thankyou.html')
    else:
        return 'Something went wrong, Try Again!'

# def write_to_file(data):
#  with open('database.txt', mode='a') as database:
#    email = data["email"]
#    subject= data["subject"]
#    message = data["message"]
#    file = database.write(f'\n{email},{subject},{message}')

def write_to_csv(data):
  with open('database.csv', mode='a') as csv_database:
    email = data["email"]
    subject= data["subject"]
    message = data["message"]
    
    csv_writer = csv.writer(csv_database, delimiter=',',
                            quotechar='', quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow([email, subject, message])
    
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


