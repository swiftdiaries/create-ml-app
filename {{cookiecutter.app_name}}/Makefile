.PHONY: help lint run

# Makefile variables
VENV_NAME:=venv
PYTHON=${VENV_NAME}/bin/python3

# Include your variables here
RANDOM_SEED:={{cookiecutter.random_seed}}
NUM_EPOCHS:={{cookiecutter.num_epochs}}
INPUT_DIM:={{cookiecutter.input_dim}}
HIDDEN_DIM:={{cookiecutter.hidden_dim}}
OUTPUT_DIM:={{cookiecutter.output_dim}}

.DEFAULT: help
help:
	@echo "make venv"
	@echo "       prepare development environment, use only once"
	@echo "make lint"
	@echo "       run pylint"
	@echo "make run"
	@echo "       run project"

# Install dependencies whenever setup.py is changed.
venv: $(VENV_NAME)/bin/activate
$(VENV_NAME)/bin/activate: setup.py
	test -d $(VENV_NAME) || python3 -m venv $(VENV_NAME)
	${PYTHON} -m pip install -U pip
	${PYTHON} -m pip install -e .
	rm -rf ./*.egg-info
	touch $(VENV_NAME)/bin/activate

lint: venv
	${PYTHON} -m pylint main.py

run: venv
	${PYTHON} main.py --seed $(RANDOM_SEED) --num_epochs $(NUM_EPOCHS) --input_dim $(INPUT_DIM) --hidden_dim $(HIDDEN_DIM) --output_dim $(OUTPUT_DIM)