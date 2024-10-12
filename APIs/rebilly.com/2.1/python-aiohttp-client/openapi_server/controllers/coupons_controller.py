from typing import List, Dict
from aiohttp import web

from openapi_server.models.coupon import Coupon
from openapi_server.models.coupon_expiration import CouponExpiration
from openapi_server.models.coupon_redemption import CouponRedemption
from openapi_server.models.error import Error
from openapi_server.models.invalid_error import InvalidError
from openapi_server import util


async def get_coupon(request: web.Request, id, organization_id=None) -> web.Response:
    """Retrieve a coupon

    Retrieve a coupon with specified coupon ID string. 

    :param id: The resource identifier string.
    :type id: str
    :param organization_id: Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    :type organization_id: str

    """
    return web.Response(status=200)


async def get_coupon_collection(request: web.Request, organization_id=None, limit=None, offset=None, filter=None, q=None, sort=None) -> web.Response:
    """Retrieve a list of coupons

    Retrieve a list of coupons. 

    :param organization_id: Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    :type organization_id: str
    :param limit: The collection items limit.
    :type limit: int
    :param offset: The collection items offset.
    :type offset: int
    :param filter: The collection items filter requires a special format. Use \&quot;,\&quot; for multiple allowed values.  Use \&quot;;\&quot; for multiple fields. See the [filter guide](https://api-reference.rebilly.com/#section/Using-filter-with-collections) for more options and examples about this format. 
    :type filter: str
    :param q: The partial search of the text fields.
    :type q: str
    :param sort: The collection items sort field and order (prefix with \&quot;-\&quot; for descending sort).
    :type sort: List[str]

    """
    return web.Response(status=200)


async def get_coupon_redemption(request: web.Request, id, organization_id=None) -> web.Response:
    """Retrieve a coupon redemption with specified identifier string

    

    :param id: The resource identifier string.
    :type id: str
    :param organization_id: Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    :type organization_id: str

    """
    return web.Response(status=200)


async def get_coupon_redemption_collection(request: web.Request, organization_id=None, limit=None, offset=None, filter=None, q=None, sort=None) -> web.Response:
    """Retrieve a list of coupon redemptions

    

    :param organization_id: Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    :type organization_id: str
    :param limit: The collection items limit.
    :type limit: int
    :param offset: The collection items offset.
    :type offset: int
    :param filter: The collection items filter requires a special format. Use \&quot;,\&quot; for multiple allowed values.  Use \&quot;;\&quot; for multiple fields. See the [filter guide](https://api-reference.rebilly.com/#section/Using-filter-with-collections) for more options and examples about this format. 
    :type filter: str
    :param q: The partial search of the text fields.
    :type q: str
    :param sort: The collection items sort field and order (prefix with \&quot;-\&quot; for descending sort).
    :type sort: List[str]

    """
    return web.Response(status=200)


async def post_coupon(request: web.Request, body, organization_id=None) -> web.Response:
    """Create a coupon

    Create a coupon. 

    :param body: Coupon resource.
    :type body: dict | bytes
    :param organization_id: Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    :type organization_id: str

    """
    body = Coupon.from_dict(body)
    return web.Response(status=200)


async def post_coupon_expiration(request: web.Request, id, organization_id=None, body=None) -> web.Response:
    """Set a coupon&#39;s expiration time

    Set a coupon&#39;s expiry time with the specified coupon ID. The expiredTime of a coupon must be greater than its issuedTime. This cannot be performed on expired coupons. 

    :param id: The resource identifier string.
    :type id: str
    :param organization_id: Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    :type organization_id: str
    :param body: Coupon resource.
    :type body: dict | bytes

    """
    body = CouponExpiration.from_dict(body)
    return web.Response(status=200)


async def post_coupon_redemption(request: web.Request, body, organization_id=None) -> web.Response:
    """Redeem a coupon

    Redeem a coupon. 

    :param body: Redeem a coupon.
    :type body: dict | bytes
    :param organization_id: Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    :type organization_id: str

    """
    body = CouponRedemption.from_dict(body)
    return web.Response(status=200)


async def post_coupon_redemption_cancellation(request: web.Request, id, organization_id=None) -> web.Response:
    """Cancel a coupon redemption

    

    :param id: The resource identifier string.
    :type id: str
    :param organization_id: Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    :type organization_id: str

    """
    return web.Response(status=200)


async def put_coupon(request: web.Request, id, body, organization_id=None) -> web.Response:
    """Create or update a coupon with predefined coupon ID

    Create or update a coupon with predefined coupon ID. 

    :param id: The resource identifier string.
    :type id: str
    :param body: Coupon resource.
    :type body: dict | bytes
    :param organization_id: Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    :type organization_id: str

    """
    body = Coupon.from_dict(body)
    return web.Response(status=200)
