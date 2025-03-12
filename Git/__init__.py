# /Git/__init__.py


def setup() -> None:
    from pathlib import Path

    configuration: Path = Path("~/.config/git").expanduser()
    parent: Path = Path(__file__).parent

    if not configuration.exists():
        configuration.symlink_to(parent)
        print(f"{parent.name.title()}: Successfully Established Link")

    else:
        print(f"{parent.name.title()}: Already Established Link")


if __name__ == "__main__":
    setup()
