from setuptools import find_packages, setup

setup(
    name='twenty-four-api',
    version='0.0.1',
    description='Twenty Four API',
    author='Quinn Weber',
    maintainer='Quinn Weber',
    maintainer_email='quinnsweber@gmail.com',
    packages=find_packages(exclude=('tests',)),
    install_requires=(
        'flask',
        'boto3',
    ),
)
