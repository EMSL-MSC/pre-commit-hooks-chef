[![Build Status](https://travis-ci.org/EMSL-MSC/pre-commit-hooks-chef.svg?branch=master)](https://travis-ci.org/EMSL-MSC/pre-commit-hooks-chef)
[![Coverage Status](https://img.shields.io/coveralls/EMSL-MSC/pre-commit-hooks-chef.svg?branch=master)](https://coveralls.io/r/EMSL-MSC/pre-commit-hooks-chef)

pre-commit-hooks-chef
==========

Some out-of-the-box hooks for pre-commit for chef development.

See also: https://github.com/pre-commit/pre-commit


### Using pre-commit-hooks with pre-commit

Add this to your `.pre-commit-config.yaml`

    -   repo: git://github.com/pre-commit/pre-commit-hooks
        sha: ''  # Use the sha you want to point at
        hooks:
        -   id: trailing-whitespace
        # -   id: ...


### Hooks available

- `check-rspec` - run rspec on chef recipes.
- `check-foodcritic` - run foodcritic on chef cookbooks.
- `check-cookstyle` - run cookstyle on specific cookbook files.

### As a standalone package

If you'd like to use these hooks, they're also available as a standalone
package.

Simply `pip install pre-commit-hooks-chef`
