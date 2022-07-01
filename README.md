## Motivation

I needed a way to start ssh-agent and keep it across terminal sessions. Most desktop environments will do this for you.

## Installation

To install use pip:

```bash
xpip install xontrib-init-ssh-agent
# or: xpip install -U git+https://github.com/theRealBithive/xontrib-init-ssh-agent
```

## Usage

```bash
xontrib load init_ssh_agent
```

To kill the ssh_agent use the `ssh-agent -k` command. n.b. the environment variables will not be unset and a new agent is only started with another terminal session.


## Known issues

Works fine on my PC(tm)

## Credits

This package was created with [xontrib cookiecutter template](https://github.com/xonsh/xontrib-cookiecutter).
