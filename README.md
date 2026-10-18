# CloudPulse test application

Upload the contents of this folder to its own public repository, normally `YOUR_USERNAME/cloudpulse-test-app`. The `.github/workflows/demo-ci.yml` file must be at the repository root's `.github/workflows/` path.

This repository produces real Python/pytest logs for the CloudPulse dashboard to analyze. It contains no API keys or CloudPulse credentials.

## Choose a scenario

In GitHub → **Actions → CloudPulse Demo CI → Run workflow**, select:

| Scenario | Result |
|---|---|
| `success` | Tests pass |
| `test_failure` | Real pytest assertion failure: expected 249, actual 250 |
| `missing_dependency` | Real `ModuleNotFoundError` for a deliberately nonexistent module |
| `syntax_error` | Real Python `SyntaxError` while compiling invalid sample source |
| `configuration_error` | Real `KeyError` for an unset required environment variable |

For pushes/pull requests, the scenario comes from `scenario.txt`. Change that file, commit, and push to produce a selected result. Set it back to `success` afterward.

The missing module is deliberately fictional. Do not try to install a similarly named public package just to fix this demonstration. Switch the scenario back to success.

## Connect CloudPulse

Add a **Workflow runs** webhook in this repository's settings:

- Payload URL: `https://YOUR_CLOUDPULSE_HOST/webhook/github`
- Content type: `application/json`
- Secret: the same private `GITHUB_WEBHOOK_SECRET` configured in CloudPulse
- SSL verification: enabled

The CloudPulse backend also needs this repository in `GITHUB_REPOSITORIES` and a suitable GitHub token to read Actions logs.

The scenario scripts only generate CI outcomes. The LLM explanations are generated separately by the CloudPulse backend using Gemini. The repository contains no hardcoded CloudPulse analysis.
