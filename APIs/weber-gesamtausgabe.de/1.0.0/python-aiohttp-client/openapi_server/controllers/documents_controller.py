from typing import List, Dict
from aiohttp import web

from openapi_server.models.document import Document
from openapi_server.models.error import Error
from openapi_server import util


async def documents_doc_idget(request: web.Request, doc_id) -> web.Response:
    """Returns documents by ID

    This endpoint returns documents, indicated by an ID.  Accepted ID formats are WeGA, e.g. A002068 or http://weber-gesamtausgabe.de/A002068, VIAF, e.g. http://viaf.org/viaf/14959938, or  GND, e.g. http://d-nb.info/gnd/118629662 

    :param doc_id: The document identifier to search for
    :type doc_id: str

    """
    return web.Response(status=200)


async def documents_find_by_author_author_idget(request: web.Request, author_id, doc_type=None, offset=None, limit=None) -> web.Response:
    """Finds documents by author

    This endpoint returns a list of documents by a given author – optionally filtered by document type  

    :param author_id: The author ID to search for. Accepted ID formats are WeGA, e.g. A002068 or http://weber-gesamtausgabe.de/A002068, VIAF, e.g. http://viaf.org/viaf/14959938, or  GND, e.g. http://d-nb.info/gnd/118629662 
    :type author_id: str
    :param doc_type: The WeGA document type
    :type doc_type: List[str]
    :param offset: Position of first item to retrieve (starting from 1)
    :type offset: int
    :param limit: Number of items to retrieve (200 max)
    :type limit: int

    """
    return web.Response(status=200)


async def documents_find_by_date_get(request: web.Request, from_date, to_date=None, doc_type=None, offset=None, limit=None) -> web.Response:
    """Finds documents by date

    This endpoint returns a list of documents related to the given date – optionally filtered by document type.  

    :param from_date: The min date to search for
    :type from_date: str
    :param to_date: The max date to search for
    :type to_date: str
    :param doc_type: The WeGA document type
    :type doc_type: List[str]
    :param offset: Position of first item to retrieve (starting from 1)
    :type offset: int
    :param limit: Number of items to retrieve (200 max)
    :type limit: int

    """
    from_date = util.deserialize_date(from_date)
    to_date = util.deserialize_date(to_date)
    return web.Response(status=200)


async def documents_find_by_mention_doc_idget(request: web.Request, doc_id, doc_type=None, offset=None, limit=None) -> web.Response:
    """Finds documents by reference

    This endpoint returns a list of documents that reference a particular docID – optionally filtered by document type.  

    :param doc_id: The document ID that is to be mentioned. Accepted ID formats are WeGA, e.g. A002068 or http://weber-gesamtausgabe.de/A002068, VIAF, e.g. http://viaf.org/viaf/14959938, or  GND, e.g. http://d-nb.info/gnd/118629662 
    :type doc_id: str
    :param doc_type: The WeGA document type
    :type doc_type: List[str]
    :param offset: Position of first item to retrieve (starting from 1)
    :type offset: int
    :param limit: Number of items to retrieve (200 max)
    :type limit: int

    """
    return web.Response(status=200)


async def documents_get(request: web.Request, doc_type=None, offset=None, limit=None) -> web.Response:
    """Lists all documents

    The Documents endpoint returns a list of all documents from the WeGA digital edition. 

    :param doc_type: The WeGA document type
    :type doc_type: List[str]
    :param offset: Position of first item to retrieve (starting from 1)
    :type offset: int
    :param limit: Number of items to retrieve (200 max)
    :type limit: int

    """
    return web.Response(status=200)
