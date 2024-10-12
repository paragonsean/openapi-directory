from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def distance_between_pairs_output_format_get(request: web.Request, output_format, from_points, to_points, output_srs=None, criteria=None, distance_unit=None, departure=None, correct_side=None, disable=None, route_description=None, max_pairs=None) -> web.Response:
    """Get distance and travel time between each pair of geographic points

    Represents the distance and time of the shortest or fastest paths between all pairs of fromPoints and toPoints. The number of fromPoints times the number of toPoints should not exceed 100 or the request will time out.

    :param output_format: Format of representation
    :type output_format: str
    :param from_points: A comma-separated list of origin points.  See &lt;a href&#x3D;https://github.com/bcgov/ols-router/blob/gh-pages/glossary.md#fromPoints target&#x3D;&#39;_blank&#39;&gt;fromPoints&lt;/a&gt;
    :type from_points: str
    :param to_points: A comma-separated list of destination points. See &lt;a href&#x3D;https://github.com/bcgov/ols-router/blob/gh-pages/glossary.md#toPoints target&#x3D;&#39;_blank&#39;&gt;toPoints&lt;/a&gt;
    :type to_points: str
    :param output_srs: The EPSG code of the spatial reference system (SRS) to use for output geometries. See &lt;a href&#x3D;https://github.com/bcgov/ols-router/blob/gh-pages/glossary.md#outputSRS target&#x3D;\&quot;_blank\&quot;&gt;outputSRS&lt;/a&gt;
    :type output_srs: int
    :param criteria: Routing criteria to optimize (e.g., shortest, fastest). Default is shortest.
    :type criteria: str
    :param distance_unit: distance unit of measure (e.g., km, mi). Default is km.
    :type distance_unit: str
    :param departure: departure date and time in internet timestamp notation as defined in RFC 3339, section 5.6 (e.g., 2019-02-28T11:36:00-08:00);&lt;br&gt; Ignored if time-dependency modules are disabled
    :type departure: str
    :param correct_side: If true, route starts and ends on same side of road as start and end points.Default is false.
    :type correct_side: bool
    :param disable: A comma-separated list of time-related modules to disable (e.g., sc,tf,ev,td).&lt;br&gt;&lt;br&gt;Module names include:&lt;br&gt; sc – ferry schedules; disabled by default; disabled by default and only suitable for demos&lt;br&gt;tf – historic traffic congestion; disabled by default and only suitable for demos&lt;br&gt;ev – road events; disabled by default and only suitable for demos&lt;br&gt;td – time-dependency; disabling this disables sc, tf, and ev modules&lt;br&gt;tr – turn restrictions; if td is disabled, time-dependent turn restrictions are ignored&lt;br&gt;tc - turn costs (e.g., left turns take longer than right turns)
    :type disable: str
    :param route_description: Route description (e.g., Shortest route from 1002 Johnson St, Victoria to 1105 Royal Ave,New Westminster)
    :type route_description: str
    :param max_pairs: The maximum number of pairs to return for each toPoint.  Pairs are ordered by distance/time from fromPoint. For example, given 1 fromPoint, and 10 toPoints, and maxPairs&#x3D;1 , return the nearest toPoint to the fromPoint. Given 3 fromPoints and 10 toPoints, maxPairs&#x3D;3 means return the 3 nearest toPoints to each fromPoint.
    :type max_pairs: int

    """
    departure = util.deserialize_datetime(departure)
    return web.Response(status=200)


