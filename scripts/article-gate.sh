#!/usr/bin/env bash
# article-gate.sh — exits 1 if daily post limit has been reached, 0 if more can be written
# Limit: 3 posts per calendar day (NZ time)
# Usage: bash scripts/article-gate.sh && echo "can write" || echo "limit reached"

POSTS_DIR="$(dirname "$0")/../content/posts"
MAX_PER_DAY=3
TODAY="$(TZ=Pacific/Auckland date '+%Y-%m-%d')"

count=$(grep -rl "\"generated_date\": \"${TODAY}\"" "${POSTS_DIR}" 2>/dev/null | wc -l)

if [ "${count}" -ge "${MAX_PER_DAY}" ]; then
  echo "LIMIT REACHED: ${count}/${MAX_PER_DAY} posts already generated today (${TODAY} NZT)"
  exit 1
else
  echo "OK: ${count}/${MAX_PER_DAY} posts today — can write more"
  exit 0
fi
