from setuptools import setup

setup(
    name='data2midi',
    url='https://github.com/trwiley/data2midi',
    author='Taylor Wiley',
    author_email='taylor.r.wiley@gmail.com',
    packages=['data2midi'],
    install_requires=['numpy', 'pandas', 'sklearn', 'MIDIUtil'],
    version='0.1.2',
    license='GNU GPL',
    description='simple library for sonifying tabular numeric data by converting it into a MIDI file.'
)
