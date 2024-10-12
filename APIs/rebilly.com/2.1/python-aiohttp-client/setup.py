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
    description="Rebilly REST API",
    author_email="integrations@rebilly.com",
    url="",
    keywords=["OpenAPI", "Rebilly REST API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    # Introduction The Rebilly API is built on HTTP.  Our API is RESTful.  It has predictable resource URLs.  It returns HTTP response codes to indicate errors.  It also accepts and returns JSON in the HTTP body.  You can use your favorite HTTP/REST library for your programming language to use Rebilly&#39;s API, or you can use one of our SDKs (currently available in [PHP](https://github.com/Rebilly/rebilly-php) and [Javascript](https://github.com/Rebilly/rebilly-js-sdk)).  We have other APIs that are also available.  Every action from our [app](https://app.rebilly.com) is supported by an API which is documented and available for use so that you may automate any workflows necessary.  This document contains the most commonly integrated resources.  # Authentication  When you sign up for an account, you are given your first secret API key. You can generate additional API keys, and delete API keys (as you may need to rotate your keys in the future). You authenticate to the Rebilly API by providing your secret key in the request header.  Rebilly offers three forms of authentication:  secret key, publishable key, JSON Web Tokens, and public signature key. - [Secret API key](#section/Authentication/SecretApiKey): used for requests made   from the server side. Never share these keys. Keep them guarded and secure. - [Publishable API key](#section/Authentication/PublishableApiKey): used for    requests from the client side. For now can only be used to create    a [Payment Token](#operation/PostToken) and    a [File token](#operation/PostFile). - [JWT](#section/Authentication/JWT): short lifetime tokens that can be assigned a specific expiration time.  Never share your secret keys. Keep them guarded and secure.  &amp;lt;!-- ReDoc-Inject: &amp;lt;security-definitions&amp;gt; --&amp;gt;  # Errors Rebilly follow&#39;s the error response format proposed in [RFC 7807](https://tools.ietf.org/html/rfc7807) also known as Problem Details for HTTP APIs.  As with our normal API responses, your client must be prepared to gracefully handle additional members of the response.  ## Forbidden &amp;lt;RedocResponse pointer&#x3D;{\&quot;#/components/responses/Forbidden\&quot;} /&amp;gt;  ## Conflict &amp;lt;RedocResponse pointer&#x3D;{\&quot;#/components/responses/Conflict\&quot;} /&amp;gt;  ## NotFound &amp;lt;RedocResponse pointer&#x3D;{\&quot;#/components/responses/NotFound\&quot;} /&amp;gt;  ## Unauthorized &amp;lt;RedocResponse pointer&#x3D;{\&quot;#/components/responses/Unauthorized\&quot;} /&amp;gt;  ## ValidationError &amp;lt;RedocResponse pointer&#x3D;{\&quot;#/components/responses/ValidationError\&quot;} /&amp;gt;  # SDKs  Rebilly offers a Javascript SDK and a PHP SDK to help interact with the API.  However, no SDK is required to use the API.  Rebilly also offers [FramePay](https://docs.rebilly.com/docs/developer-docs/framepay/),  a client-side iFrame-based solution to help create payment tokens while minimizing PCI DSS compliance burdens and maximizing the customizability. [FramePay](https://docs.rebilly.com/docs/developer-docs/framepay/) is interacting with the [payment tokens creation operation](#operation/PostToken).  ## Javascript SDK  Installation and usage instructions can be found [here](https://docs.rebilly.com/docs/developer-docs/sdks). SDK code examples are included in these docs.  ## PHP SDK For all PHP SDK examples provided in these docs you will need to configure the &#x60;$client&#x60;. You may do it like this:  &#x60;&#x60;&#x60;php $client &#x3D; new Rebilly\\Client([     &#39;apiKey&#39; &#x3D;&amp;gt; &#39;YourApiKeyHere&#39;,     &#39;baseUrl&#39; &#x3D;&amp;gt; &#39;https://api.rebilly.com&#39;, ]); &#x60;&#x60;&#x60;  # Using filter with collections Rebilly provides collections filtering. You can use &#x60;?filter&#x60; param on collections to define which records should be shown in the response.  Here is filter format description:  - Fields and values in filter are separated with &#x60;:&#x60;: &#x60;?filter&#x3D;firstName:John&#x60;.  - Sub-fields are separated with &#x60;.&#x60;: &#x60;?filter&#x3D;billingAddress.country:US&#x60;.  - Multiple filters are separated with &#x60;;&#x60;: &#x60;?filter&#x3D;firstName:John;lastName:Doe&#x60;. They will be joined with &#x60;AND&#x60; logic. In this example: &#x60;firstName:John&#x60; AND &#x60;lastName:Doe&#x60;.  - You can use multiple values using &#x60;,&#x60; as values separator: &#x60;?filter&#x3D;firstName:John,Bob&#x60;. Multiple values specified for a field will be joined with &#x60;OR&#x60; logic. In this example: &#x60;firstName:John&#x60; OR &#x60;firstName:Bob&#x60;.  - To negate the filter use &#x60;!&#x60;: &#x60;?filter&#x3D;firstName:!John&#x60;. Note that you can negate multiple values like this: &#x60;?filter&#x3D;firstName:!John,!Bob&#x60;. This filter rule will exclude all Johns and Bobs from the response.  - You can use range filters like this: &#x60;?filter&#x3D;amount:1..10&#x60;.  - You can use gte (greater than or equals) filter like this: &#x60;?filter&#x3D;amount:1..&#x60;, or lte (less than or equals) than filter like this: &#x60;?filter&#x3D;amount:..10&#x60;. This also works for datetime-based fields.  - You can create some [predefined values lists](https://user-api-docs.rebilly.com/#tag/Lists) and use them in filter: &#x60;?filter&#x3D;firstName:@yourListName&#x60;. You can also exclude list values: &#x60;?filter&#x3D;firstName:!@yourListName&#x60;.  - Datetime-based fields accept values formatted using RFC 3339 like this: &#x60;?filter&#x3D;createdTime:2021-02-14T13:30:00Z&#x60;.   # Expand to include embedded objects Rebilly provides the ability to pre-load additional  objects with a request.   You can use &#x60;?expand&#x60; param on most requests to expand and include embedded objects within the &#x60;_embedded&#x60; property of the response.  The &#x60;_embedded&#x60; property contains an array of  objects keyed by the expand parameter value(s).  You may expand multiple objects by passing them as comma-separated to the expand value like so:  &#x60;&#x60;&#x60; ?expand&#x3D;recentInvoice,customer &#x60;&#x60;&#x60;  And in the response, you would see:  &#x60;&#x60;&#x60; \&quot;_embedded\&quot;: [     \&quot;recentInvoice\&quot;: {...},     \&quot;customer\&quot;: {...} ] &#x60;&#x60;&#x60; Expand may be utilitized not only on &#x60;GET&#x60; requests but also on &#x60;PATCH&#x60;, &#x60;POST&#x60;, &#x60;PUT&#x60; requests too.   # Getting started guide  Rebilly&#39;s API has over 300 operations.  That&#39;s more than you&#39;ll  need to implement your use cases.  If you have a use  case you would like to implement, please consult us for feedback on the best API operations for the task.  Our getting started guide will demonstrate a basic order form use case.  It will allow us to highlight core resources in Rebilly that will be helpful for many other use cases too.  Within 25 minutes, you&#39;ll have sent API requests (via our console) to create a subscription order. 
    """
)

