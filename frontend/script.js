const state = {
  apiUrl: 'http://127.0.0.1:8000/fruits/',
  fruits: [] // FIX: Liste statt Dictionary
};

function init() {
  loadFruits();
}

async function loadFruits() {
  const res = await fetch(state.apiUrl);
  state.fruits = await res.json(); // erwartet jetzt ein Array
  renderFruits();
}

function renderFruits() {
  const out = document.getElementById('output');
  out.innerHTML = '<ul>' + getFruitItems() + '</ul>';
}

function getFruitItems() {
  let html = '';
  for (let i = 0; i < state.fruits.length; i++) { // FIX: normale for-Schleife
    html += fruitItemTemplate(state.fruits[i]);
  }
  return html;
}

function fruitItemTemplate(fruit) {
  return `<li>${fruit.name} – ${fruit.color} – ${fruit.weight}g</li>`;
}
