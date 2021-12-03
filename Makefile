format:
	black **
	isort boombash/**
	isort tests/**
test:
	python -m unittest
