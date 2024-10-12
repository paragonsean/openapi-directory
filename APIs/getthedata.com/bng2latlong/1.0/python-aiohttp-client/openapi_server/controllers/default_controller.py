from typing import List, Dict
from aiohttp import web

from openapi_server.models.bng2latlong_easting_northing_get200_response import Bng2latlongEastingNorthingGet200Response
from openapi_server import util


async def bng2latlong_easting_northing_get(request: web.Request, easting, northing) -> web.Response:
    """Returns latitude and longitude for the given easting and northing.

    Takes an OSGB36 easting and northing (British National Grid) and returns the geographically equivalent WGS84 latitude and longitude. #### A successful request returns the following fields: * status - this will be &#x60;ok&#x60; * easting - the easting provided in the request * northing - the northing provided in the request * latitude - the latitude of the converted coordinates * longitude - the longitude of the converted coordinates #### An unsuccessful request returns the following fields: * status - this will be &#x60;error&#x60; * error - an error message 

    :param easting: An OSGB36 (British National Grid) easting.
    :type easting: int
    :param northing: An OSGB36 (British National Grid) northing.
    :type northing: int

    """
    return web.Response(status=200)
