import os
from pathlib import Path

allowed = {"success", "test_failure", "missing_dependency", "syntax_error", "configuration_error"}
scenario = os.getenv("REQUESTED_SCENARIO", "").strip() or Path("scenario.txt").read_text().strip()
if scenario not in allowed:
    raise ValueError("Choose one of: " + ", ".join(sorted(allowed)))
with open(os.environ["GITHUB_ENV"], "a", encoding="utf-8") as env:
    env.write(f"SCENARIO={scenario}\n")
print(f"Selected controlled demonstration: {scenario}")
