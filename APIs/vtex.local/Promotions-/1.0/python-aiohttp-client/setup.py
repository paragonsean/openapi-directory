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
    description="Promotions &amp; Taxes API",
    author_email="",
    url="",
    keywords=["OpenAPI", "Promotions &amp; Taxes API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
      &gt; Check the new [Promotions onboarding guide](https://developers.vtex.com/vtex-rest-api/docs/promotions-overview). We created this guide to improve the onboarding experience for developers at VTEX. It assembles all documentation on our Developer Portal about Promotions and is organized by focusing on the developer&#39;s journey.     The Promotions &amp; Taxes API allows you to manage and retrieve all promotions, coupons and tax rules from your VTEX store.     ## Index     ### Coupons   &#x60;POST&#x60; [Create multiple coupons](https://developers.vtex.com/vtex-rest-api/reference/post_api-rnb-pvt-multiple-coupons)   &#x60;POST&#x60; [Create coupon](https://developers.vtex.com/vtex-rest-api/reference/post_api-rnb-pvt-coupon)   &#x60;GET&#x60; [Get coupon by coupon code](https://developers.vtex.com/vtex-rest-api/reference/getbycouponcode)   &#x60;GET&#x60; [Get archived coupon by coupon code](https://developers.vtex.com/vtex-rest-api/reference/getarchivedbycouponcode)   &#x60;POST&#x60; [Archive coupon by coupon code](https://developers.vtex.com/vtex-rest-api/reference/archivebycouponcode)   &#x60;POST&#x60; [Update coupon](https://developers.vtex.com/vtex-rest-api/reference/update)   &#x60;GET&#x60; [Get all coupons](https://developers.vtex.com/vtex-rest-api/reference/getall)   &#x60;POST&#x60; [Coupon Massive Generation](https://developers.vtex.com/vtex-rest-api/reference/massivegeneration)   &#x60;GET&#x60; [Get coupon usage](https://developers.vtex.com/vtex-rest-api/reference/getusage)   &#x60;POST&#x60; [Unarchive coupon by coupon code](https://developers.vtex.com/vtex-rest-api/reference/unarchivebycouponcode)     ### Promotions and Taxes   &#x60;GET&#x60; [Get All Promotions](https://developers.vtex.com/vtex-rest-api/reference/getallbenefits)   &#x60;GET&#x60; [Get All Taxes](https://developers.vtex.com/vtex-rest-api/reference/getalltaxes)   &#x60;GET&#x60; [Get Promotion or Tax By ID](https://developers.vtex.com/vtex-rest-api/reference/getcalculatorconfigurationbyid)   &#x60;POST&#x60; [Create or Update Promotion or Tax](https://developers.vtex.com/vtex-rest-api/reference/createorupdatecalculatorconfiguration)   &#x60;POST&#x60; [Create Multiple SKU Promotion](https://developers.vtex.com/vtex-rest-api/reference/post_api-rnb-pvt-import-calculatorconfiguration)   &#x60;PUT&#x60; [Update Multiple SKU Promotion](https://developers.vtex.com/vtex-rest-api/reference/put_api-rnb-pvt-import-calculatorconfiguration-promotionid)   &#x60;POST&#x60; [Archive Promotion or Tax](https://developers.vtex.com/vtex-rest-api/reference/archivepromotion-1)   &#x60;POST&#x60; [Unarchive Promotion or Tax](https://developers.vtex.com/vtex-rest-api/reference/unarchivepromotion-1)   &#x60;GET&#x60; [List archived Promotions](https://developers.vtex.com/vtex-rest-api/reference/getarchivedpromotions)   &#x60;GET&#x60; [List archived Taxes](https://developers.vtex.com/vtex-rest-api/reference/getarchivedtaxes)       ### Campaign Audiences   &#x60;GET&#x60; [Get campaign audience configuration](https://developers.vtex.com/vtex-rest-api/reference/getcampaignconfiguration)   &#x60;POST&#x60; [Create campaign audience](https://developers.vtex.com/vtex-rest-api/reference/setcampaignconfiguration)
    """
)

