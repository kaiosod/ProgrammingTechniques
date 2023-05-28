#!/bin/bash

cond=0
name=0
new_name=0

while [ $cond -ne 1 ]
do
	clear 
	echo "Digite 1 para Sair"
	echo "Digite 2 para Cadastro"
	echo "Digite 3 para Consulta"
	echo "Digite 4 para Alteração"
   	echo "-----------------------"
   	read cond

   	if [ $cond -eq 2 ]; then
       		echo "===Cadastro==="
		read -p "Digite seu nome-" nome
		read -p "Digite sua idade-" idade
		read -p "Digite sua nota-" nota
		echo -e "$nome, $idade, $nota" >> dataset.txt
	elif [ $cond -eq 1 ]; then 
	       echo "Finalizado"	
    	elif [ $cond -eq 3 ]; then
		echo "===Consulta==="
		echo "Insira o nome do aluno"
		read name

		grep "$nome" dataset.txt 
    	elif [ $cond -eq 4 ]; then
		echo "===Alteração==="
		echo "Digite o nome do aluno"
		echo "Digite o novo nome"
		read new_name
		grep "$nome" dataset.txt | echo "$new_name" >> dataset.txt
        	
    	else
        	echo "Opção Inválida"
    	fi
done

