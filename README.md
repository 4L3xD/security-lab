# Laboratório de Segurança
Este projeto contém aplicações vulneráveis, seus respectivos [exploits](https://en.wikipedia.org/wiki/Exploit_(computer_security)) e correções.

### Objetivo
Possibilitar o desenvolvimento técnico em Segurança da Informação através de laboratórios práticos de Segurança de Aplicações com enfoque nas subáreas:
- Pentesting;
- Desenvolvimento Seguro;
- DevSecOps.

___
**Público-alvo:** _Desenvolvedores e profissionais de Segurança da Informação._
___

## Como executar este projeto
Este repositório contém diretórios nomeados com vulnerabilidades, sendo cada diretório um laboratório.

Para executar o laboratório da vulnerabilidade SSRF, _por exemplo_, é necessário:

1. Entrar na raíz do projeto:
`cd SSRF/var/www/TestApp`

2. Executar o arquivo bash que faz build da imagem e executa o container docker:
`sudo bash start.sh`

3. Listar containers:
`docker ps -l`

Ao finalizar os estudos da vulnerabilidade em questão você pode parar o container e deletar a imagem do mesmo:
```sudo bash stop.sh```.

### Comandos úteis
**Atualiza alterações de script no servidor** 
```sudo touch uwsgi.ini```