async def distance_between_pairs_output_format_post(request: web.Request, output_format, from_points, to_points, output_srs=None, criteria=None, distance_unit=None, departure=None, correct_side=None, disable=None, route_description=None, max_pairs=None) -> web.Response:
    """Get distance and travel time between each pair of geographic points

    Represents the distance and time of the shortest or fastest paths between all pairs of fromPoints and toPoints. The number of fromPoints times the number of toPoints should not exceed 100 or the request will time out.

    :param output_format: Format of representation
    :type output_format: str
    :param from_points: A comma-separated list of origin points.  See &lt;a href&#x3D;https://github.com/bcgov/ols-router/blob/gh-pages/glossary.md#fromPoints target&#x3D;&#39;_blank&#39;&gt;fromPoints&lt;/a&gt;
    :type from_points: str
    :param to_points: A comma-separated list of destination points. See &lt;a href&#x3D;https://github.com/bcgov/ols-router/blob/gh-pages/glossary.md#toPoints target&#x3D;&#39;_blank&#39;&gt;toPoints&lt;/a&gt;
    :type to_points: str
    :param output_srs: The EPSG code of the spatial reference system (SRS) to use for output geometries. See &lt;a href&#x3D;https://github.com/bcgov/ols-router/blob/gh-pages/glossary.md#outputSRS target&#x3D;\&quot;_blank\&quot;&gt;outputSRS&lt;/a&gt;
    :type output_srs: int
    :param criteria: Routing criteria to optimize (e.g., shortest, fastest). Default is shortest.
    :type criteria: str
    :param distance_unit: distance unit of measure (e.g., km, mi). Default is km.
    :type distance_unit: str
    :param departure: departure date and time in internet timestamp notation as defined in RFC 3339, section 5.6 (e.g., 2019-02-28T11:36:00-08:00);&lt;br&gt; Ignored if time-dependency modules are disabled
    :type departure: str
    :param correct_side: If true, route starts and ends on same side of road as start and end points.Default is false.
    :type correct_side: bool
    :param disable: A comma-separated list of time-related modules to disable (e.g., sc,tf,ev,td).&lt;br&gt;&lt;br&gt;Module names include:&lt;br&gt; sc – ferry schedules; disabled by default; disabled by default and only suitable for demos&lt;br&gt;tf – historic traffic congestion; disabled by default and only suitable for demos&lt;br&gt;ev – road events; disabled by default and only suitable for demos&lt;br&gt;td – time-dependency; disabling this disables sc, tf, and ev modules&lt;br&gt;tr – turn restrictions; if td is disabled, time-dependent turn restrictions are ignored&lt;br&gt;tc - turn costs (e.g., left turns take longer than right turns)
    :type disable: str
    :param route_description: Route description (e.g., Shortest route from 1002 Johnson St, Victoria to 1105 Royal Ave,New Westminster)
    :type route_description: str
    :param max_pairs: The maximum number of pairs to return for each toPoint.  Pairs are ordered by distance/time from fromPoint. For example, given 1 fromPoint, and 10 toPoints, and maxPairs&#x3D;1 , return the nearest toPoint to the fromPoint. Given 3 fromPoints and 10 toPoints, maxPairs&#x3D;3 means return the 3 nearest toPoints to each fromPoint.
    :type max_pairs: int

    """
    departure = util.deserialize_datetime(departure)
    return web.Response(status=200)


