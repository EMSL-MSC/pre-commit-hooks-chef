import pytest

from pre_commit_hooks.check_cookstyle import check_cookstyle


@pytest.mark.parametrize(
    ('filename', 'expected_retval'), (
        ('recipes/default.rb', 1),
    ),
)
def test_check_cookstyle_bad(temp_bad_cookbook_dir, filename, expected_retval):
    with temp_bad_cookbook_dir.as_cwd():
        ret = check_cookstyle([filename])
        assert ret == expected_retval


@pytest.mark.parametrize(
    ('filename', 'expected_retval'), (
        ('spec/unit/recipes/default_spec.rb', 0),
        ('recipes/default.rb', 0),
        ('metadata.rb', 0),
        ('recipes/not_there.rb', 1),
    ),
)
def test_check_cookstyle(temp_cookbook_dir, filename, expected_retval):
    with temp_cookbook_dir.as_cwd():
        ret = check_cookstyle([filename])
        assert ret == expected_retval
