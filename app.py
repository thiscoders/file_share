# -*- coding: utf-8 -*-

import os
from flask import Flask, render_template, request

app = Flask(__name__)


def make_tree(path='static'):
    tree = dict(name=path, children=[])
    try:
        lst = os.listdir(path)
    except OSError:
        print("error...")
    else:
        for name in lst:
            fn = os.path.join(path, name)
            if os.path.isdir(fn):
                tree_sub = make_tree(fn)
                tree['children'].append(tree_sub)
            else:
                tree['children'].append(dict(name=name, path=fn))
    return tree


@app.route('/', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        password = request.form.get('password')
        if password != '1':
            return render_template('login.html', error_msg='口令错误！')
        else:
            tree = make_tree()
            return render_template('tree.html', tree=tree)


if __name__ == '__main__':
    static_exist = os.path.exists(app.static_folder)
    if not static_exist:
        os.mkdir(app.static_folder)
    app.run(host='0.0.0.0', debug=True)
