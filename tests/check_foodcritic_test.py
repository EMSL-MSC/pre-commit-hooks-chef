import pytest

from pre_commit_hooks.check_foodcritic import check_foodcritic


@pytest.mark.parametrize(('filename', 'expected_retval'), (
    ('metadata.rb', 1),
))
def test_check_foodcritic_bad(temp_bad_cookbook_dir, filename, expected_retval):
    with temp_bad_cookbook_dir.as_cwd():
        ret = check_foodcritic([filename])
        assert ret == expected_retval


@pytest.mark.parametrize(('filename', 'expected_retval'), (
    ('metadata.rb', 0),
))
def test_check_foodcritic(temp_cookbook_dir, filename, expected_retval):
    with temp_cookbook_dir.as_cwd():
        ret = check_foodcritic([filename])
        assert ret == expected_retval
