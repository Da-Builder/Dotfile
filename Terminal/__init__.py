# /Terminal/__init__.py


# Define Setup
def setup() -> None:
    import subprocess
    from pathlib import Path

    # Setup Configuration File
    PATH = "~/.local/share/org.gnome.Ptyxis/palettes/"

    if not (path := Path(PATH).expanduser()).parent.exists():
        path.parent.mkdir()

    if path.is_dir(follow_symlinks=False):
        path.rmdir()
    if not path.exists():
        path.symlink_to(Path(__file__).parent)

    # Setup Configuration Option
    command: list[str] = [
        "dconf",
        "read",
        "/org/gnome/Ptyxis/default-profile-uuid",
    ]

    if not (
        profile := (
            subprocess.run(command, stdout=subprocess.PIPE)
            .stdout.decode()
            .strip("'\n")
        )
    ):
        return

    command = [
        "dconf",
        "write",
        f"/org/gnome/Ptyxis/Profiles/{profile}/opacity",
        "0.92",
    ]
    subprocess.run(command)

    command = [
        "dconf",
        "write",
        f"/org/gnome/Ptyxis/Profiles/{profile}/palette",
        "'Terminal One Dark'",
    ]
    if Path(__file__).parent.joinpath("Terminal One Dark.palette").exists():
        subprocess.run(command)


if __name__ == "__main__":
    setup()
