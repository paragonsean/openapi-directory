# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "openapi_server"
VERSION = "1.0.0"

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    "connexion==2.14.1",
    "swagger-ui-bundle==0.0.9",
    "aiohttp_jinja2==1.5.0",
]

setup(
    name=NAME,
    version=VERSION,
    description="Wealth Reader API",
    author_email="info@wealthreader.com",
    url="",
    keywords=["OpenAPI", "Wealth Reader API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    Las APIs regulatorias basadas en PSD2 proporcionan acceso a cierta información financiera como saldos de cuentas bancarias y transacciones. Sin embargo, hay otras fuentes de información patrimonial que no son accesibles por estas APIs. La API de Wealth Reader amplía la información ofrecida por las APIs regulatorias proporcionando acceso en tiempo real a las fuentes patrimoniales adicionales en cualquier entidad del mundo. Existen otros dos documentos relacionados que te ayudarán a integrar la API de Wealth Reader. Uno es la guía de integración del widget Javascript: https://docs-es.wealthreader.com/, y el  otro una colección Postman basada en esta documentación.
    """
)

