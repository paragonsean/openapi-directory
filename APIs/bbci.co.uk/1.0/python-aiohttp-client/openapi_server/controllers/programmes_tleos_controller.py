from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def get_broadcasts_by_channel(request: web.Request, channel, lang, rights, availability, per_page, mixin=None, _from=None) -> web.Response:
    """Get broadcasts by channel

    Get broadcasts by channel

    :param channel: The channel identifier to limit results to.
    :type channel: str
    :param lang: The language for any applicable localised strings.
    :type lang: str
    :param rights: The rights group to limit results to.
    :type rights: str
    :param availability: Whether to return all, or available programmes
    :type availability: str
    :param per_page: The number of results to return.
    :type per_page: int
    :param mixin: Request additional data in the output
    :type mixin: List[str]
    :param _from: Time to return results from, e.g. -3h
    :type _from: str

    """
    return web.Response(status=200)


async def get_highlights_by_category(request: web.Request, category, lang, rights, availability, mixin=None) -> web.Response:
    """List the highlights for a category.

    Get the editorial highlights of a given category in TV &amp; iPlayer.

    :param category: The category identifier to return results from.
    :type category: str
    :param lang: The language for any applicable localised strings.
    :type lang: str
    :param rights: The rights group to limit results to.
    :type rights: str
    :param availability: Whether to return all, or available programmes
    :type availability: str
    :param mixin: Request additional data in the output
    :type mixin: List[str]

    """
    return web.Response(status=200)


async def get_programme_highlights(request: web.Request, lang, rights, availability, mixin=None) -> web.Response:
    """Get programme highlights

    Get programme highlights

    :param lang: The language for any applicable localised strings.
    :type lang: str
    :param rights: The rights group to limit results to.
    :type rights: str
    :param availability: Whether to return all, or available programmes
    :type availability: str
    :param mixin: Request additional data in the output
    :type mixin: List[str]

    """
    return web.Response(status=200)


async def get_programmes_by_category(request: web.Request, category, lang, rights, availability, page, per_page) -> web.Response:
    """List all the programmes for a category.

    Get the list of all the Programmes (TLEOs) for a given category in TV &amp; iPlayer.

    :param category: The category identifier to return results from.
    :type category: str
    :param lang: The language for any applicable localised strings.
    :type lang: str
    :param rights: The rights group to limit results to.
    :type rights: str
    :param availability: Whether to return all, or available programmes
    :type availability: str
    :param page: The page index.
    :type page: int
    :param per_page: The number of results to return.
    :type per_page: int

    """
    return web.Response(status=200)


async def get_programmes_by_channel(request: web.Request, channel, lang, rights, availability, page, per_page) -> web.Response:
    """Get programmes by channel

    Get programmes by channel

    :param channel: The channel identifier to limit results to.
    :type channel: str
    :param lang: The language for any applicable localised strings.
    :type lang: str
    :param rights: The rights group to limit results to.
    :type rights: str
    :param availability: Whether to return all, or available programmes
    :type availability: str
    :param page: The page index.
    :type page: int
    :param per_page: The number of results to return.
    :type per_page: int

    """
    return web.Response(status=200)


async def get_programmes_by_parent_pid(request: web.Request, pid, rights, availability, initial_child_count) -> web.Response:
    """Programme for a given pid.

    Get the programme for a given programme identifier.

    :param pid: The programme identifier.
    :type pid: str
    :param rights: The rights group to limit results to.
    :type rights: str
    :param availability: Whether to return all, or available programmes
    :type availability: str
    :param initial_child_count: The depth to return child entities.
    :type initial_child_count: int

    """
    return web.Response(status=200)
