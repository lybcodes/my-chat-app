from setuptools import setup, find_packages

setup(
    name="my-chat-app",
    version="0.1.0",
    description="A simple AI chat application that can be installed via pip.",
    author="lyb",
    author_email="liyebin.lyb@alibaba-inc.com",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "fastapi",
        "uvicorn",
        "requests",
        "openai",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
