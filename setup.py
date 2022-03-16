from setuptools import setup, find_packages

setup(name='dsfc',
      version='0.1',
      description='dsfc content',
      author='Gilles Verbockhaven',
      author_email='Gilles.Verbockhaven@gmail.com',
      url='https://x.html',
      packages=find_packages('src', exclude=['data', 'notebooks']),
      package_dir={'':'src'})
