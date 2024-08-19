from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_inline_script_tag201_response import CreateInlineScriptTag201Response
from openapi_server.models.create_inline_script_tag_request import CreateInlineScriptTagRequest
from openapi_server.models.get_inline_script_tags200_response import GetInlineScriptTags200Response
from openapi_server import util


async def create_inline_script_tag(request: web.Request, body=None) -> web.Response:
    """インラインスクリプトタグの登録

    

    :param body: 作成するインラインスクリプトタグの情報
    :type body: dict | bytes

    """
    body = CreateInlineScriptTagRequest.from_dict(body)
    return web.Response(status=200)


async def delete_inline_script_tag(request: web.Request, inline_script_tag_id) -> web.Response:
    """インラインスクリプトタグの削除

    

    :param inline_script_tag_id: インラインスクリプトタグID
    :type inline_script_tag_id: int

    """
    return web.Response(status=200)


async def get_inline_script_tag(request: web.Request, inline_script_tag_id) -> web.Response:
    """インラインスクリプトタグの取得

    

    :param inline_script_tag_id: インラインスクリプトタグID
    :type inline_script_tag_id: int

    """
    return web.Response(status=200)


async def get_inline_script_tags(request: web.Request, ) -> web.Response:
    """インラインスクリプトタグの取得

    


    """
    return web.Response(status=200)


async def update_inline_script_tag(request: web.Request, inline_script_tag_id, body=None) -> web.Response:
    """インラインスクリプトタグの更新

    

    :param inline_script_tag_id: インラインスクリプトタグID
    :type inline_script_tag_id: int
    :param body: 更新するスクリプトタグの情報
    :type body: dict | bytes

    """
    body = CreateInlineScriptTagRequest.from_dict(body)
    return web.Response(status=200)
