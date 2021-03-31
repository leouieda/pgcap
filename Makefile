all: build


build:
	jupyter-book build -n -W eportfolio/

serve: build
	python tools/serve.py

clean:
	rm -rf eportfolio/_build/*
