define USAGE
Commands:
	init		Install Python dependencies
	run 		Run the application
	keycloak	Launch a keyclock container
	clean		Clean cache and .py file command for macos
	network		Create a shared docker network
	freeze		pip freeze
endef

export USAGE

app_name = flask-prod-app
docker_network = keycloakNetwork

help:
	@echo "$$USAGE"

init:
	pip install -r resources/requirements/common.txt

run:
	python3 main.py

clean:
	find . -type f -name '*.py[co]' -delete -o -type d -name __pycache__ -delete

network:
	docker network create $(docker_network)

keycloak:
	docker-compose -f resources/docker/docker-compose.yml up -d

freeze:
	 pip freeze > resources/requirements/common.txt