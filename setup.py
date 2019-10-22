try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

packages = ['mendeleystats']
requires = []

setup(name='mendeleystats',
      version='0.1.2',
      description='A command line tool to extract information about papers in a Mendeley folder.',
      long_description=open('README.md').read(),
      author=u'Yuri Malheiros',
      author_email='contato@yurimalheiros.com',
      url='https://github.com/yurimalheiros/mendeleystats',
      packages=packages,
      package_data={'': ['LICENSE', 'README.md'], 'mendeleystats': []},
      package_dir={'mendeleystats': 'mendeleystats'},
      scripts=['scripts/mendeleystats'],
      include_package_data=True,
      license=open('LICENSE').read(),
      zip_safe=False,
      install_requires = ['httplib2==0.8',
                          'numpy==1.7.1',
                          'matplotlib==1.2.1',
                          'oauth2==1.5.211',
                          'requests==2.20.0',
                          'wsgiref==0.1.2'],
      classifiers = ['Development Status :: 2 - Pre-Alpha',
                     'Environment :: Console',
                     'Intended Audience :: Science/Research',
                     'License :: OSI Approved :: MIT License',
                     'Operating System :: OS Independent',
                     'Programming Language :: Python',
                     'Topic :: Scientific/Engineering'],
)
