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
    - name: Install Dependencies
      run: |
        python -m pip install --upgrade pip
        python -m pip install -r crazy_thursday/requirements.txt
    - name: Download Corpus
      run: |
        export PYTHONPATH='.'
        python scripts/update_curpus.py
