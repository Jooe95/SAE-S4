const film1Input = document.getElementById('film1Input');
const film2Input = document.getElementById('film2Input');
const searchButton = document.getElementById('searchButton');
const commonActorsList = document.getElementById('commonActorsList');

searchButton.addEventListener('click', function () {
    const film1Title = film1Input.value.trim();
    const film2Title = film2Input.value.trim();

    const searchUrl = `/common_actors?film1_title=${encodeURIComponent(film1Title)}&film2_title=${encodeURIComponent(film2Title)}`;

    fetch(searchUrl)
        .then(response => response.json())
        .then(data => {
            commonActorsList.innerHTML = ''; 

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
