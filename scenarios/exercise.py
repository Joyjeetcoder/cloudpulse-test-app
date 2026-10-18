"""Controlled failures; every exception below is raised by real Python execution."""
import importlib
import os

scenario = os.environ.get("SCENARIO", "success")
if scenario == "missing_dependency":
    importlib.import_module("cloudpulse_deliberately_missing_package")
elif scenario == "syntax_error":
    compile("def broken_function(:\n    return 1\n", "demo_broken_module.py", "exec")
elif scenario == "configuration_error":
    required_setting = os.environ["CLOUDPULSE_DEMO_REQUIRED"]
    print("Required demo configuration is present.")
else:
    print("No additional failure requested.")
