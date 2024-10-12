from typing import List, Dict
from aiohttp import web

from openapi_server.models.json_setlists import JsonSetlists
from openapi_server import util


async def resource10_search_setlists_get_setlists_get(request: web.Request, artist_mbid=None, artist_name=None, artist_tmid=None, city_id=None, city_name=None, country_code=None, _date=None, last_fm=None, last_updated=None, p=None, state=None, state_code=None, tour_name=None, venue_id=None, venue_name=None, year=None) -> web.Response:
    """Search for setlists.

    Search for setlists.

    :param artist_mbid: the artist&#39;s Musicbrainz Identifier (mbid)
    :type artist_mbid: str
    :param artist_name: the artist&#39;s name
    :type artist_name: str
    :param artist_tmid: the artist&#39;s Ticketmaster Identifier (tmid)
    :type artist_tmid: int
    :param city_id: the city&#39;s geoId
    :type city_id: str
    :param city_name: the name of the city
    :type city_name: str
    :param country_code: the country code
    :type country_code: str
    :param _date: the date of the event (format dd-MM-yyyy)
    :type _date: str
    :param last_fm: the event&#39;s Last.fm Event ID (deprecated)
    :type last_fm: int
    :param last_updated: the date and time (UTC) when this setlist was last updated (format yyyyMMddHHmmss) - either edited or reverted. search will return setlists that were updated on or after this date
    :type last_updated: str
    :param p: the number of the result page
    :type p: int
    :param state: the state
    :type state: str
    :param state_code: the state code
    :type state_code: str
    :param tour_name: 
    :type tour_name: str
    :param venue_id: the venue id
    :type venue_id: str
    :param venue_name: the name of the venue
    :type venue_name: str
    :param year: the year of the event
    :type year: str

    """
    return web.Response(status=200)
