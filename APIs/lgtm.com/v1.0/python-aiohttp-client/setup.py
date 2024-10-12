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
    description="LGTM API specification",
    author_email="",
    url="",
    keywords=["OpenAPI", "LGTM API specification"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    The REST API for LGTM provides data so that you can customize how you integrate LGTM analysis into your workflow. It includes the following resources:   * &#x60;/&#x60; ([API root](https://lgtm.com/help/lgtm/api/api-v1#LGTM-API-specification-API-root))&amp;mdash;get version information or download the specification in OpenAPI format.   * &#x60;/projects&#x60; ([Projects](https://lgtm.com/help/lgtm/api/api-v1#LGTM-API-specification-Projects))&amp;mdash;list projects, get a summary of the current status for a project, or add new projects.   * &#x60;/analyses&#x60; ([Analyses](https://lgtm.com/help/lgtm/api/api-v1#LGTM-API-specification-Analyses))&amp;mdash;get a summary of results, download all the alerts, or trigger analysis for a specific commit.   * &#x60;/codereviews&#x60; ([Code reviews](https://lgtm.com/help/lgtm/api/api-v1#LGTM-API-specification-Code-reviews))&amp;mdash;trigger code review for a patch, and view the results.   * &#x60;/operations&#x60; ([Operations](https://lgtm.com/help/lgtm/api/api-v1#LGTM-API-specification-Operations))&amp;mdash;get information about long-running tasks, for example, analyses or code reviews that you&#39;ve requested.   * &#x60;/snapshots&#x60; ([Snapshots](https://lgtm.com/help/lgtm/api/api-v1#LGTM-API-specification-Snapshots))&amp;mdash;download and upload databases representing a snapshot of a codebase.   * &#x60;/queryjobs&#x60; ([Query jobs](https://lgtm.com/help/lgtm/api/api-v1#LGTM-API-specification-Query-jobs))&amp;mdash;submit queries to evaluate against existing projects, and download their results.   * &#x60;/system&#x60; ([System](https://lgtm.com/help/lgtm/api/api-v1#LGTM-API-specification-System))&amp;mdash;get information on the health or usage of the system.  For an overview and getting started topics, see [API for LGTM](https://lgtm.com/help/lgtm/api/api-for-lgtm). 
    """
)

