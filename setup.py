import os

import setuptools

setup_path = os.path.dirname(os.path.realpath(__file__))

install_requires = [
    "compoundfiles",
    "compressed_rtf",
    "rtfparse",
    "html2text",
]

with open(f"{setup_path}/README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="outlookmsgfile",
    version="0.2.0",
    description="Parse Microsoft Outlook MSG files",
    author="Joshua Tauberer",
    author_email="jt@occams.info",
    url="https://github.com/JoshData/convert-outlook-msg-file",
    py_modules=["outlookmsgfile", "msg2eml"],
    install_requires=install_requires,
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires=">=3.9",
    entry_points={
        "console_scripts": [
            "msg2eml=msg2eml:cli",  # Maps `msg2eml` command to the `msg2eml` function
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
