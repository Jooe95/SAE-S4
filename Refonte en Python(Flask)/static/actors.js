const searchForm = document.getElementById('searchForm');
const filmInput = document.getElementById('filmInput');
const actorsList = document.getElementById('actorsList');

searchForm.addEventListener('submit', function (event) {
    event.preventDefault();

    const filmTitle = filmInput.value.trim();

    fetch(`/actors?film=${encodeURIComponent(filmTitle)}`)
        .then(response => response.json())
        .then(data => {
            actorsList.innerHTML = ''; 

            data.actors.forEach(actor => {
                const listItem = document.createElement('li');
                listItem.textContent = actor;
                actorsList.appendChild(listItem);
            });
        })
        .catch(error => {
            console.error('Erreur lors de la recherche :', error);
        });
});
