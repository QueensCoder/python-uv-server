hello:
	echo "Hello, World!"

.PHONY: special
migration:
	@if [ -z "$(arg)" ]; then \
		echo "Error: 'arg' is required. Usage: make migration arg=<value>"; \
		exit 1; \
	fi; \
     uv --directory db/migrations run alembic revision -m "$(arg)"