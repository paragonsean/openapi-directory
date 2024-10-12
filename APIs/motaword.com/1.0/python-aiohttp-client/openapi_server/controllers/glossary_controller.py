from typing import List, Dict
from aiohttp import web

from openapi_server.models.account_glossary_upload_request import AccountGlossaryUploadRequest
from openapi_server.models.error import Error
from openapi_server.models.glossary import Glossary
from openapi_server.models.glossary_list import GlossaryList
from openapi_server.models.glossary_upload_request import GlossaryUploadRequest
from openapi_server.models.operation_status import OperationStatus
from openapi_server import util


async def create_glossary(request: web.Request, project_id, body=None) -> web.Response:
    """Upload a glossary file

    Upload a new glossary file to your project to be used during translation. Glossaries can be CSV or TBX files.

    :param project_id: Project ID
    :type project_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = GlossaryUploadRequest.from_dict(body)
    return web.Response(status=200)


async def delete_glossary(request: web.Request, project_id, glossary_id) -> web.Response:
    """Delete a glossary

    Delete the existing glossary from the project.

    :param project_id: Project ID
    :type project_id: int
    :param glossary_id: Glossary ID
    :type glossary_id: int

    """
    return web.Response(status=200)


async def download_global_glossary(request: web.Request, ) -> web.Response:
    """Download account glossary.

    Download your corporate account&#39;s global glossary. This endpoint is available only for corporate account customers. This glossary will be automatically attached to each new project under your account.


    """
    return web.Response(status=200)


async def download_glossary(request: web.Request, project_id, glossary_id) -> web.Response:
    """Download a glossary

    Download a previously uploaded glossary file.

    :param project_id: Project ID
    :type project_id: int
    :param glossary_id: Glossary ID
    :type glossary_id: int

    """
    return web.Response(status=200)


async def get_glossaries(request: web.Request, project_id) -> web.Response:
    """View glossaries

    View a list of glossaries previously uploaded to the project.

    :param project_id: Project ID
    :type project_id: int

    """
    return web.Response(status=200)


async def get_glossary(request: web.Request, project_id, glossary_id) -> web.Response:
    """View a glossary

    View the details of a glossary file uploaded to a project.

    :param project_id: Project ID
    :type project_id: int
    :param glossary_id: Glossary ID
    :type glossary_id: int

    """
    return web.Response(status=200)


async def update_global_glossary(request: web.Request, body=None) -> web.Response:
    """Create or update the account glossary

    Update your corporate account&#39;s global glossary. This endpoint is available only for corporate account customers. This glossary will be automatically attached to each new project under your account.

    :param body: 
    :type body: dict | bytes

    """
    body = AccountGlossaryUploadRequest.from_dict(body)
    return web.Response(status=200)


async def update_glossary(request: web.Request, project_id, glossary_id, body=None) -> web.Response:
    """Update a glossary

    Update the existing glossary file in the project. Public users are allowed to have only 1 glossary per project and file name and contents will replaced with the new glossary file that you are uploading via this endpoint.

    :param project_id: Project ID
    :type project_id: int
    :param glossary_id: Glossary ID
    :type glossary_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = GlossaryUploadRequest.from_dict(body)
    return web.Response(status=200)
