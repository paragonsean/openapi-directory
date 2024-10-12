from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_tag_model import CreateTagModel
from openapi_server.models.setting_model import SettingModel
from openapi_server.models.setting_model_haljson import SettingModelHaljson
from openapi_server.models.tag_model import TagModel
from openapi_server.models.tag_model_haljson import TagModelHaljson
from openapi_server.models.update_tag_model import UpdateTagModel
from openapi_server import util


async def create_tag(request: web.Request, product_id, body) -> web.Response:
    """Create Tag

    This endpoint creates a new Tag in a specified Product  identified by the &#x60;productId&#x60; parameter, which can be obtained from the [List Products](#operation/get-products) endpoint.

    :param product_id: The identifier of the Organization.
    :type product_id: str
    :type product_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateTagModel.from_dict(body)
    return web.Response(status=200)


async def delete_tag(request: web.Request, tag_id) -> web.Response:
    """Delete Tag

    This endpoint deletes a Tag identified by the &#x60;tagId&#x60; parameter. To remove a Tag from a Feature Flag or Setting use the [Update Flag](#operation/update-setting) endpoint.

    :param tag_id: The identifier of the Tag.
    :type tag_id: int

    """
    return web.Response(status=200)


async def get_settings_by_tag(request: web.Request, tag_id) -> web.Response:
    """List Settings by Tag

    This endpoint returns the list of the Settings that  has the specified Tag, identified by the &#x60;tagId&#x60; parameter.

    :param tag_id: The identifier of the Tag.
    :type tag_id: int

    """
    return web.Response(status=200)


async def get_tag(request: web.Request, tag_id) -> web.Response:
    """Get Tag

    This endpoint returns the metadata of a Tag  identified by the &#x60;tagId&#x60;.

    :param tag_id: The identifier of the Tag.
    :type tag_id: int

    """
    return web.Response(status=200)


async def get_tags(request: web.Request, product_id) -> web.Response:
    """List Tags

    This endpoint returns the list of the Tags in a  specified Product, identified by the &#x60;productId&#x60; parameter.

    :param product_id: The identifier of the Product.
    :type product_id: str
    :type product_id: str

    """
    return web.Response(status=200)


async def update_tag(request: web.Request, tag_id, body) -> web.Response:
    """Update Tag

    This endpoint updates a Tag identified by the &#x60;tagId&#x60; parameter.

    :param tag_id: The identifier of the Tag.
    :type tag_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateTagModel.from_dict(body)
    return web.Response(status=200)
