from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def get_suggestionbyversion(request: web.Request, account_name, accept, content_type, seller_id, sellerskuid, version) -> web.Response:
    """Get Version by ID

    Whenever an SKU Suggestion is updated or changed, a new version of the original one is created. All versions are logged, so you can search for previous our current states of SKU suggestions.   This endpoint retrieves a specific *version* of a chosen SKU sent by the seller. Add the Seller&#39;s ID, Seller&#39;s SKU ID, and version ID in the path to detail your search.

    :param account_name: Name of the VTEX account. Used as part of the URL
    :type account_name: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
    :type accept: str
    :param content_type: Describes the type of the content being sent.
    :type content_type: str
    :param seller_id: A string that identifies the seller in the marketplace. This ID must be created by the marketplace and informed to the seller before the integration is built.
    :type seller_id: str
    :param sellerskuid: A string that identifies the SKU in the marketplace. This is the ID that the marketplace will use for future references to this SKU, such as price and inventory notifications.
    :type sellerskuid: str
    :param version: Whenever an SKU Suggestion is updated or changed, a new version of the original one is created. All versions are logged, so you can search for previous our current states of SKU suggestions. This field is the &#x60;versionId&#x60; associated to the version you choose to search for. You can get this field&#39;s value through the [Get SKU Suggestion by ID](https://developers.vtex.com/vtex-rest-api/reference/getsuggestion). through the &#x60;latestVersionId&#x60; field.
    :type version: str

    """
    return web.Response(status=200)


async def get_versions(request: web.Request, account_name, accept, content_type, seller_id, sellerskuid) -> web.Response:
    """Get all Versions

    Whenever an SKU Suggestion is updated or changed, a new version of the original one is created. All versions are logged, so you can search for previous our current states of SKU suggestions.   This endpoint retrieves the data of *all* previous and latest versions of a specific SKU suggestion, sent by the seller. Whenever an SKU is updated, it is important to map previous versions, to compare and identify changes.   The response&#39;s object [latestversion] provides the information of the most recent version of that SKU suggestion.

    :param account_name: Name of the VTEX account. Used as part of the URL
    :type account_name: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
    :type accept: str
    :param content_type: Describes the type of the content being sent.
    :type content_type: str
    :param seller_id: A string that identifies the seller in the marketplace. This ID must be created by the marketplace and informed to the seller before the integration is built.
    :type seller_id: str
    :param sellerskuid: A string that identifies the SKU in the marketplace. This is the ID that the marketplace will use for future references to this SKU, such as price and inventory notifications.
    :type sellerskuid: str

    """
    return web.Response(status=200)
