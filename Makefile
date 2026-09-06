.PHONY: help db-up db-down db-reset backend backend-stop backend-logs frontend health

help:
	@echo "Available commands:"
	@echo "  make db-up        - start Postgres + Redis containers"
	@echo "  make db-down      - stop Postgres + Redis containers"
	@echo "  make db-reset     - wipe and recreate the database (destroys data)"
	@echo "  make backend      - start FastAPI in the background, logs to backend/uvicorn.log"
	@echo "  make backend-stop - stop the background FastAPI process"
	@echo "  make backend-logs - tail the FastAPI log"
	@echo "  make frontend     - start the Next.js dev server (runs in foreground)"
	@echo "  make health       - curl the /health endpoint"

db-up:
	docker compose up -d
	@sleep 3
	docker compose ps

db-down:
	docker compose down

db-reset:
	docker compose down -v
	docker compose up -d
	@sleep 8
	docker compose ps

backend:
	@lsof -ti :8000 | xargs kill 2>/dev/null || true
	cd backend && nohup .venv/bin/uvicorn app.main:app --reload --reload-dir app --reload-exclude '.venv/*' --port 8000 > uvicorn.log 2>&1 &
	@sleep 2
	@cat backend/uvicorn.log

backend-stop:
	@lsof -ti :8000 | xargs kill 2>/dev/null || true

backend-logs:
	tail -f backend/uvicorn.log

frontend:
	cd frontend && npm run dev

health:
	curl http://localhost:8000/health
