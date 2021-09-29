format:
	black **
	isort boombash/**
	isort tests/**
test:
	coverage run -m unittest
