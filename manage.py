#!/usr/bin/env python
import os
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

# Permitir encontrar el proyecto y la aplicación store
sys.path.insert(0, str(BASE_DIR))
sys.path.insert(0, str(BASE_DIR / "techgear_web"))

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "techgear_web.settings"
)

def main():
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)

if __name__ == "__main__":
    main()
