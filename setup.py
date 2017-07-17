from setuptools import setup,find_packages

setup(
  name = 'Adyen',
  packages = ['Adyen'],
  version = '1.1.0',
  description = 'Adyen Python Api',
  long_description = "Adyen Python Api to build ecommerce and reconciliation apps with Python. Connects to Adyen backend. Requires a 'test' or 'live' account with Adyen.",
  author = 'Adyen',
  author_email = 'support@adyen.com',
  url = 'https://github.com/Adyen/adyen-python-api-library',
  download_url = 'https://github.com/Adyen/adyen-python-api-library/archive/1.1.0.tar.gz',
  keywords = ['payments', 'adyen', 'fintech'],
  classifiers = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Libraries',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3.6'
    ]
)
