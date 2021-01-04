from setuptools import setup

setup(name='pyreminders',
      version='0.1',
      description='Python library to create iCloud Reminders through CLI',
      url='http://github.com/ohitssway/pyreminders',
      author='Saimun Shahee',
      author_email='saimun.shahee@gmail.com',
      license='MIT',
      packages=['pyreminders'],
      scripts=['bin/pyreminders'],
      zip_safe=False)
