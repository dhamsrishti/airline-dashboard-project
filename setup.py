from setuptools import setup, find_packages

setup(
    name="airline-dashboard-project",
    version="0.1.0",
    packages=find_packages(),
    package_data={
        '': ['*.yaml', '*.sql', '*.csv'],
    },
    include_package_data=True,
    install_requires=[
        "google-cloud-storage",
        "google-cloud-bigquery",
    ],
)
