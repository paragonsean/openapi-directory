from typing import List, Dict
from aiohttp import web

from openapi_server.models.query_json_get200_response import QueryJsonGet200Response
from openapi_server import util


async def query_json_get(request: web.Request, name=None, latitude=None, longitude=None, elevation=None, sw=None, query=None, filter=None, date_range=None, facets=None, sort=None, limit=None, offset=None) -> web.Response:
    """Geographic API

    Geographic API

    :param name: A displayable name for the specified place.
    :type name: str
    :param latitude: The latitude of the specified place. 
    :type latitude: str
    :param longitude: The longitude of the specified place.
    :type longitude: str
    :param elevation: The elevation of the specified place, in meters.
    :type elevation: int
    :param sw: Along with ne, forms a bounded box using the longitude and latitude coordinates specified as the southwest corner. The search results are limited to the resulting box. Two float values, separated by a comma &#x60;latitude,longitude&#x60; &lt;br/&gt; The ne parameter is required to use this parameter.
    :type sw: str
    :param query: Search keywords to perform a text search on the fields: web_description, event_name and venue_name. &#39;AND&#39; searches can be performed by wrapping query terms in quotes. If you do not specify a query, all results will be returned. 
    :type query: str
    :param filter: Filters search results based on the facets provided.  For more information on the values you can filter on, see Facets. 
    :type filter: str
    :param date_range: Start date to end date in the following format- YYYY-MM-DD:YYYY-MM-DD
    :type date_range: str
    :param facets: When facets is set to 1, a count of all facets will be included in the response.
    :type facets: int
    :param sort: Sorts your results on the fields specified. &lt;br/&gt; &#x60;sort_value1+[asc | desc],sort_value2+[asc|desc],[...]&#x60;&lt;br/&gt; Appending +asc to a facet or response will sort results on that value in ascending order. Appending +desc to a facet or response  will sort results in descending order. You can sort on multiple fields. You can sort on any facet. For the list of responses you can sort on, see the Sortable Field column in the Response table. &lt;br/&gt;&lt;br/&gt;If you are doing a spatial search with the ll parameter, you can also sort by the distance from the center of the search: dist+[asc | desc] &lt;br/&gt; **Note:** either +asc or +desc is required when using the sort parameter. 
    :type sort: str
    :param limit: Limits the number of results returned
    :type limit: int
    :param offset: Sets the starting point of the result set
    :type offset: int

    """
    return web.Response(status=200)
