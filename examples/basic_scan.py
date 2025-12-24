from pydoctor.scanner.python_version import check_python_version
from pydoctor.scanner.venv import check_venv
from pydoctor.scanner.dependencies import check_dependencies
from pydoctor.scanner.system_libs import check_system_libs


def run_environment_diagnosis():
    """
    Run all environment checks provided by pyenv-doctor
    and return their diagnostic results.
    """
    return [
        check_python_version(),
        check_venv(),
        check_dependencies(),
        check_system_libs(),
    ]


def display_diagnosis_report(results):
    """
    Display a readable diagnostic report from
    environment check results.
    """
    for result in results:
        display_single_result(result)


def display_single_result(result):
    """
    Display the outcome of a single environment check.
    """
    print(f"{result['title']}: {'OK' if result['ok'] else 'FAIL'}")

    # If the check failed, explain why and how to fix it
    if not result["ok"]:
        print(result["reason"])
        display_fix_instructions(result["fix"])

    print()


def display_fix_instructions(fixes):
    """
    Display suggested commands or actions to fix an issue.
    """
    for fix in fixes:
        print(fix)


def main():
    """
    Entry point for running a full environment diagnosis.
    """
    diagnosis_results = run_environment_diagnosis()
    display_diagnosis_report(diagnosis_results)


if __name__ == "__main__":
    main()
