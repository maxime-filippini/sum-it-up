from setuptools import setup, find_packages

setup(
    name="sumitup",
    version="0.1.0",
    description="Summarization of news articles",
    author="M. Filippini",
    author_email="maxime.filippini@gmail.com",
    packages=find_packages(),
    python_requires=">=3.7, <4",
    install_requires=["scipy", "bs4"],
    extras_require={"dev": ["pytest", "black"]},
    # entry_points={"console_scripts": []},
)
