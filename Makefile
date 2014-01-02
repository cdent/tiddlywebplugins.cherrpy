.PHONY: test dist upload

clean:
	find . -name "*.pyc" |xargs rm || true
	rm -r dist || true
	rm -r build || true
	rm -r *.egg-info || true
	rm -r __pycache__ || true
	find . -name __pycache__ -type d | xargs rm -r || true

test: clean
	py.test -x test

dist: test
	python setup.py sdist

release: clean pypi

pypi: test
	python setup.py sdist upload
