NAME=polity-vault-service

# COLORS
GREEN  := $(shell tput -Txterm setaf 2)
YELLOW := $(shell tput -Txterm setaf 3)
WHITE  := $(shell tput -Txterm setaf 7)
RESET  := $(shell tput -Txterm sgr0)

TARGET_MAX_CHAR_NUM=20

#.SILENT:

define colored
	@echo '${GREEN}$1${RESET}'
endef

## Show help
help:
	${call colored, help is running...}
	@echo ''
	@echo 'Usage:'
	@echo '  ${YELLOW}make${RESET} ${GREEN}<target>${RESET}'
	@echo ''
	@echo 'Targets:'
	@awk '/^[a-zA-Z\-\_0-9]+:/ { \
		helpMessage = match(lastLine, /^## (.*)/); \
		if (helpMessage) { \
			helpCommand = substr($$1, 0, index($$1, ":")-1); \
			helpMessage = substr(lastLine, RSTART + 3, RLENGTH); \
			printf "  ${YELLOW}%-$(TARGET_MAX_CHAR_NUM)s${RESET} ${GREEN}%s${RESET}\n", helpCommand, helpMessage; \
		} \
	} \
	{ lastLine = $$0 }' $(MAKEFILE_LIST)

.PHONY: run
run: ## Run as a background service
	docker-compose down
	docker-compose up --build allure-server
	make makemigrations
	make migrate
	make docker-superuser

## Applies migrations to the polity_vault database
migrate:
	@echo "Migrating database..."
	@docker-compose exec allure-server python3 manage.py migrate

## Makes migrations for the polity_vault database
makemigrations:
	@echo "Making migrations..."
	@docker-compose exec allure-server python3 manage.py makemigrations

## Create super user for polity_vault
docker-superuser:
	@echo "Creating super user..."
	@docker-compose exec allure-server python3 manage.py createsuperuser --noinput
