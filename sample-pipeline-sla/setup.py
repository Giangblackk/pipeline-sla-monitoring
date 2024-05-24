from setuptools import find_packages, setup

setup(
    name="sample_pipeline_sla",
    packages=find_packages(exclude=["sample_pipeline_sla_tests"]),
    install_requires=[
        "dagster",
    ],
    extras_require={"dev": ["dagster-webserver", "pytest"]},
)
