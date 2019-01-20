# Aplicação CAIXA ALTA (cliente e servidor UDP)

Os códigos em Python em anexo correspondem a uma aplicação cliente e uma aplicação servidor que utilizam o protocolo de transporte UDP para se comunicar.

Esta aplicação tem a seguinte função: 

O usuário digita uma frase em caixa baixa na aplicação cliente, que envia uma requisição ao servidor. O servidor, ao receber a frase em caixa baixa, faz a sua conversão para caixa alta (com o método upper) e envia a frase modificada ao cliente.

Você deve executar os dois códigos em computadores separados, preferencialmente no mesmo laboratório ou na sua rede doméstica. Algumas alterações serão necessárias (por exemplo, substituir o 'hostname' pelo endereço de IP do servidor e o número de porta por um número de sua escolha, supostamente pré-combinado entre cliente e servidor).

Faça as adaptações necessárias nos códigos para que a aplicação funcione corretamente no seu computador (hospedeiro cliente) e no computador do colega ao lado (hospedeiro servidor). Depois, faça modificações no código para que a aplicação funcione com o protocolo de transporte TCP (e não o UDP).
