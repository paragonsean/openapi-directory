from typing import List, Dict
from aiohttp import web

from openapi_server.models.translator import Translator
from openapi_server import util


async def setup_translator_get(request: web.Request, ) -> web.Response:
    """Returns a list of translators

    Returns a list of translators you&#39;ve previously created. The translators are returned in sorted order, with the most recent translator appearing first.


    """
    return web.Response(status=200)


async def setup_translator_id_delete(request: web.Request, id) -> web.Response:
    """Delete a translator

    Deletes the specified translator.

    :param id: Translator ID.
    :type id: str

    """
    return web.Response(status=200)


async def setup_translator_id_get(request: web.Request, id) -> web.Response:
    """Retrieve an existing translator

    Retrieves the details of an existing translator. You need only supply the unique translator identifier that was returned upon translator creation.

    :param id: Translator ID.
    :type id: str

    """
    return web.Response(status=200)


async def setup_translator_post(request: web.Request, ) -> web.Response:
    """Create or update a translator

    Creates or updates the specified translator. Any parameters not provided will be left unchanged.


    """
    return web.Response(status=200)
