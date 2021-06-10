import setuptools

with open("README.md", "r", encoding="utf8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="py_multiapi",
    version="11",
    author="Itay K",
    author_email="itayki98@gmail.com",
    description="A Python Wrapper for api.itayki.com",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/iiiiii1wepfj/py_multiapi",
    packages=setuptools.find_packages(),
    download_url = 'https://github.com/iiiiii1wepfj/py_multiapi/archive/refs/tags/v11.tar.gz',
    project_urls={'Documentation': 'https://api.itayki.com/docs', 'Source': 'https://github.com/iiiiii1wepfj/py_multiapi'},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "httpx[http2]",
    ],
)
