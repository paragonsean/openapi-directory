from typing import List, Dict
from aiohttp import web

from openapi_server.models.related_searches_response import RelatedSearchesResponse
from openapi_server.models.search_response import SearchResponse
from openapi_server.models.spell_check_response import SpellCheckResponse
from openapi_server.models.trending_searches_response import TrendingSearchesResponse
from openapi_server.models.typeahead_response import TypeaheadResponse
from openapi_server import util


async def get_related_searches(request: web.Request, x_listen_api_key, q) -> web.Response:
    """Fetch related search terms

    Suggest related search terms. The results are more comprehensive than from &#x60;GET /typeahead&#x60;. This endpoint is available only in the PRO/ENTERPRISE plan.

    :param x_listen_api_key: Get API Key on listennotes.com/api
    :type x_listen_api_key: str
    :param q: Search term, e.g., person, place, topic... 
    :type q: str

    """
    return web.Response(status=200)


async def get_trending_searches(request: web.Request, x_listen_api_key) -> web.Response:
    """Fetch trending search terms

    Fetch up to 10 most recent trending search terms on the Listen Notes platform.

    :param x_listen_api_key: Get API Key on listennotes.com/api
    :type x_listen_api_key: str

    """
    return web.Response(status=200)


async def search(request: web.Request, x_listen_api_key, q, sort_by_date=None, type=None, offset=None, len_min=None, len_max=None, episode_count_min=None, episode_count_max=None, update_freq_min=None, update_freq_max=None, genre_ids=None, published_before=None, published_after=None, only_in=None, language=None, region=None, ocid=None, ncid=None, safe_mode=None, unique_podcasts=None, page_size=None) -> web.Response:
    """Full-text search

    Full-text search on episodes, podcasts, or curated lists of podcasts. Use the &#x60;offset&#x60; parameter to paginate through search results. The FREE plan allows to see up to 30 search results (or &#x60;offset&#x60; &lt; 30) per query. The PRO plan allows to see up to 300 search results (or &#x60;offset&#x60; &lt; 300) per query. The ENTERPRISE plan allows to see up to 10,000 search results (or &#x60;offset&#x60; &lt; 10000) per query. 

    :param x_listen_api_key: Get API Key on listennotes.com/api
    :type x_listen_api_key: str
    :param q: Search term, e.g., person, place, topic... You can use double quotes to do verbatim match, e.g., \&quot;game of thrones\&quot;. Otherwise, it&#39;s fuzzy search. 
    :type q: str
    :param sort_by_date: Sort by date or not? If 0, then sort by relevance. If 1, then sort by date. 
    :type sort_by_date: int
    :param type: What type of contents do you want to search for?  
    :type type: str
    :param offset: Offset for search results, for pagination. You&#39;ll use **next_offset** from response for this parameter. 
    :type offset: int
    :param len_min: Minimum audio length in minutes. Applicable only when **type** parameter is **episode** or **podcast**. If **type** parameter is **episode**, it&#39;s for audio length of an episode. If **type** parameter is **podcast**, it&#39;s for average audio length of all episodes in a podcast. 
    :type len_min: int
    :param len_max: Maximum audio length in minutes. Applicable only when **type** parameter is **episode** or **podcast**. If **type** parameter is **episode**, it&#39;s for audio length of an episode. If **type** parameter is **podcast**, it&#39;s for average audio length of all episodes in a podcast. 
    :type len_max: int
    :param episode_count_min: Minimum number of episodes. Applicable only when type parameter is **podcast**. 
    :type episode_count_min: int
    :param episode_count_max: Maximum number of episodes. Applicable only when type parameter is **podcast**. 
    :type episode_count_max: int
    :param update_freq_min: Minimum update frequency in hours (how frequently does a podcast release a new episode). For example, if you want to find \&quot;weekly\&quot; podcasts, then you can set **update_freq_min**&#x3D;144 hours (or 6 days) and **update_freq_max**&#x3D;192 hours (or 8 days). Applicable only when type parameter is **podcast**. 
    :type update_freq_min: int
    :param update_freq_max: Maximum update frequency in hours (how frequently does a podcast release a new episode). For example, if you want to find \&quot;weekly\&quot; podcasts, then you can set **update_freq_min**&#x3D;144 hours (or 6 days) and **update_freq_max**&#x3D;192 hours (or 8 days). Applicable only when type parameter is **podcast**. 
    :type update_freq_max: int
    :param genre_ids: A comma-delimited string of a list of genre ids. If not specified, then all genres are included. You can find the id and the name of all genres from &#x60;GET /genres&#x60;. It works only when **type** is *episode* or *podcast*. 
    :type genre_ids: str
    :param published_before: Only show episodes/podcasts/curated lists published before this timestamp (in milliseconds). If **published_before** &amp; **published_after** are used at the same time, **published_before** should be bigger than **published_after**. 
    :type published_before: int
    :param published_after: Only show episodes/podcasts/curated lists published after this timestamp (in milliseconds). If **published_before** &amp; **published_after** are used at the same time, **published_before** should be bigger than **published_after**. 
    :type published_after: int
    :param only_in: A comma-delimited string to search only in specific fields. Allowed values are title, description, author, and audio. If not specified, then search every fields. 
    :type only_in: str
    :param language: Limit search results to a specific language. If not specified, it&#39;ll be any language. You can get a list of supported languages from &#x60;GET /languages&#x60;. It works only when **type** is *episode* or *podcast*. 
    :type language: str
    :param region: Limit search results to a specific region (e.g., us, gb, in...). If not specified, it&#39;ll be any region. You can get the supported country codes from &#x60;GET /regions&#x60;. It works only when **type** is *episode* or *podcast*. 
    :type region: str
    :param ocid: A comma-delimited string of podcast ids (up to 5 podcasts) - you can get a podcast id from the **podcast_id** field in response. This parameter is to limit search results from only a few specific podcasts. It works only when **type** is *episode*. 
    :type ocid: str
    :param ncid: A comma-delimited string of podcast ids (up to 5 podcasts) - you can get a podcast id from the **podcast_id** field in response. This parameter is to exclude search results of a few specific podcasts. It works only when **type** is *episode*. 
    :type ncid: str
    :param safe_mode: Whether or not to exclude podcasts/episodes with explicit language. 1 is yes and 0 is no. It works only when **type** is *episode* or *podcast*. 
    :type safe_mode: int
    :param unique_podcasts: Whether or not to keep only one episode per podcast in search results. 1 is yes and 0 is no. It works only when **type** is *episode*. 
    :type unique_podcasts: int
    :param page_size: The maximum number of search results per page. A valid value should be an integer between 1 and 10 (inclusive). 
    :type page_size: int

    """
    return web.Response(status=200)


