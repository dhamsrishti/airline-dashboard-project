from setuptools import setup, find_packages

setup(
    name="airline-dashboard-project",
    version="0.1",
    packages=find_packages(),
    package_dir={'': '.'},
    install_requires=[
        "google-cloud-storage",
        "google-cloud-bigquery",
    ],
)
