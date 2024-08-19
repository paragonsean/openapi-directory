from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_account_settings_image_request_body import CreateAccountSettingsImageRequestBody
from openapi_server.models.error_response_body import ErrorResponseBody
from openapi_server.models.get_account_settings_images_response_body import GetAccountSettingsImagesResponseBody
from openapi_server.models.get_account_settings_response_body import GetAccountSettingsResponseBody
from openapi_server.models.list_account_settings_images_response_body import ListAccountSettingsImagesResponseBody
from openapi_server.models.update_account_settings_image_request_body import UpdateAccountSettingsImageRequestBody
from openapi_server import util


async def create_account_image(request: web.Request, body) -> web.Response:
    """Create an Account Image

    Create an Account Image

    :param body: 
    :type body: dict | bytes

    """
    body = CreateAccountSettingsImageRequestBody.from_dict(body)
    return web.Response(status=200)


async def delete_account_image_by_id(request: web.Request, label_image_id) -> web.Response:
    """Delete Account Image By Id

    Delete Account Image By Id

    :param label_image_id: Label Image Id
    :type label_image_id: str

    """
    return web.Response(status=200)


async def get_account_settings_images_by_id(request: web.Request, label_image_id) -> web.Response:
    """Get Account Image By ID

    Retrieve information for an account image.

    :param label_image_id: Label Image Id
    :type label_image_id: str

    """
    return web.Response(status=200)


async def list_account_images(request: web.Request, ) -> web.Response:
    """List Account Images

    List all account images for the ShipEngine account


    """
    return web.Response(status=200)


async def list_account_settings(request: web.Request, ) -> web.Response:
    """List Account Settings

    List all account settings for the ShipEngine account


    """
    return web.Response(status=200)


async def update_account_settings_images_by_id(request: web.Request, label_image_id, body) -> web.Response:
    """Update Account Image By ID

    Update information for an account image.

    :param label_image_id: Label Image Id
    :type label_image_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateAccountSettingsImageRequestBody.from_dict(body)
    return web.Response(status=200)
