from invoke import task

project_name="mtgjson5"

@task
def format(c):
    """
    Format the code to follow coding standards.
    """
    # Sort imports
    c.run(f"isort --profile black {project_name}/")

    # Run black and edit all files in place
    c.run(f"black {project_name}/")

@task
def check_format(c):
    """
    Check code formatting.
    """
    # dry-run isort to see if imports need resorting
    c.run(f"isort --profile black --check-only {project_name}/")

    # Run black and edit all files in place
    c.run(f"black --check {project_name}/")

@task
def lint(c):
    """
    Check the code using static analyzers.
    """
    # mypy static type checking only
    c.run(f"mypy {project_name}/")

    # Run linting tools
    c.run(f"pylint {project_name}/ --rcfile=.pylintrc")

@task
def test(c):
    """
    Run tests.
    """
    # Run unit tests with coverage
    c.run("python -m pytest tests/")

@task(check_format, lint, test)
def ci(c):
    """
    Run all checks as the continuous integration would do.
    """
