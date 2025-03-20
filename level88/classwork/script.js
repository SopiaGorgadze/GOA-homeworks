// Write a function temperatureStatus that takes a temperature and returns a string:

// "Very cold" if the temperature is below -10 degrees.
// "Cold" if the temperature is from -10 to 0 degrees.
// "Normal" if the temperature is from 0 to 20 degrees.
// "Warm" if the temperature is from 20 to 30 degrees.
// "Hot" if the temperature is above 30 degrees.
// If the temperature is not provided, consider it as 20 degrees.



function temperature(status = 20){
    if(status< -10){
        return `very cold its ${status} degrees`
    }else if(status >= -10 && status < 0){
        return `cold its ${status} degrees`
    }else if(status >= 0 && status < 20){
        return `normal its ${status} degrees`
    }else if(status >= 20 && status < 30){
        return `warmits ${status} degrees`
    }else{
        return `hot ${status} degrees`}
        
}


// Calculator with Operations
// Write a function calculate that takes three parameters: two numbers and an operator. The operator can be:

// "+" for addition
// "-" for subtraction
// "*" for multiplication
// "/" for division
// If the operator is missing or unsupported, the function should return "Invalid operation". If division by zero occurs, return "Error: division by zero". If any of the parameters is missing, use 0 as the default value.




function calculator(num1 = 0, num2 = 0, operator = "Invalid operation"){
    if(operator === "+"){
        return num1 + num2
    }else if (operaror ==="-"){
        return num1 - num2
    }else if (operaror ==="*"){
        return num1 * num2
    }else if (operaror ==="/"){
        return num1 / num2
    }else if(num1 == 0 || num2 == 0){
       return "Error: division by zero"
    }
}