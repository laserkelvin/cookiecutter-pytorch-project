{%- macro heading(text) -%}
{{text}}
{% for _ in text %}={% endfor %}
{%- endmacro -%}
{{ heading(cookiecutter.friendly_name) }}

|PyPI| |Status| |Python Version| |License|

|Read the Docs| |Tests| |Codecov|

|pre-commit| |Black|

.. |PyPI| image:: https://img.shields.io/pypi/v/{{cookiecutter.project_name}}.svg
   :target: https://pypi.org/project/{{cookiecutter.project_name}}/
   :alt: PyPI
.. |Status| image:: https://img.shields.io/pypi/status/{{cookiecutter.project_name}}.svg
   :target: https://pypi.org/project/{{cookiecutter.project_name}}/
   :alt: Status
.. |Python Version| image:: https://img.shields.io/pypi/pyversions/{{cookiecutter.project_name}}
   :target: https://pypi.org/project/{{cookiecutter.project_name}}
   :alt: Python Version
.. |License| image:: https://img.shields.io/pypi/l/{{cookiecutter.project_name}}
   :target: https://opensource.org/licenses/{{cookiecutter.license}}
   :alt: License
.. |Read the Docs| image:: https://img.shields.io/readthedocs/{{cookiecutter.project_name}}/latest.svg?label=Read%20the%20Docs
   :target: https://{{cookiecutter.project_name}}.readthedocs.io/
   :alt: Read the documentation at https://{{cookiecutter.project_name}}.readthedocs.io/
.. |Tests| image:: https://github.com/{{cookiecutter.github_user}}/{{cookiecutter.project_name}}/workflows/Tests/badge.svg
   :target: https://github.com/{{cookiecutter.github_user}}/{{cookiecutter.project_name}}/actions?workflow=Tests
   :alt: Tests
.. |Codecov| image:: https://codecov.io/gh/{{cookiecutter.github_user}}/{{cookiecutter.project_name}}/branch/main/graph/badge.svg
   :target: https://codecov.io/gh/{{cookiecutter.github_user}}/{{cookiecutter.project_name}}
   :alt: Codecov
.. |pre-commit| image:: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white
   :target: https://github.com/pre-commit/pre-commit
   :alt: pre-commit
.. |Black| image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/psf/black
   :alt: Black


Features
--------

* TODO


Requirements
------------

* TODO


Installation
------------

The project environment for {{cookiecutter.friendly_name}} is controlled by `conda` 
and `poetry`; the former for maintaining the Python environment, as well as additional 
libraries like CUDA, and the latter for Python specific dependencies. There is
a bit of overlap between these two tools, however mostly because `conda`
is not great for resolving dependencies, and `poetry` can't handle things
that aren't Python (e.g. MPI, MKL).

The recommended procedure from scratch is to follow these steps:

.. code:: console

   $ conda create -n {{cookiecutter.package_name}} python=3.7
   $ conda activate {{cookiecutter.package_name}}
   $ pip install poetry
   $ poetry install

Usage
-----

Please see the `Command-line Reference <Usage_>`_ for details.


Project Structure
-----------------

The project filestructure is laid out as such::

   ├── CITATION.cff
   ├── codecov.yml
   ├── CODE_OF_CONDUCT.rst
   ├── CONTRIBUTING.rst
   ├── data
   │   ├── external
   │   ├── interim
   │   ├── processed
   │   └── raw
   ├── docs
   │   ├── codeofconduct.rst
   │   ├── conf.py
   │   ├── contributing.rst
   │   ├── index.rst
   │   ├── license.rst
   │   ├── reference.rst
   │   ├── requirements.txt
   │   └── usage.rst
   ├── environment.yml
   ├── models
   ├── notebooks
   │   ├── dev
   │   ├── exploratory
   │   └── reports
   ├── noxfile.py
   ├── poetry.lock
   ├── pyproject.toml
   ├── README.rst
   ├── scripts
   │   └── train.py
   └── src
      └── {{cookiecutter.package_name}}
         ├── __init__.py
         ├── layers
         │   ├── __init__.py
         │   ├── layers.py
         │   └── tests
         │       ├── __init__.py
         │       └── test_layers.py
         ├── __main__.py
         ├── models
         │   ├── __init__.py
         │   ├── models.py
         │   └── tests
         │       ├── __init__.py
         │       └── test_models.py
         ├── pipeline
         │   ├── data.py
         │   ├── __init__.py
         │   ├── tests
         │   │   ├── __init__.py
         │   │   ├── test_data.py
         │   │   └── test_transforms.py
         │   └── transforms.py
         ├── py.typed
         └── utils.py

A brief summary of what each folder is designed for:

1. `data` contains copies of the data used for this project. It is recommended to
form a pipeline whereby the `raw` data is preprocessed, serialized to `interim`,
and when ready for analysis, placed into `processed`.
2. `models` contains serialized weights intended for distribution, and/or testing.
3. `notebooks` contains three subfolders: `dev` is for notebook based development,
`exploratory` for data exploration, and `reports` for making figures and visualizations
for writeup.
4. `scripts` contains files that meant for headless routines, generally those with
long compute times such as model training and data cleaning.
5. `src/{{cookiecutter.package_name}}` contains the common code base for this project.


Code development
----------------

All of the code used for this project should be contained in `src/{{cookiecutter.package_name}}`,
at least in terms of the high-level functionality (i.e. not scripts), and is intended to be
a standalone Python package.

The package is structured to match the abstractions for deep learning, specifically PyTorch, 
PyTorch Lightning, and Weights and Biases, by separating parts of data structures and processing
and model/layer development.

Some concise tenets for development

* Write unit tests as you go.
* Commit changes, and commit frequently. Write semantic_ git commits!
* Formatting is done with ``black``; don't fuss about it 😃
* For new Python dependencies, use `poetry add <package>`.
* For new environment dependencies, use `conda env export -f environment.yml`.


License
-------

Distributed under the terms of the `{{cookiecutter.license.replace("-", " ")}} license`_,
*{{cookiecutter.friendly_name}}* is free and open source software.


Issues
------

If you encounter any problems,
please `file an issue`_ along with a detailed description.


Credits
-------

This project was generated from `@cjolowicz`_'s `Hypermodern Python Cookiecutter`_ template.

.. _@cjolowicz: https://github.com/cjolowicz
.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _{{cookiecutter.license.replace("-", " ")}} license: https://opensource.org/licenses/{{cookiecutter.license}}
.. _PyPI: https://pypi.org/
.. _Hypermodern Python Cookiecutter: https://github.com/cjolowicz/cookiecutter-hypermodern-python
.. _file an issue: https://github.com/{{cookiecutter.github_user}}/{{cookiecutter.project_name}}/issues
.. _pip: https://pip.pypa.io/
.. github-only
.. _Contributor Guide: CONTRIBUTING.rst
.. _Usage: https://{{cookiecutter.project_name}}.readthedocs.io/en/latest/usage.html
:: _semantic: https://gist.github.com/joshbuchea/6f47e86d2510bce28f8e7f42ae84c716
