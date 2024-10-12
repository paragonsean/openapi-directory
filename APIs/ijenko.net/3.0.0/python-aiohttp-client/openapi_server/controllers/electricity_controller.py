from typing import List, Dict
from aiohttp import web

from openapi_server.models.default_error import DefaultError
from openapi_server.models.electricity_autonomy import ElectricityAutonomy
from openapi_server.models.electricity_flows import ElectricityFlows
from openapi_server.models.electricity_flows_setup import ElectricityFlowsSetup
from openapi_server.models.electricity_self_consumption import ElectricitySelfConsumption
from openapi_server import util


async def place_electricity_autonomy(request: web.Request, place_id, when, span) -> web.Response:
    """Get autonomy rate of the place

    Compute the autonomy rate of the *Place* on a time period.  &#x60;autonomy &#x3D; 1 - (elec_drawn / elec_total_usage)&#x60; 

    :param place_id: Unique identifier of a *Place*.
    :type place_id: str
    :param when: A time part of the time span.
    :type when: str
    :param span: Timespan: H (hour), D (day), Wmo (week starting on Monday), Wsu (week starting on Sunday), M (month), Y (year)
    :type span: str

    """
    when = util.deserialize_datetime(when)
    return web.Response(status=200)


async def place_electricity_get_flows(request: web.Request, place_id, flows) -> web.Response:
    """Get electricity virtual flows

    Get the mapping of virtual electricity flows to functionalities.  Some rules are applied to expand the virtual flows using the concrete flows available.  The &#x60;factor&#x60; tells how each energy value coming from a functionality must be added with values from other functionality to compute the energy of the virtual flow. Factors are usually &#x60;1&#x60; or &#x60;-1&#x60;.  The &#x60;code&#x60; property gives the result which may be partial: - If all flows are available, &#x60;200000&#x60; is returned. - If no flows are available (indicating that the place has no   electricity functionality or that no functionality has been attached   to a flow), the &#x60;code&#x60; is &#x60;200001&#x60;. The &#x60;missing&#x60; property contains   all the requested flows. - If some flows are missing, the &#x60;code&#x60; is &#x60;200002&#x60; and the &#x60;missing&#x60;   property lists them. 

    :param place_id: Unique identifier of a *Place*.
    :type place_id: str
    :param flows: Names of the flows requested
    :type flows: List[str]

    """
    return web.Response(status=200)


async def place_electricity_get_flows_setup(request: web.Request, place_id) -> web.Response:
    """Get electricity flows setup

    Get the mapping of functionalities to electricity flows.  A functionality is attached to *at most* one flow. 

    :param place_id: Unique identifier of a *Place*.
    :type place_id: str

    """
    return web.Response(status=200)


async def place_electricity_self_consumption(request: web.Request, place_id, when, span) -> web.Response:
    """Get self-consumption rate of the place

    Compute the self-consumption rate of the *Place* on a time period.  &#x60;selfConsumption &#x3D; 1 - (elec_feed_in / elec_total_usage)&#x60; 

    :param place_id: Unique identifier of a *Place*.
    :type place_id: str
    :param when: A time part of the time span.
    :type when: str
    :param span: Timespan: H (hour), D (day), Wmo (week starting on Monday), Wsu (week starting on Sunday), M (month), Y (year)
    :type span: str

    """
    when = util.deserialize_datetime(when)
    return web.Response(status=200)
