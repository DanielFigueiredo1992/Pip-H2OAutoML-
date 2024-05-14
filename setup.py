import subprocess

# Comando a ser executado
command = 'git clone https://github.com/h2oai/wave-h2o-automl.git && cd wave-h2o-automl && make setup && source venv/bin/activate'

# Iniciar o subprocesso e capturar a saída
process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)

# Capturar e imprimir a saída em tempo real
for line in process.stdout:
    print(line.strip())

# Esperar pelo término do processo
