from typing import List, Dict
from aiohttp import web

from openapi_server.models.acquire_asset_licenses_request import AcquireAssetLicensesRequest
from openapi_server.models.asset_licensing_response import AssetLicensingResponse
from openapi_server import util


async def v3_asset_licensing_asset_id_post(request: web.Request, asset_id, accept_language=None, body=None) -> web.Response:
    """Endpoint for acquiring extended licenses with iStock credits for an asset.

    

    :param asset_id: Getty Images assetId - examples 520621493, 112301284
    :type asset_id: str
    :param accept_language: Provide a header to specify the language of result values. Supported values: cs (iStock only), de, en-GB, en-US, es, fi (iStock only), fr, hu (iStock only), id (iStock only), it, ja, ko (creative assets only), nl, pl (creative assets only), pt-BR, pt-PT, ro (iStock only), ru (creative assets only), sv, th (iStock only), tr, uk (iStock only), vi (iStock only), zh-HK (creative assets only).
    :type accept_language: str
    :param body: Structure that specifies an array of LicenseTypes (multiseat, unlimited, resale, indemnification) to acquire,              and whether or not to use Team Credits. Authenticated User must have access to Team Credits if UseTeamCredits is set to \&quot;true\&quot;.
    :type body: dict | bytes

    """
    body = AcquireAssetLicensesRequest.from_dict(body)
    return web.Response(status=200)
