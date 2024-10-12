from typing import List, Dict
from aiohttp import web

from openapi_server.models.child_objects import ChildObjects
from openapi_server.models.document import Document
from openapi_server.models.document_clone_dto import DocumentCloneDTO
from openapi_server import util


async def documents_childobjects_get_id(request: web.Request, id) -> web.Response:
    """DocumentsController: Get Dependent Objects Tree

    This endpoint is helpful for helping users and bots identify dependent objects to this DocumentsController and retreive their corresponding metadata in order to make modifications to those objects in downstream operations.

    :param id: 
    :type id: str
    :type id: str

    """
    return web.Response(status=200)


async def documents_clone_post_id(request: web.Request, id, body=None) -> web.Response:
    """Documents: Clone an existing Ooxml Document to new Parent Story

    Clone A Document that has already been uploaded to a new Story

    :param id: the Source document Id
    :type id: str
    :type id: str
    :param body: A DocumentCloneDto object with containing information required for cloning the document
    :type body: dict | bytes

    """
    body = DocumentCloneDTO.from_dict(body)
    return web.Response(status=200)


async def documents_delete_id(request: web.Request, id) -> web.Response:
    """Documents: Delete by Id

    Permantly delete a document from the Ooxml Automation API. Note that is does not make changes to the related Presalytics APIs.  Please use the delete endpoint in the story API to ensure that stories are not left with orphaned references to the Ooxml Automation API.

    :param id: 
    :type id: str
    :type id: str

    """
    return web.Response(status=200)


async def documents_download_get_id_orginal(request: web.Request, id, orginal=None) -> web.Response:
    """Documents: Download

    Download the into a bytestream for client-side processing.

    :param id: 
    :type id: str
    :type id: str
    :param orginal: 
    :type orginal: bool

    """
    return web.Response(status=200)


async def documents_get_id(request: web.Request, id) -> web.Response:
    """Documents: Get by Id

    Get by Id: Use this method to retrieve a Documents object by its primary key (id)

    :param id: 
    :type id: str
    :type id: str

    """
    return web.Response(status=200)


async def documents_post(request: web.Request, file, story_id) -> web.Response:
    """Documents: Upload

    Upload an OpenOfficeXml document (e.g., .xlsx, .pptx) for processing by the API.

    :param file: The file to upload.  Must be of type .pptx, ppt
    :type file: str
    :param story_id: The story_id of the document being uploaded.
    :type story_id: str
    :type story_id: str

    """
    return web.Response(status=200)
