from setuptools import setup


setup(
    name='cricapi-py',
    version='1.0.0',
    description='Simple and Easy way to access CricAPI data. '
                'A library showing live data, upcoming matches, fantasy summary and more',
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