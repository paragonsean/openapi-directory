from typing import List, Dict
from aiohttp import web

from openapi_server.models.measurement_families_get_list200_response import MeasurementFamiliesGetList200Response
from openapi_server.models.patch_measurement_families200_response_inner import PatchMeasurementFamilies200ResponseInner
from openapi_server.models.post_token400_response import PostToken400Response
from openapi_server import util


async def measurement_families_get_list(request: web.Request, ) -> web.Response:
    """Get list of measurement families

    This endpoint allows you to get a list of measurement families.


    """
    return web.Response(status=200)


async def patch_measurement_families(request: web.Request, body=None) -> web.Response:
    """Update/create several measurement families

    This endpoint allows you to update and/or create several measurement families at once.

    :param body: 
    :type body: list | bytes

    """
    body = [MeasurementFamiliesGetList200Response.from_dict(d) for d in body]
    return web.Response(status=200)
