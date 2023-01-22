.PHONY: check
check:
	black .
	ruff .
	mypy .
