# Frameworks_Full-Stack_Impacta
Repositório para as atividades contínuas da Faculdade Impacta na matéria Frameworks Full-Stack

`<< AC01 >>`
O usuário deverá enviar com o método POST os parâmetros "nota_1" e "nota_2". 
Caso o usuário não insira os argumentos com a nomenclatura correta, resultará em 404 - Bad Request. 
Caso o usuário insira uma nota que não seja dos tipos 'inteiro' ou 'float', resultará em 404 - Bad Request.

Exemplo de Requisição:
raw json = 
{ 
    "nota_1": 10,
    "nota_2": 5
}

Exemplo de retorno (200): 
7.5


`<< AC02 >>`
A AC02 consiste em uma pequena demonstração do uso de rotas. 

O usuário terá a tela de Login, e em seguida deverá ser "logado".
O mesmo poderá dizer que esqueceu sua senha, e será enviado a uma rota de redefinição de senha.
Após o login, o usuário pode deslogar, voltando ao início.

Está tudo bem simples, mas está funcional.
