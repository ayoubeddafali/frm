import pytest
from frm import cli

@pytest.fixture()
def parser():
    return cli.create_parser()

def test_parser_init_and_without_project_type(parser):
    """
    The parser will exit if it receives init without a project type
    """
    with pytest.raises(SystemExit):
        parser.parse_args(['--init'])

def test_parser_init_with_invalid_project_type(parser):
    """
    The parser will exit if it receives init with an invalid project type
    """
    with pytest.raises(SystemExit):
        parser.parse_args(['--init', 'error'])

def test_parser_init_with_valid_project_type(parser):
    """
    The parser will not exit if it receives a valid project type
    """
    parser.parse_args(['--init', 'java'])

def test_parser_clean(parser):
    """
   The parser will not exit if it receives a clean action
   """
    parser.parse_args(['--destroy'])

def test_parser_destroy(parser):
    """
   The parser will not exit if it receives a clean action
   """
    parser.parse_args(['--destroy'])











