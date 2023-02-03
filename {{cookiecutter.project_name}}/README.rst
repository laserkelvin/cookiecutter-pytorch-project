{%- macro heading(text) -%}
{{text}}
{% for _ in text %}={% endfor %}
{%- endmacro -%}
{{ heading(cookiecutter.friendly_name) }}

|PyPI| |Status| |Python Version|

|Tests| |Codecov|

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

The project environment for {{cookiecutter.friendly_name}} combines modern Python
environment and tooling with flexibility to use more performant, tuned software
stacks to squeeze extra deep learning performance. For the latter, ``conda`` is 
recommended, but is not a requirement to run this package as it is also designed
for continuous development on a variety of environments (i.e. laptops).

Starting from ``conda``:

.. code:: console

   $ conda create -n {{cookiecutter.package_name}} python=3.9
   $ conda activate {{cookiecutter.package_name}}
   $ pip install .

For developer installs, run ``pip install './[dev]'``. The idea is that the ``pip``
installation provides the bare minimum dependencies, however does not guarantee
performance. It is up to the user to build PyTorch from source in order to include
things like MPI support, etc. The ``environment.yml`` file contains a good starting
point to do so.


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
   ├── notebooks
   │   ├── dev
   │   ├── exploratory
   │   └── reports
   ├── noxfile.py
   ├── pyproject.toml
   ├── README.rst
   ├── scripts
   │   └── train.py
   └── src
      └── {{cookiecutter.package_name}}
         └── __init__.py


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
* Commit changes, and commit frequently. Write `semantic`_ git commits!
* Formatting is done with ``black``; don't fuss about it 😃
* For new Python dependencies, add them to ``pyproject.toml``
* For new environment dependencies, use `conda env export -f environment.yml` to overwrite.

Notes on best practices, particularly regarding CI/CD, can be found in the extensive
documentation for the `Hypermodern Python Cookiecutter`_ repository.

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

This project was generated from `@laserkelvin`_'s PyTorch Project Cookiecutter, 
a fork of  `@cjolowicz`_'s `Hypermodern Python Cookiecutter`_ template.

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
.. _semantic: https://gist.github.com/joshbuchea/6f47e86d2510bce28f8e7f42ae84c716
.. _@laserkelvin: https://github.com/laserkelvin
