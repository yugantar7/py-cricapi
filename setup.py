from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='cricapi-py',
    version='1.0.0',
    description='Simple and Easy way to access CricAPI data. '
                'A library showing live data, upcoming matches, fantasy summary and more',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/yugantar7/py-cricapi',
    author='Yugantar Malhotra',
    author_email='yugantarmalhotra95@gmail.com',
    package_dir={'': 'src'},
    packages='',
    include_package_data=True,
    install_requires=['requests>=2.5.1'],
    entry_points={
        'console_scripts': ['pycricapi=src.pycric.CricApp']
    }
)