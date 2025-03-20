// var არ ქმნის ინფორმაციის საცავს, არამედ ქმნის კუთვნილებას window ობიექტში

// ჩვენ შეგვიძლია var-ით რედეკლარაცია
const p = document.getElementById("count");
const btn = document.getElementById("btn");

let count = 0;

function increment() {
    count++
    p.textContent = `Count: ${count}`
}

btn.onclick = increment;



// prefix and postfix 

// postfix -> num++
// postfix -> ++num



// string literally

let num = 1

console.log(`hello nigga ${num}`)

alert("hello nigga")
prompt("hello niggaaaa")



// ES6 is ecma script 6

// scripting language is only read in browser


// if you wanna create games or apps you wanna use js
// if you wanna create scripting languages you wanna use ecma script


// 1) შექმენით ცვლადი სადაც მომხმარებელს prompt ის საშუალებით შემოატანინებთ თავის ბიუჯეტს, თუ ბიუჯეტი >= 500, კოპნსოლში გამოიტანეთ ტექსტი რომ მას გააჩნია საკმარაისი თანხა, სხვა შემთვევაში კი დაუბეჭდეთ რომ არასაკმარისი თანხა აქვს

// 2) განაგრძეთ პირველი დავალება და პირობაში შეიტანეთ ცვლილება, თუ ბიუჯეტი >= 500 და <= 1000 მხოლოდ მაშინ დაუბეჭდეთ რომ აქვს საკმარისი ბიუჯეტი



let budget = prompt("enter your sallary pls: ")

if(budget>= 500 && budget <= 1000){
    console.log("you have enough money")
}else{
    console.log("get out youre broke")
}


