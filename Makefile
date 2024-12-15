.PHONY: install next

install:
	pip install -r python/requirements.txt

next:
	copier copy --trust gh:gahjelle/template-aoc-python python/
