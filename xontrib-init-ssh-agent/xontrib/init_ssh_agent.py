
from xonsh.built_ins import XSH


__all__ = ()

print('This is xontrib-init-ssh-agent!')


# Good start! Get more documentation -> https://xon.sh/contents.html#guides

# accessing environment variables

# Some code in Using Python API:
var = XSH.env.get("VAR", "default")


result = __xonsh__.subproc_captured_stdout(['echo', '1'])

