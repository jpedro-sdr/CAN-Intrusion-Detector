import re
import subprocess

# Abra o arquivo de log para leitura
with open('candump_new.txt', 'r') as arquivo_log:
    # Leia cada linha do arquivo de log
    for linha in arquivo_log:
        # Use uma expressão regular para encontrar a mensagem final
        match = re.search(r'can0 (.+)$', linha)
        
        # Se houver correspondência, obtenha a mensagem final
        if match:
            mensagem_final = match.group(1)
            
            # Construa o comando para executar no CMD
            comando = f'cansend can0 {mensagem_final}'
            
            # Execute o comando no CMD
            try:
                subprocess.run(comando, shell=True, check=True)
            except subprocess.CalledProcessError as e:
                print(f'Erro ao executar o comando: {e}')
