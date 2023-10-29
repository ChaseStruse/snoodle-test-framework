import importlib.machinery
import types
from inspect import getmembers, isclass


def find_test_classes(mod):
    return [c[1] for c in getmembers(mod) if isclass(c[1]) and c[0].startswith("Test")]


def load_module(file, modnr):
    loader = importlib.machinery.SourceFileLoader(f"mod{modnr}", file)
    mod = types.ModuleType(loader.name)
    loader.exec_module(mod)
    return mod
