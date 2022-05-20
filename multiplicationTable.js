// program to generate multiplication tables

// take input from the user
const number = parseInt(prompt('Enter the number of tables: '));

//creating a multiplication table
for(let k = 1; k<=number; k++){
  for(let i = 1; i <= 10; i++) {

    // multiply i with number
    const result = i * k;

    // display the result
    console.log(`${k} * ${i} = ${result}`);
    if(i == 10){
      console.log('');
    }
}
}
