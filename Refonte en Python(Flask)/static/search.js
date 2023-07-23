// const filmListElement = document.getElementById('filmList');
// const actorListElement = document.getElementById('actorList');
// const searchInput = document.getElementById('searchInput');
// const searchForm = document.getElementById('searchForm');

// searchForm.addEventListener('submit', function(event) {
//     event.preventDefault(); // Empêche la soumission du formulaire par défaut

//     const searchTerm = searchInput.value;
//     const filmsCheckbox = document.getElementById('filmsCheckbox');
//     const actorsCheckbox = document.getElementById('actorsCheckbox');

//     // Déterminer le type de recherche en fonction des cases cochées
//     let searchType = '';
//     if (filmsCheckbox.checked) {
//         searchType = 'films';
//     } else if (actorsCheckbox.checked) {
//         searchType = 'actors';
//     }

//     fetch(`/films?search=${encodeURIComponent(searchTerm)}&type=${searchType}`)
//         .then(response => response.json())
//         .then(data => {
//             filmListElement.innerHTML = ''; // Effacer la liste de films précédente
//             actorListElement.innerHTML = ''; // Effacer la liste d'acteurs précédente

//             if (searchType === 'films' && data.films) {
//                 data.films.forEach(film => {
//                     const listItem = document.createElement('li');
//                     listItem.textContent = film;
//                     filmListElement.appendChild(listItem);
//                 });
//             }

//             if (searchType === 'actors' && data.actors) {
//                 data.actors.forEach(actor => {
//                     const listItem = document.createElement('li');
//                     listItem.textContent = actor;
//                     actorListElement.appendChild(listItem);
//                 });
//             }
//         })
//         .catch(error => {
//             console.error('Erreur lors de la recherche des films ou des acteurs :', error);
//         });
// });
const searchForm = document.getElementById('searchForm');
const searchInput = document.getElementById('searchInput');
const searchResults = document.getElementById('searchResults');
const searchType = document.getElementById('searchType');

searchForm.addEventListener('input', function (event) {
    event.preventDefault(); 

    const searchTerm = searchInput.value;
    const selectedSearchType = searchType.value;

    let searchUrl = '';
    if (selectedSearchType === 'films') {
        searchUrl = '/films?search=' + encodeURIComponent(searchTerm);
    } else if (selectedSearchType === 'actors') {
        searchUrl = '/actors?search=' + encodeURIComponent(searchTerm);
    }

    fetch(searchUrl)
        .then(response => response.json())
        .then(data => {
            searchResults.innerHTML = ''; 

            if (selectedSearchType === 'films') {
                data.films.forEach(film => {
                    const listItem = document.createElement('li');
                    listItem.textContent = film;
                    searchResults.appendChild(listItem);
                });
            } else if (selectedSearchType === 'actors') {
                data.actors.forEach(actor => {
                    const listItem = document.createElement('li');
                    listItem.textContent = actor;
                    searchResults.appendChild(listItem);
                });
            }
        })
        .catch(error => {
            console.error('Erreur lors de la recherche :', error);
        });
});


// Search2

const film1Input = document.getElementById('film1Input');
const film2Input = document.getElementById('film2Input');
const searchButton = document.getElementById('searchButton');
const commonActorsList = document.getElementById('commonActorsList');

searchButton.addEventListener('click', function () {
    const film1Title = film1Input.value.trim();
    const film2Title = film2Input.value.trim();

    const data = {
        film1_title: film1Title,
        film2_title: film2Title
    };

    fetch('/common_actors', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        commonActorsList.innerHTML = ''; // Efface la liste précédente

        data.common_actors.forEach(actor => {
            const listItem = document.createElement('li');
            listItem.textContent = actor;
            commonActorsList.appendChild(listItem);
        });
    })
    .catch(error => {
        console.error('Erreur lors de la recherche des acteurs en commun :', error);
    });
});
