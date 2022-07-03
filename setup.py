from setuptools import setup

setup(
    name='google_cloud',
    version='1.0',
    package_dir={'': 'src'},
    packages=['google_cloud'],
    install_requires=[
        'google_api_python_client',
        'google_auth_httplib2',
        'google_auth_oauthlib',
    ],
)
