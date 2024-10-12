from typing import List, Dict
from aiohttp import web

from openapi_server.models.app_api_icaro_endpoints_icaro_ambient_dose200_response import AppApiIcaroEndpointsICAROAmbientDose200Response
from openapi_server.models.app_api_icaro_endpoints_icaro_effective_dose200_response import AppApiIcaroEndpointsICAROEffectiveDose200Response
from openapi_server import util


async def app_api_icaro_endpoints_icaro_ambient_dose(request: web.Request, origin, destination, year, month, day, altitude=None, duration=None, initial_altitude=None, cruising_altitudes=None, climb_times=None, cruising_times=None, descent_time=None, final_altitude=None) -> web.Response:
    """Calculate the ambient equivalent dose along a great circle flight route. 

    The ambient dose equivalent, H*(10), is an operational quantity that simulates the  human body by measuring the dose equivalent at a depth of 10 mm within a tissue  equivalent sphere of 300 mm diameter. It is a measurable quantity that is  used to calibrate area monitors (radiation detectors) for mixed radiation fields.  &lt;br&gt; &lt;br&gt; Use this endpoint if you are comparing model predictions to measurements. &lt;br&gt; &lt;br&gt; This API can run in two modes: &lt;br&gt; &lt;br&gt; Either specify &lt;br&gt; &lt;b&gt;altitude&lt;/b&gt;, &lt;b&gt;duration&lt;/b&gt;&lt;br&gt; for constant altitude calculations; &lt;br&gt; &lt;br&gt; Or specify &lt;br&gt; &lt;b&gt;initial_altitude&lt;/b&gt;, &lt;b&gt;cruising_altitudes&lt;/b&gt;, &lt;b&gt;climb_times&lt;/b&gt;, &lt;b&gt;cruising_times&lt;/b&gt;, &lt;b&gt;descent_time&lt;/b&gt;, &lt;b&gt;final_altitude&lt;/b&gt;&lt;br&gt; to calculate dose accounting for a step climb. &lt;br&gt; &lt;br&gt; Note: the airport codes or coordinates (depending on which was specified), and the date in DD/MM/YYYY format, are echoed in the json response as strings. 

    :param origin: The ICAO code or IATA code or latitude,longitude pair (in decimal degrees) of the origin airport.
    :type origin: str
    :param destination: The ICAO code or IATA code or latitude,longitude pair (in decimal degrees) of the destination airport.
    :type destination: str
    :param year: Year in YYYY.
    :type year: int
    :param month: Month in MM.
    :type month: int
    :param day: Day in DD.
    :type day: int
    :param altitude: Altitude (in km). The minimum is 0 m, the maximum is 20 km.
    :type altitude: 
    :param duration: The flight duration in hours. The minimum is 0, the maximum is 20 hrs.
    :type duration: 
    :param initial_altitude: Initial altitude (in km). The minimum is 0 m, the maximum is 20 km.
    :type initial_altitude: 
    :param cruising_altitudes: Cruising altitudes (in km). The minimum is 0 m, the maximum is 20 km.
    :type cruising_altitudes: List[]
    :param climb_times: Climb times for each cruising altitude (hours).
    :type climb_times: List[]
    :param cruising_times: Cruising times at each cruising altitude (hours).
    :type cruising_times: List[]
    :param descent_time: Descent time from last cruising altitude to final altitude (hours).
    :type descent_time: 
    :param final_altitude: Final altitude (in km).
    :type final_altitude: 

    """
    return web.Response(status=200)


async def app_api_icaro_endpoints_icaro_effective_dose(request: web.Request, origin, destination, year, month, day, altitude=None, duration=None, initial_altitude=None, cruising_altitudes=None, climb_times=None, cruising_times=None, descent_time=None, final_altitude=None) -> web.Response:
    """Calculate the total effective dose along a great circle flight route. 

    Effective Dose is a radiation protection quantity defined by the International Commission on  Radiological Protection (ICRP) and represents the stochastic health  risk to the human body at low levels of radiation. It accounts for the different sensitivities of organs to ionising radiation, as well as the different effectiveness of various types of radiation. &lt;br&gt; &lt;br&gt; Use this endpoint if you need to estimate radiation exposures of personnel. &lt;br&gt; &lt;br&gt; This API can run in two modes: &lt;br&gt; &lt;br&gt; Either specify &lt;br&gt; &lt;b&gt;altitude&lt;/b&gt;, &lt;b&gt;duration&lt;/b&gt;&lt;br&gt; for constant altitude calculations; &lt;br&gt; &lt;br&gt; Or specify &lt;br&gt; &lt;b&gt;initial_altitude&lt;/b&gt;, &lt;b&gt;cruising_altitudes&lt;/b&gt;, &lt;b&gt;climb_times&lt;/b&gt;, &lt;b&gt;cruising_times&lt;/b&gt;, &lt;b&gt;descent_time&lt;/b&gt;, &lt;b&gt;final_altitude&lt;/b&gt;&lt;br&gt; to calculate dose accounting for a step climb. &lt;br&gt; &lt;br&gt; Note: the airport codes or coordinates (depending on which was specified), and the date in DD/MM/YYYY format, are echoed in the json response as strings. 

    :param origin: The ICAO code or IATA code or latitude,longitude pair (in decimal degrees) of the origin airport.
    :type origin: str
    :param destination: The ICAO code or IATA code or latitude,longitude pair (in decimal degrees) of the destination airport.
    :type destination: str
    :param year: Year in YYYY.
    :type year: int
    :param month: Month in MM.
    :type month: int
    :param day: Day in DD.
    :type day: int
    :param altitude: Altitude (in km). The minimum is 0 m, the maximum is 20 km.
    :type altitude: 
    :param duration: The flight duration in hours. The minimum is 0, the maximum is 20 hrs.
    :type duration: 
    :param initial_altitude: Initial altitude (in km). The minimum is 0 m, the maximum is 20 km.
    :type initial_altitude: 
    :param cruising_altitudes: Cruising altitudes (in km). The minimum is 0 m, the maximum is 20 km.
    :type cruising_altitudes: List[]
    :param climb_times: Climb times for each cruising altitude (hours).
    :type climb_times: List[]
    :param cruising_times: Cruising times at each cruising altitude (hours).
    :type cruising_times: List[]
    :param descent_time: Descent time from last cruising altitude to final altitude (hours).
    :type descent_time: 
    :param final_altitude: Final altitude (in km).
    :type final_altitude: 

    """
    return web.Response(status=200)
