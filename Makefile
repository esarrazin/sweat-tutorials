.PHONY: pdf

pdf:
	test -d pdf && rm -rf pdf || true
	mkdir -p pdf
	pixi run --no-install -q --no-progress quarto render --profile beamer
	cp _beamer/docs/*.pdf pdf/
