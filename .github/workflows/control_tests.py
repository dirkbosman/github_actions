name: CI Workflow Pytest and Flake8
on: push
jobs:
  qa:
    name: Run Tests and Linting
    runs-on: ubuntu-20.04
    steps:
      - name: Checkout code
        uses: actions/checkout@v3
      
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: "3.x"

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install pytest flake8

      - name: Run tests
        run: pytest tests/

      - name: Run flake8
        run: flake8 .
