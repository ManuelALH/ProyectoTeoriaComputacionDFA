import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="visual-automata",
    version="1.0",
    description="Automate creado como proyecto final para la materia Teoria de la Computacion.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/ManuelALH/ProyectoTeoriaComputacionDFA",
    author="ManueL Alejandro Lepiz Hernandez",
    author_email="manuel.lepiz7979@alumnos.udg.mx",
    license="",
    keywords='automata',
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
    ],
    packages=[
        "visual_automata",
        "visual_automata.fa"
    ],
    include_package_data=True,
    install_requires=[
        "automata-lib",
        "pandas",
        "graphviz",
        "colormath",
        "jupyterlab"
    ],
    entry_points={},
)