async def distance_output_format_get(request: web.Request, output_format, points, output_srs=None, criteria=None, distance_unit=None, round_trip=None, departure=None, correct_side=None, disable=None, route_description=None) -> web.Response:
    """Get distance and travel time between two geographic points

    Represents the distance and time of the shortest or fastest path between given start and end points.

    :param output_format: Format of representation
    :type output_format: str
    :param points: A list of any number of route points in start to end order. See &lt;a href&#x3D;https://github.com/bcgov/ols-router/blob/gh-pages/glossary.md#points target&#x3D;&#39;_blank&#39;&gt;points&lt;/a&gt;
    :type points: str
    :param output_srs: The EPSG code of the spatial reference system (SRS) to use for output geometries. See &lt;a href&#x3D;https://github.com/bcgov/ols-router/blob/gh-pages/glossary.md#outputSRS target&#x3D;\&quot;_blank\&quot;&gt;outputSRS&lt;/a&gt;
    :type output_srs: int
    :param criteria: Routing criteria to optimize (e.g., shortest, fastest). Default is shortest.
    :type criteria: str
    :param distance_unit: distance unit of measure (e.g., km, mi). Default is km.
    :type distance_unit: str
    :param round_trip: If true, route ends at start point. Default is false.
    :type round_trip: bool
    :param departure: departure date and time in internet timestamp notation as defined in RFC 3339, section 5.6 (e.g., 2019-02-28T11:36:00-08:00);&lt;br&gt; Ignored if time-dependency modules are disabled
    :type departure: str
    :param correct_side: If true, route starts and ends on same side of road as start and end points.Default is false.
    :type correct_side: bool
    :param disable: A comma-separated list of time-related modules to disable (e.g., sc,tf,ev,td).&lt;br&gt;&lt;br&gt;Module names include:&lt;br&gt; sc – ferry schedules; disabled by default; disabled by default and only suitable for demos&lt;br&gt;tf – historic traffic congestion; disabled by default and only suitable for demos&lt;br&gt;ev – road events; disabled by default and only suitable for demos&lt;br&gt;td – time-dependency; disabling this disables sc, tf, and ev modules&lt;br&gt;tr – turn restrictions; if td is disabled, time-dependent turn restrictions are ignored&lt;br&gt;tc - turn costs (e.g., left turns take longer than right turns)
    :type disable: str
    :param route_description: Route description (e.g., Shortest route from 1002 Johnson St, Victoria to 1105 Royal Ave,New Westminster)
    :type route_description: str

    """
    departure = util.deserialize_datetime(departure)
    return web.Response(status=200)


async def distance_output_format_post(request: web.Request, output_format, points, output_srs=None, criteria=None, distance_unit=None, round_trip=None, departure=None, correct_side=None, disable=None, route_description=None) -> web.Response:
    """Get distance and travel time between two geographic points

    Represents the distance and time of the shortest or fastest path between given start and end points.

    :param output_format: Format of representation
    :type output_format: str
    :param points: A list of any number of route points in start to end order. See &lt;a href&#x3D;https://github.com/bcgov/ols-router/blob/gh-pages/glossary.md#points target&#x3D;&#39;_blank&#39;&gt;points&lt;/a&gt;
    :type points: str
    :param output_srs: The EPSG code of the spatial reference system (SRS) to use for output geometries. See &lt;a href&#x3D;https://github.com/bcgov/ols-router/blob/gh-pages/glossary.md#outputSRS target&#x3D;\&quot;_blank\&quot;&gt;outputSRS&lt;/a&gt;
    :type output_srs: int
    :param criteria: Routing criteria to optimize (e.g., shortest, fastest). Default is shortest.
    :type criteria: str
    :param distance_unit: distance unit of measure (e.g., km, mi). Default is km.
    :type distance_unit: str
    :param round_trip: If true, route ends at start point. Default is false.
    :type round_trip: bool
    :param departure: departure date and time in internet timestamp notation as defined in RFC 3339, section 5.6 (e.g., 2019-02-28T11:36:00-08:00);&lt;br&gt; Ignored if time-dependency modules are disabled
    :type departure: str
    :param correct_side: If true, route starts and ends on same side of road as start and end points.Default is false.
    :type correct_side: bool
    :param disable: A comma-separated list of time-related modules to disable (e.g., sc,tf,ev,td).&lt;br&gt;&lt;br&gt;Module names include:&lt;br&gt; sc – ferry schedules; disabled by default; disabled by default and only suitable for demos&lt;br&gt;tf – historic traffic congestion; disabled by default and only suitable for demos&lt;br&gt;ev – road events; disabled by default and only suitable for demos&lt;br&gt;td – time-dependency; disabling this disables sc, tf, and ev modules&lt;br&gt;tr – turn restrictions; if td is disabled, time-dependent turn restrictions are ignored&lt;br&gt;tc - turn costs (e.g., left turns take longer than right turns)
    :type disable: str
    :param route_description: Route description (e.g., Shortest route from 1002 Johnson St, Victoria to 1105 Royal Ave,New Westminster)
    :type route_description: str

    """
    departure = util.deserialize_datetime(departure)
    return web.Response(status=200)


