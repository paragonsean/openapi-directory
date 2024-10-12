from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.sales_rule_coupon_repository_v1_save_post_request import SalesRuleCouponRepositoryV1SavePostRequest
from openapi_server.models.sales_rule_data_coupon_interface import SalesRuleDataCouponInterface
from openapi_server import util


async def sales_rule_coupon_repository_v1_delete_by_id_delete(request: web.Request, coupon_id) -> web.Response:
    """coupons/{couponId}

    Delete coupon by coupon id.

    :param coupon_id: 
    :type coupon_id: int

    """
    return web.Response(status=200)


async def sales_rule_coupon_repository_v1_get_by_id_get(request: web.Request, coupon_id) -> web.Response:
    """coupons/{couponId}

    Get coupon by coupon id.

    :param coupon_id: 
    :type coupon_id: int

    """
    return web.Response(status=200)


async def sales_rule_coupon_repository_v1_save_put(request: web.Request, coupon_id, body=None) -> web.Response:
    """coupons/{couponId}

    Save a coupon.

    :param coupon_id: 
    :type coupon_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = SalesRuleCouponRepositoryV1SavePostRequest.from_dict(body)
    return web.Response(status=200)
