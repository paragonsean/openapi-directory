from typing import List, Dict
from aiohttp import web

from openapi_server.models.holding_asset_classification_list_response import HoldingAssetClassificationListResponse
from openapi_server.models.holding_response import HoldingResponse
from openapi_server.models.holding_securities_response import HoldingSecuritiesResponse
from openapi_server.models.holding_type_list_response import HoldingTypeListResponse
from openapi_server.models.yodlee_error import YodleeError
from openapi_server import util


async def get_asset_classification_list(request: web.Request, ) -> web.Response:
    """Get Asset Classification List

    The get asset classifications list service is used to get the supported asset classifications. &lt;br&gt;The response includes different classification types like assetClass, country, sector, style, etc. and the values corresponding to each type.&lt;br&gt;


    """
    return web.Response(status=200)


async def get_holding_type_list(request: web.Request, ) -> web.Response:
    """Get Holding Type List

    The get holding types list service is used to get the supported holding types.&lt;br&gt;The response includes different holding types such as future, moneyMarketFund, stock, etc. and it returns the supported holding types &lt;br&gt;


    """
    return web.Response(status=200)


async def get_holdings(request: web.Request, account_id=None, asset_classification_classification_type=None, classification_value=None, include=None, provider_account_id=None) -> web.Response:
    """Get Holdings

    The get holdings service is used to get the list of holdings of a user.&lt;br&gt;Supported holding types can be employeeStockOption, moneyMarketFund, bond, etc. and is obtained using get holding type list service. &lt;br&gt;Asset classifications for the holdings need to be requested through the \&quot;include\&quot; parameter.&lt;br&gt;Asset classification information for holdings are not available by default, as it is a premium feature.&lt;br&gt;

    :param account_id: Comma separated accountId
    :type account_id: str
    :param asset_classification_classification_type: e.g. Country, Sector, etc.
    :type asset_classification_classification_type: str
    :param classification_value: e.g. US
    :type classification_value: str
    :param include: assetClassification
    :type include: str
    :param provider_account_id: providerAccountId
    :type provider_account_id: str

    """
    return web.Response(status=200)


async def get_securities(request: web.Request, holding_id=None) -> web.Response:
    """Get Security Details

    The get security details service is used to get all the security information for the holdings&lt;br&gt;

    :param holding_id: Comma separated holdingId
    :type holding_id: str

    """
    return web.Response(status=200)
