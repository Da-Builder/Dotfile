# /Application/__init__.py


def setup() -> None:
	from pathlib import Path
	from shutil import rmtree

	# Define Path
	BASE: Path = Path(__file__).parent
	PATH: Path = Path("~/.local/share/applications").expanduser()
	SOURCE: dict[str, str] = {
		"Chrome": "google-chrome.desktop",
		"Code": "code.desktop",
		"File": "org.gnome.Nautilus.desktop",
		"Mimeapp": "mimeapps.list",
	}

	# Clean Destination
	if PATH.exists():
		PATH.unlink() if not PATH.is_dir() else rmtree(PATH)
	PATH.mkdir()

	# Create Symbolic Link
	for source, destination in SOURCE.items():
		PATH.joinpath(destination).symlink_to(BASE / source)


if __name__ == "__main__":
	setup()
