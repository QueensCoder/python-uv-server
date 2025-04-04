hello:
	echo "Hello, World!"

up:
	uv run fastapi dev main.py

migrations:
	uv --directory db/migrations run alembic upgrade head

.PHONY: special
revision:
	@if [ -z "$(arg)" ]; then \
		echo "Error: 'arg' is required. Usage: make revision arg=<value>"; \
		exit 1; \
	fi; \
     uv --directory db/migrations run alembic revision -m "$(arg)"

test:
	@if [ -z "$(suite)" ]; then \
		uv run pytest; \
	else \
		uv run pytest $(suite); \
	fi