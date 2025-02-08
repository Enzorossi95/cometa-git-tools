build:
	rm -rf dist/ build/
	python3 -m build
	python3 -m twine upload --config-file .pypirc dist/*

update:
	python3 -m build
	python3 -m twine upload --config-file .pypirc dist/*