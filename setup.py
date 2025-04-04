from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="django-signal-handler",
    version="0.1.1",
    author="Konrad Beck",
    author_email="konradbeck101@gmail.com",
    description="A package for handling Django model signals.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/konradbeck/django-signal-handler.git",
    packages=find_packages(include=["signal_handler*"]),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Framework :: Django",
        "Framework :: Django :: 3.2",
        "Framework :: Django :: 4.0",
    ],
    python_requires=">=3.6",
    install_requires=[
        "django>=3.0",
    ],
    extras_require={
        "dev": ["pytest", "pytest-django"],
    }
)
