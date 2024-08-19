from typing import List, Dict
from aiohttp import web

from openapi_server.models.markdown_option import MarkdownOption
from openapi_server.models.markup_option import MarkupOption
from openapi_server.models.node_info import NodeInfo
from openapi_server.models.server_version import ServerVersion
from openapi_server import util


async def get_node_info(request: web.Request, ) -> web.Response:
    """Returns the nodeinfo of the Gitea application

    


    """
    return web.Response(status=200)


async def get_signing_key(request: web.Request, ) -> web.Response:
    """Get default signing-key.gpg

    


    """
    return web.Response(status=200)


async def get_version(request: web.Request, ) -> web.Response:
    """Returns the version of the Gitea application

    


    """
    return web.Response(status=200)


async def render_markdown(request: web.Request, body=None) -> web.Response:
    """Render a markdown document as HTML

    

    :param body: 
    :type body: dict | bytes

    """
    body = MarkdownOption.from_dict(body)
    return web.Response(status=200)


async def render_markdown_raw(request: web.Request, body) -> web.Response:
    """Render raw markdown as HTML

    

    :param body: Request body to render
    :type body: str

    """
    return web.Response(status=200)


async def render_markup(request: web.Request, body=None) -> web.Response:
    """Render a markup document as HTML

    

    :param body: 
    :type body: dict | bytes

    """
    body = MarkupOption.from_dict(body)
    return web.Response(status=200)
