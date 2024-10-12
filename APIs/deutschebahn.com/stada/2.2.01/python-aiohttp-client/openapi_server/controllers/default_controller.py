from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.s_zentrale_query import SZentraleQuery
from openapi_server.models.station_query import StationQuery
from openapi_server import util


async def stations_get(request: web.Request, offset=None, limit=None, searchstring=None, category=None, federalstate=None, eva=None, ril=None, logicaloperator=None) -> web.Response:
    """This operation provides the master data for german railway stations.

    Get a QueryResult object containing station objects from the database applying to the parameters described below.   QueryResult is a container providing the following information about the query result.   1. the total number of hits   2. the maximum number of hits to be returned in that QueryResult object   3. the offset of the first hit returned in that QueryResult object with respect to all hits returned by the query   4. the result objects    The parameters described below work as filters to reduce the number of hits returned. Some of these parameters must be used only once, others are allowed to be used multiple times. Valid parameters that are allowed to be used only once are _offset_, _limit_ and _logicaloperator_.   All other parameters described below may be used multiple times.  If a parameter is given more than once, the result will contain all hits that match all given parameter values.  E.g. _federalstate&#x3D;berlin&amp;federalstate&#x3D;saarland_ returns all stations in Berlin and Saarland.  If more than one filter criterion is used at the same time, the different filter criteria are interpreted as if they are combined by a logical AND operator, unless the parameter _logicaloperator_ is set to _or_.  E.g. _category&#x3D;1-2&amp;federalstate&#x3D;hamburg_ returns all stations in Hamburg having category 1 or 2.  _category&#x3D;1-2&amp;federalstate&#x3D;hamburg&amp;federalsate&#x3D;hessen_ returns all stations in Hamburg and Hessen having category 1 or 2, while  _searchstring&#x3D;berlin*&amp;federalstate&#x3D;hamburg&amp;federalsate&#x3D;hessen&amp;logicaloperator&#x3D;or_ will return all stations with a name starting with &#39;berlin&#39; as well as all stations in Hamburg and Hessen.  If no &#39;limit&#39; parameter is given, the number of hits (stations) is set to its maximum value of 10000.  To specify parameter values containing German umlauts, the following encoding has to be used   * ä  &#x3D;&gt; %C3%A4   * ö  &#x3D;&gt; %C3%B6   * ü  &#x3D;&gt; %C3%BC   * Ä  &#x3D;&gt; %C3%84   * Ö  &#x3D;&gt; %C3%96   * Ü  &#x3D;&gt; %C3%9C   * ß  &#x3D;&gt; %C3%9F 

    :param offset: Offset of the first hit returned in the QueryResult object with respect to all hits returned by the query. If this parameter is omitted, it will be set to 0 internally.
    :type offset: int
    :param limit: The maximum number of hits to be returned by that query. If &#39;limit&#39; is set greater than 10000, it will be reset to 10000 internally and only 10000 hits will be returned.
    :type limit: int
    :param searchstring: String to search for a station name. The wildcards * (indicating an arbitrary number of characters) and ? (indicating one single character) can be used in the search pattern. A comma separated list of station names is also supported (e.g. searchstring&#x3D;hamburg*,berlin*).
    :type searchstring: str
    :param category: Filter by station category. Category ranges are supported as well as lists of categories (e.g. category&#x3D;2-4 or category&#x3D;1,3-5). The category must be between 1 and 7 otherwise a parameter exception is returned.
    :type category: str
    :param federalstate: Filter by German federal state. Lists of federal states are also supported (e.g. federalstate&#x3D;bayern,hamburg). Wildcards are not allowed here.
    :type federalstate: str
    :param eva: Filter by EVA number. Wildcards are not allowed here.
    :type eva: int
    :param ril: Filter by Ril100-identifier. Wildcards are not allowed here.
    :type ril: str
    :param logicaloperator: Logical operator to combine query parameters (default&#x3D;AND). See above for further details.  Allowed values: or, and
    :type logicaloperator: str

    """
    return web.Response(status=200)


async def stations_id_get(request: web.Request, id) -> web.Response:
    """This operation provides the master data for a german railway station selected by its station-id.

    Get a QueryResult object containing one station object specified by its id.

    :param id: Station ID (Bahnhofsnummer)
    :type id: int

    """
    return web.Response(status=200)


async def szentralen_get(request: web.Request, offset=None, limit=None) -> web.Response:
    """This operation provides the master data for 3-S-Zentralen.

    Get a QueryResult object containing SZentralen objects from the database applying to the parameters described below.  QueryResult is a container providing the following information about the query result.   1. the total number of hits   2. the maximum number of hits to be returned in that QueryResult object   3. the offset of the first hit returned in that QueryResult object with respect to all hits returned by the query   4. the result objects 

    :param offset: Offset of the first hit returned in the QueryResult object with respect to all hits returned by the query. If this parameter is omitted, it will be set to 0 internally.
    :type offset: int
    :param limit: The maximum number of hits to be returned by that query. If &#39;limit&#39; is set greater than 10000, it will be reset to 10000 internally and only 100 hits will be returned.
    :type limit: int

    """
    return web.Response(status=200)


async def szentralen_id_get(request: web.Request, id) -> web.Response:
    """This operation provides the master data for 3-S-Zentralen select by its id.

    Get a QueryResult object containing one SZentralen object specified by its id. 

    :param id: id of the 3-S-Zentrale.
    :type id: int

    """
    return web.Response(status=200)
