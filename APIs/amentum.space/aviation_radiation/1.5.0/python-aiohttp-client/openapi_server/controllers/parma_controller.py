from typing import List, Dict
from aiohttp import web

from openapi_server.models.app_api_parma_endpoints_parma_ambient_dose200_response import AppApiParmaEndpointsPARMAAmbientDose200Response
from openapi_server.models.app_api_parma_endpoints_parma_differential_intensity200_response import AppApiParmaEndpointsPARMADifferentialIntensity200Response
from openapi_server.models.app_api_parma_endpoints_parma_effective_dose200_response import AppApiParmaEndpointsPARMAEffectiveDose200Response
from openapi_server import util


async def app_api_parma_endpoints_parma_ambient_dose(request: web.Request, latitude, longitude, year, month, day, particle, altitude=None, atmospheric_depth=None) -> web.Response:
    """The ambient dose equivalent rate calculated for a single particle type, or accumulated over all particle types. 

    The ambient dose equivalent, H*(10), is an operational quantity that simulates the  human body by measuring the dose equivalent at a depth of 10 mm within a tissue  equivalent sphere of 300 mm diameter. It is a measurable quantity that is  used to calibrate area monitors (radiation detectors) for mixed radiation fields.  Use this endpoint if you are comparing model predictions to measurements. 

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
    :param particle: The particle type as a string. Specifying &#39;total&#39;, only used for the dose calculation, returns the dose for all particle types. 
    :type particle: str
    :param altitude: Altitude (in km). The minimum is 0 m, the maximum is 47 km (the upper limit of the stratosphere).
    :type altitude: 
    :param atmospheric_depth: Atmospheric depth from the top of the atmosphere (in units of g/cm2). The minimum is 0.913 g/cm2, the maximum is 1032.66 g/cm2. WARNING: you can specify either altitude OR atmospheric depth, not both. 
    :type atmospheric_depth: 

    """
    return web.Response(status=200)


async def app_api_parma_endpoints_parma_differential_intensity(request: web.Request, latitude, longitude, year, month, day, particle, angle, altitude=None, atmospheric_depth=None) -> web.Response:
    """The energy differential intensity of a particle at a given zenith angle.

    The differential intensity of a particle is a directional quantity that describes the number of particles per unit area, per unit solid angle, per unit energy, and per unit time. The API leverages the functionality of PARMA to calculate differential intensity distributions with energies in units of MeV and Intensity in units of /cm2/sr/MeV/s. 

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
    :param particle: The particle type as a string. Specifying &#39;total&#39;, only used for the dose calculation, returns the dose for all particle types. 
    :type particle: str
    :param angle: Direction cosine. 1.0 is in the downward direction.
    :type angle: 
    :param altitude: Altitude (in km). The minimum is 0 m, the maximum is 47 km (the upper limit of the stratosphere).
    :type altitude: 
    :param atmospheric_depth: Atmospheric depth from the top of the atmosphere (in units of g/cm2). The minimum is 0.913 g/cm2, the maximum is 1032.66 g/cm2. WARNING: you can specify either altitude OR atmospheric depth, not both. 
    :type atmospheric_depth: 

    """
    return web.Response(status=200)


async def app_api_parma_endpoints_parma_effective_dose(request: web.Request, latitude, longitude, year, month, day, particle, altitude=None, atmospheric_depth=None) -> web.Response:
    """The effective dose rate calculated for a single particle type, or accumulated over all particle types. 

    Effective dose is a radiation protection quantity defined by the International Commission on Radiological Protection (ICRP) and represents the stochastic health risk to the human body at low levels of radiation. It accounts for the different sensitivities of organs to ionising radiation, as well as the different effectiveness of various types of radiation. Use this endpoint if you need to estimate radiation exposures of personnel. 

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
    :param particle: The particle type as a string. Specifying &#39;total&#39;, only used for the dose calculation, returns the dose for all particle types. 
    :type particle: str
    :param altitude: Altitude (in km). The minimum is 0 m, the maximum is 47 km (the upper limit of the stratosphere).
    :type altitude: 
    :param atmospheric_depth: Atmospheric depth from the top of the atmosphere (in units of g/cm2). The minimum is 0.913 g/cm2, the maximum is 1032.66 g/cm2. WARNING: you can specify either altitude OR atmospheric depth, not both. 
    :type atmospheric_depth: 

    """
    return web.Response(status=200)
