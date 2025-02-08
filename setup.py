"""
Cometa Git Tools - A collection of Git utilities for Commitizen and PR Summary Generation
"""

import os
from setuptools import setup, find_packages

# Read the contents of README file
with open(os.path.join(os.path.dirname(__file__), 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# Read requirements from requirements.txt if it exists
def read_requirements(filename='requirements.txt'):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return [line.strip() for line in f if line.strip() and not line.startswith('#')]
    except FileNotFoundError:
        return [
            'commitizen>=3.12.0',
            'typer>=0.9.0',
            'rich>=13.7.0',
            'google-generativeai>=0.3.2',
            'absl-py>=2.0.0',
            'questionary>=2.0.1',
        ]

setup(
    name='cometa-git-tools',
    version='0.1.3',
    description='Git tools for Commitizen and PR Summary Generation using AI',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Cometa',
    author_email='enzo@cometa.com',
    url='https://github.com/cometa/cometa-git-tools',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    include_package_data=True,
    install_requires=read_requirements(),
    entry_points={
        'commitizen.plugin': [
            'cz_ai_conventional=cz_ai_conventional:AIConventionalCz'
        ],
        'console_scripts': [
            'pr-summary=pr_summary.cli:main',
            'cometa-git=pr_summary.cli:app',
            'cz-setup=cz_ai_conventional:setup_global_config',
        ],
    },
    options={
        'commitizen': {
            'name': 'cz_ai_conventional'
        }
    },
    python_requires='>=3.7',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Version Control :: Git',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    keywords='git commitizen pr-summary ai gemini conventional-commits',
    project_urls={
        'Bug Reports': 'https://github.com/cometa/cometa-git-tools/issues',
        'Source': 'https://github.com/cometa/cometa-git-tools',
    },
    package_data={
        '': ['pyproject.toml'],
    },
    data_files=[
        ('', ['pyproject.toml']),
    ],
)
