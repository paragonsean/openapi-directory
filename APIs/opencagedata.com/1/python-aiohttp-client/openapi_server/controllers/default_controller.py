from typing import List, Dict
from aiohttp import web

from openapi_server.models.response import Response
from openapi_server import util


async def vversion_format_get(request: web.Request, version, format, q, key, abbrv=None, address_only=None, add_request=None, bounds=None, countrycode=None, jsonp=None, language=None, limit=None, min_confidence=None, no_annotations=None, no_dedupe=None, no_record=None, pretty=None, proximity=None, roadinfo=None) -> web.Response:
    """vversion_format_get

    geocode a query

    :param version: API version.
    :type version: int
    :param format: format of the response. One of &#39;json&#39;, &#39;xml&#39; or &#39;map&#39;.
    :type format: str
    :param q: string or lat,lng to be geocoded.
    :type q: str
    :param key: an application key.
    :type key: str
    :param abbrv: when true we attempt to abbreviate the formatted field of results.
    :type abbrv: bool
    :param address_only: when true we include only address details in the formatted field of results.
    :type address_only: bool
    :param add_request: if true the request is included in the response.
    :type add_request: bool
    :param bounds: four coordinate points forming the south-west and north-east corners of a bounding box (min long, min lat, max long, max lat).
    :type bounds: str
    :param countrycode: two letter code ISO 3166-1 Alpha 2 code to limit results to that country.
    :type countrycode: str
    :param jsonp: wraps the returned JSON with a function name.
    :type jsonp: str
    :param language: an IETF format language code (ex: &#39;es&#39; or &#39;pt-BR&#39;).
    :type language: str
    :param limit: maximum number of results to return. Default is 10. Maximum is 100.
    :type limit: int
    :param min_confidence: integer from 1-10. Only results with at least this confidence are returned.
    :type min_confidence: int
    :param no_annotations: when true annotations are not added to results.
    :type no_annotations: bool
    :param no_dedupe: when true results are not deduplicated.
    :type no_dedupe: bool
    :param no_record: when true query content is not logged.
    :type no_record: bool
    :param pretty: when true results are pretty printed. Useful for debugging.
    :type pretty: bool
    :param proximity: lat,lng to bias results.
    :type proximity: str
    :param roadinfo: match nearest road, include roadinfo annotation
    :type roadinfo: bool

    """
    return web.Response(status=200)
