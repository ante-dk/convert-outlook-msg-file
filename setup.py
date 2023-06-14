import setuptools

install_requires = [
    "compoundfiles>=0.3",
    "compressed_rtf>=1.0.6",
]

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="outlookmsgfile",
    version="0.1.0",
    description="Parse Microsoft Outlook MSG files",
    author="Joshua Tauberer",
    author_email="jt@occams.info",
    url="https://github.com/JoshData/convert-outlook-msg-file",
    packages=setuptools.find_packages(),
    install_requires=install_requires,
    entry_points="""
        [console_scripts]
        msg2eml=outlookmsgfile:msg2eml
    """,
    options={
        "build_scripts": {
            "executable": "/usr/bin/env python3",
        },
    },
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires='>=3.6',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
