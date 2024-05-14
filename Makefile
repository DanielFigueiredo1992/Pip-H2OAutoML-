setup:
    apt install python3.10-venv
    git clone https://github.com/h2oai/wave-h2o-automl.git
    cd wave-h2o-automl && make setup && source venv/bin/activate
