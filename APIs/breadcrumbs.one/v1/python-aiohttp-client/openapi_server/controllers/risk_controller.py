from typing import List, Dict
from aiohttp import web

from openapi_server.models.breadcrumbs_api_models_address_risk_exposure_response import BreadcrumbsAPIModelsAddressRiskExposureResponse
from openapi_server.models.breadcrumbs_api_models_transaction_risk_response import BreadcrumbsAPIModelsTransactionRiskResponse
from openapi_server.models.breadcrumbs_response_unauthorized_response import BreadcrumbsResponseUnauthorizedResponse
from openapi_server.models.breadcrumbs_response_unprocessable_response import BreadcrumbsResponseUnprocessableResponse
from openapi_server import util


async def risk_address_get(request: web.Request, chain, address, include_exposure=None) -> web.Response:
    """Will check the risk score for single address

    

    :param chain: Blockchain eg: ETH, BTC, MATIC, RON, SOL, TRX
    :type chain: str
    :param address: Blockchain address
    :type address: str
    :param include_exposure: If set to &#x60;true&#x60;, will search the one nearest illicit address (incoming and outgoing) from the specified address
    :type include_exposure: bool

    """
    return web.Response(status=200)


async def risk_transaction_get(request: web.Request, chain, hash) -> web.Response:
    """Will check the risk score for every addresses in a transaction

    

    :param chain: Blockchain eg: ETH, BTC, MATIC, RON, SOL, TRX
    :type chain: str
    :param hash: Blockchain hash
    :type hash: str

    """
    return web.Response(status=200)
