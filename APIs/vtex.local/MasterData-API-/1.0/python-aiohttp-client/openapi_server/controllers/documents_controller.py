from typing import List, Dict
from aiohttp import web

from openapi_server.models.createnewdocument import Createnewdocument
from openapi_server.models.usingfilters import Usingfilters
from openapi_server import util


async def createnewdocument(request: web.Request, accept, acronym, body) -> web.Response:
    """Create new document

    Creates documents through a JSON object where the key is the name of the field.

    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand 
    :type accept: str
    :param acronym: Identifies the kind of data
    :type acronym: str
    :param body: 
    :type body: 

    """
    return web.Response(status=200)


async def createorupdateentiredocument(request: web.Request, accept, acronym, body) -> web.Response:
    """Create or update entire document

    

    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand 
    :type accept: str
    :param acronym: Identifies the kind of data
    :type acronym: str
    :param body: 
    :type body: 

    """
    return web.Response(status=200)


async def createorupdatepartialdocument(request: web.Request, accept, acronym, body) -> web.Response:
    """Create or update partial document

    

    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand 
    :type accept: str
    :param acronym: Identifies the kind of data
    :type acronym: str
    :param body: 
    :type body: 

    """
    return web.Response(status=200)


async def deletedocument(request: web.Request, content_type, accept, acronym, id) -> web.Response:
    """Delete document

    It allows to delete a document.

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


async def getdocument(request: web.Request, content_type, accept, acronym, id) -> web.Response:
    """Get document

    Retrieves a document.    Assign the &#x60;_fields&#x60; parameter in the query string to retrieve the desired fields. If you want to return all the fields use &#x60;_fields&#x3D;_all&#x60;.

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


async def updateentiredocument(request: web.Request, accept, acronym, id, body) -> web.Response:
    """Update entire document

    

    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand 
    :type accept: str
    :param acronym: Two letter word that identifies the data structure
    :type acronym: str
    :param id: Id of the document
    :type id: str
    :param body: 
    :type body: 

    """
    return web.Response(status=200)


async def updatepartialdocument(request: web.Request, accept, acronym, id, body) -> web.Response:
    """Update partial document

    

    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand 
    :type accept: str
    :param acronym: Two letter word that identifies the data structure
    :type acronym: str
    :param id: Id of the document
    :type id: str
    :param body: 
    :type body: 

    """
    return web.Response(status=200)
