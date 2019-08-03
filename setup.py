from setuptools import setup, find_packages

from flake8_use_fstring import __version__

extra_test = [
    'pytest>=4',
]
extra_dev = [
    *extra_test,
]

setup(
    name='flake8-use-fstring',
    version=__version__,
    description='Flake8 plugin for string formatting style.',

    url='https://github.com/MichaelKim0407/flake8-use-fstring',
    author='Michael Kim',
    author_email='mkim0407@gmail.com',

    packages=find_packages(),

    python_requires='>=3.6',

    install_requires=[
        'flake8==3.*',
    ],

    extras_require={
        'test': extra_test,
        'dev': extra_dev,
    },

    entry_points={
        'flake8.extension': [
            'FS001 = flake8_use_fstring.percent:PercentFormatDetector',
            'FS002 = flake8_use_fstring.format:StrFormatDetector',
        ],
    },

    classifiers=[
        'Intended Audience :: Developers',

        'Development Status :: 3 - Alpha',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',

        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Quality Assurance',
    ],
)
