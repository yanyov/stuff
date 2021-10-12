COMPOSE_FILES = -f docker-compose-pg.yaml -f docker-compose.yaml
TIMEOUT=30

default:
        all

start:  up corda backend

initial-registration:   up corda-initial-registration corda backend

clean: destroy

all: initial-registration

up:
        docker-compose $(COMPOSE_FILES) up -d

down:
        docker-compose $(COMPOSE_FILES) down

destroy:
        docker-compose $(COMPOSE_FILES) down -v

ps:
        docker-compose $(COMPOSE_FILES) ps

corda-initial-registration:
        docker exec -d corda java -jar /opt/corda/bin/corda.jar run-migration-scripts --core-schemas --app-schemas
        sleep $(TIMEOUT)
        docker exec -d corda java -jar /opt/corda/bin/corda.jar initial-registration
        sleep $(TIMEOUT)

corda:
        docker exec -d corda java -jar /opt/corda/bin/corda.jar

backend:
        docker exec -d backend java -jar /opt/axedras/lib/axedras-api.jar --spring.config.location=file:/opt/axedras/backend.yml
