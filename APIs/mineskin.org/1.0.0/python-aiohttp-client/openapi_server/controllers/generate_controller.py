from typing import List, Dict
from aiohttp import web

from openapi_server.models.generate_upload_post200_response import GenerateUploadPost200Response
from openapi_server.models.generate_upload_post400_response import GenerateUploadPost400Response
from openapi_server.models.generate_upload_post429_response import GenerateUploadPost429Response
from openapi_server.models.generate_url_post_request import GenerateUrlPostRequest
from openapi_server.models.generate_user_post_request import GenerateUserPostRequest
from openapi_server import util


async def generate_upload_post(request: web.Request, user_agent, model=None, name=None, variant=None, visibility=None, file=None) -> web.Response:
    """generate_upload_post

    

    :param user_agent: Custom User-Agent for your application, see [user-agent.dev](https://user-agent.dev/) for implementation examples
    :type user_agent: str
    :param model: 
    :type model: str
    :param name: 
    :type name: str
    :param variant: Skin variant - automatically determined based on the image if not specified
    :type variant: str
    :param visibility: Visibility of the generated skin. 0 for public, 1 for private
    :type visibility: int
    :param file: 
    :type file: str

    """
    return web.Response(status=200)


async def generate_url_post(request: web.Request, user_agent, body) -> web.Response:
    """generate_url_post

    

    :param user_agent: Custom User-Agent for your application, see [user-agent.dev](https://user-agent.dev/) for implementation examples
    :type user_agent: str
    :param body: 
    :type body: dict | bytes

    """
    body = GenerateUrlPostRequest.from_dict(body)
    return web.Response(status=200)


async def generate_user_post(request: web.Request, user_agent, body) -> web.Response:
    """generate_user_post

    

    :param user_agent: Custom User-Agent for your application, see [user-agent.dev](https://user-agent.dev/) for implementation examples
    :type user_agent: str
    :param body: 
    :type body: dict | bytes

    """
    body = GenerateUserPostRequest.from_dict(body)
    return web.Response(status=200)
