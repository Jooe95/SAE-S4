const filmListElement = document.getElementById('filmList');
const searchInput = document.getElementById('searchInput');
const searchForm = document.getElementById('searchForm');

searchInput.addEventListener('input', function() {
    const searchTerm = searchInput.value;
    fetch(`/films?search=${encodeURIComponent(searchTerm)}`)
        .then(response => response.json())
        .then(data => {
            filmListElement.innerHTML = ''; 
            data.forEach(film => {
                const listItem = document.createElement('li');
                listItem.textContent = film.primaryTitle;
                filmListElement.appendChild(listItem);
            });
        })
        .catch(error => {
            console.error('Erreur lors de la recherche des films :', error);
        });
});

searchForm.addEventListener('submit', function(event) {
    event.preventDefault(); 
});
