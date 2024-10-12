from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.result import Result
from openapi_server.models.styles import Styles
from openapi_server.models.upload_request import UploadRequest
from openapi_server.models.upload_response import UploadResponse
from openapi_server import util


async def noauth_result_get(request: web.Request, submission_id=None) -> web.Response:
    """noauth_result_get

    

    :param submission_id: 
    :type submission_id: str

    """
    return web.Response(status=200)


async def noauth_styles_get(request: web.Request, ) -> web.Response:
    """noauth_styles_get

    


    """
    return web.Response(status=200)


async def noauth_upload_post(request: web.Request, upload_request) -> web.Response:
    """noauth_upload_post

    

    :param upload_request: 
    :type upload_request: dict | bytes

    """
    upload_request = UploadRequest.from_dict(upload_request)
    return web.Response(status=200)
