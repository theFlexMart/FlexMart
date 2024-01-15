#!/usr/bin/env bash
set -e

echo "updating lint: $(pwd)"
isort --profile black .
black .
