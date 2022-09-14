name: "update curpus"
on: [push]
jobs:
  build:
    runs-on: macos-latest
    strategy:
      matrix:
        python-version: [3.8]
    steps:
    - uses: actions/checkout@v2
    - name: Set up Python ${{ matrix.python-version }}
      uses: actions/setup-python@v2
      with:
        python-version: ${{ matrix.python-version }}
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install pylint
        pip install pylint-pydantic
        pip install -r jmm/requirements.txt
        pip install -r testcases/requirements.txt
    - name: run pylint
      run: |
        export PYTHONPATH='.'
        pylint jmm testcases
