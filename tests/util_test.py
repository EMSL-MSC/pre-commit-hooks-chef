from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

import sys

import pytest

from pre_commit_hooks.util import CalledProcessError
from pre_commit_hooks.util import cmd_output


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
