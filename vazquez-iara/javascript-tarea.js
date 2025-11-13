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
