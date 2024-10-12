from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def delete_api_specification(request: web.Request, id) -> web.Response:
    """delete_api_specification

    Delete an API specification in ReadMe

    :param id: ID of the API specification. The unique ID for each API can be found by navigating to your **API Definitions** page.
    :type id: str

    """
    return web.Response(status=200)


async def get_api_specification(request: web.Request, x_readme_version, per_page=None, page=None) -> web.Response:
    """get_api_specification

    Get API specification metadata

    :param x_readme_version: Version number of your docs project, for example, v3.0. To see all valid versions for your docs project call https://docs.readme.com/developers/reference/version#getversions.
    :type x_readme_version: str
    :param per_page: Number of items to include in pagination (up to 100, defaults to 10)
    :type per_page: int
    :param page: Used to specify further pages (starts at 1)
    :type page: int

    """
    return web.Response(status=200)


async def update_api_specification(request: web.Request, id, spec=None) -> web.Response:
    """update_api_specification

    Update an API specification in ReadMe

    :param id: ID of the API specification. The unique ID for each API can be found by navigating to your **API Definitions** page.
    :type id: str
    :param spec: OpenAPI/Swagger file
    :type spec: str

    """
    return web.Response(status=200)


async def upload_api_specification(request: web.Request, x_readme_version, spec=None) -> web.Response:
    """upload_api_specification

    Upload an API specification to ReadMe. Or, to use a newer solution see https://docs.readme.com/guides/docs/automatically-sync-api-specification-with-github

    :param x_readme_version: Version number of your docs project, for example, v3.0. To see all valid versions for your docs project call https://docs.readme.com/developers/reference/version#getversions.
    :type x_readme_version: str
    :param spec: OpenAPI/Swagger file
    :type spec: str

    """
    return web.Response(status=200)
