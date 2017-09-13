from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

import os
import sys

import pytest

from pre_commit_hooks.util import CalledProcessError
from pre_commit_hooks.util import cmd_output
from pre_commit_hooks.util import parse_command


def test_raises_on_error():
    with pytest.raises(CalledProcessError):
        cmd_output('sh', '-c', 'exit 1')


def test_output_error():
    hit_exception = False
    try:
        cmd_output('sh', '-c', 'echo hi >&2; echo hi; exit -1')
    except CalledProcessError as ex:
        print(str(ex), file=sys.stderr)
        hit_exception = True
    assert hit_exception
    ret = cmd_output('sh', '-c', 'echo hi >&2; echo hi; exit 255', retcode=255)
    assert ret == 'hi\n'


def test_output():
    ret = cmd_output('sh', '-c', 'echo hi')
    assert ret == 'hi\n'


def test_parse_command_basic():
    assert parse_command('cp') == '/bin/cp'


def test_parse_command_with_ext():
    old_path = os.getenv('PATH')
    os.environ['PATHEXT'] = '.conf'
    os.environ['PATH'] = '/etc'
    assert parse_command('adduser') == '/etc/adduser.conf'
    os.environ['PATH'] = old_path
