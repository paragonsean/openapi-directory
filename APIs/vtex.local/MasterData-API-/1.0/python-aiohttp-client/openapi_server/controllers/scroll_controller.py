from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def scrolldocuments(request: web.Request, content_type, accept, acronym) -> web.Response:
    """Scroll documents

    Scrolls through documents according to the query parameter filters.    &gt; Avoid sending too many requests with wildcards (&#x60;*&#x60;) in the search parameters or that use the &#x60;keyword&#x60; parameter. This may lead to this endpoint being temporarily blocked for your account. If this happens you will receive an error with status code &#x60;429&#x60;.    Use all the features of &#x60;search&#x60; API to perform filters.    In the first request, the &#x60;X-VTEX-MD-TOKEN&#x60; token will be obtained in the header. This token must be passed to the next request in the query string &#x60;_token&#x60; parameter. The token has a timeout of 10 minutes, which refreshes after each request.    **ATTENTION:** To inform the number of documents per request, use the query string parameter &#x60;_size&#x60;, which has the maximum value of 1000.    After the token is obtained it is no longer necessary to send the filter or document size per page parameters. You only need to resend the token until the document collection is empty.    ### First request example:  &#x60;&#x60;&#x60;  /dataentities/CL/scroll?isCluster&#x3D;true&amp;_size&#x3D;250&amp;_fields&#x3D;email,firstName  &#x60;&#x60;&#x60;    After the first request, retrieve the token in the header &#x60;X-VTEX-MD-TOKEN&#x60; and make the next requests.    ### Example of subsequent requests:  &#x60;&#x60;&#x60;  /dataentities/CL/scroll?_token&#x3D;tokenvalueexample  &#x60;&#x60;&#x60;

    :param content_type: Type of the content being sent
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand 
    :type accept: str
    :param acronym: Identifies the kind of data
    :type acronym: str

    """
    return web.Response(status=200)
