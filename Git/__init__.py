# /Git/__init__.py


# Define Setup
def setup() -> None:
    from pathlib import Path

    PATH = "~/.config/git/"
    if not (path := Path(PATH).expanduser()).exists():
        path.symlink_to(Path(__file__).parent)


if __name__ == "__main__":
    setup()
