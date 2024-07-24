"""
Main program entry point.
"""

# Standard Library Imports
from os import listdir
from os.path import isfile, join
from pathlib import Path

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


@app.get("/api/gallery")
def api_gallery() -> dict:
    """
    Gets all images in the gallery.

    Works by scanning the /static/modified/gallery directory for images and returning all of them in a list.

    Returns:
        dict: JSON response containing all images in the gallery
    """
    # Get all images in gallery directory
    images: list[str] = [
        f"/static/img/modified/gallery/{f}"
        for f in listdir("static/img/modified/gallery")
        if isfile(join("static/img/modified/gallery", f))
    ]

    # Return images
    return {
        "images": images,
        "images_count": len(images)
    }


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
