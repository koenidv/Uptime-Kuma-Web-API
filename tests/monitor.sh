#!/bin/bash

BASE_URL="http://127.0.0.1:8000"
TOKEN="${API_KEY}"

echo "Get all monitor pages:"
curl -s -L -H 'Accept: application/json' -H "Authorization: Bearer ${TOKEN}" "${BASE_URL}/monitors"
