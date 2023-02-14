PROJECT := test
PYTHON_VERSION ?= 3.8
VIRTUAL_ENV ?= .venv
REQUIREMENTS = requirements.txt
RUN := . $(VIRTUAL_ENV)/bin/activate ;

create_venv:
	if [ ! -d "${VIRTUAL_ENV}" ]; then \
		python3 -m venv $(VIRTUAL_ENV) --prompt $(PROJECT); \
	fi
	ln -sf $(VIRTUAL_ENV)/bin/activate activate

install:
	$(RUN) pip install -r $(REQUIREMENTS) --prefer-binary

venv: create_venv install

runserver:
	$(RUN) python3 manage.py runserver

run: venv runserver