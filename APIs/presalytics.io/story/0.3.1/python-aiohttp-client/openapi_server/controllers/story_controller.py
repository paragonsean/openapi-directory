from typing import List, Dict
from aiohttp import web

from openapi_server.models.file_upload import FileUpload
from openapi_server.models.outline import Outline
from openapi_server.models.problem_detail import ProblemDetail
from openapi_server.models.status import Status
from openapi_server.models.story import Story
from openapi_server import util


async def story_get(request: web.Request, include_relationships=None, include_outline=None) -> web.Response:
    """Story: Get List of User Stories

    Returns a list of stories for this user identifie via the access token presentated to the api

    :param include_relationships: Indicate whether the returned object should include child relationships
    :type include_relationships: bool
    :param include_outline: Determines whether a repsonse including story objects should include the story outline.  Defaults to true. Useful for speeding up processing times.
    :type include_outline: bool

    """
    return web.Response(status=200)


async def story_id_analytics(request: web.Request, id) -> web.Response:
    """Story: View Analytics

    returns an html document containing session and event metrics for the story

    :param id: the id from the story object
    :type id: str
    :type id: str

    """
    return web.Response(status=200)


async def story_id_delete(request: web.Request, id) -> web.Response:
    """Story: Delete by Id

    Remove a story and dependant data.

    :param id: the id from the story object
    :type id: str
    :type id: str

    """
    return web.Response(status=200)


async def story_id_file_ooxmlautomationid_delete(request: web.Request, id, ooxml_automation_id) -> web.Response:
    """Story: Delete Subdocument

    Deletes a subdcoument of this story (e.g., .pptx, .docx, .xlsx)

    :param id: the id from the story object
    :type id: str
    :type id: str
    :param ooxml_automation_id: the id of the ooxml_automation object
    :type ooxml_automation_id: str
    :type ooxml_automation_id: str

    """
    return web.Response(status=200)


async def story_id_file_ooxmlautomationid_get(request: web.Request, id, ooxml_automation_id) -> web.Response:
    """Story: Download Updated File

    Redtreives updated story as open office xml file (e.g., .pptx, .docx, .xlsx)

    :param id: the id from the story object
    :type id: str
    :type id: str
    :param ooxml_automation_id: the id of the ooxml_automation object
    :type ooxml_automation_id: str
    :type ooxml_automation_id: str

    """
    return web.Response(status=200)


async def story_id_file_post(request: web.Request, id, replace_existing=None, obsolete_id=None, include_outline=None, file=None) -> web.Response:
    """Story: Upload a File To Existing Story

    Upload a file to an existing story

    :param id: the id from the story object
    :type id: str
    :type id: str
    :param replace_existing: Indicates whether a put or post method would replace the existing contents
    :type replace_existing: bool
    :param obsolete_id: A primary key pointing to an obsolete item in the story. Item type is context-dependent
    :type obsolete_id: str
    :type obsolete_id: str
    :param include_outline: Determines whether a repsonse including story objects should include the story outline.  Defaults to true. Useful for speeding up processing times.
    :type include_outline: bool
    :param file: 
    :type file: List[str]

    """
    return web.Response(status=200)


async def story_id_get(request: web.Request, id, include_relationships=None, include_outline=None, full=None, refresh_cache=None) -> web.Response:
    """Story: Get by Id

    Returns story metadata, inlcuding json object with story outline

    :param id: the id from the story object
    :type id: str
    :type id: str
    :param include_relationships: Indicate whether the returned object should include child relationships
    :type include_relationships: bool
    :param include_outline: Determines whether a repsonse including story objects should include the story outline.  Defaults to true. Useful for speeding up processing times.
    :type include_outline: bool
    :param full: Pull a story object with associated collaborator user, permission, and session data(faster if cached from prior api call)
    :type full: bool
    :param refresh_cache: Force the api reload the &#x60;Story full&#x60; object
    :type refresh_cache: bool

    """
    return web.Response(status=200)


async def story_id_outline_get(request: web.Request, id) -> web.Response:
    """Story: Get Story Outline

    Returns Story&#39;s outline

    :param id: the id from the story object
    :type id: str
    :type id: str

    """
    return web.Response(status=200)


async def story_id_outline_post(request: web.Request, id, body) -> web.Response:
    """Story: Post Story Outline

    Update a story outline.

    :param id: the id from the story object
    :type id: str
    :type id: str
    :param body: A story outline object
    :type body: str

    """
    return web.Response(status=200)


async def story_id_public(request: web.Request, id) -> web.Response:
    """Story: Public Link to Story Reveal.js Document

    returns an html document containing a reveal.js epresentation of the story, if the story if set to is_public &#x3D; True

    :param id: the id from the story object
    :type id: str
    :type id: str

    """
    return web.Response(status=200)


async def story_id_put(request: web.Request, id, body, include_outline=None) -> web.Response:
    """Story: Modify

    Update story metadata, including story outline

    :param id: the id from the story object
    :type id: str
    :type id: str
    :param body: The updated story object
    :type body: dict | bytes
    :param include_outline: Determines whether a repsonse including story objects should include the story outline.  Defaults to true. Useful for speeding up processing times.
    :type include_outline: bool

    """
    body = Story.from_dict(body)
    return web.Response(status=200)


async def story_id_reveal(request: web.Request, id) -> web.Response:
    """Story: Get Story at Reveal.js Document

    returns an html document containing a reveal.js epresentation of the story

    :param id: the id from the story object
    :type id: str
    :type id: str

    """
    return web.Response(status=200)


async def story_id_status_get(request: web.Request, id) -> web.Response:
    """Story: Get Story Status

    Returns code indicating whether story has active running background and is healthy (e.g., the latest outline is valid)

    :param id: the id from the story object
    :type id: str
    :type id: str

    """
    return web.Response(status=200)


async def story_post(request: web.Request, body, include_outline=None) -> web.Response:
    """Story: Upload

    Upload new story to presalytics api

    :param body: A story outline json object
    :type body: dict | bytes
    :param include_outline: Determines whether a repsonse including story objects should include the story outline.  Defaults to true. Useful for speeding up processing times.
    :type include_outline: bool

    """
    body = Outline.from_dict(body)
    return web.Response(status=200)


async def story_post_file(request: web.Request, include_outline=None, file=None) -> web.Response:
    """Story: Upload a File

    Upload new story to presalytics api via an Open Office Xml file

    :param include_outline: Determines whether a repsonse including story objects should include the story outline.  Defaults to true. Useful for speeding up processing times.
    :type include_outline: bool
    :param file: 
    :type file: List[str]

    """
    return web.Response(status=200)


async def story_post_file_json(request: web.Request, include_outline=None, body=None) -> web.Response:
    """Story: Upload a File (base64)

    Upload new story to presalytics api via an Open Office Xml file

    :param include_outline: Determines whether a repsonse including story objects should include the story outline.  Defaults to true. Useful for speeding up processing times.
    :type include_outline: bool
    :param body: A json-formatted object that includes a base64 encoded file (file encoded utf-8)
    :type body: dict | bytes

    """
    body = FileUpload.from_dict(body)
    return web.Response(status=200)
