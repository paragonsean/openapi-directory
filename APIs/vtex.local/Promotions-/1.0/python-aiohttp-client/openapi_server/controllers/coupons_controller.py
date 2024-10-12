from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_rnb_pvt_coupon_post_request import ApiRnbPvtCouponPostRequest
from openapi_server.models.api_rnb_pvt_multiple_coupons_post_request_inner import ApiRnbPvtMultipleCouponsPostRequestInner
from openapi_server.models.getall200_response_inner import Getall200ResponseInner
from openapi_server.models.getarchivedbycouponcode200_response import Getarchivedbycouponcode200Response
from openapi_server.models.getusage200_response import Getusage200Response
from openapi_server.models.massive_generation_request import MassiveGenerationRequest
from openapi_server.models.update_request import UpdateRequest
from openapi_server import util


async def api_rnb_pvt_coupon_post(request: web.Request, content_type, accept, body=None) -> web.Response:
    """Create coupon

    Creates a single new coupon.

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param body: 
    :type body: dict | bytes

    """
    body = ApiRnbPvtCouponPostRequest.from_dict(body)
    return web.Response(status=200)


async def api_rnb_pvt_multiple_coupons_post(request: web.Request, content_type, accept, body=None) -> web.Response:
    """Create multiple coupons

    Creates multiple coupons with different coupon codes. This endpoint has a throttling of 60 requests per minute.

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param body: 
    :type body: list | bytes

    """
    body = [ApiRnbPvtMultipleCouponsPostRequestInner.from_dict(d) for d in body]
    return web.Response(status=200)


async def archivebycouponcode(request: web.Request, content_type, accept, coupon_code) -> web.Response:
    """Archive coupon by coupon code

    Archives a specifc coupon by its coupon code.

    :param content_type: Describes the type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param coupon_code: Coupon Code
    :type coupon_code: str

    """
    return web.Response(status=200)


async def getall(request: web.Request, content_type, accept) -> web.Response:
    """Get all coupons

      &gt; Check the new [Promotions onboarding guide](https://developers.vtex.com/vtex-rest-api/docs/promotions-overview). We created this guide to improve the onboarding experience for developers at VTEX. It assembles all documentation on our Developer Portal about Promotions and is organized by focusing on the developer&#39;s journey.     Retrieves all coupons from an account.

    :param content_type: 
    :type content_type: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
    :type accept: str

    """
    return web.Response(status=200)


async def getarchivedbycouponcode(request: web.Request, content_type, accept, coupon_code) -> web.Response:
    """Get archived coupon by coupon code

    Retrieves a specific archived coupon by its coupon code.

    :param content_type: Describes the type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param coupon_code: Coupon Code
    :type coupon_code: str

    """
    return web.Response(status=200)


async def getbycouponcode(request: web.Request, content_type, accept, coupon_code) -> web.Response:
    """Get coupon by coupon code

    Retrieves a specific coupon by its coupon code.

    :param content_type: Describes the type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param coupon_code: Coupon Code
    :type coupon_code: str

    """
    return web.Response(status=200)


async def getusage(request: web.Request, content_type, accept, coupon_code) -> web.Response:
    """Get coupon usage

    Retrieves information about the coupon usage.

    :param content_type: Describes the type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param coupon_code: Coupon Code
    :type coupon_code: str

    """
    return web.Response(status=200)


async def massive_generation(request: web.Request, content_type, accept, quantity, body) -> web.Response:
    """Coupon Massive Generation

    Generates a massive amount of coupons

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param quantity: Quantity of coupons to generate
    :type quantity: int
    :param body: 
    :type body: dict | bytes

    """
    body = MassiveGenerationRequest.from_dict(body)
    return web.Response(status=200)


async def unarchivebycouponcode(request: web.Request, content_type, accept, coupon_code) -> web.Response:
    """Unarchive coupon by coupon code

    Unarchives a specifc coupon by its coupon code.

    :param content_type: Describes the type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param coupon_code: Coupon Code
    :type coupon_code: str

    """
    return web.Response(status=200)


async def update(request: web.Request, content_type, accept, body) -> web.Response:
    """Update coupon

    Updates information of a specific coupon.

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateRequest.from_dict(body)
    return web.Response(status=200)
