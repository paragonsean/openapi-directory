from typing import List, Dict
from aiohttp import web

from openapi_server.models.project_creation_write import ProjectCreationWrite
from openapi_server.models.project_list import ProjectList
from openapi_server.models.project_read import ProjectRead
from openapi_server.models.project_write import ProjectWrite
from openapi_server import util


async def delete_project_item(request: web.Request, id) -> web.Response:
    """Removes the Project resource.

    

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def get_project_collection(request: web.Request, ) -> web.Response:
    """Retrieves the collection of Project resources.

    


    """
    return web.Response(status=200)


async def get_project_item(request: web.Request, id) -> web.Response:
    """Retrieves a Project resource.

    

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def post_project_collection(request: web.Request, project=None) -> web.Response:
    """Creates a Project resource.

    

    :param project: The new Project resource
    :type project: dict | bytes

    """
    project = ProjectCreationWrite.from_dict(project)
    return web.Response(status=200)


async def put_project_item(request: web.Request, id, project=None) -> web.Response:
    """Replaces the Project resource.

    

    :param id: 
    :type id: str
    :param project: The updated Project resource
    :type project: dict | bytes

    """
    project = ProjectWrite.from_dict(project)
    return web.Response(status=200)
