from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def directions_output_format_get(request: web.Request, output_format, points, output_srs=None, criteria=None, distance_unit=None, round_trip=None, departure=None, correct_side=None, disable=None, route_description=None) -> web.Response:
    """Get the directions, path, distance and travel time between a series of geographic points

    Represents the turn-by-turn directions, geometry, distance, and time of the shortest path or fastest path between given start and end points

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
    :param correct_side: If true, route starts and ends on same side of road as start/end point.Default is false.
    :type correct_side: bool
    :param disable: A comma-separated list of time-related modules to disable (e.g., sc,tf,ev,td).&lt;br&gt;&lt;br&gt;Module names include:&lt;br&gt; sc – ferry schedules; disabled by default; disabled by default and only suitable for demos&lt;br&gt;tf – historic traffic congestion; disabled by default and only suitable for demos&lt;br&gt;ev – road events; disabled by default and only suitable for demos&lt;br&gt;td – time-dependency; disabling this disables sc, tf, and ev modules&lt;br&gt;tr – turn restrictions; if td is disabled, time-dependent turn restrictions are ignored&lt;br&gt;tc - turn costs (e.g., left turns take longer than right turns)
    :type disable: str
    :param route_description: Route description (e.g., Shortest route from 1002 Johnson St, Victoria to 1105 Royal Ave,New Westminster)
    :type route_description: str

    """
    departure = util.deserialize_datetime(departure)
    return web.Response(status=200)


async def directions_output_format_post(request: web.Request, output_format, points, output_srs=None, criteria=None, distance_unit=None, round_trip=None, departure=None, correct_side=None, disable=None, route_description=None) -> web.Response:
    """Get the directions, path, distance and travel time between a series of geographic points

    Represents the turn-by-turn directions, geometry, distance, and time of the shortest path or fastest path between given start and end points

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
    :param correct_side: If true, route starts and ends on same side of road as start/end point.Default is false.
    :type correct_side: bool
    :param disable: A comma-separated list of time-related modules to disable (e.g., sc,tf,ev,td).&lt;br&gt;&lt;br&gt;Module names include:&lt;br&gt; sc – ferry schedules; disabled by default; disabled by default and only suitable for demos&lt;br&gt;tf – historic traffic congestion; disabled by default and only suitable for demos&lt;br&gt;ev – road events; disabled by default and only suitable for demos&lt;br&gt;td – time-dependency; disabling this disables sc, tf, and ev modules&lt;br&gt;tr – turn restrictions; if td is disabled, time-dependent turn restrictions are ignored&lt;br&gt;tc - turn costs (e.g., left turns take longer than right turns)
    :type disable: str
    :param route_description: Route description (e.g., Shortest route from 1002 Johnson St, Victoria to 1105 Royal Ave,New Westminster)
    :type route_description: str

    """
    departure = util.deserialize_datetime(departure)
    return web.Response(status=200)


async def optimal_directions_output_format_get(request: web.Request, output_format, points, output_srs=None, criteria=None, distance_unit=None, round_trip=None, departure=None, correct_side=None, disable=None, route_description=None) -> web.Response:
    """Get the directions, optimal path, distance and travel time between a start point and a series of end points which are reordered to minimize total distance or time.

    Represents the turn-by-turn directions, geometry, distance, and time of the shortest path or fastest path between a start point and a series of end points which are reordered to minimize distance/time

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


async def optimal_directions_output_format_post(request: web.Request, output_format, points, output_srs=None, criteria=None, distance_unit=None, round_trip=None, departure=None, correct_side=None, disable=None, route_description=None) -> web.Response:
    """Get the directions, optimal path, distance and travel time between a start point and one or more end points which are reordered to minimize total distance or time.

    Represents the turn-by-turn directions, geometry, distance, and time of the shortest path or fastest path between a start point and one or more end points which are reordered to minimize distance or time.

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


