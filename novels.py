from flask import Flask, render_template
app = Flask(__name__)

# For web hosting
application = app

import csv

def convert_to_dict(filename):
    datafile = open(filename, newline='')
    my_reader = csv.DictReader(datafile)
    list_of_dicts = list(my_reader)
    datafile.close()

    return list_of_dicts

# Convert CSV to dictionary
novels_list = convert_to_dict("novels.csv")

# Create tuples listing ID and novel title
pairs_list = []
for p in novels_list:
    pairs_list.append( (p['ID'], p['Title']) )

# First route
@app.route('/')
def index():
    return render_template('index.html', pairs=pairs_list)

# Second route
@app.route('/novel/<num>')
def detail(num):
    try:
        novel_dict = novels_list[int(num) - 1]
    except:
        return f"<h1>Invalid value for novel ID: {num}</h1>"

    return render_template('novel.html', novels=novel_dict)


if __name__ == '__main__':
    app.run(debug=True)