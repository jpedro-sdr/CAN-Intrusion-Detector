#!/bin/bash

# Nome do arquivo de log
logfile="candump_new.txt"

# Inicializa a variável message como vazia
message=""

# Lê o arquivo de log linha por linha
while IFS= read -r line
do
  # Procura pela mensagem no log
  if [[ $line == can0* ]]; then
    # Extrai a mensagem
    message=$(echo $line | grep -o "can0 .*")
  fi
done < "$logfile"

# Se uma mensagem foi encontrada, executa o comando cansend com a última mensagem extraída
if [[ ! -z $message ]]; then
  cansend $message
fi
