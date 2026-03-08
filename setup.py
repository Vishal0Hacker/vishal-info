from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="vishal-info",
    version="1.0.0",
    author="Vishal0Hacker",
    author_email="your-email@example.com",
    description="Mobile Number Information Lookup Module - Powered by vectorxo.online API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Vishal0Hacker/vishal-info",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=requirements,
    keywords="mobile lookup, phone information, api client, india, telecom",
    project_urls={
        "Bug Reports": "https://github.com/Vishal0Hacker/vishal-info/issues",
        "Source": "https://github.com/Vishal0Hacker/vishal-info",
        "API Documentation": "https://api.vectorxo.online/lookup",
    },
)