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
    description="",
    author_email="",
    url="",
    keywords=["OpenAPI", ""],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    &lt;strong&gt;GoDaddy Abuse API Terms of Use:&lt;/strong&gt;&lt;p&gt;GoDaddy’s Abuse API is provided to simplify and standardize the abuse reporting experience. To help us streamline the review of abuse reports, you acknowledge and agree that your use of GoDaddy’s Abuse API is subject to the following quality metrics and terms of use.&lt;/p&gt;&lt;p&gt;GoDaddy may, in its sole and absolute discretion, change or modify these terms, and such changes or modifications shall be effective immediately upon notice to you. Your use of GoDaddy’s Abuse API after such changes or modifications shall constitute your acceptance of these terms as last revised. If you do not agree to be bound by these terms as last revised, do not use (or continue to use) our Abuse API.&lt;/p&gt;&lt;p&gt;As an Abuse API user, you must only submit abuse reports via the API portal and cease all email submissions, including but not limited, to phishing@godaddy.com, netabuse@godaddy.com, malware@godaddy.com, or spam@godaddy.com, etc.  Any additional or duplicate submission outside of the API portal will be deprioritized for review. Submissions related to trademark, copyright or content issues may still be sent to trademarkclaims@godaddy.com, coyprightclaims@godaddy.com, and contentcomplaints@godaddy.com, respectively. Our [Front of Site](https://supportcenter.godaddy.com/AbuseReport) also describes other scenarios not covered by the API.&lt;/p&gt;&lt;p&gt;When you submit abuse reports via GoDaddy’s Abuse API, you must ensure that you accurately categorize the abuse type of each report to match our definitions in the API documentations provided to you. Any submission that fails to match our definitions or is miscategorized will be marked as a false positive. Examples include, but are not limited to, submissions of trademark complaints marked as phishing or malware, or submissions of copyright complaints marked as phishing or malware, etc.&lt;/p&gt;&lt;p&gt;If, at any time, the false positive rate of submissions exceeds 40% of your total submissions, as determined by GoDaddy, GoDaddy may in its sole discretion deprioritize any subsequent reports submitted by you and/or your organization.&lt;/p&gt;&lt;p&gt;You acknowledge and agree that submitting every URL for a single domain is not necessary and will not expedite the review process. If your submissions exceed five (5) URLs for a single domain, your report will be marked as a duplicate submission taking into account that the final outcome of such submissions would yield the same result as the original report. GoDaddy may in its sole discretion deprioritize reports submitted by you and/or your organization in the event more than 20% of your submissions are classified as duplicate submissions.&lt;/p&gt;&lt;p&gt;You further acknowledge and agree that our Customer Support lines are not intended to address abuse reporting matters or your use of GoDaddy’s Abuse API. Contacting Customer Support will not expedite the review process and may result in abuse reports being deprioritized, to be determined in our sole discretion.&lt;/p&gt;&lt;p&gt;Should you have any questions about GoDaddy’s Abuse API or any of the terms and conditions set forth above, please contact abuseapisupport@godaddy.com.&lt;/p&gt;
    """
)

