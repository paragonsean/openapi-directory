from typing import List, Dict
from aiohttp import web

from openapi_server.models.tfl_api_presentation_entities_journey_planner_itinerary_result import TflApiPresentationEntitiesJourneyPlannerItineraryResult
from openapi_server.models.tfl_api_presentation_entities_mode import TflApiPresentationEntitiesMode
from openapi_server import util


async def journey_journey_results(request: web.Request, _from, to, via=None, national_search=None, _date=None, time=None, time_is=None, journey_preference=None, mode=None, accessibility_preference=None, from_name=None, to_name=None, via_name=None, max_transfer_minutes=None, max_walking_minutes=None, walking_speed=None, cycle_preference=None, adjustment=None, bike_proficiency=None, alternative_cycle=None, alternative_walking=None, apply_html_markup=None, use_multi_modal_call=None, walking_optimization=None, taxi_only_trip=None, route_between_entrances=None, use_real_time_live_arrivals=None, calc_one_direction=None) -> web.Response:
    """Perform a Journey Planner search from the parameters specified in simple types

    

    :param _from: Origin of the journey. Can be WGS84 coordinates expressed as \&quot;lat,long\&quot;, a UK postcode, a Naptan (StopPoint) id, an ICS StopId, or a free-text string (will cause disambiguation unless it exactly matches a point of interest name).
    :type _from: str
    :param to: Destination of the journey. Can be WGS84 coordinates expressed as \&quot;lat,long\&quot;, a UK postcode, a Naptan (StopPoint) id, an ICS StopId, or a free-text string (will cause disambiguation unless it exactly matches a point of interest name).
    :type to: str
    :param via: Travel through point on the journey. Can be WGS84 coordinates expressed as \&quot;lat,long\&quot;, a UK postcode, a Naptan (StopPoint) id, an ICS StopId, or a free-text string (will cause disambiguation unless it exactly matches a point of interest name).
    :type via: str
    :param national_search: Does the journey cover stops outside London? eg. \&quot;nationalSearch&#x3D;true\&quot;
    :type national_search: bool
    :param _date: The date must be in yyyyMMdd format
    :type _date: str
    :param time: The time must be in HHmm format
    :type time: str
    :param time_is: Does the time given relate to arrival or leaving time? Possible options: \&quot;departing\&quot; | \&quot;arriving\&quot;
    :type time_is: str
    :param journey_preference: The journey preference eg possible options: \&quot;leastinterchange\&quot; | \&quot;leasttime\&quot; | \&quot;leastwalking\&quot;
    :type journey_preference: str
    :param mode: The mode must be a comma separated list of modes. eg possible options: \&quot;public-bus,overground,train,tube,coach,dlr,cablecar,tram,river,walking,cycle\&quot;
    :type mode: List[str]
    :param accessibility_preference: The accessibility preference must be a comma separated list eg. \&quot;noSolidStairs,noEscalators,noElevators,stepFreeToVehicle,stepFreeToPlatform\&quot;
    :type accessibility_preference: List[str]
    :param from_name: An optional name to associate with the origin of the journey in the results.
    :type from_name: str
    :param to_name: An optional name to associate with the destination of the journey in the results.
    :type to_name: str
    :param via_name: An optional name to associate with the via point of the journey in the results.
    :type via_name: str
    :param max_transfer_minutes: The max walking time in minutes for transfer eg. \&quot;120\&quot;
    :type max_transfer_minutes: str
    :param max_walking_minutes: The max walking time in minutes for journeys eg. \&quot;120\&quot;
    :type max_walking_minutes: str
    :param walking_speed: The walking speed. eg possible options: \&quot;slow\&quot; | \&quot;average\&quot; | \&quot;fast\&quot;.
    :type walking_speed: str
    :param cycle_preference: The cycle preference. eg possible options: \&quot;allTheWay\&quot; | \&quot;leaveAtStation\&quot; | \&quot;takeOnTransport\&quot; | \&quot;cycleHire\&quot;
    :type cycle_preference: str
    :param adjustment: Time adjustment command. eg possible options: \&quot;TripFirst\&quot; | \&quot;TripLast\&quot;
    :type adjustment: str
    :param bike_proficiency: A comma separated list of cycling proficiency levels. eg possible options: \&quot;easy,moderate,fast\&quot;
    :type bike_proficiency: List[str]
    :param alternative_cycle: Option to determine whether to return alternative cycling journey
    :type alternative_cycle: bool
    :param alternative_walking: Option to determine whether to return alternative walking journey
    :type alternative_walking: bool
    :param apply_html_markup: Flag to determine whether certain text (e.g. walking instructions) should be output with HTML tags or not.
    :type apply_html_markup: bool
    :param use_multi_modal_call: A boolean to indicate whether or not to return 3 public transport journeys, a bus journey, a cycle hire journey, a personal cycle journey and a walking journey
    :type use_multi_modal_call: bool
    :param walking_optimization: A boolean to indicate whether to optimize journeys using walking
    :type walking_optimization: bool
    :param taxi_only_trip: A boolean to indicate whether to return one or more taxi journeys. Note, setting this to true will override \&quot;useMultiModalCall\&quot;.
    :type taxi_only_trip: bool
    :param route_between_entrances: A boolean to indicate whether public transport routes should include directions between platforms and station entrances.
    :type route_between_entrances: bool
    :param use_real_time_live_arrivals: A boolean to indicate if we want to receive real time live arrivals data where available.
    :type use_real_time_live_arrivals: bool
    :param calc_one_direction: A boolean to make Journey Planner calculate journeys in one temporal direction only. In other words, only calculate journeys after the &#39;depart&#39; time, or before the &#39;arrive&#39; time. By default, the Journey Planner engine (EFA) calculates journeys in both temporal directions.
    :type calc_one_direction: bool

    """
    return web.Response(status=200)


async def journey_meta(request: web.Request, ) -> web.Response:
    """Gets a list of all of the available journey planner modes

    


    """
    return web.Response(status=200)
