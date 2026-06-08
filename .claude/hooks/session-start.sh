#!/bin/bash
# SessionStart hook — install build deps so the dist/ generators and the
# product verifier work in Claude Code on the web.
set -euo pipefail

# Only needed in the remote (web) environment.
if [ "${CLAUDE_CODE_REMOTE:-}" != "true" ]; then
  exit 0
fi

REQ="${CLAUDE_PROJECT_DIR:-.}/build/requirements.txt"
if [ -f "$REQ" ]; then
  python3 -m pip install --quiet --disable-pip-version-check -r "$REQ"
fi
