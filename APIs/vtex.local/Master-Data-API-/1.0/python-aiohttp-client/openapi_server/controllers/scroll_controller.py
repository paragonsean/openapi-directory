from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def scrolldocuments(request: web.Request, data_entity_name, content_type, accept, rest_range, token=None, fields=None, where=None, _schema=None, keyword=None, sort=None) -> web.Response:
    """Scroll documents

    In the first request, the &#x60;X-VTEX-MD-TOKEN&#x60; token will be returned in the header. This token must be passed to the next request in the query string &#x60;_token&#x60; parameter. The token has a timeout of 10 minutes, which refreshes after each request.    After the token is obtained it is no longer necessary to send the filter or document size per page parameters. You only need to resend the token until the document collection is empty.    &gt; Avoid sending too many requests with wildcards (&#x60;*&#x60;) in the search parameters or that use the &#x60;keyword&#x60; parameter. This may lead to this endpoint being temporarily blocked for your account. If this happens you will receive an error with status code &#x60;429&#x60;.    ## Request examples    First request:  &#x60;&#x60;&#x60;  /dataentities/Client/scroll?isCluster&#x3D;true&amp;_size&#x3D;250&amp;_fields&#x3D;email,firstName  &#x60;&#x60;&#x60;    Retrieve the token in the header &#x60;X-VTEX-MD-TOKEN&#x60; from the first request&#39;s response and use it to make the next requests.    Subsequent requests:  &#x60;&#x60;&#x60;  /dataentities/Client/scroll?_token&#x3D;{tokenValueExample}  &#x60;&#x60;&#x60;

    :param data_entity_name: Name of the data entity. Defined by the api. Examples of native data entities you can use are &#x60;CL&#x60; for client profiles and &#x60;AD&#x60; for client addresses.
    :type data_entity_name: str
    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param rest_range: Defines the collection of documents to be returned. A range within the collection limited by 100 documents per query.
    :type rest_range: str
    :param token: Value of the header &#x60;X-VTEX-MD-TOKEN&#x60; returned in your first request. Send its value in this query string in the subsequent requests. The token has a timeout of 10 minutes, which refreshes after each new request.
    :type token: str
    :param fields: Fields that should be returned by document. Separate fields&#39; names with commas. For example &#x60;_fields&#x3D;email,firstName,document&#x60;. You can also use &#x60;_all&#x60; to fetch all fields.
    :type fields: str
    :param where: Filter specification.
    :type where: str
    :param _schema: Name of the schema the document to be created needs to be compliant with.
    :type _schema: str
    :param keyword: String to search. Use quotes for a partial query. For example, &#x60;_keyword&#x3D;Maria&#x60; or &#x60;_keyword&#x3D;\&quot;Maria\&quot;&#x60;.
    :type keyword: str
    :param sort: Sets sorting mode in two parts. The first part is the name of the field you want to sort by. In the second part, use &#x60;ASC&#x60; for ascending or &#x60;DESC&#x60; for descending.
    :type sort: str

    """
    return web.Response(status=200)
