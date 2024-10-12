from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.event_occurence_detail import EventOccurenceDetail
from openapi_server.models.events_search_response import EventsSearchResponse
from openapi_server import util


async def events_get(request: web.Request, fieldset, category=None, activity=None, ambience=None, genre=None, name=None, q=None, from_day=None, to_day=None, capacity_min=None, capacity_max=None, center=None, radius=None, bbox=None, polygon=None, within=None, offset=None, limit=None) -> web.Response:
    """Find event occurrences in the area. Returns results at specific place and time, event groups are expanded for every occurrence.

    

    :param fieldset: Return results starting at specified offset (summary, context, detail)
    :type fieldset: str
    :param category: List of required EventCategory ids (Tier 1)
    :type category: List[str]
    :param activity: List of required activity type ids (compliment to category)
    :type activity: str
    :param ambience: List of required ambience ids
    :type ambience: str
    :param genre: List of required genre ids
    :type genre: str
    :param name: Matching on event and place names
    :type name: str
    :param q: Text query matching titles, description, various text, tags, category
    :type q: str
    :param from_day: Start on or after date specified (2015-10-16)
    :type from_day: str
    :param to_day: Start on or before date specified (2015-10-16)
    :type to_day: str
    :param capacity_min: Min capacity at location
    :type capacity_min: 
    :param capacity_max: Min capacity at location
    :type capacity_max: 
    :param center: latitude,longitude of the origin point
    :type center: str
    :param radius: Distance from origin in meters
    :type radius: int
    :param bbox: Corner of a bounding box (lat,lng). Requires 0 or 2 pairs
    :type bbox: List[str]
    :param polygon: Closed custom polygon. Ordered list of lat,lng pairs
    :type polygon: List[str]
    :param within: Search within specified geopolitical place id
    :type within: str
    :param offset: Return results starting at specified offset
    :type offset: int
    :param limit: Max results to return
    :type limit: int

    """
    return web.Response(status=200)


async def events_id_get(request: web.Request, id, fieldset=None) -> web.Response:
    """Get Specific event details.

    

    :param id: event @id
    :type id: str
    :param fieldset: 
    :type fieldset: str

    """
    return web.Response(status=200)
