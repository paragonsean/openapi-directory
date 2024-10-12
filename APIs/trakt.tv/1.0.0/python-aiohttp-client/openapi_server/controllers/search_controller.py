from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def get_id_lookup_results(request: web.Request, id_type, id, type=None, trakt_api_version=None, trakt_api_key=None) -> web.Response:
    """Get ID lookup results

    #### &amp;#128196; Pagination &amp;#10024; Extended Info  Lookup items by their Trakt, IMDB, TMDB, or TVDB ID. If you use the search url without a &#x60;type&#x60; it might return multiple items if the &#x60;id_type&#x60; is not globally unique. Specify the &#x60;type&#x60; of results by sending a single value or a comma delimited string for multiple types.  | Type | URL | |---|---| | &#x60;trakt&#x60; | &#x60;/search/trakt/:id&#x60; | |  | &#x60;/search/trakt/:id?type&#x3D;movie&#x60; | |  | &#x60;/search/trakt/:id?type&#x3D;show&#x60; | |  | &#x60;/search/trakt/:id?type&#x3D;episode&#x60; | |  | &#x60;/search/trakt/:id?type&#x3D;person&#x60; | | &#x60;imdb&#x60; | &#x60;/search/imdb/:id&#x60; | | &#x60;tmdb&#x60; | &#x60;/search/tmdb/:id&#x60; | |  | &#x60;/search/tmdb/:id?type&#x3D;movie&#x60; | |  | &#x60;/search/tmdb/:id?type&#x3D;show&#x60; | |  | &#x60;/search/tmdb/:id?type&#x3D;episode&#x60; | |  | &#x60;/search/tmdb/:id?type&#x3D;person&#x60; | | &#x60;tvdb&#x60; | &#x60;/search/tvdb/:id&#x60; | |  | &#x60;/search/tvdb/:id?type&#x3D;show&#x60; | |  | &#x60;/search/tvdb/:id?type&#x3D;episode&#x60; |

    :param id_type: Type of ID to lookup.
    :type id_type: str
    :param id: ID that matches with the type.
    :type id: str
    :param type: Search type.
    :type type: str
    :param trakt_api_version: e.g. 2
    :type trakt_api_version: str
    :param trakt_api_key: e.g. [client_id]
    :type trakt_api_key: str

    """
    return web.Response(status=200)


async def get_text_query_results(request: web.Request, type, query, trakt_api_version=None, trakt_api_key=None, body=None) -> web.Response:
    """Get text query results

    #### &amp;#128196; Pagination &amp;#10024; Extended Info &amp;#127898; Filters  Search all text fields that a media object contains (i.e. title, overview, etc). Results are ordered by the most relevant score. Specify the &#x60;type&#x60; of results by sending a single value or a comma delimited string for multiple types.  #### Special Characters  Our search engine (Solr) gives the following characters special meaning when they appear in a query:  &#x60;+ - &amp;&amp; || ! ( ) { } [ ] ^ \&quot; ~ * ? : /&#x60;  To interpret any of these characters literally (and not as a special character), precede the character with a backslash &#x60;\\&#x60; character.  #### Search Fields  By default, all text fields are used to search for the &#x60;query&#x60;. You can optionally specify the &#x60;fields&#x60; parameter with a single value or comma delimited string for multiple fields. Each &#x60;type&#x60; has specific &#x60;fields&#x60; that can be specified. This can be useful if you want to support more strict searches (i.e. title only).  | Type | Field | |---|---| | &#x60;movie&#x60; | &#x60;title&#x60; | |  | &#x60;tagline&#x60; | |  | &#x60;overview&#x60; | |  | &#x60;people&#x60; | |  | &#x60;translations&#x60; | |  | &#x60;aliases&#x60; | | &#x60;show&#x60; | &#x60;title&#x60; | |  | &#x60;overview&#x60; | |  | &#x60;people&#x60; | |  | &#x60;translations&#x60; | |  | &#x60;aliases&#x60; | | &#x60;episode&#x60; | &#x60;title&#x60; | |  | &#x60;overview&#x60; | | &#x60;person&#x60; | &#x60;name&#x60; | |  | &#x60;biography&#x60; | | &#x60;list&#x60; | &#x60;name&#x60; | |  | &#x60;description&#x60; |

    :param type: Search type.
    :type type: str
    :param query: Search all text based fields.
    :type query: str
    :param trakt_api_version: e.g. 2
    :type trakt_api_version: str
    :param trakt_api_key: e.g. [client_id]
    :type trakt_api_key: str
    :param body: Specific text fields.
    :type body: str

    """
    return web.Response(status=200)
