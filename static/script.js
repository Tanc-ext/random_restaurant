// Add an event listener to the button
document.getElementById('getRestaurantButton').addEventListener('click', function() {
    // Send a POST request to the Flask endpoint
    fetch(getRestaurantUrl, {
        method: 'POST'
    })
    .then(response => response.json()) // Parse the JSON response
    .then(data => {
        // Update the page content with the random restaurant
        document.getElementById('restaurantDisplay').innerHTML =
            'Your random restaurant is: <strong>' + data.restaurant + '</strong>';
    })
    .catch(error => {
        console.error('Error:', error);
    });
});