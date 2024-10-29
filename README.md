# Todo-list assignment

This is the completed take-home assignment for "Bugs and Glitches".

## Installation

>[!TIP]
>This repository provides a Guix manifest. Guix users may use this to create an ephemeral environment on the Guix System, or the Guix package manager.

This repository uses `PDM`, a modern package manager for Python. More of how it is used can be referred in the [documentation](https://pdm-project.org/en/latest/).

To get started, we will install and update `PDM` with `pip`:

```console
pip install --user pdm
pdm self update
```

>[!NOTE]
>In case if the `pdm` command is still not exposed to the shell, you may try running:
>
>```console
>python -m pdm <command>
>```

To install the dependencies:

```console
pdm install
```

## Running

The web-application can be run in development mode by:

```console
pdm run fastapi dev main.py
```
