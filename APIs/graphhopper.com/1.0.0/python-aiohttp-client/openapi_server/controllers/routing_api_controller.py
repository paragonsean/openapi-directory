from typing import List, Dict
from aiohttp import web

from openapi_server.models.gh_error import GHError
from openapi_server.models.info_response import InfoResponse
from openapi_server.models.route_request import RouteRequest
from openapi_server.models.route_response import RouteResponse
from openapi_server.models.vehicle_profile_id import VehicleProfileId
from openapi_server import util


async def get_route(request: web.Request, point, point_hint=None, snap_prevention=None, vehicle=None, curbside=None, turn_costs=None, locale=None, elevation=None, details=None, optimize=None, instructions=None, calc_points=None, debug=None, points_encoded=None, ch_disable=None, weighting=None, heading=None, heading_penalty=None, pass_through=None, block_area=None, avoid=None, algorithm=None, round_trip_distance=None, round_trip_seed=None, alternative_route_max_paths=None, alternative_route_max_weight_factor=None, alternative_route_max_share_factor=None) -> web.Response:
    """GET Route Endpoint

    The GET request is the most simple one: just specify the parameter in the URL and you are done. Can be tried directly in every browser. 

    :param point: The points for which the route should be calculated. Format: &#x60;[latitude,longitude]&#x60;. Specify at least an origin and a destination. Via points are possible. The maximum number depends on your plan. 
    :type point: List[str]
    :param point_hint: The &#x60;point_hint&#x60; is typically a road name to which the associated &#x60;point&#x60; parameter should be snapped to. Specify no &#x60;point_hint&#x60; parameter or the same number as you have &#x60;point&#x60; parameters. 
    :type point_hint: List[str]
    :param snap_prevention: Optional parameter to avoid snapping to a certain road class or road environment. Currently supported values are &#x60;motorway&#x60;, &#x60;trunk&#x60;, &#x60;ferry&#x60;, &#x60;tunnel&#x60;, &#x60;bridge&#x60; and &#x60;ford&#x60;. Multiple values are specified like &#x60;snap_prevention&#x3D;ferry&amp;snap_prevention&#x3D;motorway&#x60;. 
    :type snap_prevention: List[str]
    :param vehicle: The vehicle profile for which the route should be calculated. 
    :type vehicle: dict | bytes
    :param curbside: Optional parameter. It specifies on which side a point should be relative to the driver when she leaves/arrives at a start/target/via point. You need to specify this parameter for either none or all points. Only supported for motor vehicles and OpenStreetMap. 
    :type curbside: List[str]
    :param turn_costs: Specifies if turn restrictions should be considered. Enabling this option increases the route computation time. Only supported for motor vehicles and OpenStreetMap. 
    :type turn_costs: bool
    :param locale: The locale of the resulting turn instructions. E.g. &#x60;pt_PT&#x60; for Portuguese or &#x60;de&#x60; for German. 
    :type locale: str
    :param elevation: If &#x60;true&#x60;, a third coordinate, the altitude, is included with all positions in the response. This changes the format of the &#x60;points&#x60; and &#x60;snapped_waypoints&#x60; fields of the response, in both their encodings. Unless you switch off the &#x60;points_encoded&#x60; parameter, you need special code on the client side that can handle three-dimensional coordinates. A request can fail if the vehicle profile does not support elevation. See the features object for every vehicle profile. 
    :type elevation: bool
    :param details: Optional parameter to retrieve path details. You can request additional details for the route: &#x60;street_name&#x60;,  &#x60;time&#x60;, &#x60;distance&#x60;, &#x60;max_speed&#x60;, &#x60;toll&#x60;, &#x60;road_class&#x60;, &#x60;road_class_link&#x60;, &#x60;road_access&#x60;, &#x60;road_environment&#x60;, &#x60;lanes&#x60;, and &#x60;surface&#x60;. Read more about the usage of path details [here](https://discuss.graphhopper.com/t/2539). 
    :type details: List[str]
    :param optimize: Normally, the calculated route will visit the points in the order you specified them. If you have more than two points, you can set this parameter to &#x60;\&quot;true\&quot;&#x60; and the points may be re-ordered to minimize the total travel time. Keep in mind that the limits on the number of locations of the Route Optimization API applies, and the request costs more credits. 
    :type optimize: str
    :param instructions: If instructions should be calculated and returned 
    :type instructions: bool
    :param calc_points: If the points for the route should be calculated at all. 
    :type calc_points: bool
    :param debug: If &#x60;true&#x60;, the output will be formatted. 
    :type debug: bool
    :param points_encoded: Allows changing the encoding of location data in the response. The default is polyline encoding, which is compact but requires special client code to unpack. (We provide it in our JavaScript client library!) Set this parameter to &#x60;false&#x60; to switch the encoding to simple coordinate pairs like &#x60;[lon,lat]&#x60;, or &#x60;[lon,lat,elevation]&#x60;. See the description of the response format for more information. 
    :type points_encoded: bool
    :param ch_disable: Use this parameter in combination with one or more parameters from below. 
    :type ch_disable: bool
    :param weighting: Determines the way the \&quot;best\&quot; route is calculated. Besides &#x60;fastest&#x60; you can use &#x60;short_fastest&#x60; which finds a reasonable balance between the distance influence (&#x60;shortest&#x60;) and the time (&#x60;fastest&#x60;). You could also use &#x60;shortest&#x60; but is deprecated and not recommended for motor vehicles. All except &#x60;fastest&#x60; require &#x60;ch.disable&#x3D;true&#x60;. 
    :type weighting: str
    :param heading: Favour a heading direction for a certain point. Specify either one heading for the start point or as many as there are points. In this case headings are associated by their order to the specific points. Headings are given as north based clockwise angle between 0 and 360 degree. This parameter also influences the tour generated with &#x60;algorithm&#x3D;round_trip&#x60; and forces the initial direction.  Requires &#x60;ch.disable&#x3D;true&#x60;. 
    :type heading: List[int]
    :param heading_penalty: Time penalty in seconds for not obeying a specified heading. Requires &#x60;ch.disable&#x3D;true&#x60;. 
    :type heading_penalty: int
    :param pass_through: If &#x60;true&#x60;, u-turns are avoided at via-points with regard to the &#x60;heading_penalty&#x60;. Requires &#x60;ch.disable&#x3D;true&#x60;. 
    :type pass_through: bool
    :param block_area: Block road access by specifying a point close to the road segment to be blocked, with the format &#x60;lat,lon&#x60;. You can also block all road segments crossing a geometric shape. Specify a circle using the format &#x60;lat,lon,radius&#x60;, or a polygon using the format &#x60;lat1,lon1,lat2,lon2,...,latN,lonN&#x60;. You can specify several shapes, separating them with &#x60;;&#x60;. Requires &#x60;ch.disable&#x3D;true&#x60;. 
    :type block_area: str
    :param avoid: Specify which road classes and environments you would like to avoid.  Possible values are &#x60;motorway&#x60;, &#x60;steps&#x60;, &#x60;track&#x60;, &#x60;toll&#x60;, &#x60;ferry&#x60;, &#x60;tunnel&#x60; and &#x60;bridge&#x60;. Separate several values with &#x60;;&#x60;. Obviously not all the values make sense for all vehicle profiles e.g. &#x60;bike&#x60; is already forbidden on a &#x60;motorway&#x60;. Requires &#x60;ch.disable&#x3D;true&#x60;. 
    :type avoid: str
    :param algorithm: Rather than looking for the shortest or fastest path, this parameter lets you solve two different problems related to routing: With &#x60;alternative_route&#x60;, we give you not one but several routes that are close to optimal, but not too similar to each other.  With &#x60;round_trip&#x60;, the route will get you back to where you started. This is meant for fun (think of a bike trip), so we will add some randomness. The &#x60;round_trip&#x60; option requires &#x60;ch.disable&#x3D;true&#x60;. You can control both of these features with additional parameters, see below.  
    :type algorithm: str
    :param round_trip_distance: If &#x60;algorithm&#x3D;round_trip&#x60;, this parameter configures approximative length of the resulting round trip. Requires &#x60;ch.disable&#x3D;true&#x60;. 
    :type round_trip_distance: int
    :param round_trip_seed: If &#x60;algorithm&#x3D;round_trip&#x60;, this sets the random seed. Change this to get a different tour for each value. 
    :type round_trip_seed: int
    :param alternative_route_max_paths: If &#x60;algorithm&#x3D;alternative_route&#x60;, this parameter sets the number of maximum paths which should be calculated. Increasing can lead to worse alternatives. 
    :type alternative_route_max_paths: int
    :param alternative_route_max_weight_factor: If &#x60;algorithm&#x3D;alternative_route&#x60;, this parameter sets the factor by which the alternatives routes can be longer than the optimal route. Increasing can lead to worse alternatives. 
    :type alternative_route_max_weight_factor: 
    :param alternative_route_max_share_factor: If &#x60;algorithm&#x3D;alternative_route&#x60;, this parameter specifies how similar an alternative route can be to the optimal route. Increasing can lead to worse alternatives. 
    :type alternative_route_max_share_factor: 

    """
    vehicle = .from_dict(vehicle)
    return web.Response(status=200)


