from distutils.core import setup
from distutils.command.install import install
import sys

class install_with_kernelspec(install):
    def run(self):
        install.run(self)
        from IPython.kernel.kernelspec import install_kernel_spec
        install_kernel_spec('kernelspec', 'fortran', replace=True)

with open('README.md') as f:
    readme = f.read()

svem_flag = '--single-version-externally-managed'
if svem_flag in sys.argv:
    # Die, setuptools, die.
    sys.argv.remove(svem_flag)

setup(name='fortran_kernel',
      version='0.1',
      description='A Fortran kernel for Jupyter',
      long_description=readme,
      author='Luis Marti',
      author_email='lmarti@gmail.com',
      url='https://github.com/lmarti/ifortran',
      py_modules=['fortran_kernel'],
      cmdclass={'install': install_with_kernelspec},
      install_requires=['pexpect>=3.3'],
      classifiers = [
          'Framework :: IPython',
          'License :: OSI Approved :: BSD License',
          'Programming Language :: Python :: 3',
          'Topic :: System :: Shells',
      ]
)