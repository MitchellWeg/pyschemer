from setuptools import setup
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='pyschemer',
    version='1.0.2',    
    description='A database visualization tool',
    url='https://github.com/MitchellWeg/schemer',
    author='Mitchell Weggemans',
    author_email='mitchell.w@live.nl',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='BSD 2-clause',
    packages=['pyschemer'],
    install_requires=['ERDot',
                      'pygraphviz',                     
                      'prettytable',                     
                      ],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',  
        'Operating System :: POSIX :: Linux',        
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
    ],
)