# Database CI/CD Project

![CI](https://github.com/dhruv0515/db-cicd-project/actions/workflows/ci.yml/badge.svg)

This project demonstrates:

- Version-controlled database migrations
- Automated schema validation
- GitHub Actions CI pipeline
- PostgreSQL service integration

## Workflow

On every push:
1. PostgreSQL container starts
2. Migration scripts execute
3. Automated tests validate schema

## Tech Stack
- PostgreSQL
- Pytest
- GitHub Actions
- Python

Testing CI pipeline trigger