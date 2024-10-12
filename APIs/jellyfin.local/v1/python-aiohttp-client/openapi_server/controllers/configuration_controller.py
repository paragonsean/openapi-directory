from typing import List, Dict
from aiohttp import web

from openapi_server.models.media_encoder_path_dto import MediaEncoderPathDto
from openapi_server.models.metadata_options import MetadataOptions
from openapi_server.models.server_configuration import ServerConfiguration
from openapi_server import util


async def get_configuration(request: web.Request, ) -> web.Response:
    """Gets application configuration.

    


    """
    return web.Response(status=200)


async def get_default_metadata_options(request: web.Request, ) -> web.Response:
    """Gets a default MetadataOptions object.

    


    """
    return web.Response(status=200)


async def get_named_configuration(request: web.Request, key) -> web.Response:
    """Gets a named configuration.

    

    :param key: Configuration key.
    :type key: str

    """
    return web.Response(status=200)


async def update_configuration(request: web.Request, body) -> web.Response:
    """Updates application configuration.

    

    :param body: Configuration.
    :type body: dict | bytes

    """
    body = ServerConfiguration.from_dict(body)
    return web.Response(status=200)


async def update_media_encoder_path(request: web.Request, body) -> web.Response:
    """Updates the path to the media encoder.

    

    :param body: Media encoder path form body.
    :type body: dict | bytes

    """
    body = MediaEncoderPathDto.from_dict(body)
    return web.Response(status=200)


async def update_named_configuration(request: web.Request, key) -> web.Response:
    """Updates named configuration.

    

    :param key: Configuration key.
    :type key: str

    """
    return web.Response(status=200)
