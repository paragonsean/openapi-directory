from typing import List, Dict
from aiohttp import web

from openapi_server.models.applications_api_response import ApplicationsAPIResponse
from openapi_server.models.meshery_application import MesheryApplication
from openapi_server import util


async def id_delete_application_file(request: web.Request, ) -> web.Response:
    """Handle DELETE request for Application File Deploy

    Delete a deployed application file with the request


    """
    return web.Response(status=200)


async def id_delete_meshery_application_file(request: web.Request, id) -> web.Response:
    """Handle Delete for a Meshery Application File

    Deletes a meshery application file with ID: id

    :param id: id for a specific
    :type id: str
    :type id: str

    """
    return web.Response(status=200)


async def id_get_application_file_request(request: web.Request, ) -> web.Response:
    """Handle GET request for Application Files

    Returns requests for all Meshery Applications


    """
    return web.Response(status=200)


async def id_get_meshery_application(request: web.Request, id) -> web.Response:
    """Handle GET request for Meshery Application with the given id

    Fetches the list of all applications saved by the current user

    :param id: id for a specific
    :type id: str
    :type id: str

    """
    return web.Response(status=200)


async def id_post_application_file_request(request: web.Request, ) -> web.Response:
    """Handle POST request for Application Files

    Save attached Meshery Application File


    """
    return web.Response(status=200)


async def id_post_deploy_application_file(request: web.Request, upload_yaml_yml_file=None) -> web.Response:
    """Handle POST request for Application File Deploy

    Deploy an attached application file with the request

    :param upload_yaml_yml_file: 
    :type upload_yaml_yml_file: str

    """
    return web.Response(status=200)
