from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_project_alt1_request import CreateProjectAlt1Request
from openapi_server.models.error import Error
from openapi_server.models.project import Project
from openapi_server import util


async def create_project(request: web.Request, user_id, body) -> web.Response:
    """Create a project

    This method creates a new project for the specified user.

    :param user_id: The ID of the user.
    :type user_id: 
    :param body: 
    :type body: dict | bytes

    """
    body = CreateProjectAlt1Request.from_dict(body)
    return web.Response(status=200)


async def create_project_alt1(request: web.Request, body) -> web.Response:
    """Create a project

    This method creates a new project for the specified user.

    :param body: 
    :type body: dict | bytes

    """
    body = CreateProjectAlt1Request.from_dict(body)
    return web.Response(status=200)


async def delete_project(request: web.Request, project_id, user_id, should_delete_clips=None) -> web.Response:
    """Delete a project

    This method deletes a project and optionally also the videos that it contains.

    :param project_id: The ID of the project.
    :type project_id: 
    :param user_id: The ID of the user.
    :type user_id: 
    :param should_delete_clips: Whether to delete all the videos in the project along with the project itself.
    :type should_delete_clips: bool

    """
    return web.Response(status=200)


async def delete_project_alt1(request: web.Request, project_id, should_delete_clips=None) -> web.Response:
    """Delete a project

    This method deletes a project and optionally also the videos that it contains.

    :param project_id: The ID of the project.
    :type project_id: 
    :param should_delete_clips: Whether to delete all the videos in the project along with the project itself.
    :type should_delete_clips: bool

    """
    return web.Response(status=200)


async def edit_project(request: web.Request, project_id, user_id, body) -> web.Response:
    """Edit a project

    This method edits an existing project.

    :param project_id: The ID of the project.
    :type project_id: 
    :param user_id: The ID of the user.
    :type user_id: 
    :param body: 
    :type body: dict | bytes

    """
    body = CreateProjectAlt1Request.from_dict(body)
    return web.Response(status=200)


async def edit_project_alt1(request: web.Request, project_id, body) -> web.Response:
    """Edit a project

    This method edits an existing project.

    :param project_id: The ID of the project.
    :type project_id: 
    :param body: 
    :type body: dict | bytes

    """
    body = CreateProjectAlt1Request.from_dict(body)
    return web.Response(status=200)


async def get_project(request: web.Request, project_id, user_id) -> web.Response:
    """Get a specific project

    This method gets a single project that belongs to the specified user.

    :param project_id: The ID of the project.
    :type project_id: 
    :param user_id: The ID of the user.
    :type user_id: 

    """
    return web.Response(status=200)


async def get_project_alt1(request: web.Request, project_id) -> web.Response:
    """Get a specific project

    This method gets a single project that belongs to the specified user.

    :param project_id: The ID of the project.
    :type project_id: 

    """
    return web.Response(status=200)


async def get_projects(request: web.Request, user_id, direction=None, page=None, per_page=None, sort=None) -> web.Response:
    """Get all the projects that belong to a user

    This method gets all the projects that belong to the specified user.

    :param user_id: The ID of the user.
    :type user_id: 
    :param direction: The sort direction of the results.
    :type direction: str
    :param page: The page number of the results to show.
    :type page: 
    :param per_page: The number of items to show on each page of results, up to a maximum of 100.
    :type per_page: 
    :param sort: The way to sort the results.
    :type sort: str

    """
    return web.Response(status=200)


async def get_projects_alt1(request: web.Request, direction=None, page=None, per_page=None, sort=None) -> web.Response:
    """Get all the projects that belong to a user

    This method gets all the projects that belong to the specified user.

    :param direction: The sort direction of the results.
    :type direction: str
    :param page: The page number of the results to show.
    :type page: 
    :param per_page: The number of items to show on each page of results, up to a maximum of 100.
    :type per_page: 
    :param sort: The way to sort the results.
    :type sort: str

    """
    return web.Response(status=200)
