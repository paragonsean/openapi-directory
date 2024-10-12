from typing import List, Dict
from aiohttp import web

from openapi_server.models.gh_error import GHError
from openapi_server.models.isochrone_response import IsochroneResponse
from openapi_server.models.vehicle_profile_id import VehicleProfileId
from openapi_server import util


async def get_isochrone(request: web.Request, point, time_limit=None, distance_limit=None, vehicle=None, buckets=None, reverse_flow=None, weighting=None) -> web.Response:
    """Isochrone Endpoint

    ### Example You can get an example response via:  &#x60;&#x60;&#x60; curl \&quot;https://graphhopper.com/api/1/isochrone?point&#x3D;51.131108,12.414551&amp;key&#x3D;[YOUR_KEY]\&quot; &#x60;&#x60;&#x60;  Don&#39;t forget to replace the placeholder with your own key.  ### Introduction ![Isochrone screenshot](./img/isochrone-example.png)  An isochrone of a location is &#39;&#39;a line connecting points at which a vehicle arrives at the same time&#39;&#39;, see Wikipedia. With the same API you can also calculate isodistances, just use the parameter distance_limit instead of time_limit&#x60;.  ### Use Cases Some possible areas in which this API may be useful to you:  - real estate analysis - realtors - vehicle scheduling - geomarketing - reach of electric vehicles - transport planning - logistics (distribution and retail network planning)  ### API Clients and Examples See the [clients](#section/API-Clients) section in the main documentation, and [live examples](https://graphhopper.com/api/1/examples/#isochrone). 

    :param point: Specify the start coordinate
    :type point: str
    :param time_limit: Specify which time the vehicle should travel. In seconds.
    :type time_limit: int
    :param distance_limit: Specify which distance the vehicle should travel. In meters.
    :type distance_limit: int
    :param vehicle: The vehicle profile for which the route should be calculated. 
    :type vehicle: dict | bytes
    :param buckets: Number by which to divide the given &#x60;time_limit&#x60; to create &#x60;buckets&#x60; nested isochrones of time intervals &#x60;time_limit-n*time_limit/buckets&#x60;. Applies analogously to &#x60;distance_limit&#x60;.
    :type buckets: int
    :param reverse_flow: If &#x60;false&#x60; the flow goes from point to the polygon, if &#x60;true&#x60; the flow goes from the polygon \&quot;inside\&quot; to the point. Example use case for &#x60;false&#x60;&amp;#58; *How many potential customer can be reached within 30min travel time from your store* vs. &#x60;true&#x60;&amp;#58; *How many customers can reach your store within 30min travel time.* 
    :type reverse_flow: bool
    :param weighting: Use &#x60;\&quot;shortest\&quot;&#x60; to get an isodistance line instead of an isochrone.
    :type weighting: str

    """
    vehicle = .from_dict(vehicle)
    return web.Response(status=200)
