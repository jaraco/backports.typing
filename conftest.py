import six

collect_ignore = ['backports/typing.py'] if six.PY2 else []
collect_ignore.append('bundle-typing.py')
