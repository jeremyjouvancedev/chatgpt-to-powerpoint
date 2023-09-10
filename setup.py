from setuptools import setup, find_packages

# Read the requirements.txt file
with open('requirements.txt', 'r') as f:
    requirements = f.read().splitlines()

setup(
    name="chatgpt_to_powerpoint",
    version="0.1",
    packages=find_packages(),
    install_requires=requirements,
)