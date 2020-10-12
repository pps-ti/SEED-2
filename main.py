from pymongo import MongoClient
from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)
client = MongoClient("")
db = client.worshop_mongodb
collection = db.crud


@app.route('/', methods=['GET', 'POST'])
def index():
    data = [i for i in collection.find()]
    if request.method == "POST":
        collection.insert_one({'_id': request.form['NPM'],
                               'Nama': request.form['Nama'],
                               'Jurusan': request.form['Jurusan']})
        return redirect(url_for('index'))
    return render_template('index.html', data=data)


@app.route('/edit/<npm>', methods=['GET', 'POST'])
def edit(npm):
    data = collection.find_one({'_id': npm})
    if request.method == 'POST':
        collection.update_one({'_id': request.form['NPM']},
                              {'$set': {'Nama': request.form['Nama'],
                                        'Jurusan': request.form['Jurusan']}})
        return redirect(url_for('index'))
    return render_template('edit.html', data=data)


@app.route('/hapus/<npm>')
def hapus(npm):
    collection.delete_one({'_id': npm})
    return redirect(url_for('index'))

# app.run(debug=True)
