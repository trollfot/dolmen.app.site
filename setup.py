from setuptools import setup, find_packages
from os.path import join

name = 'dolmen.app.site'
version = '0.2dev'
readme = open(join('src', 'dolmen', 'app', 'site', 'README.txt')).read()
history = open(join('docs', 'HISTORY.txt')).read()


install_requires = [
    'setuptools',
    'grok',
    'dolmen.content',
    'grokcore.startup',
    ]

setup(name = name,
      version = version,
      description = 'Dolmen CMS',
      long_description = readme + '\n\n' + history,
      keywords = 'Grok Zope3 CMS Dolmen',
      author = 'Souheil Chelfouh',
      author_email = 'trollfot@gmail.com',
      url = 'http://www.dolmen-project.org',
      license = 'GPL',
      packages=find_packages('src', exclude=['ez_setup']),
      package_dir={'': 'src'},
      namespace_packages = ['dolmen', 'dolmen.app'],
      include_package_data = True,
      platforms = 'Any',
      zip_safe = False,
      install_requires = install_requires,
      test_suite="dolmen.app.site",
      classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Zope3',
        'Intended Audience :: Other Audience',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
      ],
)
