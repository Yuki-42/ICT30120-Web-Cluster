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


@app.get("/gallery")
def gallery() -> str:
    """
    Displays the gallery page.

    Returns:
        str: Rendered gallery page
    """
    return render_template("gallery.html")


@app.get("/contact")
def contact() -> str:
    """
    Displays the contact page.

    Returns:
        str: Rendered contact page
    """
    return render_template("contact.html")


if __name__ == "__main__":
    app.run("0.0.0.0", 8080, debug=True)
