from django.shortcuts import render
import sqlite3
import datetime
import os

# Create your views here.

def consulta(nome, senha):
    connectUser = False 
    con = sqlite3.connect('db.sqlite3')
    cur = con.cursor()

    for resp in cur.execute(f"SELECT * FROM app_usuario WHERE nome='{nome}' AND senha='{senha}'"):
        connectUser = True

    con.close()

    return connectUser

def index(request):
    data = {}
    if request.method == 'POST':
        connectUser = consulta(request.POST['nome'], request.POST['senha'])
        if connectUser:
            data['key'] = 'AcHaCTF{SQL_1NJeCti0n_BaBy}'
    return render(request, 'app/login.html', data)