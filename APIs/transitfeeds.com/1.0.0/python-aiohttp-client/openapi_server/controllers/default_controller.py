from typing import List, Dict
from aiohttp import web

from openapi_server.models.api401_response import API401Response
from openapi_server.models.api404_response import API404Response
from openapi_server.models.get_feed_versions_response import GetFeedVersionsResponse
from openapi_server.models.get_feeds_response import GetFeedsResponse
from openapi_server.models.get_latest_feed_version_response import GetLatestFeedVersionResponse
from openapi_server.models.get_locations_response import GetLocationsResponse
from openapi_server import util


async def get_feed_versions(request: web.Request, key, feed=None, page=None, limit=None, err=None, warn=None) -> web.Response:
    """Retrieve a list of versions of specified (or all) feeds.

    This API call allows you to easily see every single feed update in the TranstiFeeds.com system. Since this can be quite long, it&#39;s also possible to filter this list by a single feed ID. 

    :param key: Your personal API key, used for authentication.
    :type key: str
    :param feed: If you only want to retrieve feed versions for a particular feed, include its ID here. You can use the &#x60;/getFeeds&#x60; call to discover feed IDs.
    :type feed: str
    :param page: The page number of results to return. For example, if you specify a &#x60;page&#x60; of &#x60;2&#x60; with a &#x60;limit&#x60; of 10, then results 11-20 are returned. The number of pages available is included in the response. 
    :type page: int
    :param limit: The maximum number of results to return..
    :type limit: int
    :param err: To include any errors detected when importing this feed in the response, specify a valud of &#x60;1&#x60;.
    :type err: int
    :param warn: To include any warnings detected when importing this feed in the response, specify a valud of &#x60;1&#x60;.
    :type warn: int

    """
    return web.Response(status=200)


async def get_feeds(request: web.Request, key, location=None, descendants=None, page=None, limit=None, type=None) -> web.Response:
    """Retrieve a list of feeds.

    Used this API to retrieve a list of feeds in the system. Doing so can be usedful to discover feed IDs that can be used in other API calls. 

    :param key: Your personal API key, used for authentication.
    :type key: str
    :param location: This is the unique ID of a location. If specified, feeds will only be returned that belong to this location (and perhaps sub-locations too, depending on the &#x60;descendants&#x60; value). You can use the &#x60;/getLocations&#x60; API endpoint to determine location IDs. 
    :type location: int
    :param descendants: If a location is specified in &#x60;location&#x60;, this flag can be used to control if returned feeds must be assigned directly to the location, or if feeds belonging to sub-locations can also be returned. If &#x60;0&#x60;, then feeds must be assigned directly to the specified location.
    :type descendants: int
    :param page: The page number of results to return. For example, if you specify a &#x60;page&#x60; of &#x60;2&#x60; with a &#x60;limit&#x60; of 10, then results 11-20 are returned. The number of pages available is included in the response. 
    :type page: int
    :param limit: The maximum number of results to return..
    :type limit: int
    :param type: The type of feeds to return. If unspecified, feeds of all types are returned.
    :type type: str

    """
    return web.Response(status=200)


async def get_latest_feed_version(request: web.Request, key, feed) -> web.Response:
    """Retrieve the download URL for the latest version of a feed.

    Once you have used &#x60;/getFeeds&#x60; to discover a feed&#39;s URL, you can use this endpoint to download its latest version from TranstiFeeds. It will be unmodified in the original format from the provider. 

    :param key: Your personal API key, used for authentication.
    :type key: str
    :param feed: The ID of the feed to retrieve the latest feed version for. You can use the &#x60;/getFeeds&#x60; call to discover feed IDs.
    :type feed: str

    """
    return web.Response(status=200)


async def get_locations(request: web.Request, key) -> web.Response:
    """Retrieve a list of locations.

    Retrieve a list of locations. Each location (except for the root) has a parent location, and each location has zero or more child locations. This hierarchy is generally structured so countries contain states, states contain cities (although this typically depends on the country). 

    :param key: Your personal API key, used for authentication.
    :type key: str

    """
    return web.Response(status=200)
