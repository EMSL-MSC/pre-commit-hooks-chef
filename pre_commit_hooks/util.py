from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

import subprocess
from os import getenv
from os import path
from os import pathsep


class CalledProcessError(RuntimeError):
    pass


def cmd_output(*cmd, **kwargs):
    retcode = kwargs.pop('retcode', 0)
    popen_kwargs = {'stdout': subprocess.PIPE, 'stderr': subprocess.PIPE}
    popen_kwargs.update(kwargs)
    proc = subprocess.Popen(cmd, **popen_kwargs)
    stdout, stderr = proc.communicate()
    stdout = stdout.decode('UTF-8')
    if stderr is not None:  # pragma: no cover
        stderr = stderr.decode('UTF-8')
    if retcode is not None and proc.returncode != retcode:
        raise CalledProcessError(cmd, retcode, proc.returncode, stdout, stderr)
    return stdout


def parse_command(exe):
    """Walk the system path and return executable path."""
    real_cmd = None
    for ext in getenv('PATHEXT', '').split(pathsep):  # pragma: no branch
        for binpath in getenv('PATH').split(pathsep):  # pragma: no branch
            check_cmd = path.join(binpath, exe.strip()) + ext
            if path.isfile(check_cmd):  # pragma: no branch
                real_cmd = check_cmd
                break
        if real_cmd:  # pragma: no branch
            break
    return real_cmd
