from typing import List, Dict
from aiohttp import web

from openapi_server.models.dependencies_out import DependenciesOut
from openapi_server.models.entities_out import EntitiesOut
from openapi_server.models.http_validation_error import HTTPValidationError
from openapi_server.models.sentence_dependencies_out import SentenceDependenciesOut
from openapi_server.models.user_request_in import UserRequestIn
from openapi_server.models.version_out import VersionOut
from openapi_server import util


async def read_dependencies_v1_en_core_web_sm_dependencies_post(request: web.Request, body) -> web.Response:
    """Read Dependencies

    

    :param body: 
    :type body: dict | bytes

    """
    body = UserRequestIn.from_dict(body)
    return web.Response(status=200)


async def read_entities_v1_en_core_web_sm_entities_post(request: web.Request, body) -> web.Response:
    """Read Entities

    

    :param body: 
    :type body: dict | bytes

    """
    body = UserRequestIn.from_dict(body)
    return web.Response(status=200)


async def read_root_v1_en_core_web_sm_get(request: web.Request, ) -> web.Response:
    """Read Root

    


    """
    return web.Response(status=200)


async def read_sentence_dependencies_v1_en_core_web_sm_sentence_dependencies_post(request: web.Request, body) -> web.Response:
    """Read Sentence Dependencies

    

    :param body: 
    :type body: dict | bytes

    """
    body = UserRequestIn.from_dict(body)
    return web.Response(status=200)


async def read_version_v1_en_core_web_sm_version_get(request: web.Request, ) -> web.Response:
    """Read Version

    


    """
    return web.Response(status=200)
