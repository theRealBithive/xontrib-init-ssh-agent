import subprocess

__all__ = ()

# Launches the ssh-agent if no PID or SOCK is in the ENV

if not __xonsh__.env.get('SSH_AGENT_PID', False):

    output = subprocess.check_output('ssh-agent')

    output = output.decode("utf-8")
    output = output.split(';')
    # Split the output on ; which seperates the commands resulting in a List that looks like this:
    # ['SSH_AUTH_SOCK=/tmp/ssh-XXXXXXIOvdyN/agent.20259', ' export SSH_AUTH_SOCK', '\nSSH_AGENT_PID=20260', ' export SSH_AGENT_PID', '\necho Agent pid 20260', '\n']

    SSH_AUTH_SOCK = output[0].split('=')[1]
    SSH_AGENT_PID = output[2].split('=')[1]

    __xonsh__.env['SSH_AUTH_SOCK'] = SSH_AUTH_SOCK
    __xonsh__.env['SSH_AGENT_PID'] = SSH_AGENT_PID
