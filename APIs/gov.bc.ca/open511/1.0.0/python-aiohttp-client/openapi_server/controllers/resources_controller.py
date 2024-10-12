from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def areas_get(request: web.Request, format=None) -> web.Response:
    """Lists the geographical areas (e.g. districts) that can be used to filter events.

    

    :param format: The format of the response
    :type format: str

    """
    return web.Response(status=200)


async def events_get(request: web.Request, format=None, status=None, severity=None, jurisdiction=None, event_type=None, created=None, updated=None, road_name=None, area_id=None, bbox=None) -> web.Response:
    """Lists road events

    The events resource provides information about road events (e.g. accidents, construction, special events). The response is a list of event elements matching the filtering parameters if any are provided. 

    :param format: The format of the response
    :type format: str
    :param status: Limits the response to events having a given status.
    :type status: str
    :param severity: Limits the response to events tagged with one of the listed severity values. The possible values are: [MINOR, MODERATE, MAJOR].  Multiple values may be listed, and should be separated by a comma. The default is to return events of any severity.
    :type severity: str
    :param jurisdiction: Limits the response to events reported by a given jurisdiction. The value given must be specified as the ID of a jurisdiction returned by the /jurisdiction resource. The default is to return events from all jurisdictions.
    :type jurisdiction: str
    :param event_type: Limits the response to events tagged with one of the listed event types.  The possible values include: [CONSTRUCTION, INCIDENT, SPECIAL_EVENT, WEATHER_CONDITION].  Multiple values may be listed, and should be separated by a comma. The default is to return events of all types.
    :type event_type: str
    :param created: Limits the response to events based on the date and time that the event was created (first recorded). The date/time must be specified in ISO 8601 format, and may be prefixed by one of the following operators [&lt;, &lt;&#x3D;, &gt;, &gt;&#x3D;] to indicate &#39;before&#39;, &#39;before or equal to&#39;, &#39;after&#39; or &#39;after or equal to&#39; respectively.  For example, &gt;2013-12-01T12:00:00Z requests all events create after Dec. 1, 2015 at 12pm (noon) Coordinated Universal Time.  The default is to return events with any creation time.
    :type created: str
    :param updated: Limits the response to events based on the date and time that the event was last updated. The date/time must be specified in ISO 8601 format, and may be prefixed by one of the following operators [&lt;, &lt;&#x3D;, &gt;, &gt;&#x3D;] to indicate &#39;before&#39;, &#39;before or equal to&#39;, &#39;after&#39; or &#39;after or equal to&#39; respectively.  For example, &gt;2013-12-01T12:00:00Z requests all events updated after Dec. 1, 2015 at 12pm (noon) Coordinated Universal Time. The default is to return events with any update time
    :type updated: str
    :param road_name: Limits the response to events on a given road as specified by the road name.  An example of a valid road name is &#39;Highway 1&#39;. The default is to return events on all roads.
    :type road_name: str
    :param area_id: Limits the response to events within one of the specified areas.  An area must be specified as the ID of an item returned by the /areas resource. For example: an area_id of &#39;drivebc.ca/1&#39; limits events to those within the Lower Mainland District.  The default is to return events in all areas.
    :type area_id: str
    :param bbox: Limits the response to events that fall within the specified geographical bounding box.  The bbox format must be &#39;[min longitude],[min latitude],[max longitude],[max latitude]&#39; with WGS84 coordinates.  For example: -123.45,48.99,-122.45,49.49.  The default is to return events in all geographical locations.
    :type bbox: str

    """
    return web.Response(status=200)


async def jurisdiction_get(request: web.Request, format=None) -> web.Response:
    """Lists the jurisdictions publishing data through this Open511 API implementation

    

    :param format: The format of the response
    :type format: str

    """
    return web.Response(status=200)


async def jurisdictiongeography_get(request: web.Request, format=None) -> web.Response:
    """Provides the geographical boundaries for all the jurisdictions.

    

    :param format: The format of the response
    :type format: str

    """
    return web.Response(status=200)