async def truck_directions_output_format_get(request: web.Request, output_format, points, output_srs=None, criteria=None, distance_unit=None, round_trip=None, departure=None, correct_side=None, truck_route_multiplier=None, partition=None, disable=None, route_description=None) -> web.Response:
    """Get the directions, path, distance and travel time between a series of geographic points for a commercial vehicle

    Represents the turn-by-turn directions, geometry, distance, and time of the shortest path or fastest path between given start and end points for a commercial vehicle

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
    :param correct_side: If true, route starts and ends on same side of road as start/end point.Default is false.
    :type correct_side: bool
    :param truck_route_multiplier: The truck route multiplier value is used to multiply the cost of using roads that are not truck routes.
    :type truck_route_multiplier: int
    :param partition: A comma-separated list of values to identify sections of the route that correspond to truck route sections and non-truck route sections, ferry sections and non-ferry sections, and locality names.  The response includes a partitions attribute, which is an array of objects, each of which has an index (into the route coordinate array) and a value for each of the attributes requested in the partition parameter. Any or all of the following values can be used. &lt;br&gt;&lt;br&gt;Partition values:&lt;br&gt; isTruckRoute – Distinguish between truck route sections and non-truck route sections &lt;br&gt; isFerry – Distinguish between ferry sections and non-ferry sections &lt;br&gt; locality – Include the locality name for the route partition
    :type partition: str
    :param disable: A comma-separated list of time-related modules to disable (e.g., sc,tf,ev,td).&lt;br&gt;&lt;br&gt;Module names include:&lt;br&gt; sc – ferry schedules; disabled by default; disabled by default and only suitable for demos&lt;br&gt;tf – historic traffic congestion; disabled by default and only suitable for demos&lt;br&gt;ev – road events; disabled by default and only suitable for demos&lt;br&gt;td – time-dependency; disabling this disables sc, tf, and ev modules&lt;br&gt;tr – turn restrictions; if td is disabled, time-dependent turn restrictions are ignored&lt;br&gt;tc - turn costs (e.g., left turns take longer than right turns)
    :type disable: str
    :param route_description: Route description (e.g., Shortest route from 1002 Johnson St, Victoria to 1105 Royal Ave,New Westminster)
    :type route_description: str

    """
    departure = util.deserialize_datetime(departure)
    return web.Response(status=200)


async def truck_directions_output_format_post(request: web.Request, output_format, points, output_srs=None, criteria=None, distance_unit=None, round_trip=None, departure=None, correct_side=None, truck_route_multiplier=None, partition=None, disable=None, route_description=None) -> web.Response:
    """Get the directions, path, distance and travel time between a series of geographic points

    Represents the turn-by-turn directions, geometry, distance, and time of the shortest path or fastest path between given start and end points

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
    :param correct_side: If true, route starts and ends on same side of road as start/end point.Default is false.
    :type correct_side: bool
    :param truck_route_multiplier: The truck route multiplier value is used to multiply the cost of using roads that are not truck routes.
    :type truck_route_multiplier: int
    :param partition: A comma-separated list of values to identify sections of the route that correspond to truck route sections and non-truck route sections, ferry sections and non-ferry sections, and locality names.  The response includes a partitions attribute, which is an array of objects, each of which has an index (into the route coordinate array) and a value for each of the attributes requested in the partition parameter. Any or all of the following values can be used. &lt;br&gt;&lt;br&gt;Partition values:&lt;br&gt; isTruckRoute – Distinguish between truck route sections and non-truck route sections &lt;br&gt; isFerry – Distinguish between ferry sections and non-ferry sections &lt;br&gt; locality – Include the locality name for the route partition
    :type partition: str
    :param disable: A comma-separated list of time-related modules to disable (e.g., sc,tf,ev,td).&lt;br&gt;&lt;br&gt;Module names include:&lt;br&gt; sc – ferry schedules; disabled by default; disabled by default and only suitable for demos&lt;br&gt;tf – historic traffic congestion; disabled by default and only suitable for demos&lt;br&gt;ev – road events; disabled by default and only suitable for demos&lt;br&gt;td – time-dependency; disabling this disables sc, tf, and ev modules&lt;br&gt;tr – turn restrictions; if td is disabled, time-dependent turn restrictions are ignored&lt;br&gt;tc - turn costs (e.g., left turns take longer than right turns)
    :type disable: str
    :param route_description: Route description (e.g., Shortest route from 1002 Johnson St, Victoria to 1105 Royal Ave,New Westminster)
    :type route_description: str

    """
    departure = util.deserialize_datetime(departure)
    return web.Response(status=200)


