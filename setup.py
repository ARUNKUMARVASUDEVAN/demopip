from setuptools import setup,find_packages

setup(name="census-income",
           version="1.5.3",
           author="sunny",
           author_email="oyeahitsarun@gmail.com",
           packages=find_packages(),
           install_requres=["pandas","numpy","flask"]
      )