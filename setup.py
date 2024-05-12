from setuptools import setup, find_packages

setup(
    name='skript',
    version='0.1',
    packages=find_packages(),
    description='A Python package that translates natural language to bash commands using LLaMA 3.',
    author='Sankeerth Rao Karingula',
    author_email='sankeerth1729@gmail.com',
    url='https://github.com/sankeerthrao/skript',  # Optional
    install_requires=[
        'mlx_lm>=0.1',  # Replace '0.1' with the minimum version you need
        # Add other dependencies as needed
    ],
    entry_points={
        'console_scripts': [
            'skript=skript.cli:main',  # Ensures that `skript` command starts your CLI
        ],
    },
    include_package_data=True,
    package_data={
        # Include any other necessary files like model weights or additional data
    },
    zip_safe=False
)
