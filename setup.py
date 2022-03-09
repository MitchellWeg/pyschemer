from setuptools import setup

setup(
    name='schemer',
    version='0.1.0',    
    description='A database visualization tool',
    url='https://github.com/MitchellWeg/schemer',
    author='Mitchell Weggemans',
    author_email='mitchell.w@live.nl',
    license='BSD 2-clause',
    packages=['schemer'],
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