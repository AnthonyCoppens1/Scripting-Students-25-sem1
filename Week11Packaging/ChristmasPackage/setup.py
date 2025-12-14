from setuptools import setup, find_packages
setup(name='ChristmasPackage',
      version='1.0',
      description='Our very first unique Christmas Package',
      author='Anthony',
      license='MIT',
      packages=find_packages(include=['mypackage']),
      install_requires=['wheel', 'playsound', 'pygame', 'requests', 'Pillow'])