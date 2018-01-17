from setuptools import find_packages
from setuptools import setup


def read(fname):
    with open(fname) as fp:
        content = fp.read()
    return content


setup(
    name='mgun',
    version='0.1.8',
    description='HTTP REST Client based on requests with dynamic url building',
    long_description=read('README.rst'),
    author='Danilchenko Maksim',
    author_email='dmax.dev@gmail.com',
    packages=find_packages(exclude=('test*', )),
    package_dir={'mgun': 'mgun'},
    include_package_data=True,
    install_requires=[
        'requests'
    ],
    license='MIT',
    url='https://github.com/maximdanilchenko/mgun',
    zip_safe=False,
    keywords='http client rest requests mgun',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    test_suite='tests'
)
