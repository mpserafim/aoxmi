from setuptools import setup
import sys

sys.path.append('./src')

setup(
    name='aoxmi',
    version='0.0.1',
    packages=['OXM', 'pygtk_chart'],
    package_dir={'': 'src'},
    url='https://github.com/mpserafim/aoxmi',
    license='GPLv2+',
    author='mpserafim',
    author_email='mpserafim@mps.eti.br',
    description='Another Opensource XenServer Management Interface',
    requires=['configobj', 'gi', 'raven'],
    scripts=['openxenmanager'],
    package_data={'OXM': ['aoxmi.conf',
                          'ui/*.glade',
                          'images/*.gif',
                          'images/*.png',
                          'images/menu/*.png',
                          'images_map/*'],
                  'pygtk_chart': ['data/tango.color']},
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: X11 Applications :: GTK',
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: GNU General Public License v2 or '
        'later (GPLv2+)',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2.7',
        'Topic :: System :: Monitoring',
        'Topic :: System :: Systems Administration',
        'Topic :: Utilities'
    ]
)
