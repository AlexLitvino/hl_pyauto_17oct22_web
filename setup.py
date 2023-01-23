from distutils.core import setup

setup(name='HL Web Test',
      version='1.0',
      description='Sample testing project',
      packages=['web_test'],
      install_requires=['pytest',
                        'selenium',
                        'webdriver-manager',
                        ]
      )
