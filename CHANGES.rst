1.1
===

Issue #1

This backport now relies on the more authoritative
`typing <https://pypi.io/project/typing>`_ package
and requires it selectively on the necessary platforms.

For compatibility, the ``backports.typing`` namespace
remains and simply imports all from it.

Therefore, a package requiring typing can _require_ this
package to selectively install the ``typing`` module on
the relevant platforms and then in the code may simply
``import typing``.

Also, hosting was moved to Github with continuous
deployment.

1.0
===

Initial release.
