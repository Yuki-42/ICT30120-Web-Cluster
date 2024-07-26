// Gallery JS

// Send a request to the api to get all images
function getImages() {
    $.ajax({
        url: '/api/gallery',
        type: 'GET',
        success: function(data) {
            // If the request is successful, display the images
            displayImages(data);
        }
    });
}

// Display the images
function displayImages(data) {
    console.log(data);

    // Get the gallery element
    const gallery = document.getElementById('gallery');

    // Clear the gallery
    gallery.innerHTML = '';

    // Loop through the images
    for (let i = 0; i < data["images"].length; i++) {
        // Get image data
        let image = data["images"][i];

        console.log(image)
        // Create image container
        const container = document.createElement('div');
        container.className = 'gallery-image';

        // Create an image title
        const title = document.createElement('h3');
        title.textContent = image["name"];

        // Create an image description
        const description = document.createElement('p');
        description.textContent = image["description"];

        // Create an image element
        const img = document.createElement('img');

        // Set the image source
        img.src = image["path"];

        // Add the image to the gallery
        container.appendChild(title);
        container.appendChild(img);
        container.appendChild(description);

        gallery.appendChild(container);
    }
}

// Call the getImages function when the page loads
document.addEventListener('DOMContentLoaded', function() {
    getImages();
});
