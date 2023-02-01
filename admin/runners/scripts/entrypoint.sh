#!/bin/bash

# FETCH THE INSTALLATION TOKEN AT THE ORGANIZATIONAL LEVEL
export TOKEN=$(curl \
  -X POST \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer $GITHUB_PAT"\
  -H "X-GitHub-Api-Version: 2022-11-28" \
  https://api.github.com/orgs/$ORG/actions/runners/registration-token | jq -r '.token')

# INIT AND CONFIGURE THE GITHUB RUNNER TO BE EPHEMERAL
/home/runner/config.sh --unattended \
    --url "https://github.com/$ORG" \
    --token $TOKEN \
    --labels self-hosted,linux,ubuntu \
    --ephemeral

# START THE RUNNER
/home/runner/run.sh

# ON COMPLETION REMOVE THE RUNNER CONFIGURATION
/home/runner/config.sh remove \
    --token $TOKEN
