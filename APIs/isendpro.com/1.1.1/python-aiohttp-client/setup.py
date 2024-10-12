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
    description="API iSendPro",
    author_email="support@isendpro.com",
    url="",
    keywords=["OpenAPI", "API iSendPro"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    [1] Liste des fonctionnalités : - envoi de SMS à un ou plusieurs destinataires, - lookup HLR, - récupération des récapitulatifs de campagne, - gestion des répertoires, - ajout en liste noire. - comptage du nombre de caractères des SMS  [2] Pour utiliser cette API vous devez: - Créer un compte iSendPro sur https://isendpro.com/ - Créditer votre compte      - Remarque: obtention d&#39;un crédit de test possible sous conditions - Noter votre clé de compte (keyid)   - Elle vous sera indispensable à l&#39;utilisation de l&#39;API   - Vous pouvez la trouver dans le rubrique mon \&quot;compte\&quot;, sous-rubrique \&quot;mon API\&quot; - Configurer le contrôle IP   - Le contrôle IP est configurable dans le rubrique mon \&quot;compte\&quot;, sous-rubrique \&quot;mon API\&quot;   - Il s&#39;agit d&#39;un système de liste blanche, vous devez entrer les IP utilisées pour appeler l&#39;API   - Vous pouvez également désactiver totalement le contrôle IP 
    """
)

