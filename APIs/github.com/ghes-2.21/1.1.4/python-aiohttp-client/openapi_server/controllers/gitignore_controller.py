from typing import List, Dict
from aiohttp import web

from openapi_server.models.gitignore_template import GitignoreTemplate
from openapi_server import util


async def gitignore_get_all_templates(request: web.Request, ) -> web.Response:
    """Get all gitignore templates

    List all templates available to pass as an option when [creating a repository](https://docs.github.com/enterprise-server@2.21/rest/reference/repos#create-a-repository-for-the-authenticated-user).


    """
    return web.Response(status=200)


async def gitignore_get_template(request: web.Request, name) -> web.Response:
    """Get a gitignore template

    The API also allows fetching the source of a single template. Use the raw [media type](https://docs.github.com/enterprise-server@2.21/rest/overview/media-types/) to get the raw contents.

    :param name: 
    :type name: str

    """
    return web.Response(status=200)
