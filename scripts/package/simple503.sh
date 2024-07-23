#!/usr/bin/env bash
rm -rf repository
simple503 --config pyproject.toml .
set -a 
source .env
aws s3 cp --recursive "repository" "s3://${BUCKET_NAME}/" 