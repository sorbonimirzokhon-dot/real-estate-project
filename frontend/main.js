// 1. Находим элементы на странице
const searchInput = document.getElementById("searchInput");
const searchBtn = document.getElementById("searchBtn");
const housesContainer = document.getElementById("houses");

// 2. Функция, которая отрисовывает дома на экране
function renderHouses(houses) {
    housesContainer.innerHTML = ""; // Очищаем список перед новым поиском
    
    if (houses.length === 0) {
        housesContainer.innerHTML = "<p>Домов не найдено</p>";
        return;
    }

    houses.forEach(house => {
        const div = document.createElement("div");
        div.className = "house-card";
        div.style = "border: 1px dashed #999; padding: 15px; margin: 10px;";
        div.innerHTML = `
            <h4>${house.title}</h4>
            <p>Город: <b>${house.city}</b></p>
            <p>Цена: ${house.price} сомони</p>
        `;
        housesContainer.appendChild(div);
    });
}

// 3. Логика кнопки "Поиск"
searchBtn.onclick = () => {
    const city = searchInput.value.trim();
    
    // Стучимся к твоему Python серверу
    fetch(`http://127.0.0.1:8000/search?city=${city}`)
        .then(response => response.json())
        .then(data => {
            console.log("Данные от Бэкенда:", data);
            renderHouses(data.houses); // Передаем список домов в функцию отрисовки
        })
        .catch(err => {
            console.error("Ошибка:", err);
            alert("Сервер не отвечает. Проверь терминал!");
        });
};