.DEFAULT_GOAL :=
DC = docker compose
CHESS_API_SERVICE=chess_api


# BASE DOCKER COMMANDS
up: ## Build and start all services in detached mode.
	${DC} up -d --build

down: ## Stop and remove all running services.
	${DC} down

logs: ## Display logs for all services, useful for monitoring and debugging.
	${DC} logs --follow


restart: ## Restart all running services to apply any changes.
	${DC} restart

## Special api commands
chess_api_logs: ## Display logs for the university api service only.
	${DC} logs --follow ${CHESS_API_SERVICE}

chess_api_shell: ## Access the shell inside the university api container for debugging or manual operations.
	${DC} exec ${CHESS_API_SERVICE} /bin/bash


# HELP
.PHONY: help
help: ## Show this help message
	@echo "Usage: make [command]"
	@echo ""
	@echo "Commands:"
	@awk 'BEGIN {FS = ":.*?## "; section=""; prev_section=""} \
		/^[#].*/ { \
			section = substr($$0, 3); \
		} \
		/^[a-zA-Z0-9_-]+:.*?## / { \
			if (section != prev_section) { \
				print ""; \
				print "\033[1;34m" section "\033[0m"; \
				prev_section = section; \
			} \
			gsub(/\\n/, "\n                      \t\t"); \
			printf " \x1b[36;1m%-28s\033[0m%s\n", $$1, $$2; \
		}' $(MAKEFILE_LIST)