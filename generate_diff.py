import os
import subprocess
import sys

if len(sys.argv) != 2:
    quit('Generate latexdiff of previous constitutional version.  Usage: ' + sys.argv[0] + ' (integer)')

try:
    num_revisions_back = int(sys.argv[1])
except ValueError as num_revisions_back:
    quit('Expected an integer to be passed, instead got ' + str(num_revisions_back))

if num_revisions_back < 0:
    quit('Expected positive integer to be passed, instead got ' + str(num_revisions_back))

null_output_file = 'null_output'

# Check that latexdiff is installed
try:
    subprocess.call(['latexdiff', '--version'], stdout=open(null_output_file, 'w'))
except OSError as e:
    quit('latexdiff does not seem to be installed: try sudo apt-get install latexdiff')

constitution_tex = 'mcr_constitution.tex'
constitution_old = 'mcr_constitution.OLD'
constitution_dif = 'mcr_constitution_diff.tex'
log_file = 'log'

if not os.path.isfile(constitution_tex):
    quit('Did not find ' + constitution_tex)

# Generate log of revisions to constitution_tex
with open(log_file, 'w') as f:
    subprocess.call(['git', 'log', '--follow', constitution_tex], stdout=f)

log_contents = open(log_file, 'r').readlines()
list_of_hashes = []
for line in log_contents:
    if line.startswith('commit'):
        list_of_hashes.append(line.replace('commit ', '').strip())

print(list_of_hashes)

if num_revisions_back > len(list_of_hashes) - 1:
    num_revisions_back = len(list_of_hashes) - 1
    print('Too many revisions back: giving you diff with first version instead')

# Generate old file contents
with open(constitution_old, 'w') as f:
    subprocess.call(['git', 'show', list_of_hashes[num_revisions_back] + ':' + constitution_tex], stdout=f)

# Generate diff tex file
with open(constitution_dif, 'w') as f:
    subprocess.call(['latexdiff', constitution_old, constitution_tex], stdout=f)

# If pdf already exists, delete it first
if os.path.isfile(constitution_dif.replace('.tex', '.pdf')):
    subprocess.call(['rm', constitution_dif.replace('.tex', '.pdf')])

subprocess.call(['pdflatex', constitution_dif], stdout=open(null_output_file, 'w'))
subprocess.call(['pdflatex', constitution_dif], stdout=open(null_output_file, 'w'))
subprocess.call(['pdflatex', constitution_dif], stdout=open(null_output_file, 'w'))

# Tidy up our generated files
subprocess.call(['rm', constitution_old, constitution_dif, log_file, null_output_file])

# Check that a valid pdf was created by pdflatex
if not os.path.isfile(constitution_dif.replace('.tex', '.pdf')):
    quit('pdf of diff not created as expected: check latex log file...')

if os.path.getsize(constitution_dif.replace('.tex', '.pdf')) < 1024:
    quit('pdf of diff not created as expected: check latex log file...')

# Tidy up pdflatex generated files
subprocess.call(['rm', constitution_dif.replace('.tex', '.aux'), constitution_dif.replace('.tex', '.log')])

