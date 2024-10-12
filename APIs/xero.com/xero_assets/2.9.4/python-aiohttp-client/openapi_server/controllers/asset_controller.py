from typing import List, Dict
from aiohttp import web

from openapi_server.models.asset import Asset
from openapi_server.models.asset_status_query_param import AssetStatusQueryParam
from openapi_server.models.asset_type import AssetType
from openapi_server.models.assets import Assets
from openapi_server.models.setting import Setting
from openapi_server import util


async def create_asset(request: web.Request, xero_tenant_id, body) -> web.Response:
    """adds a fixed asset

    Adds an asset to the system

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param body: Fixed asset you are creating
    :type body: dict | bytes

    """
    body = Asset.from_dict(body)
    return web.Response(status=200)


async def create_asset_type(request: web.Request, xero_tenant_id, body=None) -> web.Response:
    """adds a fixed asset type

    Adds an fixed asset type to the system

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param body: Asset type to add
    :type body: dict | bytes

    """
    body = AssetType.from_dict(body)
    return web.Response(status=200)


async def get_asset_by_id(request: web.Request, xero_tenant_id, id) -> web.Response:
    """Retrieves fixed asset by id

    By passing in the appropriate asset id, you can search for a specific fixed asset in the system 

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param id: fixed asset id for single object
    :type id: str
    :type id: str

    """
    return web.Response(status=200)


async def get_asset_settings(request: web.Request, xero_tenant_id) -> web.Response:
    """searches fixed asset settings

    By passing in the appropriate options, you can search for available fixed asset types in the system

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str

    """
    return web.Response(status=200)


async def get_asset_types(request: web.Request, xero_tenant_id) -> web.Response:
    """searches fixed asset types

    By passing in the appropriate options, you can search for available fixed asset types in the system

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str

    """
    return web.Response(status=200)


async def get_assets(request: web.Request, xero_tenant_id, status, page=None, page_size=None, order_by=None, sort_direction=None, filter_by=None) -> web.Response:
    """searches fixed asset

    By passing in the appropriate options, you can search for available fixed asset in the system

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param status: Required when retrieving a collection of assets. See Asset Status Codes
    :type status: dict | bytes
    :param page: Results are paged. This specifies which page of the results to return. The default page is 1.
    :type page: int
    :param page_size: The number of records returned per page. By default the number of records returned is 10.
    :type page_size: int
    :param order_by: Requests can be ordered by AssetType, AssetName, AssetNumber, PurchaseDate and PurchasePrice. If the asset status is DISPOSED it also allows DisposalDate and DisposalPrice.
    :type order_by: str
    :param sort_direction: ASC or DESC
    :type sort_direction: str
    :param filter_by: A string that can be used to filter the list to only return assets containing the text. Checks it against the AssetName, AssetNumber, Description and AssetTypeName fields.
    :type filter_by: str

    """
    status = .from_dict(status)
    return web.Response(status=200)
