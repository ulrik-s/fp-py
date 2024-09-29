from click.testing import CliRunner
from fp_py import cli


def test_pr():
    runner = CliRunner()
    result = runner.invoke(cli, ["pr"])
    assert result.exit_code == 0
    assert result.output == "Hello World\n"
