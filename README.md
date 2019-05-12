# Constitution of the Somerville Middle Common Room

This repository contains the official record of the Constitution and changes to it.

## Editing the constitution

Proposed changes should be made to `constitution.tex`.

The script `compile_latest.py` will generate a pdf of the current `constitution.tex` file.

The script `compile_diff.py` will generate a diff view of the constitution highlighting all changes that have been made since a specific point in time. The easiest way to use this script is to supply a date shortly before the time you started making changes:

```bash
python compile_diff.py 2019-01-01
```

## Tagging new versions

Once changes have been approved by the MCR (at a General Meeting) and the College (at Governing Body), a new release should be tagged with the term that the changes are effective from, e.g. `EffectiveMT19`.

## Requirements

You need the following software to be installed to use the scripts in this repository, and it is currently assumed that you are using Linux such as Ubuntu:

- [git](https://git-scm.com/)
- [python](https://www.python.org/)
- [pdflatex](https://www.latex-project.org/)
- [latexdiff](https://ctan.org/pkg/latexdiff?lang=en)
