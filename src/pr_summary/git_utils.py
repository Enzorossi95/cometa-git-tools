"""Git utilities for PR Summary Generator"""

import subprocess
from typing import Optional
import typer
from rich import print


def get_branch_name() -> str:
    """Get the current branch name"""
    result = subprocess.run(['git', 'branch', '--show-current'], capture_output=True, text=True)
    return result.stdout.strip()


def extract_ticket_from_branch(branch_name: str) -> Optional[str]:
    """Extract ticket number from branch name (e.g., 'SIS-123' from 'feature/SIS-123-description')"""
    import re

    match = re.search(r'(?:^|/)?(SIS-\d+)', branch_name)
    return match.group(1) if match else None


def get_branch_changes(base_branch: str = 'master') -> str:
    """Get all changes that will be included in the PR
    
    Args:
        base_branch (str): The base branch to compare against (e.g., 'main', 'master', 'develop')
    """
    branch = get_branch_name()
    print(f'[blue]📊 Analyzing changes between {branch} and {base_branch}...[/blue]')

    base = subprocess.run(['git', 'merge-base', base_branch, branch], capture_output=True, text=True)
    if base.returncode != 0:
        print(f'[bold red]Error: Could not find common ancestor with {base_branch}[/bold red]')
        print('[yellow]Tips:[/yellow]')
        print(f'  • Ensure branch {base_branch} exists and is up to date')
        print(f'  • Try running: git fetch origin {base_branch}')
        print('  • Check if you have the correct base branch name')
        raise typer.Exit(1)

    result = subprocess.run(
        ['git', 'diff', '--stat', '--patch', base.stdout.strip() + '..HEAD'], capture_output=True, text=True
    )
    if result.returncode != 0:
        print('[bold red]Error: Could not get branch changes[/bold red]')
        raise typer.Exit(1)

    commits = subprocess.run(
        ['git', 'log', '--pretty=format:%h - %s%n%b', base.stdout.strip() + '..HEAD'],
        capture_output=True,
        text=True,
    )
    files = subprocess.run(
        ['git', 'diff', '--name-status', base.stdout.strip() + '..HEAD'], capture_output=True, text=True
    )

    print(f'[green]✓ Found {len(files.stdout.splitlines())} changed files[/green]')
    print(f'[green]✓ Found {len(commits.stdout.splitlines())} commits[/green]')

    full_changes = f"""
                Branch Information:
                - Current branch: {branch}
                - Target branch: {base_branch}
                - Changes from: {base.stdout.strip()}

                Commits in this PR:
                {commits.stdout}

                Files Changed:
                {files.stdout}

                Detailed Changes:
                {result.stdout}
                """
    return full_changes
