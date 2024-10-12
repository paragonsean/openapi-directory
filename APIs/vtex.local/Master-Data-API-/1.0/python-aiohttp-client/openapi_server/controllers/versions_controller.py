from typing import List, Dict
from aiohttp import web

from openapi_server.models.document_response import DocumentResponse
from openapi_server.models.getversion import Getversion
from openapi_server.models.listversion import Listversion
from openapi_server import util


async def getversion(request: web.Request, data_entity_name, content_type, accept, id, version_id) -> web.Response:
    """Get version

    Returns the version of a document.

    :param data_entity_name: Name of the data entity. Defined by the api. Examples of native data entities you can use are &#x60;CL&#x60; for client profiles and &#x60;AD&#x60; for client addresses.
    :type data_entity_name: str
    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param id: ID of the Document.
    :type id: str
    :param version_id: ID of the version to update.
    :type version_id: str

    """
    return web.Response(status=200)


async def listversions(request: web.Request, data_entity_name, content_type, accept, id, load=None, fields=None) -> web.Response:
    """List versions

    Allows to list the versions of a document.

    :param data_entity_name: Name of the data entity. Defined by the api. Examples of native data entities you can use are &#x60;CL&#x60; for client profiles and &#x60;AD&#x60; for client addresses.
    :type data_entity_name: str
    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param id: ID of the Document.
    :type id: str
    :param load: If true, return all the fields in each version of the document
    :type load: bool
    :param fields: If &#x60;load&#x60; is true, the response will return only these specific fields
    :type fields: str

    """
    return web.Response(status=200)


async def putversion(request: web.Request, data_entity_name, content_type, accept, id, version_id) -> web.Response:
    """Put version

    Updates document with version values.

    :param data_entity_name: Name of the data entity. Defined by the api. Examples of native data entities you can use are &#x60;CL&#x60; for client profiles and &#x60;AD&#x60; for client addresses.
    :type data_entity_name: str
    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param id: ID of the Document.
    :type id: str
    :param version_id: ID of the version to update
    :type version_id: str

    """
    return web.Response(status=200)
