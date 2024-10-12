from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def get_channels(request: web.Request, lang, region=None) -> web.Response:
    """List all the channels.

    Get the list of all the channels TV &amp; iPlayer.

    :param lang: The language for any applicable localised strings.
    :type lang: str
    :param region: The region to get the channels for.
    :type region: str

    """
    return web.Response(status=200)


async def get_highlights_by_channel(request: web.Request, channel, lang, rights, availability, live=None, mixin=None) -> web.Response:
    """List the highlights for a channel.

    Get the editorial highlights of a given channel in TV &amp; iPlayer.

    :param channel: The channel identifier to limit results to.
    :type channel: str
    :param lang: The language for any applicable localised strings.
    :type lang: str
    :param rights: The rights group to limit results to.
    :type rights: str
    :param availability: Whether to return all, or available programmes
    :type availability: str
    :param live: Whether to include live programmes
    :type live: bool
    :param mixin: Request additional data in the output
    :type mixin: List[str]

    """
    return web.Response(status=200)


async def get_schedule_by_channel(request: web.Request, channel, _date, lang, rights, availability) -> web.Response:
    """Get schedule by channel

    Get schedule by channel

    :param channel: The channel identifier to limit results to.
    :type channel: str
    :param _date: The date to return the schedule for, yyyy-mm-dd format
    :type _date: str
    :param lang: The language for any applicable localised strings.
    :type lang: str
    :param rights: The rights group to limit results to.
    :type rights: str
    :param availability: Whether to return all, or available programmes
    :type availability: str

    """
    return web.Response(status=200)
