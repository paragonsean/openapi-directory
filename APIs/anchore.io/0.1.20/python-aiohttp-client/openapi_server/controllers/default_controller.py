from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_error_response import ApiErrorResponse
from openapi_server.models.file_content_search_result import FileContentSearchResult
from openapi_server.models.retrieved_file import RetrievedFile
from openapi_server.models.secret_search_result import SecretSearchResult
from openapi_server.models.service_version import ServiceVersion
from openapi_server.models.token_response import TokenResponse
from openapi_server import util


async def get_oauth_token(request: web.Request, client_id=None, grant_type=None, password=None, username=None) -> web.Response:
    """get_oauth_token

    Request a jwt token for subsequent operations, this request is authenticated with normal HTTP auth

    :param client_id: The type of client used for the OAuth token
    :type client_id: str
    :param grant_type: OAuth Grant type for token
    :type grant_type: str
    :param password: Password for corresponding user
    :type password: str
    :param username: User to assign OAuth token to
    :type username: str

    """
    return web.Response(status=200)


async def health_check(request: web.Request, ) -> web.Response:
    """health_check

    Health check, returns 200 and no body if service is running


    """
    return web.Response(status=200)


async def list_file_content_search_results(request: web.Request, image_digest) -> web.Response:
    """Return a list of analyzer artifacts of the specified type

    

    :param image_digest: 
    :type image_digest: str

    """
    return web.Response(status=200)


async def list_retrieved_files(request: web.Request, image_digest) -> web.Response:
    """Return a list of analyzer artifacts of the specified type

    

    :param image_digest: 
    :type image_digest: str

    """
    return web.Response(status=200)


async def list_secret_search_results(request: web.Request, image_digest) -> web.Response:
    """Return a list of analyzer artifacts of the specified type

    

    :param image_digest: 
    :type image_digest: str

    """
    return web.Response(status=200)


async def ping(request: web.Request, ) -> web.Response:
    """ping

    Simple status check


    """
    return web.Response(status=200)


async def version_check(request: web.Request, ) -> web.Response:
    """version_check

    Returns the version object for the service, including db schema version info


    """
    return web.Response(status=200)
