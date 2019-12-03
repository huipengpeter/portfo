from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)

@app.route('/')
def my_home():
    #print(url_for('static', filename='favicon.ico'))
    return render_template('index.html')

#lightning_weather_storm_2781
@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'did not save to the database'
    else:
        return 'something wrong'

def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject = data['subject']
        message = data["message"]
        file = database.write(f'\n{email},{subject},{message}')

def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as database2:
        email = data["email"]
        subject = data['subject']
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter = ',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])
if __name__ == '__main__':
    app.run()