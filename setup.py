from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='cursofiap-package',
    version='1.0.0',
    packages=find_packages(),
    description='Descricao da sua lib cursofiap',
    author='seu nome',
    author_email='seu.email@example.com',
    url='https://github.com/tadrianonet/cursofiap',  
    license='MIT',  
    long_description=long_description,
    long_description_content_type='text/markdown'
)
