from setuptools import setup, find_packages


with open("README.rst", "r") as f:
    readme = f.read()

setup(
    name="frm",
    version="0.1.0",
    description="CLI framework to quickly setup CD workflow for your project.",
    long_description=readme,
    author='Ayoub ED-DAFALI',
    author_email='ayoubensalem@gmail.com',
    packages=find_packages('src'),
    package_dir={'':'src'},
    install_requires=[],
    entry_points={
        'console_scripts': [
            'frm=frm.cli:main'],
    }
)

