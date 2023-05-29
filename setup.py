from distutils.core import setup
setup(
  name = 'auth_package',         # How you named your package folder (MyLib)
  packages = ['auth_package'],   # Chose the same as "name"
  version = '1.0',      # Start with a small number and increase it with every change you make
  license='unlicense',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Auth package for authentication with microservices',   # Give a short description about your library
  author = 'Ramin Zamanighiri',                   # Type in your name
  author_email = 'zamaniramin549@gmail.com',      # Type in your E-Mail
  url = 'https://www.ramzamani.com/',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/zamaniramin549/auth_project_package/archive/refs/tags/1.0.tar.gz',    # I explain this later on
  keywords = ['microservices', 'Auth package', 'API'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'requests',
      ],
  classifiers=[
    'Development Status :: 4 - Beta',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: unlicense',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
  ],
)