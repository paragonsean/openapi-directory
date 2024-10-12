from typing import List, Dict
from aiohttp import web

from openapi_server.models.pricebycontext_request import PricebycontextRequest
from openapi_server.models.saveprice_request import SavepriceRequest
from openapi_server import util


async def deletebysku_id(request: web.Request, content_type, accept, an, sku_id) -> web.Response:
    """Delete Price by SKU Id

    Delete all prices from an SKU.  &gt; If your account is using Pricing v2, you should avoid using these routes. Please refer directly to the [Pricing v2 API](https://documenter.getpostman.com/view/101975/vtex-pricing-api/6YsWxKT)   &gt; If you are still using Pricing v1, please [check if your store is able to migrate to take advantage of many more features](https://help.vtex.com/en/faq/how-to-migrate-a-store-to-pricing-v2)

    :param content_type: Describes the type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param an: 
    :type an: str
    :param sku_id: 
    :type sku_id: str

    """
    return web.Response(status=200)


async def getallpaged(request: web.Request, content_type, accept, an, page, page_size) -> web.Response:
    """Get all paged prices

    Get all paged prices.  &gt; If your account is using Pricing v2, you should avoid using these routes. Please refer directly to the [Pricing v2 API](https://documenter.getpostman.com/view/101975/vtex-pricing-api/6YsWxKT)   &gt; If you are still using Pricing v1, please [check if your store is able to migrate to take advantage of many more features](https://help.vtex.com/en/faq/how-to-migrate-a-store-to-pricing-v2)

    :param content_type: Describes the type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param an: 
    :type an: str
    :param page: 
    :type page: str
    :param page_size: 
    :type page_size: str

    """
    return web.Response(status=200)


async def pricebycontext(request: web.Request, content_type, accept, an, body) -> web.Response:
    """Get Price by context

    Get price by context.  &gt; If your account is using Pricing v2, you should avoid using these routes. Please refer directly to the [Pricing v2 API](https://documenter.getpostman.com/view/101975/vtex-pricing-api/6YsWxKT)   &gt; If you are still using Pricing v1, please [check if your store is able to migrate to take advantage of many more features](https://help.vtex.com/en/faq/how-to-migrate-a-store-to-pricing-v2)

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param an: 
    :type an: str
    :param body: 
    :type body: dict | bytes

    """
    body = PricebycontextRequest.from_dict(body)
    return web.Response(status=200)


async def pricebysku_id(request: web.Request, content_type, accept, an, sku_id) -> web.Response:
    """Get Price by SKU ID

    Price by SKU ID               &gt; If your account is using Pricing v2, you should avoid using these routes. Please refer directly to the [Pricing v2 API](https://developers.vtex.com/docs/api-reference/pricing-api)

    :param content_type: Describes the type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param an: 
    :type an: str
    :param sku_id: 
    :type sku_id: str

    """
    return web.Response(status=200)


async def pricebysku_idandtrade_policy(request: web.Request, accept, an, content_type, sku_id, trade_policy) -> web.Response:
    """Get Price by SKU ID and Trade Policy

    Retrieve price by SKU ID and Trade Policy.  &gt; If your account is using Pricing v2, you should avoid using these routes. Please refer directly to the [Pricing v2 API](https://documenter.getpostman.com/view/101975/vtex-pricing-api/6YsWxKT)   &gt; If you are still using Pricing v1, please [check if your store is able to migrate to take advantage of many more features](https://help.vtex.com/en/faq/how-to-migrate-a-store-to-pricing-v2)

    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param an: 
    :type an: str
    :param content_type: Describes the type of the content being sent.
    :type content_type: str
    :param sku_id: 
    :type sku_id: str
    :param trade_policy: 
    :type trade_policy: str

    """
    return web.Response(status=200)


async def saveprice(request: web.Request, content_type, accept, an, body) -> web.Response:
    """Save Price

    Save price.  &gt; If your account is using Pricing v2, you should avoid using these routes. Please refer directly to the [Pricing v2 API](https://documenter.getpostman.com/view/101975/vtex-pricing-api/6YsWxKT)   &gt; If you are still using Pricing v1, please [check if your store is able to migrate to take advantage of many more features](https://help.vtex.com/en/faq/how-to-migrate-a-store-to-pricing-v2)

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param an: 
    :type an: str
    :param body: 
    :type body: list | bytes

    """
    body = [SavepriceRequest.from_dict(d) for d in body]
    return web.Response(status=200)
