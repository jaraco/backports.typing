import path
import pip


def find_module(root):
	"""
	Search root for a typing module
	"""
	mod, = (
		item
		for item in root.walk()
		if item.isfile()
		and item.basename() == 'typing.py'
	)
	return mod


def main():
	with path.tempdir() as tmp_install:
		pip.main(['install', '--prefix', tmp_install, 'typing>=3.5.2'])
		module = find_module(tmp_install)
		target = path.Path('backports') / 'typing.py'
		if target.exists():
			target.remove()
		module.copy(target)

if __name__ == '__main__':
	main()
