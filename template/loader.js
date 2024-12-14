const Bodyloader = document.getElementById("loader");
const body = document.getElementById("content");

function ready() {
  Bodyloader.classList.add("uk-hidden");
  body.classList.remove("uk-hidden");
}