from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_paged_response_dealer_db_models_voucher_history import APIPagedResponseDealerDBModelsVoucherHistory
from openapi_server import util


async def voucher_history_get_voucher_history(request: web.Request, voucher_code=None, changed_before=None, changed_after=None, limit=None, offset=None) -> web.Response:
    """Gets voucher history data

    No Documentation Found.

    :param voucher_code: Optional. Filter history data by Voucher Code.
    :type voucher_code: str
    :param changed_before: Optional. Filter history data where changes occured before provided date.
    :type changed_before: str
    :param changed_after: Optional. Filter history data where changes occured after provided date.
    :type changed_after: str
    :param limit: Optional. The page limit. The default page limit is 10.
    :type limit: int
    :param offset: Optional. The page offset. The default page offset is 0.
    :type offset: int

    """
    changed_before = util.deserialize_datetime(changed_before)
    changed_after = util.deserialize_datetime(changed_after)
    return web.Response(status=200)
