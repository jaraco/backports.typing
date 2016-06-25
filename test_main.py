import importlib


def test_natural_import():
	importlib.import_module('typing')


def test_backport_import():
	importlib.import_module('backports.typing')
