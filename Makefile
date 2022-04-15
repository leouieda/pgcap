all: build

build:
	jupyter-book build -n -W .

serve: build
	python tools/serve.py

clean:
	rm -rf _build/
