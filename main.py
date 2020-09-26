from pymongo import MongoClient
from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)
koneksi = MongoClient("")

db = koneksi.workshop_mongodb
col_sifo = db.crud

@app.route('/', methods=['GET','POST'])
def index():
    data = [i for i in col_sifo.find()]
    if request.method == "POST":
        col_sifo.insert_one({'_id': request.form['Npm'],
                            'Nama': request.form['Nama'],
                            'Jurusan': request.form['Jurusan']})
        return redirect(url_for('index'))
    return render_template('index.html', data=data)

@app.route('/edit/<npm>', methods=['GET','POST'])
def edit(npm):
    data = col_sifo.find_one({'_id': npm})
    if request.method == 'POST':
        col_sifo.update_one({'_id': request.form['Npm']},
                            {"$set": {"Nama": request.form['Nama'],
                            "Jurusan": request.form['Jurusan']}
                            })
        return redirect(url_for('index'))
    return render_template('edit.html', data=data)

@app.route('/hapus/<npm>')
def hapus(npm):
    col_sifo.delete_one({'_id':npm})
    return redirect(url_for('index'))

#app.run(debug=True)
