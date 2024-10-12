from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.tag import Tag
from openapi_server.models.tag_set import TagSet
from openapi_server.models.tag_set_submission import TagSetSubmission
from openapi_server.models.tag_submission import TagSubmission
from openapi_server import util


async def tags_get(request: web.Request, owned_by=None, tag_set=None, url_words=None) -> web.Response:
    """List tags

    Retrieve tags.

    :param owned_by: Restrict results to those owned by this user.
    :type owned_by: str
    :param tag_set: Restrict results to tags belonging to this tag set.
    :type tag_set: str
    :param url_words: Restrict results by urlWords. Should be used with ownedBy when searching for one of your own tags.
    :type url_words: str

    """
    return web.Response(status=200)


async def tags_id_get(request: web.Request, id) -> web.Response:
    """Retrieve a single tag by id

    

    :param id: Id of the tag to return
    :type id: str

    """
    return web.Response(status=200)


async def tags_post(request: web.Request, body) -> web.Response:
    """Create a new tag

    

    :param body: Tag object to be created
    :type body: dict | bytes

    """
    body = TagSubmission.from_dict(body)
    return web.Response(status=200)


async def tagsets_get(request: web.Request, owned_by=None, url_words=None) -> web.Response:
    """List tag sets

    Retrieve tag sets.

    :param owned_by: Restrict results to those owned by this user.
    :type owned_by: str
    :param url_words: Restrict results by urlWords. Should be used with ownedBy when searching for one of your own tag sets.
    :type url_words: str

    """
    return web.Response(status=200)


async def tagsets_id_get(request: web.Request, id) -> web.Response:
    """Retrieve a single tag set by id

    

    :param id: Id of the tag set to return
    :type id: str

    """
    return web.Response(status=200)


async def tagsets_post(request: web.Request, body) -> web.Response:
    """Create a new tag set

    

    :param body: Tag set to be created
    :type body: dict | bytes

    """
    body = TagSetSubmission.from_dict(body)
    return web.Response(status=200)
