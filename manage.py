"""CL utility for administrative tasks"""
import os
import sys


def main():
    """Execute admin tasks"""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'movies.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django.  Is it installed and available on your PYTHONPATH env variable?"
            "You might need to activate your venv"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

