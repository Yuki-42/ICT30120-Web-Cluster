"""
Main program entry point.
"""

# Standard Library Imports

# Third Party Imports
from flask import Flask, Response, render_template

# Local Imports

# Create flask app
app: Flask = Flask(__name__, static_folder="static", template_folder="templates")


# Create index route
@app.get("/")
def index() -> str:
    """
    Displays the index page.

    Returns:
        str: Rendered index page
    """
    return render_template("index.html")


if __name__ == "__main__":
    app.run("0.0.0.0", 8080, debug=True)
