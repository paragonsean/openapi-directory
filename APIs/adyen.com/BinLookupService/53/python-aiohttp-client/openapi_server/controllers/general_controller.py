from typing import List, Dict
from aiohttp import web

from openapi_server.models.cost_estimate_request import CostEstimateRequest
from openapi_server.models.cost_estimate_response import CostEstimateResponse
from openapi_server.models.service_error import ServiceError
from openapi_server.models.three_ds_availability_request import ThreeDSAvailabilityRequest
from openapi_server.models.three_ds_availability_response import ThreeDSAvailabilityResponse
from openapi_server import util


async def post_get3ds_availability(request: web.Request, body=None) -> web.Response:
    """Check if 3D Secure is available

    Verifies whether 3D Secure is available for the specified BIN or card brand. For 3D Secure 2, this endpoint also returns device fingerprinting keys.  For more information, refer to [3D Secure 2](https://docs.adyen.com/online-payments/3d-secure/native-3ds2).

    :param body: 
    :type body: dict | bytes

    """
    body = ThreeDSAvailabilityRequest.from_dict(body)
    return web.Response(status=200)


async def post_get_cost_estimate(request: web.Request, body=None) -> web.Response:
    """Get a fees cost estimate

    &gt;This API is available only for merchants operating in Australia, the EU, and the UK.  Use the Adyen Cost Estimation API to pre-calculate interchange and scheme fee costs. Knowing these costs prior actual payment authorisation gives you an opportunity to charge those costs to the cardholder, if necessary.  To retrieve this information, make the call to the &#x60;/getCostEstimate&#x60; endpoint. The response to this call contains the amount of the interchange and scheme fees charged by the network for this transaction, and also which surcharging policy is possible (based on current regulations).  &gt; Since not all information is known in advance (for example, if the cardholder will successfully authenticate via 3D Secure or if you also plan to provide additional Level 2/3 data), the returned amounts are based on a set of assumption criteria you define in the &#x60;assumptions&#x60; parameter.

    :param body: 
    :type body: dict | bytes

    """
    body = CostEstimateRequest.from_dict(body)
    return web.Response(status=200)
