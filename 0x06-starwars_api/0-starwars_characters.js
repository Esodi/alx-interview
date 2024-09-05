#!/usr/bin/nodejs

const request = require('request');

// Ensure that the movie ID is provided as an argument
if (process.argv.length < 3) {
    console.error('Please provide a Movie ID.');
    process.exit(1);
}

const movieId = process.argv[2];
const baseUrl = 'https://swapi-api.alx-tools.com/api/';

// Fetch movie details
request(`${baseUrl}films/${movieId}/`, (err, res, body) => {
    if (err) {
        console.error('Error fetching movie details:', err);
        return;
    }

    if (res.statusCode !== 200) {
        console.error('Failed to fetch movie details. Status code:', res.statusCode);
        return;
    }

    const movie = JSON.parse(body);
    const characterUrls = movie.characters;

    // Fetch each character's details
    characterUrls.forEach((url, index) => {
        request(url, (err, res, body) => {
            if (err) {
                console.error('Error fetching character details:', err);
                return;
            }

            if (res.statusCode !== 200) {
                console.error('Failed to fetch character details. Status code:', res.statusCode);
                return;
            }

            const character = JSON.parse(body);
            console.log(character.name);

            // Print a separator line if this is not the last character
            if (index < characterUrls.length - 1) {
                console.log('---');
            }
        });
    });
});

