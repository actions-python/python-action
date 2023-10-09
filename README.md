# Create a Python Action

Use this template to bootstrap the creation of a Python action. :rocket:

This template includes compilation support, tests, a validation workflow, and
publishing guidance. There's also a simple template in the
[Hello world Python action repository](https://github.com/actions-python/hello-world-python-action).

## Create an action from this template

Click the **Use this template** button, and provide the details for your action.

## Getting Started

1. Create a virtual environment

   ```sh
   python3 -m venv .venv
   source .venv/bin/activate
   ```

1. Install the dependencies

   ```sh
   pip install -e ".[dev]"
   pre-commit install
   ```

1. Run the tests

   ```sh
   $ pytest --cov --cov-report=term-missing -q
   .....                                                        [100%]

   --------- coverage: platform <platform>, python <python> ----------
   Name              Stmts   Miss Branch BrPart  Cover   Missing
   -------------------------------------------------------------
   src/__init__.py       2      0      0      0   100%
   src/main.py          13      0      0      0   100%
   src/wait.py           6      0      2      0   100%
   -------------------------------------------------------------
   TOTAL                21      0      2      0   100%

   5 passed in 1.20s
   ```

## Update `action.yml`

The [`action.yml`](action.yml) file defines metadata for your action. For
details about this file, see
[Metadata syntax for GitHub Actions](https://docs.github.com/en/actions/creating-actions/metadata-syntax-for-github-actions).

If you copied this repository, you should update your action's `action.yml`.

## Publish

GitHub Action is run from GitHub repositories. You can use tag to create a
release.

```sh
git tag v1 -f --no-sign
git push origin v1 -f
```

## Usage

After testing, you can create a v1 tag and make other developers to use the
versioned action.

```yaml
steps:
  - name: Checkout
    id: checkout
    uses: actions/checkout@v4

  - name: Test Local Action
    id: test-action
    uses: actions-python/python-action@v1
    with:
      milliseconds: 1000
```
