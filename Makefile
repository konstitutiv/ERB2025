SHELL := /bin/zsh

up:
	source ~/.zshrc && workon erb2025 && \
	python manage.py runserver

static:
	python manage.py collectstatic