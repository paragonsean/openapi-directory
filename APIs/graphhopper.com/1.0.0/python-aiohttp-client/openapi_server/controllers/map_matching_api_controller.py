from typing import List, Dict
from aiohttp import web

from openapi_server.models.gh_error import GHError
from openapi_server.models.route_response import RouteResponse
from openapi_server import util


async def post_gpx(request: web.Request, gps_accuracy=None, vehicle=None) -> web.Response:
    """Map-match a GPX file

    ### Example You get an example response for a GPX via:  &#x60;&#x60;&#x60; curl -XPOST -H \&quot;Content-Type: application/gpx+xml\&quot; \&quot;https://graphhopper.com/api/1/match?vehicle&#x3D;car&amp;key&#x3D;[YOUR_KEY]\&quot; --data @/path/to/some.gpx &#x60;&#x60;&#x60;  A minimal working GPX file looks like &#x60;&#x60;&#x60;gpx &lt;gpx&gt;  &lt;trk&gt;   &lt;trkseg&gt;    &lt;trkpt lat&#x3D;\&quot;51.343657\&quot; lon&#x3D;\&quot;12.360708\&quot;&gt;&lt;/trkpt&gt;    &lt;trkpt lat&#x3D;\&quot;51.343796\&quot; lon&#x3D;\&quot;12.361337\&quot;&gt;&lt;/trkpt&gt;    &lt;trkpt lat&#x3D;\&quot;51.342784\&quot; lon&#x3D;\&quot;12.361882\&quot;&gt;&lt;/trkpt&gt;   &lt;/trkseg&gt;  &lt;/trk&gt; &lt;/gpx&gt; &#x60;&#x60;&#x60;  ### Introduction ![Map Matching screenshot](./img/map-matching-example.gif)  The Map Matching API is part of the GraphHopper Directions API and with this API you can snap measured GPS points typically as GPX files to a digital road network to e.g. clean data or attach certain data like elevation or turn instructions to it. Read more at Wikipedia.  In the example screenshot above and demo you see the Map Matching API in action where the black line is the GPS track and the green one is matched result.  Most of the times, you can simply POST a GPX file, but some of the request parameters of the [Routing API](#tag/Routing-API) apply here, too.  ### API Clients and Examples See the [clients](#section/API-Clients) section in the main documentation, and [live examples](https://graphhopper.com/api/1/examples/#map-matching).  ### Limits and Counts The cost for one request depends on the number of GPS location and is documented [here](https://graphhopper.com/api/1/docs/FAQ/).  One request should not exceed the Map Matching API location limit depending on the package, see the pricing in our dashboard. 

    :param gps_accuracy: Specify the precision of a point, in meter
    :type gps_accuracy: int
    :param vehicle: Specify the vehicle profile like car
    :type vehicle: str

    """
    return web.Response(status=200)
