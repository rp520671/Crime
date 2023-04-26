from setuptools import setup

setup(
    name='Crime',
    version='0.1',
    packages=['app'],
    include_package_data=True,
    install_requires=[
        'flask',
        'pymongo'
    ],
    entry_points={
        'console_scripts': [
            'Crime=app:app'
        ]
    }
)
