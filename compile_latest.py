import os
import subprocess

constitution_tex = 'mcr_constitution.tex'

if not os.path.isfile(constitution_tex):
    quit('Did not find ' + constitution_tex)

subprocess.call(['pdflatex', constitution_tex], stdout=open(os.devnull, 'w'))
subprocess.call(['pdflatex', constitution_tex], stdout=open(os.devnull, 'w'))
subprocess.call(['pdflatex', constitution_tex], stdout=open(os.devnull, 'w'))

subprocess.call(['rm', constitution_tex.replace('.tex', '.aux'), constitution_tex.replace('.tex', '.log')])

