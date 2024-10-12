from typing import List, Dict
from aiohttp import web

from openapi_server.models.meshery_pattern import MesheryPattern
from openapi_server.models.patterns_api_response import PatternsAPIResponse
from openapi_server import util


async def id_delete_deploy_pattern(request: web.Request, ) -> web.Response:
    """Handle DELETE request for Pattern Deploy

    Delete a deployed pattern with the request


    """
    return web.Response(status=200)


async def id_delete_meshery_pattern(request: web.Request, id) -> web.Response:
    """Handle Delete for a Meshery Pattern

    Deletes a meshery pattern with ID: id

    :param id: id for a specific
    :type id: str
    :type id: str

    """
    return web.Response(status=200)


async def id_get_meshery_pattern(request: web.Request, id) -> web.Response:
    """Handle GET for a Meshery Pattern

    Fetches the pattern with the given id

    :param id: id for a specific
    :type id: str
    :type id: str

    """
    return web.Response(status=200)


async def id_get_pattern_files(request: web.Request, ) -> web.Response:
    """Handle GET request for patterns

    Returns the list of all the patterns saved by the current user This will return all the patterns with their details


    """
    return web.Response(status=200)


async def id_getoam_meshery_pattern(request: web.Request, type) -> web.Response:
    """Handles the get requests for the OAM objects

    Getting list of workloads/traits/scopes  {type} being of either trait, scope, workload; registration of adapter capabilities.

    :param type: Automatically added
    :type type: str

    """
    return web.Response(status=200)


async def id_post_deploy_pattern(request: web.Request, upload_yaml_yml_file=None) -> web.Response:
    """Handle POST request for Pattern Deploy

    Deploy an attached pattern with the request

    :param upload_yaml_yml_file: 
    :type upload_yaml_yml_file: str

    """
    return web.Response(status=200)


async def id_post_pattern_file(request: web.Request, ) -> web.Response:
    """Handle POST requests for patterns

    Edit/update a meshery pattern


    """
    return web.Response(status=200)


async def id_postoam_meshery_pattern(request: web.Request, type) -> web.Response:
    """Handles registering OMA objects

    Adding a workload/trait/scope  {type} being of either trait, scope, workload; registration of adapter capabilities.

    :param type: Automatically added
    :type type: str

    """
    return web.Response(status=200)
