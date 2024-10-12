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
    description="Marketing API",
    author_email="",
    url="",
    keywords=["OpenAPI", "Marketing API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    &lt;p&gt;The &lt;i&gt;Marketing API &lt;/i&gt; offers two platforms that sellers can use to promote and advertise their products:&lt;/p&gt; &lt;ul&gt;&lt;li&gt;&lt;b&gt;Promoted Listings&lt;/b&gt; is an eBay ad service that lets sellers set up &lt;i&gt;ad campaigns &lt;/i&gt; for the products they want to promote. eBay displays the ads in search results and in other marketing modules as &lt;b&gt;SPONSORED&lt;/b&gt; listings. If an item in a Promoted Listings campaign sells, the seller is assessed a Promoted Listings fee, which is a seller-specified percentage applied to the sales price. For complete details, refer to the &lt;a href&#x3D;\&quot;/api-docs/sell/static/marketing/pl-landing.html\&quot;&gt;Promoted Listings playbook&lt;/a&gt;.&lt;/li&gt;&lt;li&gt;&lt;b&gt;Promotions Manager&lt;/b&gt; gives sellers a way to offer discounts on specific items as a way to attract buyers to their inventory. Sellers can set up discounts (such as \&quot;20% off\&quot; and other types of offers) on specific items or on an entire customer order. To further attract buyers, eBay prominently displays promotion &lt;i&gt;teasers&lt;/i&gt; throughout buyer flows. For complete details, see &lt;a href&#x3D;\&quot;/api-docs/sell/static/marketing/promotions-manager.html\&quot;&gt;Promotions Manager&lt;/a&gt;.&lt;/li&gt;&lt;/ul&gt;  &lt;p&gt;&lt;b&gt;Marketing reports&lt;/b&gt;, on both the Promoted Listings and Promotions Manager platforms, give sellers information that shows the effectiveness of their marketing strategies. The data gives sellers the ability to review and fine tune their marketing efforts.&lt;/p&gt; &lt;p class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Important!&lt;/b&gt; Sellers must have an active eBay Store subscription, and they must accept the &lt;b&gt;Terms and Conditions&lt;/b&gt; before they can make requests to these APIs in the Production environment. There are also site-specific listings requirements and restrictions associated with these marketing tools, as listed in the \&quot;requirements and restrictions\&quot; sections for &lt;a href&#x3D;\&quot;/api-docs/sell/marketing/static/overview.html#PL-requirements\&quot;&gt;Promoted Listings&lt;/a&gt; and &lt;a href&#x3D;\&quot;/api-docs/sell/marketing/static/overview.html#PM-requirements\&quot;&gt;Promotions Manager&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;The table below lists all the Marketing API calls grouped by resource.&lt;/p&gt;
    """
)

