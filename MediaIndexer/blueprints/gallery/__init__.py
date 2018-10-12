from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
import json
import os
import get_files
import tempfile
from w3c_validator import validate

gallery = Blueprint(
    name='gallery',
    import_name=__name__,
    static_folder='static',
    static_url_path='/static',
    template_folder='templates',
    url_prefix='/gallery'
)

@gallery.route('/', defaults={'page': ''})
@gallery.route('/<page>')
@gallery.route('/<page>/')
def index(**kwargs):
    r = os.path.abspath(os.path.join(os.curdir, kwargs["page"]))
    directories = get_files.get_dirs(directory = r, depth=1, absolute=True)
    images = get_files.get_files(directory = r, extensions=['.jpg'], depth=1, absolute=True)
    for key, item in kwargs.items():
        print("{}: {}".format(key, item))
    html = render_template('index.html', directorys=directories, images=images)
    with tempfile.NamedTemporaryFile(mode="w", delete=True) as f:
        f.write(html)
        f.flush()
        print(validate(f.name))
    return html

@gallery.route('/items.json', defaults={'page': ''})
@gallery.route('/<page>/items.json')
def items(**kwargs):
    r = os.path.abspath(os.path.join(os.curdir, kwargs["page"]))
    directories = get_files.get_dirs(directory = r, depth=1, absolute=True)
    images = get_files.get_files(directory = r, extensions=['.jpg'], depth=1, absolute=True)
    for key, item in kwargs.items():
        print("{}: {}".format(key, item))
    items_json = render_template('items.json', directorys=directories, images=images)
    return items_json

import json
@gallery.route('/items2.json', defaults={'page': ''})
@gallery.route('/<page>/items2.json')
def items2(**kwargs):
    x = dict()
    sizes = {
        "small": 128,
        "medium": 608,
        "large": 1024,
    }


    r = os.path.abspath(os.path.join(os.curdir, kwargs["page"]))
    directories = get_files.get_dirs(directory = r, depth=1, absolute=True)
    images = get_files.get_files(directory = r, extensions=['.jpg'], depth=1, absolute=True)
    for key, item in kwargs.items():
        print("{}: {}".format(key, item))
    items_json = render_template('items.json', directorys=directories, images=images)
    return items_json

@gallery.route('/style.css')
def css(**kwargs):
    for key, item in kwargs.items():
        print("{}: {}".format(key, item))
    return render_template('style.css')


@gallery.route('/hello')
@gallery.route('/hello/')
def hello(**kwargs):
    for key, item in kwargs.items():
        print("{}: {}".format(key, item))
    return render_template('index.html')

