import click
from click.testing import CliRunner
from dragon import cli


def test_cli():
    runner = CliRunner()
    result = runner.invoke(cli)
    click.echo(result.output)
    assert result.exit_code == 0
    assert result.output == 'Dragon!\n'
