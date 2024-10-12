from typing import List, Dict
from aiohttp import web

from openapi_server.models.account_style_guide_upload_request import AccountStyleGuideUploadRequest
from openapi_server.models.error import Error
from openapi_server.models.operation_status import OperationStatus
from openapi_server.models.style_guide import StyleGuide
from openapi_server.models.style_guide_list import StyleGuideList
from openapi_server.models.style_guide_upload_request import StyleGuideUploadRequest
from openapi_server import util


async def create_style_guide(request: web.Request, project_id, body=None) -> web.Response:
    """Upload a new style guide

    Upload a new style guide

    :param project_id: Project ID
    :type project_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = StyleGuideUploadRequest.from_dict(body)
    return web.Response(status=200)


async def delete_style_guide(request: web.Request, project_id, style_guide_id) -> web.Response:
    """Delete a style guide

    Delete the existing style guide from the project.

    :param project_id: Project ID
    :type project_id: int
    :param style_guide_id: Style Guide ID
    :type style_guide_id: int

    """
    return web.Response(status=200)


async def download_global_style_guide(request: web.Request, ) -> web.Response:
    """Download account style guide

    Download your account&#39;s global style guide. This endpoint is available only for corporate account customers. This style guide will be automatically attached to each new project under your account.


    """
    return web.Response(status=200)


async def download_style_guide(request: web.Request, project_id, style_guide_id) -> web.Response:
    """Download a style guide

    Download a previously uploaded style guide file.

    :param project_id: Project ID
    :type project_id: int
    :param style_guide_id: Style Guide ID
    :type style_guide_id: int

    """
    return web.Response(status=200)


async def get_style_guide(request: web.Request, project_id, style_guide_id, _with=None) -> web.Response:
    """View a style guide

    View the details of a style guide uploaded to a project

    :param project_id: Project ID
    :type project_id: int
    :param style_guide_id: Style Guide ID
    :type style_guide_id: int
    :param _with: Attach further information. Possible values &#39;preview&#39; to fetch temporary preview URLs. This is NOT recommended to be used with list calls. Only use with[]&#x3D;preview for single document/style guide calls.
    :type _with: List[str]

    """
    return web.Response(status=200)


async def get_style_guides(request: web.Request, project_id, _with=None) -> web.Response:
    """View style guides

    View a list of style guides in your project.

    :param project_id: Project ID
    :type project_id: int
    :param _with: Attach further information. Possible values &#39;preview&#39; to fetch temporary preview URLs. This is NOT recommended to be used with list calls. Only use with[]&#x3D;preview for single document/style guide calls.
    :type _with: List[str]

    """
    return web.Response(status=200)


async def update_global_style_guide(request: web.Request, body=None) -> web.Response:
    """Create or update the account style guide

    Update your corporate account&#39;s global style guide. This endpoint is available only for corporate account customers. This style guide will be automatically attached to each new project under your account.

    :param body: 
    :type body: dict | bytes

    """
    body = AccountStyleGuideUploadRequest.from_dict(body)
    return web.Response(status=200)


async def update_style_guide(request: web.Request, project_id, style_guide_id, body=None) -> web.Response:
    """Update a style guide

    Update the existing style guide in the project. Public users are allowed to have only 1 style guide per project and file name and contents will replaced with the new style guide that you are uploading via this endpoint.

    :param project_id: Project ID
    :type project_id: int
    :param style_guide_id: Style guide ID
    :type style_guide_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = StyleGuideUploadRequest.from_dict(body)
    return web.Response(status=200)
