from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.offerings_offering_id_analytics_pulses_responses_get_response_time_parameter import OfferingsOfferingIdAnalyticsPulsesResponsesGetResponseTimeParameter
from openapi_server.models.pulse_response import PulseResponse
from openapi_server import util


async def offerings_offering_id_analytics_pulses_get(request: web.Request, offering_id) -> web.Response:
    """Find all pulse IDs in the specified offering

    Responds with the IDs of all pulses that learners have responded to in a specified offering.

    :param offering_id: offering&#39;s id
    :type offering_id: str

    """
    return web.Response(status=200)


async def offerings_offering_id_analytics_pulses_pulse_id_responses_get(request: web.Request, offering_id, pulse_id) -> web.Response:
    """Find pulses by offeringId and pulseId

    Responds with pulse&#39;s responses, matching the pulseId, in an offering matching the offeringId.

    :param offering_id: offering&#39;s id
    :type offering_id: str
    :param pulse_id: pulse&#39;s base id
    :type pulse_id: str

    """
    return web.Response(status=200)


async def offerings_offering_id_analytics_pulses_responses_get(request: web.Request, offering_id, pulse_type=None, response_time=None) -> web.Response:
    """Find pulses by offeringId

    Responds with pulse&#39;s responses in an offering matching the offeringId.

    :param offering_id: offering&#39;s id
    :type offering_id: str
    :param pulse_type: Filter pulse responses by type.
    :type pulse_type: str
    :param response_time: Filter pulse responses by responseTime. Lower then (&#x60;lt&#x60;), lower then or equal (&#x60;lte&#x60;), greater then (&#x60;gt&#x60;) and greater then or equal (&#x60;gte&#x60;) operators are available. Example of filtering by time range __gte__2017-03-14T07:30:00Z__
    :type response_time: dict | bytes

    """
    response_time = .from_dict(response_time)
    return web.Response(status=200)
