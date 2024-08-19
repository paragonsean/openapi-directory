from typing import List, Dict
from aiohttp import web

from openapi_server.models.app_api_cari7_endpoints_cari7_ambient_dose200_response import AppApiCari7EndpointsCARI7AmbientDose200Response
from openapi_server.models.app_api_cari7_endpoints_cari7_effective_dose200_response import AppApiCari7EndpointsCARI7EffectiveDose200Response
from openapi_server import util


async def app_api_cari7_endpoints_cari7_ambient_dose(request: web.Request, altitude, latitude, longitude, year, month, day, utc, particle) -> web.Response:
    """The ambient dose equivalent rate calculated for a single particle type, or accumulated over all particle types. 

    The ambient dose equivalent, H*(10), is an operational quantity that simulates the  human body by measuring the dose equivalent at a depth of 10 mm within a tissue  equivalent sphere of 300 mm diameter. It is a measurable quantity that is  used to calibrate area monitors (radiation detectors) for mixed radiation fields.  Use this endpoint if you are comparing model predictions to measurements. 

    :param altitude: Altitude (in km). The minimum is 0 m, the maximum is 47 km (the upper limit of the stratosphere).
    :type altitude: 
    :param latitude: Latitude. -90 (S) to 90 (N).
    :type latitude: 
    :param longitude: Longitude. -180 (W) to 180 (E).
    :type longitude: 
    :param year: Year in YYYY.
    :type year: int
    :param month: Month in MM.
    :type month: int
    :param day: Day in DD.
    :type day: int
    :param utc: Hour in 24 hour time.
    :type utc: int
    :param particle: The particle type as a string. Specifying &#39;total&#39; returns the dose for all particle types. 
    :type particle: str

    """
    return web.Response(status=200)


async def app_api_cari7_endpoints_cari7_effective_dose(request: web.Request, altitude, latitude, longitude, year, month, day, utc, particle) -> web.Response:
    """The effective dose rate calculated for a single particle type, or accumulated over all particle types. 

    Effective Dose is a radiation protection quantity defined by the International Commission on  Radiological Protection (ICRP) and represents the stochastic health  risk to the human body at low levels of radiation. It accounts for the different sensitivities of organs to ionising radiation, as well as the different effectiveness of various types of radiation. Use this endpoint if you need to estimate radiation exposures of personnel. 

    :param altitude: Altitude (in km). The minimum is 0 m, the maximum is 47 km (the upper limit of the stratosphere).
    :type altitude: 
    :param latitude: Latitude. -90 (S) to 90 (N).
    :type latitude: 
    :param longitude: Longitude. -180 (W) to 180 (E).
    :type longitude: 
    :param year: Year in YYYY.
    :type year: int
    :param month: Month in MM.
    :type month: int
    :param day: Day in DD.
    :type day: int
    :param utc: Hour in 24 hour time.
    :type utc: int
    :param particle: The particle type as a string. Specifying &#39;total&#39; returns the dose for all particle types. 
    :type particle: str

    """
    return web.Response(status=200)
