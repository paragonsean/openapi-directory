from typing import List, Dict
from aiohttp import web

from openapi_server.models.general_api_settings import GeneralAPISettings
from openapi_server.models.general_attachment_settings import GeneralAttachmentSettings
from openapi_server.models.general_repo_settings import GeneralRepoSettings
from openapi_server.models.general_ui_settings import GeneralUISettings
from openapi_server import util


async def get_general_api_settings(request: web.Request, ) -> web.Response:
    """Get instance&#39;s global settings for api

    


    """
    return web.Response(status=200)


async def get_general_attachment_settings(request: web.Request, ) -> web.Response:
    """Get instance&#39;s global settings for Attachment

    


    """
    return web.Response(status=200)


async def get_general_repository_settings(request: web.Request, ) -> web.Response:
    """Get instance&#39;s global settings for repositories

    


    """
    return web.Response(status=200)


async def get_general_ui_settings(request: web.Request, ) -> web.Response:
    """Get instance&#39;s global settings for ui

    


    """
    return web.Response(status=200)
