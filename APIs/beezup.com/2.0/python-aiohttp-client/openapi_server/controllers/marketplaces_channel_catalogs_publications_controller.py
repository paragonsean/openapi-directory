from typing import List, Dict
from aiohttp import web

from openapi_server.models.account_publications import AccountPublications
from openapi_server.models.beez_up_common_error_response_message import BeezUPCommonErrorResponseMessage
from openapi_server.models.publish_catalog_to_marketplace_request import PublishCatalogToMarketplaceRequest
from openapi_server import util


async def get_publications(request: web.Request, marketplace_technical_code, account_id, publication_types, channel_catalog_id=None, count=None) -> web.Response:
    """Fetch the publication history for an account, sorted by descending start date

    

    :param marketplace_technical_code: Marketplace Technical Code to query (required)
    :type marketplace_technical_code: str
    :param account_id: Account Id to query (required)
    :type account_id: int
    :param publication_types: Publication types by which to filter (optional)
    :type publication_types: List[str]
    :param channel_catalog_id: Channel Catalog Id by which to filter (optional)
    :type channel_catalog_id: str
    :param count: Amount of entries to fetch (optional, default set to 10)
    :type count: int

    """
    return web.Response(status=200)


async def publish_catalog_to_marketplace(request: web.Request, marketplace_technical_code, account_id, body) -> web.Response:
    """[PREVIEW] Launch a publication of the catalog to the marketplace

    

    :param marketplace_technical_code: Marketplace Technical Code to query (required)
    :type marketplace_technical_code: str
    :param account_id: Account Id to query (required)
    :type account_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = PublishCatalogToMarketplaceRequest.from_dict(body)
    return web.Response(status=200)
