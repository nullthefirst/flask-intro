"""Using Flask template engines.

In this example we're using Flask template engine (Jinja2) to simplify
the process to generate the resulting HTML.

**TODO**
In our previous example we had to do a lot of string handling to
create the <ul> with authors.
It's your turn to use the template engine to build the same result.
"""
from flask import Flask
from flask import render_template_string  # !Important

app = Flask(__name__)


@app.route('/')
def hello_world():
    library_name = "Poe"
    html = """
        <html>
            <h1>Welcome to {{library}} library!</h1>
            <ul>
                {% for author in authors_list%}
                    <li>{{ author }}</li>
                {% endfor %}
            </ul>
        </html>
    """
    authors = ["Alan Poe", "Jorge L. Borges"]

    rendered_html = render_template_string(
        html, library=library_name, authors_list=authors)

    return rendered_html
