const boxi = document.querySelectorAll("#box");

console.log(boxi)

boxi.forEach(function (box) {
    box.addEventListener("click", function (event) {
      this.style.backgroundColor = "#" + Math.floor(Math.random()*16777215).toString(16);
    });
  }); 


