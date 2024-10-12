from typing import List, Dict
from aiohttp import web

from openapi_server.models.product_search_who_bought_also_bought200_response_inner import ProductSearchWhoBoughtAlsoBought200ResponseInner
from openapi_server import util


async def product_search_accessories(request: web.Request, accept, content_type, product_id) -> web.Response:
    """Get Product Search of Accessories

    Retrieves general information about the product&#39;s accessories.

    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param content_type: Describes the type of the content being sent.
    :type content_type: str
    :param product_id: Product&#39;s unique identifier
    :type product_id: int

    """
    return web.Response(status=200)


async def product_search_show_together(request: web.Request, accept, content_type, product_id) -> web.Response:
    """Get Product Search of Show Together

    Retrieves general information about the products that are show together with the product in question.

    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param content_type: Describes the type of the content being sent.
    :type content_type: str
    :param product_id: Product&#39;s unique identifier
    :type product_id: int

    """
    return web.Response(status=200)


async def product_search_similars(request: web.Request, accept, content_type, product_id) -> web.Response:
    """Get Product Search of Similars

    Retrieves general information about related product searches.

    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param content_type: Describes the type of the content being sent.
    :type content_type: str
    :param product_id: Product&#39;s unique identifier
    :type product_id: int

    """
    return web.Response(status=200)


async def product_search_suggestions(request: web.Request, accept, content_type, product_id) -> web.Response:
    """Get Product Search of Suggestions

    Retrieves general information about other product suggestions related to the product.

    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param content_type: Describes the type of the content being sent.
    :type content_type: str
    :param product_id: Product&#39;s unique identifier
    :type product_id: int

    """
    return web.Response(status=200)


async def product_search_who_bought_also_bought(request: web.Request, accept, content_type, product_id) -> web.Response:
    """Get Product Search of Who Bought Also Bought

    Retrieves general information about other related products that the user also bought.

    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param content_type: Describes the type of the content being sent.
    :type content_type: str
    :param product_id: Product unique identifier.
    :type product_id: str

    """
    return web.Response(status=200)


async def product_search_who_saw_also_bought(request: web.Request, accept, content_type, product_id) -> web.Response:
    """Get Product Search of Who Saw Also Bought

    Retrieves general information about other related products that the users saw and also bought.

    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param content_type: Describes the type of the content being sent.
    :type content_type: str
    :param product_id: Product unique identifier.
    :type product_id: str

    """
    return web.Response(status=200)


async def product_search_who_saw_also_saw(request: web.Request, accept, content_type, product_id) -> web.Response:
    """Get Product Search of Who Saw Also Saw

    Retrieves general information about other related products that the users also saw.

    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param content_type: Describes the type of the content being sent.
    :type content_type: str
    :param product_id: Product unique identifier.
    :type product_id: int

    """
    return web.Response(status=200)
