1.2
===

Merge with skeleton.

Use ``pkgutil`` for backports namespace package.

1.1
===

Per Issue #1, this backport now relies on the more authoritative
`typing <https://pypi.io/project/typing>`_ package
and requires it selectively on the necessary platforms.

For compatibility and to supply forward compatibility,
the ``backports.typing`` namespace hosts a bundled
copy of late releases of the authoritative package
(3.5.2 with this release).

Therefore, a package requiring typing can _require_ this
package to selectively install the ``typing`` module on
the relevant platforms and then in the code may simply
``import typing``.

Also, hosting was moved to Github with continuous
deployment.

1.0
===

Initial release.
