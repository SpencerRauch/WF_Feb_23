console.log("linked")
var url = "https://pokeapi.co/api/v2/pokemon/"

var pokeInputElement = document.querySelector("#pokeNameInput")
var resultsElement = document.querySelector("#results")


async function getPoke(){
    var searchTerm = pokeInputElement.value
    console.log(searchTerm)
    var response = await fetch(url+searchTerm)
    var data = await response.json()
    console.log(data)
    resultsElement.innerHTML = `
    <img src="${data.sprites.front_default}" alt="${data.name}" width="200px">
    `
    
}

async function getRand(){
    var random = Math.floor(Math.random()*999);
    var response = await fetch(url+random)
    var data = await response.json()
    console.log(data)
    resultsElement.innerHTML = `
        <h1>${data.name} </h1>
        <img src="${data.sprites.front_default}" alt="${data.name}" width="300px">
    `

}