async def truck_distance_between_pairs_output_format_get(request: web.Request, output_format, from_points, to_points, output_srs=None, criteria=None, distance_unit=None, departure=None, correct_side=None, disable=None, route_description=None, max_pairs=None) -> web.Response:
    """Get distance and travel time between each pair of geographic points for a commercial vehicle

    Represents the distance and time of the shortest or fastest paths between all pairs of fromPoints and toPoints for a commercial vehicle. The number of fromPoints times the number of toPoints should not exceed 100 or the request will time out.

    :param output_format: Format of representation
    :type output_format: str
    :param from_points: A comma-separated list of origin points.  See &lt;a href&#x3D;https://github.com/bcgov/ols-router/blob/gh-pages/glossary.md#fromPoints target&#x3D;&#39;_blank&#39;&gt;fromPoints&lt;/a&gt;
    :type from_points: str
    :param to_points: A comma-separated list of destination points. See &lt;a href&#x3D;https://github.com/bcgov/ols-router/blob/gh-pages/glossary.md#toPoints target&#x3D;&#39;_blank&#39;&gt;toPoints&lt;/a&gt;
    :type to_points: str
    :param output_srs: The EPSG code of the spatial reference system (SRS) to use for output geometries. See &lt;a href&#x3D;https://github.com/bcgov/ols-router/blob/gh-pages/glossary.md#outputSRS target&#x3D;\&quot;_blank\&quot;&gt;outputSRS&lt;/a&gt;
    :type output_srs: int
    :param criteria: Routing criteria to optimize (e.g., shortest, fastest). Default is shortest.
    :type criteria: str
    :param distance_unit: distance unit of measure (e.g., km, mi). Default is km.
    :type distance_unit: str
    :param departure: departure date and time in internet timestamp notation as defined in RFC 3339, section 5.6 (e.g., 2019-02-28T11:36:00-08:00);&lt;br&gt; Ignored if time-dependency modules are disabled
    :type departure: str
    :param correct_side: If true, route starts and ends on same side of road as start and end points.Default is false.
    :type correct_side: bool
    :param disable: A comma-separated list of time-related modules to disable (e.g., sc,tf,ev,td).&lt;br&gt;&lt;br&gt;Module names include:&lt;br&gt; sc – ferry schedules; disabled by default; disabled by default and only suitable for demos&lt;br&gt;tf – historic traffic congestion; disabled by default and only suitable for demos&lt;br&gt;ev – road events; disabled by default and only suitable for demos&lt;br&gt;td – time-dependency; disabling this disables sc, tf, and ev modules&lt;br&gt;tr – turn restrictions; if td is disabled, time-dependent turn restrictions are ignored&lt;br&gt;tc - turn costs (e.g., left turns take longer than right turns)
    :type disable: str
    :param route_description: Route description (e.g., Shortest route from 1002 Johnson St, Victoria to 1105 Royal Ave,New Westminster)
    :type route_description: str
    :param max_pairs: The maximum number of pairs to return for each toPoint.  Pairs are ordered by distance/time from fromPoint. For example, given 1 fromPoint, and 10 toPoints, and maxPairs&#x3D;1 , return the nearest toPoint to the fromPoint. Given 3 fromPoints and 10 toPoints, maxPairs&#x3D;3 means return the 3 nearest toPoints to each fromPoint.
    :type max_pairs: int

    """
    departure = util.deserialize_datetime(departure)
    return web.Response(status=200)


