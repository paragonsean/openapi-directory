from typing import List, Dict
from aiohttp import web

from openapi_server.models.search_response import SearchResponse
from openapi_server import util


async def kgsearch_entities_search(request: web.Request, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, ids=None, indent=None, languages=None, limit=None, prefix=None, query=None, types=None) -> web.Response:
    """kgsearch_entities_search

    Searches Knowledge Graph for entities that match the constraints. A list of matched entities will be returned in response, which will be in JSON-LD format and compatible with http://schema.org

    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param ids: The list of entity id to be used for search instead of query string. To specify multiple ids in the HTTP request, repeat the parameter in the URL as in ...?ids&#x3D;A&amp;ids&#x3D;B
    :type ids: List[str]
    :param indent: Enables indenting of json results.
    :type indent: bool
    :param languages: The list of language codes (defined in ISO 693) to run the query with, e.g. &#39;en&#39;.
    :type languages: List[str]
    :param limit: Limits the number of entities to be returned.
    :type limit: int
    :param prefix: Enables prefix match against names and aliases of entities
    :type prefix: bool
    :param query: The literal query string for search.
    :type query: str
    :param types: Restricts returned entities with these types, e.g. Person (as defined in http://schema.org/Person). If multiple types are specified, returned entities will contain one or more of these types.
    :type types: List[str]

    """
    return web.Response(status=200)
