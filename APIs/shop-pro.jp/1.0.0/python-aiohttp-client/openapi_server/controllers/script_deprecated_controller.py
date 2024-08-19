from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_script_tag200_response import CreateScriptTag200Response
from openapi_server.models.create_script_tag_request import CreateScriptTagRequest
from openapi_server.models.get_script_tags200_response import GetScriptTags200Response
from openapi_server import util


async def create_script_tag(request: web.Request, body=None) -> web.Response:
    """スクリプトタグの作成

    

    :param body: 作成するスクリプトタグの情報
    :type body: dict | bytes

    """
    body = CreateScriptTagRequest.from_dict(body)
    return web.Response(status=200)


async def get_script_tag(request: web.Request, script_tag_id) -> web.Response:
    """スクリプトタグの取得

    

    :param script_tag_id: スクリプトタグID
    :type script_tag_id: int

    """
    return web.Response(status=200)


async def get_script_tags(request: web.Request, ) -> web.Response:
    """スクリプトタグの取得

    


    """
    return web.Response(status=200)


async def update_script_tag(request: web.Request, script_tag_id, body=None) -> web.Response:
    """スクリプトタグの更新

    

    :param script_tag_id: スクリプトタグID
    :type script_tag_id: int
    :param body: 作成するスクリプトタグの情報
    :type body: dict | bytes

    """
    body = CreateScriptTagRequest.from_dict(body)
    return web.Response(status=200)


async def v1_script_tags_script_tag_id_json_delete(request: web.Request, script_tag_id) -> web.Response:
    """スクリプトタグの削除

    

    :param script_tag_id: スクリプトタグID
    :type script_tag_id: int

    """
    return web.Response(status=200)
