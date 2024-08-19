from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def call5476365e031f5909e4fe331d(request: web.Request, stop_id) -> web.Response:
    """JSON - Next Buses

    &lt;h4 class&#x3D;\&quot;text-primary\&quot;&gt;Description&lt;/h4&gt;    &lt;p&gt;Returns next bus arrival times at a stop.&lt;/p&gt;    &lt;h4 class&#x3D;\&quot;text-primary\&quot;&gt;Response Elements&lt;/h4&gt;    &lt;table class&#x3D;\&quot;table table-condensed table-hover\&quot;&gt;  &lt;thead&gt;  &lt;tr&gt;  &lt;th class&#x3D;\&quot;col-md-3\&quot;&gt;Element&lt;/th&gt;    &lt;th&gt;Description&lt;/th&gt;  &lt;/tr&gt;  &lt;/thead&gt;    &lt;tbody&gt;  &lt;tr&gt;  &lt;td&gt;Predictions&lt;/td&gt;    &lt;td&gt;  Array containing bus predictions (&lt;a href&#x3D;  \&quot;#NextBusPrediction\&quot;&gt;NextBusPrediction&lt;/a&gt;).  &lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td&gt;StopName&lt;/td&gt;    &lt;td&gt;Full name of the given StopID.&lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td colspan&#x3D;\&quot;2\&quot;&gt;  &lt;div class&#x3D;\&quot;text-primary\&quot; style&#x3D;\&quot;margin-top: 1em\&quot;&gt;  &lt;a id&#x3D;\&quot;NextBusPrediction\&quot; name&#x3D;  \&quot;NextBusPrediction\&quot;&gt;NextBusPrediction Elements&lt;/a&gt;  &lt;/div&gt;  &lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td&gt;DirectionNum&lt;/td&gt;    &lt;td&gt;Denotes a binary direction (0 or 1) of the bus. There is no  specific mapping to direction, but a different value for the same  route signifies that the buses are traveling in opposite  directions. Use the DirectionText element to show the actual  destination of the bus.&lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td&gt;DirectionText&lt;/td&gt;    &lt;td&gt;Customer-friendly description of direction and destination for  a bus.&lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td&gt;Minutes&lt;/td&gt;    &lt;td&gt;Minutes until bus arrival at this stop. Numeric value.&lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td&gt;RouteID&lt;/td&gt;    &lt;td&gt;Base route name as shown on the bus. This can be used in other  bus-related methods. Note that all variants will be shown as their  base route names (i.e.: 10Av1 and 10Av2 will be shown as 10A).&lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td&gt;TripID&lt;/td&gt;    &lt;td&gt;Trip identifier. This can be correlated with the data in our  bus schedule information as well as bus positions.&lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td&gt;VehicleID&lt;/td&gt;    &lt;td&gt;Bus identifier. This can be correlated with results returned  from bus positions.&lt;/td&gt;  &lt;/tr&gt;  &lt;/tbody&gt;  &lt;/table&gt;

    :param stop_id: 7-digit regional stop ID.
    :type stop_id: str

    """
    return web.Response(status=200)


async def call5476365e031f5909e4fe331e(request: web.Request, stop_id) -> web.Response:
    """XML - Next Buses

    &lt;h4 class&#x3D;\&quot;text-primary\&quot;&gt;Description&lt;/h4&gt;    &lt;p&gt;Returns next bus arrival times at a stop.&lt;/p&gt;    &lt;h4 class&#x3D;\&quot;text-primary\&quot;&gt;Response Elements&lt;/h4&gt;    &lt;table class&#x3D;\&quot;table table-condensed table-hover\&quot;&gt;  &lt;thead&gt;  &lt;tr&gt;  &lt;th class&#x3D;\&quot;col-md-3\&quot;&gt;Element&lt;/th&gt;    &lt;th&gt;Description&lt;/th&gt;  &lt;/tr&gt;  &lt;/thead&gt;    &lt;tbody&gt;  &lt;tr&gt;  &lt;td&gt;Predictions&lt;/td&gt;    &lt;td&gt;  Array containing bus predictions (&lt;a href&#x3D;  \&quot;#NextBusPrediction\&quot;&gt;NextBusPrediction&lt;/a&gt;).  &lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td&gt;StopName&lt;/td&gt;    &lt;td&gt;Full name of the given StopID.&lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td colspan&#x3D;\&quot;2\&quot;&gt;  &lt;div class&#x3D;\&quot;text-primary\&quot; style&#x3D;\&quot;margin-top: 1em\&quot;&gt;  &lt;a id&#x3D;\&quot;NextBusPrediction\&quot; name&#x3D;  \&quot;NextBusPrediction\&quot;&gt;NextBusPrediction Elements&lt;/a&gt;  &lt;/div&gt;  &lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td&gt;DirectionNum&lt;/td&gt;    &lt;td&gt;Denotes a binary direction (0 or 1) of the bus. There is no  specific mapping to direction, but a different value for the same  route signifies that the buses are traveling in opposite  directions. Use the DirectionText element to show the actual  destination of the bus.&lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td&gt;DirectionText&lt;/td&gt;    &lt;td&gt;Customer-friendly description of direction and destination for  a bus.&lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td&gt;Minutes&lt;/td&gt;    &lt;td&gt;Minutes until bus arrival at this stop. Numeric value.&lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td&gt;RouteID&lt;/td&gt;    &lt;td&gt;Base route name as shown on the bus. This can be used in other  bus-related methods. Note that all variants will be shown as their  base route names (i.e.: 10Av1 and 10Av2 will be shown as 10A).&lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td&gt;TripID&lt;/td&gt;    &lt;td&gt;Trip identifier. This can be correlated with the data in our  bus schedule information as well as bus positions.&lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td&gt;VehicleID&lt;/td&gt;    &lt;td&gt;Bus identifier. This can be correlated with results returned  from bus positions.&lt;/td&gt;  &lt;/tr&gt;  &lt;/tbody&gt;  &lt;/table&gt;

    :param stop_id: 7-digit regional stop ID.
    :type stop_id: str

    """
    return web.Response(status=200)
