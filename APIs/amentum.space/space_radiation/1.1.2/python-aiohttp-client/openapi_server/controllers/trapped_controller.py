from typing import List, Dict
from aiohttp import web

from openapi_server.models.flux import Flux
from openapi_server import util


async def app_api_endpoints_trapped_radiation_calculate_flux_mean(request: web.Request, model, coord_sys, coord_units, coord1, coord2, coord3, year, month, day, hour, minute, second) -> web.Response:
    """Calculate mean particle flux 

    at given coordinates and date-time. 

    :param model: &lt;br&gt;Which model to use: &lt;br&gt;&lt;br&gt; - Energetic electrons (AE9) &lt;br&gt; - Energetic protons (AP9)  &lt;br&gt; - Space plasma model for electrons (SPME) &lt;br&gt; - for hydrogen (SPMH) &lt;br&gt; - for helium (SPMHE) &lt;br&gt; - for oxygen (SPMO)  
    :type model: str
    :param coord_sys: &lt;br&gt;Coordinate system to use:  &lt;br&gt;&lt;br&gt; - Geodetic/WGS84 (GDZ) &lt;br&gt; - Geocentric Cartesian (GEO) &lt;br&gt; - Geocentric Earth Inertial (GEI) &lt;br&gt; See \&quot;Bhavnani, K. H., &amp; Vancour, R. P. (1991).  Coordinate systems for space and geophysical applications\&quot;  for coord system definitions. 
    :type coord_sys: str
    :param coord_units: &lt;br&gt;Coordinate units to use: km (KM) or Earth Radii (RE) 
    :type coord_units: str
    :param coord1: &lt;br&gt;First coordinate value to specify position. &lt;br&gt;&lt;br&gt; Ordering for GEI, GEO coords:X, Y, Z&lt;br&gt; Ordering for GDZ coords: Alt, Lat, Long&lt;br&gt;  Valid ranges for latitude: -90, 90&lt;br&gt;  Valid ranges for longitude: 0, 360&lt;br&gt;  
    :type coord1: 
    :param coord2: &lt;br&gt;Second coordinate value.
    :type coord2: 
    :param coord3: &lt;br&gt;Third coordinate value.
    :type coord3: 
    :param year: &lt;br&gt;
    :type year: int
    :param month: &lt;br&gt;
    :type month: int
    :param day: &lt;br&gt;
    :type day: int
    :param hour: &lt;br&gt;
    :type hour: int
    :param minute: &lt;br&gt;
    :type minute: int
    :param second: &lt;br&gt;
    :type second: int

    """
    return web.Response(status=200)


async def app_api_endpoints_trapped_radiation_calculate_flux_percentile(request: web.Request, model, coord_sys, coord_units, coord1, coord2, coord3, year, month, day, hour, minute, second, percentile) -> web.Response:
    """Calculate percentile particle flux 

    at given coordinates and date-time. 

    :param model: &lt;br&gt;Which model to use: &lt;br&gt;&lt;br&gt; - Energetic electrons (AE9) &lt;br&gt; - Energetic protons (AP9)  &lt;br&gt; - Space plasma model for electrons (SPME) &lt;br&gt; - for hydrogen (SPMH) &lt;br&gt; - for helium (SPMHE) &lt;br&gt; - for oxygen (SPMO)  
    :type model: str
    :param coord_sys: &lt;br&gt;Coordinate system to use:  &lt;br&gt;&lt;br&gt; - Geodetic/WGS84 (GDZ) &lt;br&gt; - Geocentric Cartesian (GEO) &lt;br&gt; - Geocentric Earth Inertial (GEI) &lt;br&gt; See \&quot;Bhavnani, K. H., &amp; Vancour, R. P. (1991).  Coordinate systems for space and geophysical applications\&quot;  for coord system definitions. 
    :type coord_sys: str
    :param coord_units: &lt;br&gt;Coordinate units to use: km (KM) or Earth Radii (RE) 
    :type coord_units: str
    :param coord1: &lt;br&gt;First coordinate value to specify position. &lt;br&gt;&lt;br&gt; Ordering for GEI, GEO coords:X, Y, Z&lt;br&gt; Ordering for GDZ coords: Alt, Lat, Long&lt;br&gt;  Valid ranges for latitude: -90, 90&lt;br&gt;  Valid ranges for longitude: 0, 360&lt;br&gt;  
    :type coord1: 
    :param coord2: &lt;br&gt;Second coordinate value.
    :type coord2: 
    :param coord3: &lt;br&gt;Third coordinate value.
    :type coord3: 
    :param year: &lt;br&gt;
    :type year: int
    :param month: &lt;br&gt;
    :type month: int
    :param day: &lt;br&gt;
    :type day: int
    :param hour: &lt;br&gt;
    :type hour: int
    :param minute: &lt;br&gt;
    :type minute: int
    :param second: &lt;br&gt;
    :type second: int
    :param percentile: &lt;br&gt;Integer percentile at which to calc flux (50 is the median value). 
    :type percentile: int

    """
    return web.Response(status=200)
