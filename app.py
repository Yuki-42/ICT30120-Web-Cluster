"""
Main program entry point.
"""

# Standard Library Imports

# Third Party Imports
from flask import Flask, Response, redirect, render_template, request, url_for

# Local Imports
from database import Database

# Create flask app
app: Flask = Flask(__name__, static_folder="static", template_folder="templates")

# Create database
db: Database = Database()


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


@app.post("/contact")
def contact_post() -> Response:
    """
    Handles the contact form submission.

    Returns:
        Response: Redirect to contact page
    """
    # Get form data
    name: str = request.form.get("name")
    email: str = request.form.get("email")
    phone: str = request.form.get("phone", None)
    subject: str = request.form.get("subject")
    message: str = request.form.get("message")

    # Create new contact request
    db.contact_requests.new(name, email, subject, message, phone)

    # Redirect to contact page
    return redirect(
        url_for("contact")
    )


if __name__ == "__main__":
    app.run("0.0.0.0", 8080, debug=True)
