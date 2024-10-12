from typing import List, Dict
from aiohttp import web

from openapi_server.models.custom_vision_error import CustomVisionError
from openapi_server.models.tag import Tag
from openapi_server import util


async def create_tag(request: web.Request, project_id, name, description=None, type=None) -> web.Response:
    """Create a tag for the project.

    

    :param project_id: The project id.
    :type project_id: str
    :type project_id: str
    :param name: The tag name.
    :type name: str
    :param description: Optional description for the tag.
    :type description: str
    :param type: Optional type for the tag.
    :type type: str

    """
    return web.Response(status=200)


async def delete_tag(request: web.Request, project_id, tag_id) -> web.Response:
    """Delete a tag from the project.

    

    :param project_id: The project id.
    :type project_id: str
    :type project_id: str
    :param tag_id: Id of the tag to be deleted.
    :type tag_id: str
    :type tag_id: str

    """
    return web.Response(status=200)


async def get_tag(request: web.Request, project_id, tag_id, iteration_id=None) -> web.Response:
    """Get information about a specific tag.

    

    :param project_id: The project this tag belongs to.
    :type project_id: str
    :type project_id: str
    :param tag_id: The tag id.
    :type tag_id: str
    :type tag_id: str
    :param iteration_id: The iteration to retrieve this tag from. Optional, defaults to current training set.
    :type iteration_id: str
    :type iteration_id: str

    """
    return web.Response(status=200)


async def get_tags(request: web.Request, project_id, iteration_id=None) -> web.Response:
    """Get the tags for a given project and iteration.

    

    :param project_id: The project id.
    :type project_id: str
    :type project_id: str
    :param iteration_id: The iteration id. Defaults to workspace.
    :type iteration_id: str
    :type iteration_id: str

    """
    return web.Response(status=200)


async def update_tag(request: web.Request, project_id, tag_id, body) -> web.Response:
    """Update a tag.

    

    :param project_id: The project id.
    :type project_id: str
    :type project_id: str
    :param tag_id: The id of the target tag.
    :type tag_id: str
    :type tag_id: str
    :param body: The updated tag model.
    :type body: dict | bytes

    """
    body = Tag.from_dict(body)
    return web.Response(status=200)
