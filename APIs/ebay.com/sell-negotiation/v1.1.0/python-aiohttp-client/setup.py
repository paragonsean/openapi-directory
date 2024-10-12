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
    description="Negotiation API",
    author_email="",
    url="",
    keywords=["OpenAPI", "Negotiation API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    The &lt;b&gt;Negotiations API&lt;/b&gt; gives sellers the ability to proactively send discount offers to buyers who have shown an \&quot;interest\&quot; in their listings.  &lt;br&gt;&lt;br&gt;By sending buyers discount offers on listings where they have shown an interest, sellers can increase the velocity of their sales.  &lt;br&gt;&lt;br&gt;There are various ways for a buyer to show &lt;i&gt;interest &lt;/i&gt; in a listing. For example, if a buyer adds the listing to their &lt;b&gt;Watch&lt;/b&gt; list, or if they add the listing to their shopping cart and later abandon the cart, they are deemed to have shown an interest in the listing.  &lt;br&gt;&lt;br&gt;In the offers that sellers send, they can discount their listings by either a percentage off the listing price, or they can set a new discounted price that is lower than the original listing price.  &lt;br&gt;&lt;br&gt;For details about how seller offers work, see &lt;a href&#x3D;\&quot;/api-docs/sell/static/marketing/offers-to-buyers.html\&quot; title&#x3D;\&quot;Selling Integration Guide\&quot;&gt;Sending offers to buyers&lt;/a&gt;.
    """
)

