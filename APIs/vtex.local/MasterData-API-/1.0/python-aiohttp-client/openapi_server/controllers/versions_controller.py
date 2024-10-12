from typing import List, Dict
from aiohttp import web

from openapi_server.models.getversion import Getversion
from openapi_server.models.listversion import Listversion
from openapi_server.models.putversion import Putversion
from openapi_server import util


async def getversion(request: web.Request, content_type, accept, acronym, id, version_id) -> web.Response:
    """Get version

    Returns the version of a document.

    :param content_type: Type of the content being sent
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand 
    :type accept: str
    :param acronym: Two letter word that identifies the data structure
    :type acronym: str
    :param id: Id of the document
    :type id: str
    :param version_id: Id of the version to get
    :type version_id: str

    """
    return web.Response(status=200)


async def listversions(request: web.Request, content_type, accept, acronym, id) -> web.Response:
    """List versions

    Allows to list the versions of a document.

    :param content_type: Type of the content being sent
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand 
    :type accept: str
    :param acronym: Two letter word that identifies the data structure
    :type acronym: str
    :param id: Id of the document
    :type id: str

    """
    return web.Response(status=200)


async def putversion(request: web.Request, content_type, accept, acronym, id, version_id) -> web.Response:
    """Put version

    Updates document with version values.

    :param content_type: Type of the content being sent
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand 
    :type accept: str
    :param acronym: Two letter word that identifies the data structure
    :type acronym: str
    :param id: Id of the document
    :type id: str
    :param version_id: Id of the version to update
    :type version_id: str

    """
    return web.Response(status=200)
