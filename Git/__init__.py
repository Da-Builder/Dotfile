# /Git/__init__.py


def setup() -> None:
	from pathlib import Path
	from shutil import rmtree

	# Define Path
	BASE: Path = Path(__file__).parent / "Configuration"
	PATH: Path = Path("~/.gitconfig").expanduser()

	# Clean Destination
	if PATH.exists():
		PATH.unlink() if not PATH.is_dir() else rmtree(PATH)

	# Create Symbolic Link
	PATH.symlink_to(BASE)


if __name__ == "__main__":
	setup()
