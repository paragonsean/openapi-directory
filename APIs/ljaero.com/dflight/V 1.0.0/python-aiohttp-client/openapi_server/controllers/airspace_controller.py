from typing import List, Dict
from aiohttp import web

from openapi_server.models.airspace_by_distance import AirspaceByDistance
from openapi_server.models.airspace_by_polygon import AirspaceByPolygon
from openapi_server.models.airspace_by_route import AirspaceByRoute
from openapi_server.models.airspace_distance_response import AirspaceDistanceResponse
from openapi_server.models.airspace_poly_response import AirspacePolyResponse
from openapi_server.models.airspace_route_response import AirspaceRouteResponse
from openapi_server.models.http_validation_error import HTTPValidationError
from openapi_server import util


async def asp_by_distance_us_v1_airspace_distance_query_post(request: web.Request, body, x_api_key=None) -> web.Response:
    """Retrieve all requested types of airspace located within given distance of location.

    Retrieve selected types of airspace existing within given distance from a point. Request body parameters are: * latitude:  WGS84 latitude coordinate of your selected point, in decimal degrees * longitude:  WGS84 longitude coordinate of your selected point, in decimal degrees * distance:  distance in meters (max allowed value is 25000) * asptypes:  list of one or more airspace types you wish to retrieve. Allowed values are &#39;CAS&#39;, &#39;SUA&#39;, &#39;MAA&#39;, and &#39;MTR&#39;.  Successful requests return a list of GeoJSON FeatureCollections, one for each Airspace type indicated in the request. Within each feature collection, there will be a separate Feature for each Airspace instance found. All Features will include a property indicating the *airspace_type*. Additional properties for each *airspace_type* are as follows: * CAS (Controlled Airspace)     - *name*     - *cas_class*: B, C, D, or E2     - *floor*: integer value in ft MSL     - *ceiling*: integer value in ft MSL     - *lannc*: true/false indicating whether or not authorization for this airspace may be obtained via LAANC * SUA (Special Use Airspace)     - *name*     - *sua_type*: AA &#x3D; Alert Area, MOA &#x3D; Military Operations Area, NSA &#x3D; National Security Area, PA &#x3D; Prohibited Area, RA &#x3D; Restricted Area, WA &#x3D; Warning Area     - *floor*: lower limit of the airspace     - *floor_uom*: unit of measure used for the numeric floor value: FT (feet) or FL (flight level)     - *floor_ref*: reference level used for the numeric floor value: AGL, MSL, or STD (standard atmosphere, used for flight level values)     - *ceiling*: upper limit of the airspace     - *ceiling_uom*: unit of measure used for the numeric floor value: FT (feet) or FL (flight level)     - *ceiling_ref*: reference level used for the numeric ceiling value: AGL, MSL, or STD (standard atmosphere, used for flight level values)     - *ceiling_ref*: reference level used for the numeric ceiling value: AGL, MSL, or STD (standard atmosphere, used for flight level values)     - *schedule*: default activation days/times (other times by NOTAM) * MAA (Miscellaneous Activity Area)     - *name*     - *maa_type*: one of the following - ULTRALIGHT, PARACHUTE JUMP AREA, AEROBATIC PRACTICE, GLIDER, HANG GLIDER, SPACE LAUNCH ACTIVITY     - *use_times*: textual description of days/times when activity in the area should be expected * MTR (Military Training Route)     - *name*     - *use_times*: textual description of days/times when MTR is active/hot     - *terrain_following*: boolean value indicating whether terrain following activity occurs on the route     - *max_extent_nm*: maximum distance that aircraft can deviate from route centerline

    :param body: 
    :type body: dict | bytes
    :param x_api_key: 
    :type x_api_key: str

    """
    body = AirspaceByDistance.from_dict(body)
    return web.Response(status=200)