async def truck_distance_between_pairs_output_format_post(request: web.Request, output_format, from_points, to_points, output_srs=None, criteria=None, distance_unit=None, departure=None, correct_side=None, disable=None, route_description=None, max_pairs=None) -> web.Response:
    """Get distance and travel time between each pair of geographic points

    Represents the distance and time of the shortest or fastest paths between all pairs of fromPoints and toPoints. The number of fromPoints times the number of toPoints should not exceed 100 or the request will time out.

    :param output_format: Format of representation
    :type output_format: str
    :param from_points: A comma-separated list of origin points.  See &lt;a href&#x3D;https://github.com/bcgov/ols-router/blob/gh-pages/glossary.md#fromPoints target&#x3D;&#39;_blank&#39;&gt;fromPoints&lt;/a&gt;
    :type from_points: str
    :param to_points: A comma-separated list of destination points. See &lt;a href&#x3D;https://github.com/bcgov/ols-router/blob/gh-pages/glossary.md#toPoints target&#x3D;&#39;_blank&#39;&gt;toPoints&lt;/a&gt;
    :type to_points: str
    :param output_srs: The EPSG code of the spatial reference system (SRS) to use for output geometries. See &lt;a href&#x3D;https://github.com/bcgov/ols-router/blob/gh-pages/glossary.md#outputSRS target&#x3D;\&quot;_blank\&quot;&gt;outputSRS&lt;/a&gt;
    :type output_srs: int
    :param criteria: Routing criteria to optimize (e.g., shortest, fastest). Default is shortest.
    :type criteria: str
    :param distance_unit: distance unit of measure (e.g., km, mi). Default is km.
    :type distance_unit: str
    :param departure: departure date and time in internet timestamp notation as defined in RFC 3339, section 5.6 (e.g., 2019-02-28T11:36:00-08:00);&lt;br&gt; Ignored if time-dependency modules are disabled
    :type departure: str
    :param correct_side: If true, route starts and ends on same side of road as start and end points.Default is false.
    :type correct_side: bool
    :param disable: A comma-separated list of time-related modules to disable (e.g., sc,tf,ev,td).&lt;br&gt;&lt;br&gt;Module names include:&lt;br&gt; sc – ferry schedules; disabled by default; disabled by default and only suitable for demos&lt;br&gt;tf – historic traffic congestion; disabled by default and only suitable for demos&lt;br&gt;ev – road events; disabled by default and only suitable for demos&lt;br&gt;td – time-dependency; disabling this disables sc, tf, and ev modules&lt;br&gt;tr – turn restrictions; if td is disabled, time-dependent turn restrictions are ignored&lt;br&gt;tc - turn costs (e.g., left turns take longer than right turns)
    :type disable: str
    :param route_description: Route description (e.g., Shortest route from 1002 Johnson St, Victoria to 1105 Royal Ave,New Westminster)
    :type route_description: str
    :param max_pairs: The maximum number of pairs to return for each toPoint.  Pairs are ordered by distance/time from fromPoint. For example, given 1 fromPoint, and 10 toPoints, and maxPairs&#x3D;1 , return the nearest toPoint to the fromPoint. Given 3 fromPoints and 10 toPoints, maxPairs&#x3D;3 means return the 3 nearest toPoints to each fromPoint.
    :type max_pairs: int

    """
    departure = util.deserialize_datetime(departure)
    return web.Response(status=200)


