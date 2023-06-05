// const contas = [
//   { numero: 12345, saldo: 1000 },
//   { numero: 54321, saldo: 500 },
//   { numero: 98765, saldo: 2500 },
// ];
// 1- verificar se as contas existem e se tem saldo.
// function transfer(origem, destino, valor) {
//   const contaOrigem = contas.find((c) => c.numero === origem);
//   // console.log(contaOrigem)
//   if (!contaOrigem) {
//     // console.log("Conta de origem nao existe");
//     return;
//   } else if (contaOrigem.saldo < valor) {
//     // console.log('Saldo insuficiente');
//     return;
//   }
// verificar se a conta de origem existe.
  // const contaDestino = contas.find((c) => c.numero === destino);
  // console.log(contaDestino)
  // if (!contaDestino) {
    // console.log("Conta de destino nao existe");
    // return;
  // } else if (contaDestino.saldo < valor) {
    // console.log('Saldo insuficiente');
    // return;
  // }
// Realizer transferencia
//   contaOrigem.saldo -= valor;
//   contaDestino.saldo += valor;
// }

// transfer(12345, 54321, 1000);
// const result1 = transfer(12345, 54321, 1000);
// const result2 = transfer(12345, 5432100000, 900);
// console.log(result)
// console.log(result1)
// console.log(result2)


// This function return the amount of coins and they'r value as an Array

// function change(valor, moedas) {
//   let result = [];
//   for( let i = 0; i < moedas.length; i ++) {
//     while(valor >= moedas[i]) {
//       valor -= moedas[i]
//       result.push(moedas[i])
//     }
//   }
//   return result
// }

// const moedas = [25, 10, 5, 1]
// const valor = 80;
// const resultado = change(valor, moedas)
// console.log(resultado)
const obj1 = {
  name: 'Rogerinho'
};

const obj2 = {
  name: 'Rogerinho'
};

const obj3 = obj1;
const a = 'Rogerinho';
const b = 'Rogerinho';

console.log(a === b);
console.log(obj1 === obj2)
console.log(obj1 === obj3);
