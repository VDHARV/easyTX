from setuptools import setup, find_packages


setup(
    name='data_xchg',
    version='1',
    license='MIT',
    author="VDHARV",
    author_email='vdharv4bharat@gmail.com',
    packages=find_packages('data_xchg'),
    package_dir={'': 'data_xcfg'},
    url='https://github.com/VDHARV/data_xchg',
    keywords='udp transfer',
    install_requires=[
          'socket', 'cv2', 'numpy'
      ],

)