async def truck_distance_output_format_get(request: web.Request, output_format, points, output_srs=None, criteria=None, distance_unit=None, round_trip=None, departure=None, correct_side=None, truck_route_multiplier=None, disable=None, route_description=None) -> web.Response:
    """Get distance and travel time between two geographic points for a commercial vehicle

    Represents the distance and time of the shortest or fastest path between given start and end points.

    :param output_format: Format of representation
    :type output_format: str
    :param points: A list of any number of route points in start to end order. See &lt;a href&#x3D;https://github.com/bcgov/ols-router/blob/gh-pages/glossary.md#points target&#x3D;&#39;_blank&#39;&gt;points&lt;/a&gt;
    :type points: str
    :param output_srs: The EPSG code of the spatial reference system (SRS) to use for output geometries. See &lt;a href&#x3D;https://github.com/bcgov/ols-router/blob/gh-pages/glossary.md#outputSRS target&#x3D;\&quot;_blank\&quot;&gt;outputSRS&lt;/a&gt;
    :type output_srs: int
    :param criteria: Routing criteria to optimize (e.g., shortest, fastest). Default is shortest.
    :type criteria: str
    :param distance_unit: distance unit of measure (e.g., km, mi). Default is km.
    :type distance_unit: str
    :param round_trip: If true, route ends at start point. Default is false.
    :type round_trip: bool
    :param departure: departure date and time in internet timestamp notation as defined in RFC 3339, section 5.6 (e.g., 2019-02-28T11:36:00-08:00);&lt;br&gt; Ignored if time-dependency modules are disabled
    :type departure: str
    :param correct_side: If true, route starts and ends on same side of road as start and end points.Default is false.
    :type correct_side: bool
    :param truck_route_multiplier: The truck route multiplier value is used to multiply the cost of using roads that are not truck routes.
    :type truck_route_multiplier: int
    :param disable: A comma-separated list of time-related modules to disable (e.g., sc,tf,ev,td).&lt;br&gt;&lt;br&gt;Module names include:&lt;br&gt; sc – ferry schedules; disabled by default; disabled by default and only suitable for demos&lt;br&gt;tf – historic traffic congestion; disabled by default and only suitable for demos&lt;br&gt;ev – road events; disabled by default and only suitable for demos&lt;br&gt;td – time-dependency; disabling this disables sc, tf, and ev modules&lt;br&gt;tr – turn restrictions; if td is disabled, time-dependent turn restrictions are ignored&lt;br&gt;tc - turn costs (e.g., left turns take longer than right turns)
    :type disable: str
    :param route_description: Route description (e.g., Shortest route from 1002 Johnson St, Victoria to 1105 Royal Ave,New Westminster)
    :type route_description: str

    """
    departure = util.deserialize_datetime(departure)
    return web.Response(status=200)


async def truck_distance_output_format_post(request: web.Request, output_format, points, output_srs=None, criteria=None, distance_unit=None, round_trip=None, departure=None, correct_side=None, disable=None, route_description=None) -> web.Response:
    """Get distance and travel time between two geographic points

    Represents the distance and time of the shortest or fastest path between given start and end points.

    :param output_format: Format of representation
    :type output_format: str
    :param points: A list of any number of route points in start to end order. See &lt;a href&#x3D;https://github.com/bcgov/ols-router/blob/gh-pages/glossary.md#points target&#x3D;&#39;_blank&#39;&gt;points&lt;/a&gt;
    :type points: str
    :param output_srs: The EPSG code of the spatial reference system (SRS) to use for output geometries. See &lt;a href&#x3D;https://github.com/bcgov/ols-router/blob/gh-pages/glossary.md#outputSRS target&#x3D;\&quot;_blank\&quot;&gt;outputSRS&lt;/a&gt;
    :type output_srs: int
    :param criteria: Routing criteria to optimize (e.g., shortest, fastest). Default is shortest.
    :type criteria: str
    :param distance_unit: distance unit of measure (e.g., km, mi). Default is km.
    :type distance_unit: str
    :param round_trip: If true, route ends at start point. Default is false.
    :type round_trip: bool
    :param departure: departure date and time in internet timestamp notation as defined in RFC 3339, section 5.6 (e.g., 2019-02-28T11:36:00-08:00);&lt;br&gt; Ignored if time-dependency modules are disabled
    :type departure: str
    :param correct_side: If true, route starts and ends on same side of road as start and end points.Default is false.
    :type correct_side: bool
    :param disable: A comma-separated list of time-related modules to disable (e.g., sc,tf,ev,td).&lt;br&gt;&lt;br&gt;Module names include:&lt;br&gt; sc – ferry schedules; disabled by default; disabled by default and only suitable for demos&lt;br&gt;tf – historic traffic congestion; disabled by default and only suitable for demos&lt;br&gt;ev – road events; disabled by default and only suitable for demos&lt;br&gt;td – time-dependency; disabling this disables sc, tf, and ev modules&lt;br&gt;tr – turn restrictions; if td is disabled, time-dependent turn restrictions are ignored&lt;br&gt;tc - turn costs (e.g., left turns take longer than right turns)
    :type disable: str
    :param route_description: Route description (e.g., Shortest route from 1002 Johnson St, Victoria to 1105 Royal Ave,New Westminster)
    :type route_description: str

    """
    departure = util.deserialize_datetime(departure)
    return web.Response(status=200)
