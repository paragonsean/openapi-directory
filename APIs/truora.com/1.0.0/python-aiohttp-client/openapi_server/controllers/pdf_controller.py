from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def create_pdf(request: web.Request, check_id) -> web.Response:
    """Create PDF

    Creates a PDF containing the background check results.

    :param check_id: ID of the check
    :type check_id: str

    """
    return web.Response(status=200)


async def get_pdf(request: web.Request, check_id, lang=None) -> web.Response:
    """Get PDF

    Downloads the PDF in the specified language, Spanish by default.

    :param check_id: ID of the check
    :type check_id: str
    :param lang: Used to specify the language for the PDF, if not specified the PDF will be downloaded in Spanish.
    :type lang: str

    """
    return web.Response(status=200)
