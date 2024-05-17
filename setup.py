from setuptools import setup, find_packages

setup(
    name="pvz_hybrid_script",
    version="0.0.1",
    packages=find_packages(),
    install_requires=[
        "pyautogui",
    ],
    author="MarcWebber",
    author_email="xuzihao030324@gmail.com",
    description="A script that automates the game Plants vs Zombies",
    keywords="pvz, plants vs zombies, automation",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)
