This MCP is built for integration with Goose.

https://block.github.io/goose/docs/tutorials/custom-extensions/#step-4-test-your-mcp-server

## ENV
Add these envs in your environment

```
JIRA_API_TOKEN=""
JIRA_URL="https://<org>.atlassian.net"
JIRA_USER_EMAIL="abc@gmail.com"
```

Get token via https://id.atlassian.com/manage-profile/security/api-tokens

## Install

`uv pip install .`

## Integrate to Goose

Follow: https://id.atlassian.com/manage-profile/security/api-tokens
Or use `goose configure` if using goose cli
