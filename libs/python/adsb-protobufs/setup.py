from setuptools import setup, find_packages

setup(
    name="adsb-protobufs",
    version="0.0.1",
    author="David Guerrero",
    author_email="heldroe@gmail.com",
    description="Protobuf definitions to manage ADSB related events.",
    license="Apache",
    keywords="adsb protobuf protocol",
    url="https://github.com/Heldroe/adsb2kafka/libs/python/adsb-protobufs",
    packages=find_packages(),
    install_requires=[
        "protobuf==5.29.3",
    ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Intended Audience :: System Administrators",
        "Programming Language :: Python :: 3.13",
        "License :: OSI Approved :: Apache Software License",
    ],
)
