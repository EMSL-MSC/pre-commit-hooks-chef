from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

import pytest

from pre_commit_hooks.util import cmd_output


@pytest.yield_fixture
def temp_bad_cookbook_dir(tmpdir):
    with tmpdir.as_cwd():
        cmd_output('chef', 'generate', 'cookbook', 'test')
        with open('test/recipes/default.rb', 'w') as md_fd:
            md_fd.write('foo = "blah"\n')
        cb_dir = tmpdir.join('test')
    yield cb_dir


@pytest.yield_fixture
def temp_cookbook_dir(tmpdir):
    with tmpdir.as_cwd():
        cmd_output('chef', 'generate', 'cookbook', 'test')
        with open('test/LICENSE', 'w') as lic_fd:
            lic_fd.write('My License\n')
        with open('test/metadata.rb') as md_fd:
            content = md_fd.read()
        content = content.replace('# issues_url', 'issues_url')
        content = content.replace('# source_url', 'source_url')
        content = content.replace('maintainer \'The Authors\'', 'maintainer \'John Doe\'')
        content = content.replace('maintainer_email \'you@example.com\'', 'maintainer_email \'john.doe@example.com\'')
        content = content.replace('license \'All Rights Reserved\'', 'license \'Apache-2.0\'')
        content += 'supports \'centos\'\n'
        with open('test/metadata.rb', 'w') as md_fd:
            md_fd.write(content)
        cb_dir = tmpdir.join('test')
    yield cb_dir
