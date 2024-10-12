from typing import List, Dict
from aiohttp import web

from openapi_server.models.driver import Driver
from openapi_server.models.driver_race_projection import DriverRaceProjection
from openapi_server.models.race import Race
from openapi_server.models.race_result import RaceResult
from openapi_server.models.series import Series
from openapi_server import util


async def driver_details(request: web.Request, format, driverid) -> web.Response:
    """Driver Details

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param driverid: Unique FantasyData Driver ID. Example:&lt;code&gt;80000268&lt;/code&gt;.
    :type driverid: str

    """
    return web.Response(status=200)


async def driver_race_projections_entry_list(request: web.Request, format, raceid) -> web.Response:
    """Driver Race Projections (Entry List)

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param raceid: Unique FantasyData Race ID. Example:&lt;code&gt;1&lt;/code&gt;, &lt;code&gt;2&lt;/code&gt;, etc.
    :type raceid: str

    """
    return web.Response(status=200)


async def drivers(request: web.Request, format) -> web.Response:
    """Drivers

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str

    """
    return web.Response(status=200)


async def race_results(request: web.Request, format, raceid) -> web.Response:
    """Race Results

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param raceid: Unique FantasyData Race ID. Example:&lt;code&gt;1&lt;/code&gt;, &lt;code&gt;2&lt;/code&gt;, etc.
    :type raceid: str

    """
    return web.Response(status=200)


async def races_schedule(request: web.Request, format, season) -> web.Response:
    """Races / Schedule

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str
    :param season: Year of the season. &lt;br&gt;Examples: &lt;code&gt;2015&lt;/code&gt;, &lt;code&gt;2016&lt;/code&gt;.
    :type season: str

    """
    return web.Response(status=200)


async def series(request: web.Request, format) -> web.Response:
    """Series

    

    :param format: Desired response format. Valid entries are &lt;code&gt;XML&lt;/code&gt; or &lt;code&gt;JSON&lt;/code&gt;.
    :type format: str

    """
    return web.Response(status=200)
