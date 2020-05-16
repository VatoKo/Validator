import importlib
import os
import pkgutil
from pathlib import Path


class Rule:
    def __init__(self):
        pass

    def __call__(self, arg):
        return False

    def __from_str__(self):
        pass


# Iterate each module in the given package and fill __all__ dictionary
__all__ = {}
for (_, file, _) in pkgutil.iter_modules([Path(__file__).parent]):
    # Get Absolute Path
    module_abs_path = f"validator.rules_src.{file}"

    # Import given module
    pkg = importlib.import_module(module_abs_path)

    # Import all classes from given modules
    names = [x for x in pkg.__dict__ if not x.startswith("_")]
    print(names)
    # add class from module to globals() adn all (e.g. add 'min.Min')
    __all__.update({k.lower(): getattr(pkg, k) for k in names})