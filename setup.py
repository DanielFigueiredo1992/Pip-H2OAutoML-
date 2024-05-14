from setuptools import setup, find_packages
import subprocess

# Função para chamar o Makefile
def run_make():
    subprocess.run(['make', '-f', 'Makefile', 'setup'], check=True)

# Chama a função para executar o Makefile


# Configuração do pacote
setup(
    name='nome_do_pacote',
    version='0.1',
    author='Seu Nome',
    author_email='seu@email.com',
    description='Uma descrição breve do seu pacote',
    url='URL do seu repositório no GitHub ou outro lugar',
)
run_make()
