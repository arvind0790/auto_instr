from setuptools import setup, find_packages
setup(
    name='auto_instr',
    version='0.7.5',
    author='Arvind Kumar',
    author_email='vind0790@gmail.com',
    packages=find_packages(),
    scripts=[],
    url='https://github.com/arvind0790/auto_instr',
    # download_url='https://github.com/arvind0790/auto_instr/archive/master.zip',
    license='MIT License',
    description='Library for automating scientific instruments.',
    long_description=open('README.rst','r').read(),
    # long_description=open('README.rst','r').read() + "\n\n" + open('CHANGES.txt').read(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: MacOS",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX",
        "Operating System :: Unix",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Scientific/Engineering",
    ],
    keywords="measure instrument experiment control automate bench smu power supply oscilloscope thermonic function generator"
)
