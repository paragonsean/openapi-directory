from typing import List, Dict
from aiohttp import web

from openapi_server.models.post_versions_publish_anon200_response import POSTVersionsPublishAnon200Response
from openapi_server.models.post_versions_publish_anon_request import POSTVersionsPublishAnonRequest
from openapi_server import util


async def p_ost_versions_publish_anon(request: web.Request, body=None) -> web.Response:
    """Publish Anonymous

    Anonymously publish to API Docs.  This endpoint will take a JSON spec or a URL to a swagger or raml spec.  &#x60;&#x60;&#x60; {   \&quot;specData\&quot;: {...} } &#x60;&#x60;&#x60;  or  &#x60;&#x60;&#x60; {   \&quot;url\&quot;: \&quot;http://petstore.swagger.io/v2/swagger.json\&quot; } &#x60;&#x60;&#x60;  The spec will be published to api-docs.io anonymously, which means you will not be able to update or remove this documentation.  The response will contain a url to the published documentation.  &#x60;&#x60;&#x60; {   \&quot;url\&quot;: \&quot;https://swagger-petstore.api-docs.io/v1.0.0\&quot; } &#x60;&#x60;&#x60;   The limitations of anonymous publishing * Cannot update/remove the documentation * Cannot choose the subdomain * Cannot choose the version * Cannot add theming

    :param body: 
    :type body: dict | bytes

    """
    body = POSTVersionsPublishAnonRequest.from_dict(body)
    return web.Response(status=200)
