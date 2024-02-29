from setuptools import setup, find_packages
VERSION = "0.0.2"
DESCRIPTION = "ProCap is a captcha solving service."
LONG_DESCRIPTION = "A api wrapper for ProCap."

setup(
    name="procap",
    version=VERSION,
    author="ProCap",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=["requests"],
    keywords=["python", "captcha", "solver", "hcaptcha", "procap", "captcha solver", "hcaptcha solver", "captcha bypass"],
    classifiers=[
    "Development Status :: 3 - Alpha",
    "Intended Audience :: Developers",
    "Programming Language :: Python :: 3",
    "Operating System :: OS Independent",
]
)
