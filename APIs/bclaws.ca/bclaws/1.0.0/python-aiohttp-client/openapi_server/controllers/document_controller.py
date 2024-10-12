from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def document_id_aspect_id_civix_index_id_civix_document_id_get(request: web.Request, aspect_id, civix_index_id, civix_document_id) -> web.Response:
    """Retrieves a specific document from the BCLaws legislative repository (HTML format)

    The /document API allows you to retrieve actual documents from the BCLaws legislative repository. To retrieve a document from the repository you need the aspect identifier and two other specific pieces of information about the document: the index identifier and the document identifier. These unique identifiers can be retrieved from the /content API.

    :param aspect_id: The identifier of the &#39;aspect&#39; (content group) to search
    :type aspect_id: str
    :param civix_index_id: Index identification code
    :type civix_index_id: str
    :param civix_document_id: The document identification code for an index or directory
    :type civix_document_id: str

    """
    return web.Response(status=200)


async def document_id_aspect_id_civix_index_id_civix_document_id_search_search_string_get(request: web.Request, aspect_id, civix_index_id, civix_document_id, search_string) -> web.Response:
    """Retrieves a specific document from the BCLaws legislative repository with search text highlighted (HTML format)

    The /document API allows you to retrieve actual documents from the BCLaws legislative repository. To retrieve a document from the repository you need the aspect identifier and two other specific pieces of information about the document: the index identifier and the document identifier. These unique identifiers can be retrieved from the /content API.

    :param aspect_id: The identifier of the &#39;aspect&#39; (content group) to search
    :type aspect_id: str
    :param civix_index_id: Index identification code
    :type civix_index_id: str
    :param civix_document_id: The document identification code for an index or directory
    :type civix_document_id: str
    :param search_string: The text to search for within the document
    :type search_string: str

    """
    return web.Response(status=200)


async def document_id_aspect_id_civix_index_id_civix_document_id_xml_get(request: web.Request, aspect_id, civix_index_id, civix_document_id) -> web.Response:
    """Retrieves a specific document from the BCLaws legislative repository (XML format)

    The /document API allows you to retrieve actual documents from the BCLaws legislative repository. To retrieve a document from the repository you need the aspect identifier and two other specific pieces of information about the document: the index identifier and the document identifier. These unique identifiers can be retrieved from the /content API.

    :param aspect_id: The identifier of the &#39;aspect&#39; (content group) to search
    :type aspect_id: str
    :param civix_index_id: Index identification code
    :type civix_index_id: str
    :param civix_document_id: The document identification code for an index or directory
    :type civix_document_id: str

    """
    return web.Response(status=200)


async def document_id_aspect_id_civix_index_id_civix_document_id_xml_search_search_string_get(request: web.Request, aspect_id, civix_index_id, civix_document_id, search_string) -> web.Response:
    """Retrieves a specific document from the BCLaws legislative repository with search text highlighted (XML format)

    The /document API allows you to retrieve actual documents from the BCLaws legislative repository. To retrieve a document from the repository you need the aspect identifier and two other specific pieces of information about the document: the index identifier and the document identifier. These unique identifiers can be retrieved from the /content API.

    :param aspect_id: The identifier of the &#39;aspect&#39; (content group) to search
    :type aspect_id: str
    :param civix_index_id: Index identification code
    :type civix_index_id: str
    :param civix_document_id: The document identification code for an index or directory
    :type civix_document_id: str
    :param search_string: The text to search for within the document
    :type search_string: str

    """
    return web.Response(status=200)