async def asp_by_poly_us_v1_airspace_polygon_query_post(request: web.Request, body, x_api_key=None) -> web.Response:
    """Retrieve all requested types of airspace located within given GeoJSON Polygon.

    Retrieve selected types of airspace located within given area. Request body parameters are: * poly:  [GeoJSON Polygon](https://www.rfc-editor.org/rfc/rfc7946.html#appendix-A) defining the area. Max allowed area is 1000 km^2. * asptypes:  list of one or more airspace types you wish to retrieve. Allowed values are &#39;CAS&#39;, &#39;SUA&#39;, &#39;MAA&#39;, and &#39;MTR&#39;.  Successful requests return a list of GeoJSON FeatureCollections, one for each Airspace type indicated in the request. Within each feature collection, there will be a separate Feature for each Airspace instance found. All Features will include a property indicating the *airspace_type*. Additional properties for each *airspace_type* are as follows: * CAS (Controlled Airspace)     - *name*     - *cas_class*: B, C, D, or E2     - *floor*: integer value in ft MSL     - *ceiling*: integer value in ft MSL     - *lannc*: true/false indicating whether or not authorization for this airspace may be obtained via LAANC * SUA (Special Use Airspace)     - *name*     - *sua_type*: AA &#x3D; Alert Area, MOA &#x3D; Military Operations Area, NSA &#x3D; National Security Area, PA &#x3D; Prohibited Area, RA &#x3D; Restricted Area, WA &#x3D; Warning Area     - *floor*: lower limit of the airspace     - *floor_uom*: unit of measure used for the numeric floor value: FT (feet) or FL (flight level)     - *floor_ref*: reference level used for the numeric floor value: AGL, MSL, or STD (standard atmosphere, used for flight level values)     - *ceiling*: upper limit of the airspace     - *ceiling_uom*: unit of measure used for the numeric floor value: FT (feet) or FL (flight level)     - *ceiling_ref*: reference level used for the numeric ceiling value: AGL, MSL, or STD (standard atmosphere, used for flight level values)     - *schedule*: default activation days/times (other times by NOTAM) * MAA (Miscellaneous Activity Area)     - *name*     - *maa_type*: one of the following - ULTRALIGHT, PARACHUTE JUMP AREA, AEROBATIC PRACTICE, GLIDER, HANG GLIDER, SPACE LAUNCH ACTIVITY     - *use_times*: textual description of days/times when activity in the area should be expected * MTR (Military Training Route)     - *name*     - *use_times*: textual description of days/times when MTR is active/hot     - *terrain_following*: boolean value indicating whether terrain following activity occurs on the route     - *max_extent_nm*: maximum distance that aircraft can deviate from route centerline

    :param body: 
    :type body: dict | bytes
    :param x_api_key: 
    :type x_api_key: str

    """
    body = AirspaceByPolygon.from_dict(body)
    return web.Response(status=200)


async def asp_by_route_us_v1_airspace_route_query_post(request: web.Request, body, x_api_key=None) -> web.Response:
    """Retrieve all requested types of airspace traversed by route.

    Retrieve selected types of airspace traversed by route. Request body parameters are: * route:  [GeoJSON Linestring](https://www.rfc-editor.org/rfc/rfc7946.html#appendix-A) defining the route. Max allowed length is 50 km. * asptypes:  list of one or more airspace types you wish to retrieve. Allowed values are &#39;CAS&#39;, &#39;SUA&#39;, &#39;MAA&#39;, and &#39;MTR&#39;.  Successful requests return a list of GeoJSON FeatureCollections, one for each Airspace type indicated in the request. Within each feature collection, there will be a separate Feature for each Airspace instance found. All Features will include a property indicating the *airspace_type*. Additional properties for each *airspace_type* are as follows: * CAS (Controlled Airspace)     - *name*     - *cas_class*: B, C, D, or E2     - *floor*: integer value in ft MSL     - *ceiling*: integer value in ft MSL     - *lannc*: true/false indicating whether or not authorization for this airspace may be obtained via LAANC * SUA (Special Use Airspace)     - *name*     - *sua_type*: AA &#x3D; Alert Area, MOA &#x3D; Military Operations Area, NSA &#x3D; National Security Area, PA &#x3D; Prohibited Area, RA &#x3D; Restricted Area, WA &#x3D; Warning Area     - *floor*: lower limit of the airspace     - *floor_uom*: unit of measure used for the numeric floor value: FT (feet) or FL (flight level)     - *floor_ref*: reference level used for the numeric floor value: AGL, MSL, or STD (standard atmosphere, used for flight level values)     - *ceiling*: upper limit of the airspace     - *ceiling_uom*: unit of measure used for the numeric floor value: FT (feet) or FL (flight level)     - *ceiling_ref*: reference level used for the numeric ceiling value: AGL, MSL, or STD (standard atmosphere, used for flight level values)     - *schedule*: default activation days/times (other times by NOTAM) * MAA (Miscellaneous Activity Area)     - *name*     - *maa_type*: one of the following - ULTRALIGHT, PARACHUTE JUMP AREA, AEROBATIC PRACTICE, GLIDER, HANG GLIDER, SPACE LAUNCH ACTIVITY     - *use_times*: textual description of days/times when activity in the area should be expected * MTR (Military Training Route)     - *name*     - *use_times*: textual description of days/times when MTR is active/hot     - *terrain_following*: boolean value indicating whether terrain following activity occurs on the route     - *max_extent_nm*: maximum distance that aircraft can deviate from route centerline

    :param body: 
    :type body: dict | bytes
    :param x_api_key: 
    :type x_api_key: str

    """
    body = AirspaceByRoute.from_dict(body)
    return web.Response(status=200)
