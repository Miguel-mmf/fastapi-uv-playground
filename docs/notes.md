## Installation
___

You can install uv today via our standalone installers, or from PyPI.

```bash
pipx install uv && uv --version
```

## Working on project
___

uv manages project dependencies and environments, with support for lockfiles, workspaces, and more, similar to *rye* or *poetry*:

```bash
uv init . -p 
```

Project structure:

    .
    ├── .venv
    │   ├── bin
    │   ├── lib
    │   └── pyvenv.cfg
    ├── .python-version
    ├── README.md
    ├── hello.py
    ├── pyproject.toml
    └── uv.lock

* The pyproject.toml contains metadata about your project.
* The .python-version file contains the project's default Python version.
* The .venv folder contains your project's virtual environment, a Python environment that is isolated from the rest of your system.
* uv.lock is a cross-platform lockfile that contains exact information about your project's dependencies. Unlike the pyproject.toml which is used to specify the broad requirements of your project, the lockfile contains the exact resolved versions that are installed in the project environment.


## Managing dependencies 
___

You can add dependencies to your `pyproject.toml` with the uv add command.

```bash
uv add 'fastapi[standard]'
```

To remove a package, you can use uv remove:
```bash
uv remove fastapi'
```

To upgrade a package, run uv lock with the --upgrade-package flag:
```bash
uv lock --upgrade-package fastapi'
```

## Running commands
___

`uv run` can be used to run arbitrary scripts or commands in your project environment:
```bash
uv run hello.py
```

## Building distributions
___

`uv build` can be used to build source distributions and binary distributions (wheel) for your project.
```bash
uv build
```

## Python management
___

uv installs Python and allows quickly switching between versions.

```bash
uv python install 3.12
```



___
Ref.: [uv docs](https://docs.astral.sh/uv/)
