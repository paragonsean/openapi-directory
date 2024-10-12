from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def get_channel(request: web.Request, channel_id, aliases=None) -> web.Response:
    """Channel Detail

    Return the content of the selected channel.

    :param channel_id: The identifier for the selected channel.
    :type channel_id: str
    :param aliases: Flag to display Legacy and Provider Ids.
    :type aliases: bool

    """
    return web.Response(status=200)


async def list_channels(request: web.Request, platform_id=None, region_id=None, aliases=None, _date=None, schedule_start=None, schedule_end=None, schedule_updated_since=None) -> web.Response:
    """Channel Collection

    If you are interested in a list of channels that have had there schedule updated you can filter by the following query params.  - scheduleStart  - scheduleEnd  - scheduleUpdatedSince  adding these query params will filter the channel collection to only return channels that have been updated within the given range, updatedSince stores the state of your previous call.  Example Usage: Every 10 minutes get me the channels that have updated schedules for the next 2 weeks.  /channel?platform&#x3D;{uuid}&amp;scheduleStart&#x3D;{today}&amp;scheduleEnd&#x3D;{today + 2 weeks}&amp;updatedSince&#x3D;{10 minutes ago}  Also please note epg numbers are only exposed when a platform and region are passed to the query.

    :param platform_id: The identifier for the selected platform. Multiple platforms can be passed to the API without a region Id. Passing multiple platforms without a region will not return epg numbers as these are linked to a platform and region.
    :type platform_id: str
    :param region_id: The platform region ID for the channel selection.
    :type region_id: str
    :param aliases: Flag to display Legacy and Provider Ids.
    :type aliases: bool
    :param _date: Date of the Channel State to select, this will display channel names and attributes in the future or past.
    :type _date: str
    :param schedule_start: The Start Date for the schedule.
    :type schedule_start: str
    :param schedule_end: The End Date for the schedule.
    :type schedule_end: str
    :param schedule_updated_since: Schedule Updated Since
    :type schedule_updated_since: str

    """
    return web.Response(status=200)