async def truck_optimal_directions_output_format_get(request: web.Request, output_format, points, output_srs=None, criteria=None, distance_unit=None, round_trip=None, departure=None, correct_side=None, truck_route_multiplier=None, partition=None, disable=None, route_description=None) -> web.Response:
    """Get the directions, optimal path, distance and travel time between a start point and a series of end points which are reordered to minimize total distance or time for a commercial vehicle

    Represents the turn-by-turn directions, geometry, distance, and time of the shortest path or fastest path between a start point and a series of end points which are reordered to minimize distance/time for a commercial vehicle.

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
    :param partition: A comma-separated list of values to identify sections of the route that correspond to truck route sections and non-truck route sections, ferry sections and non-ferry sections, and locality names.  The response includes a partitions attribute, which is an array of objects, each of which has an index (into the route coordinate array) and a value for each of the attributes requested in the partition parameter. Any or all of the following values can be used. &lt;br&gt;&lt;br&gt;Partition values:&lt;br&gt; isTruckRoute – Distinguish between truck route sections and non-truck route sections &lt;br&gt; isFerry – Distinguish between ferry sections and non-ferry sections &lt;br&gt; locality – Include the locality name for the route partition
    :type partition: str
    :param disable: A comma-separated list of time-related modules to disable (e.g., sc,tf,ev,td).&lt;br&gt;&lt;br&gt;Module names include:&lt;br&gt; sc – ferry schedules; disabled by default; disabled by default and only suitable for demos&lt;br&gt;tf – historic traffic congestion; disabled by default and only suitable for demos&lt;br&gt;ev – road events; disabled by default and only suitable for demos&lt;br&gt;td – time-dependency; disabling this disables sc, tf, and ev modules&lt;br&gt;tr – turn restrictions; if td is disabled, time-dependent turn restrictions are ignored&lt;br&gt;tc - turn costs (e.g., left turns take longer than right turns)
    :type disable: str
    :param route_description: Route description (e.g., Shortest route from 1002 Johnson St, Victoria to 1105 Royal Ave,New Westminster)
    :type route_description: str

    """
    departure = util.deserialize_datetime(departure)
    return web.Response(status=200)


async def truck_optimal_directions_output_format_post(request: web.Request, output_format, points, output_srs=None, criteria=None, distance_unit=None, round_trip=None, departure=None, correct_side=None, truck_route_multiplier=None, partition=None, disable=None, route_description=None) -> web.Response:
    """Get the directions, optimal path, distance and travel time between a start point and one or more end points which are reordered to minimize total distance or time.

    Represents the turn-by-turn directions, geometry, distance, and time of the shortest path or fastest path between a start point and one or more end points which are reordered to minimize distance or time.

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
    :param partition: A comma-separated list of values to identify sections of the route that correspond to truck route sections and non-truck route sections, ferry sections and non-ferry sections, and locality names.  The response includes a partitions attribute, which is an array of objects, each of which has an index (into the route coordinate array) and a value for each of the attributes requested in the partition parameter. Any or all of the following values can be used. &lt;br&gt;&lt;br&gt;Partition values:&lt;br&gt; isTruckRoute – Distinguish between truck route sections and non-truck route sections &lt;br&gt; isFerry – Distinguish between ferry sections and non-ferry sections &lt;br&gt; locality – Include the locality name for the route partition
    :type partition: str
    :param disable: A comma-separated list of time-related modules to disable (e.g., sc,tf,ev,td).&lt;br&gt;&lt;br&gt;Module names include:&lt;br&gt; sc – ferry schedules; disabled by default; disabled by default and only suitable for demos&lt;br&gt;tf – historic traffic congestion; disabled by default and only suitable for demos&lt;br&gt;ev – road events; disabled by default and only suitable for demos&lt;br&gt;td – time-dependency; disabling this disables sc, tf, and ev modules&lt;br&gt;tr – turn restrictions; if td is disabled, time-dependent turn restrictions are ignored&lt;br&gt;tc - turn costs (e.g., left turns take longer than right turns)
    :type disable: str
    :param route_description: Route description (e.g., Shortest route from 1002 Johnson St, Victoria to 1105 Royal Ave,New Westminster)
    :type route_description: str

    """
    departure = util.deserialize_datetime(departure)
    return web.Response(status=200)
