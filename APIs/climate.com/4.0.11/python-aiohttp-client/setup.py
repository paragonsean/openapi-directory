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
    description="Climate FieldView Platform APIs",
    author_email="developer@climate.com",
    url="",
    keywords=["OpenAPI", "Climate FieldView Platform APIs"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    **Last Modified**: Wed Jan  4 12:47:29 UTC 2023   All endpoints are only accessible via HTTPS.  * All API endpoints are located at &#x60;https://platform.climate.com&#x60; (e.g. &#x60;https://platform.climate.com/v4/fields&#x60;).  * The authorization token endpoint is located at &#x60;https://api.climate.com/api/oauth/token&#x60;.  ## Troubleshooting  &#x60;X-Http-Request-Id&#x60; response header will be returned on every call, successful or not. If you experience an issue with our api and need to contact technical support, please supply the value of the &#x60;X-Http-Request-Id&#x60; header along with an approximate time of when the request was made.  ## Request Limits  When you’re onboarded to Climate’s API platform, your &#x60;x-api-key&#x60; is assigned a custom usage plan. Usage plans are unique to each partner and have the following key attributes:   1. Throttling information     * burstLimit: Maximum rate limit over a period ranging from 1 second to a few seconds     * rateLimit: A steady-state rate limit  2. Quota information     * Limit: The maximum number of requests that can be made in a given month  When the request rate threshold is exceeded, a &#x60;429&#x60; response code is returned. Optionally, the [&#x60;Retry-After&#x60;](https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.37) header may be returned:   Following are examples of rate limit errors:  1. Rate limit exceeded:  &lt;br&gt;HTTP/1.1 429  &lt;br&gt;Content-Type: application/json &lt;br&gt;Content-Length: 32     {\&quot;message\&quot;:\&quot;Too Many Requests\&quot;}  2. Quota exhausted: &lt;br&gt;HTTP/1.1 429  &lt;br&gt;Content-Type: application/json &lt;br&gt;Content-Length: 29      {\&quot;message\&quot;:\&quot;Limit Exceeded\&quot;}  ## Pagination  Pagination is performed via headers. Any request which returns a &#x60;\&quot;results\&quot;&#x60; array may be paginated. The following figure shows how query results are laid out with X-Limit&#x3D;4 and no filter applied.  &lt;img style&#x3D;\&quot;width:70%;height:auto;\&quot; src&#x3D;\&quot;https://s3-us-west-2.amazonaws.com/climate-com/images/svg_upload_tests/paging.png\&quot;&gt;  * If there are no results, a response code of &#x60;304&#x60; will be returned.  * If the response is the last set of results, a response code of &#x60;200&#x60; or &#x60;206&#x60; will be returned.  * If there are more results, a response code of &#x60;206&#x60; will be returned.  * If &#x60;X-Next-Token&#x60; is provided in the request headers but the token has expired, a response code of &#x60;409&#x60; will be returned. This is only applicable for some endpoints; see specific endpoint documentation below.  #### X-Limit  The page size can be controlled with the &#x60;X-Limit&#x60; header. Valid values are &#x60;1-100&#x60; and defaults to &#x60;100&#x60;.  #### X-Next-Token  If the results are paginated, a response header of &#x60;X-Next-Token&#x60; will be returned. Use the associated value in the subsequent request (via the &#x60;X-Next-Token&#x60; request header) to retrieve the next page. The following sequence diagram shows how to use &#x60;X-Next-Token&#x60; to fetch all the records.  &lt;img src&#x3D;\&quot;https://s3-us-west-2.amazonaws.com/climate-com/images/svg_upload_tests/x-next-token.svg\&quot;&gt;   ## Chunked Uploads  Uploads larger than &#x60;5MiB&#x60; (&#x60;5242880 bytes&#x60;) must be done in &#x60;5MiB&#x60; chunks (with the exception of the final chunk). Each chunk request MUST contain a &#x60;Content-Range&#x60; header specifying the portion of the upload, and a &#x60;Content-Type&#x60; header specifying binary content type (&#x60;application/octet-stream&#x60;). Range uploads must be contiguous. The maximum upload size is capped at &#x60;500MiB&#x60; (&#x60;524288000 bytes&#x60;).  ## Chunked Downloads  Downloads larger than &#x60;5MiB&#x60; (&#x60;5242880 bytes&#x60;) must be done in &#x60;1-5MiB&#x60; chunks (with the exception of the final chunk, which may be less than &#x60;1MiB&#x60;). Each chunk request MUST contain a &#x60;Range&#x60; header specifying the requested portion of the download, and an &#x60;Accept&#x60; header specifying binary and json content types  (&#x60;application/octet-stream,application/json&#x60;) or all content types (&#x60;*/*&#x60;).  ## Drivers  If you need drivers to process agronomic data, download the ADAPT plugin below. We only support the plugin in the Windows environment, minimum is Windows 7 SP1.  For asPlanted, asHarvested and asApplied data: * [ADAPT Plugin](https://dev.fieldview.com/drivers/ClimateADAPTPlugin_latest.exe) &lt;br&gt;Release notes can be found [here](https://dev.fieldview.com/drivers/adapt-release-notes.txt). &lt;br&gt;Download and use of the ADAPT plugin means that you agree to the EULA for use of the ADAPT plugin.  &lt;br&gt;Please review the [EULA](https://dev.fieldview.com/EULA/ADAPT%20Plugin%20EULA-06-19.pdf) (last updated on June 6th, 2019) before download and use of the ADAPT plugin. &lt;br&gt;For more information, please refer to:   * [ADAPT Resources](https://adaptframework.org/)   * [ADAPT Overview](https://aggateway.atlassian.net/wiki/spaces/ADM/overview)   * [ADAPT FAQ](https://aggateway.atlassian.net/wiki/spaces/ADM/pages/165942474/ADAPT+Frequently-Asked+Questions+FAQ)   * [ADAPT Videos](https://adaptframework.org/adapt-videos/)  ## Sample Test Data  Sample agronomic data: * [asPlanted and asHarvested data](https://dev.fieldview.com/sample-agronomic-data/Planting_Harvesting_data_04_18_2018_21_46_18.zip) * [asApplied data set 1](https://dev.fieldview.com/sample-agronomic-data/as-applied-data1.zip) * [asApplied data set 2](https://dev.fieldview.com/sample-agronomic-data/as-applied-data2.zip) &lt;br&gt;To upload the sample data to your account, please follow the instructions in this [link](https://support.climate.com/kt#/kA02A000000AaxzSAC/en_US).  Sample soil data: * [Sample soil data](https://dev.fieldview.com/sample-soil-data/soil-sample.xml) --- 
    """
)

