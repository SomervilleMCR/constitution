import os
import subprocess

# First, check that latexdiff is installed
try:
    subprocess.call(['latexdiff', '--version'], stdout=open(os.devnull, 'w'))
except OSError as e:
    quit('latexdiff does not seem to be installed: try sudo apt-get install latexdiff')

constitution_tex = 'mcr_constitution.tex'
constitution_old = 'mcr_constitution.OLD'
log_file = 'log'

if not os.path.isfile(constitution_tex):
    quit('Did not find ' + constitution_tex)

# Generate log of revisions to constitution_tex
with open(log_file, 'w') as f:
    subprocess.call(['git', 'log', '--follow', constitution_tex], stdout=f)





