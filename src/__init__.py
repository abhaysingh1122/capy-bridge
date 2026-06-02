"""capy-bridge.

Control Claude Code on your computer from your phone, over Telegram.
Meet Capybara — a chill, always-on AI sidekick with full access to your
machine, running on your existing Claude Code login.
"""

import tomllib
from importlib.metadata import PackageNotFoundError
from importlib.metadata import version as _pkg_version
from pathlib import Path

# Read version from pyproject.toml when running from source (always current).
# Fall back to installed package metadata for pip installs without source tree.
_pyproject = Path(__file__).resolve().parent.parent / "pyproject.toml"
try:
    with open(_pyproject, "rb") as _f:
        __version__: str = tomllib.load(_f)["project"]["version"]
except Exception:
    try:
        __version__ = _pkg_version("capy-bridge")
    except PackageNotFoundError:
        __version__ = "0.0.0-dev"

__author__ = "Abhay Singh"
__license__ = "MIT"
__homepage__ = "https://github.com/abhaysingh1122/capy-bridge"
