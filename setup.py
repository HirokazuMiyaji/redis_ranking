# coding: utf-8


try:
    from setuptools import setup
except ImportError:
    from distuutils.core import setup


setup(
    name='redis_ranking',
    version='0.0.1',
    description='Python Ranking using Redis',
    long_description='',
    url='http://github.com/HirokazuMiyaji/redis_ranking',
    author='Hirokazu Miyaji',
    maintainer_email='hirokazu.miyaji@gmail.com',
    keywords=['Redis', 'Ranking', 'redis', 'ranking'],
    license='MIT',
    packages=['ranking'],
    test_suite='tests.test_ranking',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
    ]
)