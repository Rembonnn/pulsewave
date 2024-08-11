# Makefile Variable
PYTHON = python
ALCHEMY = alembic
SEEDER = seeders/users_faker.py
GENERATOR = scripts/generate.py
ENV_FILE = .env

# Makefile Command
install:
	pip install -r requirements.txt

serve:
	$(PYTHON) pulsewave.py

init-migrations:
	$(ALCHEMY) init migrations

revision:
	$(ALCHEMY) revision -m "Create users table"

upgrade:
	$(ALCHEMY) upgrade head

autogenerate:
	$(ALCHEMY) revision --autogenerate -m "Auto-generated migration"

create-db:
	psql -h 127.0.0.1 -p 5432 -U postgres -d pulsewave -c 'CREATE TABLE IF NOT EXISTS users (id UUID PRIMARY KEY DEFAULT uuid_generate_v4(), name VARCHAR(255), email VARCHAR(255) UNIQUE, password VARCHAR(255), email_verified_at TIMESTAMP, created_at TIMESTAMP DEFAULT NOW(), updated_at TIMESTAMP DEFAULT NOW());'

drop-db:
	psql -h 127.0.0.1 -p 5432 -U postgres -d pulsewave -c 'DROP TABLE IF EXISTS users;'

seed-users-data:
	$(PYTHON) $(SEEDER)

generate-model:
	$(PYTHON) $(GENERATOR) model

generate-controller:
	$(PYTHON) $(GENERATOR) controller

generate-middleware:
	$(PYTHON) $(GENERATOR) middleware

check-env:
	@if [ ! -f $(ENV_FILE) ]; then \
		echo "$(ENV_FILE) file not found. Please create it with the correct database configuration."; \
		exit 1; \
	fi

all: check-env init-migrations autogenerate upgrade seed

.PHONY: install serve init-migrations revision upgrade autogenerate create-db drop-db seed-users-data generate-model generate-controller generate-middleware check-env all