async def post_route(request: web.Request, body=None) -> web.Response:
    """POST Route Endpoint

    Please see the [GET endpoint](#operation/getRoute) for a simpler method on how to get started. If you are familiar with POST requests and JSON then do not hesitate to continue here.  Especially when you use many locations you should get familiar with this POST endpoint as the GET endpoint has an URL length limitation. Additionally the request of this POST endpoint can be compressed and can slightly speed up the request.  To do a request you send JSON data. Both request scenarios GET and POST are identical except that all singular parameter names are named as their plural for a POST request. The effected parameters are: &#x60;points&#x60;, &#x60;point_hints&#x60; and &#x60;snap_preventions&#x60;.  **Please note that in opposite to the GET endpoint, points are specified in the order of &#x60;longitude, latitude&#x60;**.  For example &#x60;point&#x3D;10,11&amp;point&#x3D;20,22&#x60; will be converted to the &#x60;points&#x60; array (plural): &#x60;&#x60;&#x60;json { \&quot;points\&quot;: [[11,10], [22,20]] } &#x60;&#x60;&#x60; Note again that also the order changes from &#x60;[latitude,longitude]&#x60; to &#x60;[longitude,latitude]&#x60; similar to [GeoJson](http://geojson.org/geojson-spec.html#examples).  Example: &#x60;&#x60;&#x60;bash curl -X POST -H \&quot;Content-Type: application/json\&quot; \&quot;https://graphhopper.com/api/1/route?key&#x3D;[YOUR_KEY]\&quot; -d &#39;{\&quot;elevation\&quot;:false,\&quot;points\&quot;:[[-0.087891,51.534377],[-0.090637,51.467697]],\&quot;vehicle\&quot;:\&quot;car\&quot;}&#39; &#x60;&#x60;&#x60; 

    :param body: 
    :type body: dict | bytes

    """
    body = RouteRequest.from_dict(body)
    return web.Response(status=200)


async def route_info_get(request: web.Request, ) -> web.Response:
    """Coverage information

    Use this to find out details about the supported vehicle profiles and features, or if you just need to ping the server. 


    """
    return web.Response(status=200)
