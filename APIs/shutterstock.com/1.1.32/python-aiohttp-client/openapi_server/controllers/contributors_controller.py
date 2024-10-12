from typing import List, Dict
from aiohttp import web

from openapi_server.models.collection import Collection
from openapi_server.models.collection_data_list import CollectionDataList
from openapi_server.models.collection_item_data_list import CollectionItemDataList
from openapi_server.models.contributor_profile import ContributorProfile
from openapi_server.models.contributor_profile_data_list import ContributorProfileDataList
from openapi_server import util


async def get_contributor(request: web.Request, contributor_id) -> web.Response:
    """Get details about a single contributor

    This endpoint shows information about a single contributor, including contributor type, equipment they use, and other attributes.

    :param contributor_id: Contributor ID
    :type contributor_id: str

    """
    return web.Response(status=200)


async def get_contributor_collection_items(request: web.Request, contributor_id, id, page=None, per_page=None, sort=None) -> web.Response:
    """Get the items in contributors&#39; collections

    This endpoint lists the IDs of items in a contributor&#39;s collection and the date that each was added.

    :param contributor_id: Contributor ID
    :type contributor_id: str
    :param id: Collection ID that belongs to the contributor
    :type id: str
    :param page: Page number
    :type page: int
    :param per_page: Number of results per page
    :type per_page: int
    :param sort: Sort order
    :type sort: str

    """
    return web.Response(status=200)


async def get_contributor_collections(request: web.Request, contributor_id, id) -> web.Response:
    """Get details about contributors&#39; collections

    This endpoint gets more detailed information about a contributor&#39;s collection, including its cover image, timestamps for its creation, and most recent update. To get the items in collections, use GET /v2/contributors/{contributor_id}/collections/{id}/items.

    :param contributor_id: Contributor ID
    :type contributor_id: str
    :param id: Collection ID that belongs to the contributor
    :type id: str

    """
    return web.Response(status=200)


async def get_contributor_collections_list(request: web.Request, contributor_id, sort=None) -> web.Response:
    """List contributors&#39; collections

    This endpoint lists collections based on contributor ID.

    :param contributor_id: Contributor ID
    :type contributor_id: str
    :param sort: Sort order
    :type sort: str

    """
    return web.Response(status=200)


async def get_contributor_list(request: web.Request, id) -> web.Response:
    """Get details about multiple contributors

    This endpoint lists information about one or more contributors, including contributor type, equipment they use and other attributes.

    :param id: One or more contributor IDs
    :type id: List[str]

    """
    return web.Response(status=200)
