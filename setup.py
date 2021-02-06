import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='testaklib',
    version='0.0.1',
    author='Anil Koppula',
    author_email='koppulaanil1786@gmail.com',
    description='A small mathematics library',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/anil121786/testaklib',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Natural Language :: English',
    ],
    python_requires='>=3.6'
)