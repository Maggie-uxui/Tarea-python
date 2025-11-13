function preguntarNumero(txt){
    let numUser;
    numUser=parseFloat(prompt(txt));
    while (isNaN(numUser)){
     alert("Solo se permiten numeros");
     numUser=parseFloat(prompt(txt));
    }
    return numUser
}

//1
let num1, num2, suma;
num1=parseInt(preguntarNumero("Ingrese un Numero"));
num2=parseInt(preguntarNumero("Ingrese un Numero"));
suma=num1+num2;
console.log(suma);
// //2
while (num2==0){
alert("El segundo numero no puede se un Cero...Ingrese nuevamente");
num2=parseInt(preguntarNumero("Ingrese un Numero"));
}
div=num1/num2;
console.log(div);

//3
let numR, color;
numR=parseInt(preguntarNumero("Ingrese un Numero"))
color=prompt("Ingrese un color")

for(let i=1; i<=numR; i=i+1){
    console.log(color + i);
}

4
let numUser, promedio, sumaA, contador, numUser2, numMayor;


numUser2=preguntarNumero("Ingrese un Numero");
numMayor=numUser2
sumaA=0;
contador=0;
promedio=0;
while(numUser2!=0){
    if(numMayor<numUser2){
        numMayor=numUser2
    }
    sumaA=sumaA+numUser2;
    contador=contador+1;
    numUser2=preguntarNumero("Ingrese un Numero");
}
if (contador==0){
    alert("No ingreso ningun numero, No se puede Obtener un promedio")
}
promedio=sumaA/contador
console.log(promedio)
console.log(numMayor)

//5
function esPar(num){
    if (num%2 == 0){
        return(console.log(num + " Es Par"));
    }else{
        return(console.log(num + " Es Impar"));
    }
}

esPar(0)

//-----------------------array---------------------------
//1 y 2

// let frutas=["manzanas","peras","bananas","duraznito"];
// console.log(frutas[0],frutas[frutas.length-1]);

// frutas.push("naranjas");
// console.log(frutas.length);

//3 y 4

// let colores=[], coloresUser, colorUser, estaColor;

// for (let i=0; i<5; i++){
//     coloresUser=prompt("Ingrese un color");
//     colores.push(coloresUser);
// }

// for (let i=0; i<5; i++){
//     console.log(colores[i])
// }

// colorUser=prompt("Ingrese un color que quiera Buscar");
// for (let i=0; i<coloresUser.length; i++){
//     if (coloresUser[i]==colorUser){
//         estaColor=true
//     }
// }
// if (estaColor==true) {
//     alert("El color "+ colorUser + " esta en la lista.")
// }else{
//     alert("El color "+ colorUser + " no esta en la lista.")
// }

// 5

let numeros=[4,98,257,-85,0,21,-582,148,-293], numeroMayor, suma, positivos=[], pares=[];
positivos=0
suma=0
numeroMayor=numeros[0]


for (i=0; i<numeros.length; i++){
    
    if (numeros[i]>numeroMayor) {
        numeroMayor=numeros[i];
    }

    suma=suma+numeros[i];

    if (numeros[i]>0) {
        positivos=positivos+1;
    }

    if (numeros[i] % 2 == 0) {
        pares.push(numeros[i]);
    }
}

console.log(pares)