async def spellcheck(request: web.Request, x_listen_api_key, q) -> web.Response:
    """Spell check on a search term

    Suggest a list of words that correct the spelling errors of a search term. This endpoint is available only in the PRO/ENTERPRISE plan.

    :param x_listen_api_key: Get API Key on listennotes.com/api
    :type x_listen_api_key: str
    :param q: Search term, e.g., person, place, topic... 
    :type q: str

    """
    return web.Response(status=200)


async def typeahead(request: web.Request, x_listen_api_key, q, show_podcasts=None, show_genres=None, safe_mode=None) -> web.Response:
    """Typeahead search

    Suggest search terms, podcast genres, and podcasts.

    :param x_listen_api_key: Get API Key on listennotes.com/api
    :type x_listen_api_key: str
    :param q: Search term, e.g., person, place, topic... You can use double quotes to do verbatim match, e.g., \&quot;game of thrones\&quot;. Otherwise, it&#39;s fuzzy search. 
    :type q: str
    :param show_podcasts: Autosuggest podcasts. This only searches podcast title and publisher and returns very limited info of 5 podcasts. 1 is yes, 0 is no. It&#39;s a bit slow to autosuggest podcasts, so we turn it off by default. If show_podcasts&#x3D;1, you can also pass iTunes id (e.g., 474722933) to the q parameter to fetch podcast meta data. 
    :type show_podcasts: int
    :param show_genres: Whether or not to autosuggest genres. 1 is yes, 0 is no. 
    :type show_genres: int
    :param safe_mode: Whether or not to exclude podcasts/episodes with explicit language. 1 is yes and 0 is no. It works only when **show_podcasts** is *1*. 
    :type safe_mode: int

    """
    return web.Response(status=200)
