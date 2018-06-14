.PHONY: venv
venv:
	python3 -m venv ./.venv

.PHONY: install_precommit
install_precommit:
	python3 -m pip install pre-commit; \
	python3 -m pip install flake8 pylint;
	pre-commit install; \
	pre-commit autoupdate;
