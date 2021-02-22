const carForm = document.getElementById("car-form");

const carsDataBox = document.getElementById("cars-data-box");
const carInput = document.getElementById("cars");

const modelsDataBox = document.getElementById("models-data-box");
const modelInput = document.getElementById("models");

const btnBox = document.getElementById("btn-box");
const alertBox = document.getElementById("alert-box");

const modelText = document.getElementById("model-text");

$.ajax({
  type: "GET",
  url: "/prices/cars-json/",
  success: function (response) {
    console.log(response.data);
    const carsData = response.data;
    carsData.map((item) => {
      const option = document.createElement("div");
      option.textContent = item.name;
      option.setAttribute("class", "item");
      option.setAttribute("data-value", item.value);
      carsDataBox.appendChild(option);
    });
  },
  error: function (error) {
    console.log(error);
  },
});

carInput.addEventListener("change", (e) => {
  btnBox.classList.remove("not-visible");
  console.log(e.target.value);
  const selectedCar = e.target.value;

  modelsDataBox.innerHTML = "";
  modelText.textContent = "Choose a model";
  modelText.classList.add("default");

  $.ajax({
    type: "GET",
    url: `/prices/models-json/${selectedCar}/`,
    success: function (response) {
      console.log(response);
      const modelsData = response.data;
      modelsData.map((item) => {
        const option = document.createElement("div");
        option.textContent = item.name;
        option.setAttribute("class", "item");
        option.setAttribute("data-value", item.value);
        modelsDataBox.appendChild(option);
      });
    },
    error: function (error) {
      console.log(error);
    },
  });
});
