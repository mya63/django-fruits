const state = { apiUrl: 'http://127.0.0.1:8000/fruits/', fruits: {} };

function init() { loadFruits(); }

async function loadFruits() {
  const res = await fetch(state.apiUrl);
  state.fruits = await res.json();
  renderFruits();
}

function renderFruits() {
  const out = document.getElementById('output');
  out.innerHTML = '<ul>' + getFruitItems() + '</ul>';
}

function getFruitItems() {
  let html = '';
  for (const key in state.fruits) html += fruitItemTemplate(state.fruits[key]);
  return html;
}

function fruitItemTemplate(fruit) {
  return `<li>${fruit.name} – ${fruit.color} – ${fruit.weight}g</li>`;
}
