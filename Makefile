test-run:
	poetry run python src/main.py ex.ogg

install-deps:
	poetry lock
	poetry --no-root install
