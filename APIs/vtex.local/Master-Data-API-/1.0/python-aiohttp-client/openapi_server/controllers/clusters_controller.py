from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def validatedocumentbyclusters(request: web.Request, data_entity_name, accept, id, body) -> web.Response:
    """Validate document by clusters

    Check if a document is present in one or more clusters (specific set of field values).    &gt; There is a limit of five rules per request.

    :param data_entity_name: Name of the data entity. Defined by the api. Examples of native data entities you can use are &#x60;CL&#x60; for client profiles and &#x60;AD&#x60; for client addresses.
    :type data_entity_name: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param id: ID of the Document.
    :type id: str
    :param body: Request body for validating a document by clusters
    :type body: str

    """
    return web.Response(status=200)
