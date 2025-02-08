"""PR Summary Generator CLI"""

import typer
import os
import subprocess
from typing import Optional, Tuple
from rich import print
from rich.panel import Panel
from rich.console import Console
from .git_utils import get_branch_changes
from .gemini_utils import generate_pr_summary

app = typer.Typer()
console = Console()


def create_pr_command(output_file: str) -> str:
    """Generate the GitHub CLI command for creating a PR"""
    return (
        f'gh pr create --title "feat: $(git branch --show-current)" --body-file {output_file} --base master'
    )


def show_command_panel(command: str):
    """Display a nice panel with the command"""
    panel = Panel(
        f'[bold white]{command}[/bold white]',
        title='[bold blue]Run this command to create your PR[/bold blue]',
        border_style='green',
        padding=(1, 2),
    )
    print('\n')
    console.print(panel)
    print('\n')


def process_summary(api_key: str, output_file: str, jira_number: Optional[str] = None) -> Tuple[str, str]:
    """Process and save the summary, return the summary and PR command"""
    diff = get_branch_changes()
    if not diff.strip():
        print('[bold yellow]Warning: No changes found in branch to generate summary[/bold yellow]')
        raise typer.Exit(1)

    try:
        summary = generate_pr_summary(diff, api_key, jira_number)

        with open(output_file, 'w') as f:
            f.write(summary)

        print(f'\n[bold green]✨ Summary generated and saved to {output_file}[/bold green]')
        return summary, create_pr_command(output_file)

    except Exception as e:
        print(f'[bold red]Error generating summary: {str(e)}[/bold red]')
        raise typer.Exit(1)


@app.command(name='generate')
def generate_summary_command(
    output_file: str = 'pr_summary.md',
    api_key: Optional[str] = None,
    jira_number: Optional[str] = typer.Option(
        None, '--jira', '-j', help='JIRA ticket number (e.g., SIS-290)'
    ),
):
    """Generate a PR summary from git changes using Gemini AI"""
    if not api_key:
        api_key = os.getenv('GEMINI_API_KEY')
        if not api_key:
            print(
                "[bold red]Error: GEMINI_API_KEY not found. Please provide it as an argument or set it as an environment variable. ie: export GEMINI_API_KEY='XXXXXXX'[/bold red]"
            )
            raise typer.Exit(1)

    try:
        _, command = process_summary(api_key, output_file, jira_number)
        show_command_panel(command)

    except Exception as e:
        print(f'[bold red]Error generating summary: {str(e)}[/bold red]')
        raise typer.Exit(1)


@app.command(name='create')
def generate_and_create_pr_command(
    output_file: str = 'pr_summary.md',
    api_key: Optional[str] = None,
    jira_number: Optional[str] = typer.Option(
        None, '--jira', '-j', help='JIRA ticket number (e.g., SIS-290)'
    ),
):
    """Generate summary and create PR directly using GitHub CLI"""
    if not api_key:
        api_key = os.getenv('GEMINI_API_KEY')
        if not api_key:
            print(
                '[bold red]Error: GEMINI_API_KEY not found. Please provide it as an argument or set it as an environment variable.[/bold red]'
            )
            raise typer.Exit(1)

    try:
        _, command = process_summary(api_key, output_file, jira_number)

        print('[bold blue]Creating PR...[/bold blue]')
        result = subprocess.run(command, shell=True, capture_output=True, text=True)

        if result.returncode == 0:
            print('\n[bold green]✨ PR created successfully![/bold green]')
            print(f'[bold white]{result.stdout}[/bold white]')
        else:
            print('\n[bold red]Error creating PR:[/bold red]')
            print(f'[red]{result.stderr}[/red]')
            raise typer.Exit(1)

    except Exception as e:
        print(f'[bold red]Error: {str(e)}[/bold red]')
        raise typer.Exit(1)


def main():
    app()
