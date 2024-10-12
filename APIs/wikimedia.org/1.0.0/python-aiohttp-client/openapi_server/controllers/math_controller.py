from typing import List, Dict
from aiohttp import web

from openapi_server.models.problem import Problem
from openapi_server import util


async def media_math_check_type_post(request: web.Request, type, q) -> web.Response:
    """Check and normalize a TeX formula.

    Checks the supplied TeX formula for correctness and returns the normalised formula representation as well as information about identifiers. Available types are tex and inline-tex. The response contains the &#x60;x-resource-location&#x60; header which can be used to retrieve the render of the checked formula in one of the supported rendering formats. Just append the value of the header to &#x60;/media/math/{format}/&#x60; and perform a GET request against that URL.  Stability: [stable](https://www.mediawiki.org/wiki/API_versioning#Stable). 

    :param type: The input type of the given formula; can be tex or inline-tex
    :type type: str
    :param q: The formula to check
    :type q: str

    """
    return web.Response(status=200)


async def media_math_formula_hash_get(request: web.Request, hash) -> web.Response:
    """Get a previously-stored formula

    Returns the previously-stored formula via &#x60;/media/math/check/{type}&#x60; for the given hash.  Stability: [stable](https://www.mediawiki.org/wiki/API_versioning#Stable). 

    :param hash: The hash string of the previous POST data
    :type hash: str

    """
    return web.Response(status=200)


async def media_math_render_format_hash_get(request: web.Request, format, hash) -> web.Response:
    """Get rendered formula in the given format.

    Given a request hash, renders a TeX formula into its mathematic representation in the given format. When a request is issued to the &#x60;/media/math/check/{format}&#x60; POST endpoint, the response contains the &#x60;x-resource-location&#x60; header denoting the hash ID of the POST data. Once obtained, this endpoint has to be used to obtain the actual render.  Stability: [stable](https://www.mediawiki.org/wiki/API_versioning#Stable). 

    :param format: The output format; can be svg or mml
    :type format: str
    :param hash: The hash string of the previous POST data
    :type hash: str

    """
    return web.Response(status=200)
