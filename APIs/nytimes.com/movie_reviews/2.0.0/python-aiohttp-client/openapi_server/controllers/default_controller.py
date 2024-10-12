from typing import List, Dict
from aiohttp import web

from openapi_server.models.critics_resource_type_json_get200_response import CriticsResourceTypeJsonGet200Response
from openapi_server.models.reviews_search_json_get200_response import ReviewsSearchJsonGet200Response
from openapi_server import util


async def critics_resource_type_json_get(request: web.Request, resource_type) -> web.Response:
    """critics_resource_type_json_get

    

    :param resource_type: all | full-time | part-time | [reviewer-name]  Specify all to get all Times reviewers, or specify full-time or part-time to get that subset. Specify a reviewer&#39;s name to get details about a particular reviewer. 
    :type resource_type: str

    """
    return web.Response(status=200)


async def reviews_resource_type_json_get(request: web.Request, resource_type, offset=None, order=None) -> web.Response:
    """reviews_resource_type_json_get

    

    :param resource_type: Specify all to retrieve all reviews, including NYT Critics&#39; Picks.  Specify picks to get NYT Critics&#39; Picks currently in theaters.  
    :type resource_type: str
    :param offset: Positive integer, multiple of 20
    :type offset: int
    :param order: Sets the sort order of the results.  Results ordered by-title are in ascending alphabetical order. Results ordered by one of the date parameters are in reverse chronological order.  If you do not specify a sort order, the results will be ordered by publication-date. 
    :type order: str

    """
    return web.Response(status=200)


async def reviews_search_json_get(request: web.Request, query=None, critics_pick=None, reviewer=None, publication_date=None, opening_date=None, offset=None, order=None) -> web.Response:
    """reviews_search_json_get

    

    :param query: Search keywords; matches movie title and indexed terms  To limit your search to exact matches only, surround your search string with single quotation marks (e.g., query&#x3D;&#39;28+days+later&#39;). Otherwise, responses will include partial matches (\&quot;head words\&quot;) as well as exact matches (e.g., president will match president, presidents and presidential).      If you specify multiple terms without quotation marks, they will be combined in an OR search.      If you omit the query parameter, your request will be equivalent to a reviews and NYT Critics&#39; Picks request. 
    :type query: str
    :param critics_pick: Set this parameter to Y to limit the results to NYT Critics&#39; Picks. To get only those movies that have not been highlighted by Times critics, specify critics-pick&#x3D;N. (To get all reviews regardless of critics-pick status, simply omit this parameter.) 
    :type critics_pick: str
    :param reviewer: Include this parameter to limit your results to reviews by a specific critic. Reviewer names should be formatted like this: Manohla Dargis. 
    :type reviewer: str
    :param publication_date: Single date: YYYY-MM-DD  Start and end date: YYYY-MM-DD;YYYY-MM-DD  The publication-date is the date the review was first published in The Times. 
    :type publication_date: str
    :param opening_date: Single date: YYYY-MM-DD  Start and end date: YYYY-MM-DD;YYYY-MM-DD  The opening-date is the date the movie&#39;s opening date in the New York region. 
    :type opening_date: str
    :param offset: Positive integer, multiple of 20
    :type offset: int
    :param order: Sets the sort order of the results.  Results ordered by-title are in ascending alphabetical order. Results ordered by one of the date parameters are in reverse chronological order.  If you do not specify a sort order, the results will be ordered by publication-date. 
    :type order: str

    """
    return web.Response(status=200)
