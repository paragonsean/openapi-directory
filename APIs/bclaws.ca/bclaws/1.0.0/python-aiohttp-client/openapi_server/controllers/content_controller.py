from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def content_aspect_id_civix_document_id_get(request: web.Request, aspect_id, civix_document_id) -> web.Response:
    """Lists the metadata available for the specified index or directory from the BCLaws legislative respository

    

    :param aspect_id: The identifier of the &#39;aspect&#39; (content group) to search
    :type aspect_id: str
    :param civix_document_id: The document identification code for an index or directory
    :type civix_document_id: str

    """
    return web.Response(status=200)


async def content_aspect_id_get(request: web.Request, aspect_id) -> web.Response:
    """Describes the documents and directories available within a specific &#39;aspect&#39; (content group) of the BCLaws library

    

    :param aspect_id: The identifier of the &#39;aspect&#39; (content group) to search
    :type aspect_id: str

    """
    return web.Response(status=200)
