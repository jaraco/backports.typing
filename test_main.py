import importlib

import six
import pytest


def test_natural_import():
	importlib.import_module('typing')


@pytest.mark.xfail(six.PY2,
	reason="bundled module is Python 3 only")
def test_backport_import():
	importlib.import_module('backports.typing')
