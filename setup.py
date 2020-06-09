import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
  name='python-latex',  
  version='1.0.0',
  author="Joshua Neely",
  author_email="joshua.a.neely@gmail.com",
  description="Convenience wrappers around latex compilation with python",
  long_description=long_description,
  long_description_content_type="text/markdown",
  url="https://github.com/JoshuaNeely/python-latex",
  packages=setuptools.find_packages(),
  classifiers=[
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
  ],
  install_requires=[
    'latex',
    'watchdog',
  ],
  entry_points={
    "console_scripts": [
      "python_latex = python_latex.python_latex:main",
    ],
  },
)
