from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_paged_response_dealer_db_models_voucher import APIPagedResponseDealerDBModelsVoucher
from openapi_server.models.api_paged_response_dealer_db_models_voucher_history import APIPagedResponseDealerDBModelsVoucherHistory
from openapi_server.models.dealer_db_models_voucher import DealerDBModelsVoucher
from openapi_server import util


async def api_v2_vouchers_voucher_code_get(request: web.Request, voucher_code, deleted=None) -> web.Response:
    """Get a voucher

    No Documentation Found.

    :param voucher_code: The voucher code of the voucher to get.
    :type voucher_code: str
    :param deleted: Optional. Filter vouchers by Deleted state. By default only vouchers that are not deleted are returned.
    :type deleted: str

    """
    return web.Response(status=200)


async def vouchers_delete(request: web.Request, voucher_code) -> web.Response:
    """Delete a voucher

    No Documentation Found.

    :param voucher_code: The voucher code of the voucher to delete.
    :type voucher_code: str

    """
    return web.Response(status=200)


async def vouchers_get(request: web.Request, type=None, dealer_code=None, license_to=None, purpose=None, order_number=None, email=None, modified_by=None, created_after=None, created_before=None, punched_after=None, punched_before=None, punched=None, expiration_after=None, expiration_before=None, deleted=None, limit=None, offset=None) -> web.Response:
    """Gets a list of vouchers

    No Documentation Found.

    :param type: Optional. Filter vouchers by Type
    :type type: str
    :param dealer_code: Optional. Filter vouchers by DealerCode
    :type dealer_code: str
    :param license_to: Optional. Filter vouchers by LicenseTo. Wildcard supported (*).
    :type license_to: str
    :param purpose: Optional. Filter vouchers by Purpose. Wildcard supported (*).
    :type purpose: str
    :param order_number: Optional. Filter vouchers by OrderNumber
    :type order_number: str
    :param email: Optional. Filter vouchers by Email. Wildcard supported (*).
    :type email: str
    :param modified_by: Optional. Filter vouchers by ModifiedBy
    :type modified_by: str
    :param created_after: Optional. Filter vouchers by CreatedDate
    :type created_after: str
    :param created_before: Optional. Filter vouchers by CreatedDate
    :type created_before: str
    :param punched_after: Optional. Filter vouchers by PunchedDate
    :type punched_after: str
    :param punched_before: Optional. Filter vouchers by PunchedDate
    :type punched_before: str
    :param punched: Optional. Filter vouchers by Punched status
    :type punched: bool
    :param expiration_after: Optional. Filter vouchers by ExpirationDate
    :type expiration_after: str
    :param expiration_before: Optional. Filter vouchers by ExpirationDate
    :type expiration_before: str
    :param deleted: Optional. Filter vouchers by Deleted state. By default only vouchers that are not deleted are returned.
    :type deleted: str
    :param limit: Optional. The page limit. The default page limit is 10.
    :type limit: int
    :param offset: Optional. The page offset. The default page offset is 0.
    :type offset: int

    """
    created_after = util.deserialize_datetime(created_after)
    created_before = util.deserialize_datetime(created_before)
    punched_after = util.deserialize_datetime(punched_after)
    punched_before = util.deserialize_datetime(punched_before)
    expiration_after = util.deserialize_datetime(expiration_after)
    expiration_before = util.deserialize_datetime(expiration_before)
    return web.Response(status=200)


async def vouchers_get_voucher_history(request: web.Request, voucher_code, limit=None, offset=None) -> web.Response:
    """Get a voucher&#39;s history.

    No Documentation Found.

    :param voucher_code: The voucher code to get history for.
    :type voucher_code: str
    :param limit: Optional. The page limit. The default page limit is 10.
    :type limit: int
    :param offset: Optional. The page offset. The default page offset is 0.
    :type offset: int

    """
    return web.Response(status=200)


async def vouchers_post(request: web.Request, body) -> web.Response:
    """Create a voucher

    No Documentation Found.

    :param body: The voucher to add.
    :type body: dict | bytes

    """
    body = DealerDBModelsVoucher.from_dict(body)
    return web.Response(status=200)


async def vouchers_put(request: web.Request, voucher_code, body) -> web.Response:
    """Update a voucher

    No Documentation Found.

    :param voucher_code: The voucher code of the voucher to update.
    :type voucher_code: str
    :param body: The updated voucher.
    :type body: dict | bytes

    """
    body = DealerDBModelsVoucher.from_dict(body)
    return web.Response(status=200)
