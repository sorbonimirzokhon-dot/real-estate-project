const input = document.getElementById("searchInput");
const button = document.getElementById("searchBtn");
const result = document.getElementById("result");
const housesContainer = document.getElementById("houses");
const placeholder = document.getElementById("houses-placeholder");

button.addEventListener("click", () => {
    const city = input.value.trim();

    // Очистка старого
    result.textContent = "";
    housesContainer.innerHTML = "";

    if (city.length === 0) {
        result.textContent = "Введите город";
        placeholder.style.display = "block";
        return;
    }

    fetch(`http://127.0.0.1:8000/search?city=${city}`)
        .then(response => response.json())
        .then(data => {
            placeholder.style.display = "none";

            if (!data.houses || data.houses.length === 0) {
                result.textContent = "Нет домов для показа";
                return;
            }

            data.houses.forEach(house => {
                const div = document.createElement("div");
                div.innerHTML = `
                    <h4>${house.title}</h4>
                    <p>City: ${house.city}</p>
                    <p>Price: ${house.price}</p>
                    <hr>
                `;
                housesContainer.appendChild(div);
            });
        })
        .catch(() => {
            result.textContent = "Ошибка соединения с сервером";
            placeholder.style.display = "block";
        });
});
