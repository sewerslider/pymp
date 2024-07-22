test-run:
	poetry run python src/main.py ex.mp3

install-deps:
	poetry lock
	poetry --no-root install
