from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_shop_script_tag200_response import CreateShopScriptTag200Response
from openapi_server.models.create_shop_script_tag_request import CreateShopScriptTagRequest
from openapi_server.models.get_shop_script_tags200_response import GetShopScriptTags200Response
from openapi_server import util


async def create_shop_script_tag(request: web.Request, body=None) -> web.Response:
    """スクリプトタグの作成

    

    :param body: 作成するスクリプトタグの情報
    :type body: dict | bytes

    """
    body = CreateShopScriptTagRequest.from_dict(body)
    return web.Response(status=200)


async def delete_script_tag(request: web.Request, script_tag_id) -> web.Response:
    """スクリプトタグの削除

    

    :param script_tag_id: スクリプトタグID
    :type script_tag_id: int

    """
    return web.Response(status=200)


async def get_shop_script_tag(request: web.Request, script_tag_id) -> web.Response:
    """スクリプトタグの取得

    

    :param script_tag_id: スクリプトタグID
    :type script_tag_id: int

    """
    return web.Response(status=200)


async def get_shop_script_tags(request: web.Request, ) -> web.Response:
    """スクリプトタグの取得

    


    """
    return web.Response(status=200)


async def update_shop_script_tag(request: web.Request, script_tag_id, body=None) -> web.Response:
    """スクリプトタグの更新

    

    :param script_tag_id: スクリプトタグID
    :type script_tag_id: int
    :param body: 作成するスクリプトタグの情報
    :type body: dict | bytes

    """
    body = CreateShopScriptTagRequest.from_dict(body)
    return web.Response(status=200)
