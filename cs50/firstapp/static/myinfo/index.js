
// set h1 text using js
document.getElementById("title").innerText = "Faizan Patel"

// variables
let name = "Faizan" // string
let age = 30  // number

// constant
const city = "Leicester"

// object (a JavaScript Object - JSON!)
let person = {
    name: "faizan",
    age: 28,
    city: "Leicester"
}

console.log(person)
// read a property (in two ways)
console.log(person.name)
console.log(person['name'])
console.log()

// nulls and undefined!
let country;  // value and type of this variable is undefiend
let favTeam = null // to clear the value of a variable (object)
console.log(typeof country)  // undefined
console.log(typeof favTeam)  // object

// Arrays 
let selectedColors = ['red', 'blue']
console.log(typeof selectedColors)
console.log(selectedColors.length)

// functions...

// definition
function myFun(name, lastName){
    console.log("Hello, " + name + " " + lastName + "!")
}

function square(num){
    return num*num
}

// call
myFun('Faizan')  // an argument is undefined by default (if not given)
myFun('Faizan', 'Patel')

let x = square(2)
