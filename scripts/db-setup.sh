#!/usr/bin/env sh

export PGUSER="postgres"
psql -c "CREATE DATABASE IF NOT EXISTS inventory" #create inventory database
psql inventory -c "CREATE EXTENSION IF NOT EXISTS \"uuid-ossp\";" #create UUID extension for psql