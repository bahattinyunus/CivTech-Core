from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="civtech-core",
    version="0.1.0",
    author="Bahattin Yunus Çetin",
    author_email="bahattinyunus@example.com", 
    description="The foundational core for CivTech applications.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bahattinyunus/CivTech-Core",
    project_urls={
        "Bug Tracker": "https://github.com/bahattinyunus/CivTech-Core/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.8",
)
