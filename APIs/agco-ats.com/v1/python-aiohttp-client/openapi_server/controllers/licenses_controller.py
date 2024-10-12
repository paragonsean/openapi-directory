from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_models_api_error import APIModelsApiError
from openapi_server.models.api_paged_response_dealer_db_models_license import APIPagedResponseDealerDBModelsLicense
from openapi_server.models.dealer_db_models_license import DealerDBModelsLicense
from openapi_server import util


async def api_v2_licenses_idget(request: web.Request, id) -> web.Response:
    """Get a license.

    No Documentation Found.

    :param id: The ID of the license to get.
    :type id: str

    """
    return web.Response(status=200)


async def licenses_get(request: web.Request, voucher_code=None, dealer_code=None, status=None, limit=None, offset=None) -> web.Response:
    """Gets a list of licenses with the specified criteria.

    No Documentation Found.

    :param voucher_code: Optional. Filter by VoucherCode
    :type voucher_code: str
    :param dealer_code: Optional. Filter by DealerCode
    :type dealer_code: str
    :param status: Optional. Filter by Status.  By default only active licenses will be returned.
    :type status: str
    :param limit: Optional. The page limit. The default page limit is 10.
    :type limit: int
    :param offset: Optional. The page offset. The default page offset is 0.
    :type offset: int

    """
    return web.Response(status=200)
