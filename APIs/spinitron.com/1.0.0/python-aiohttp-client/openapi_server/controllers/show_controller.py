from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.show import Show
from openapi_server.models.shows_get200_response import ShowsGet200Response
from openapi_server import util


async def shows_get(request: web.Request, start=None, end=None, count=None, page=None, fields=None, expand=None) -> web.Response:
    """Returns scheduled shows optionally filtered by {start} and/or {end} datetimes

    **Terminology**: Spinitron defines a *show* as a radio program. A show can have one or more *schedules*, each of which may specify either an *occurence* or a *repetition*, which represents a set of occurences. Thus scheduled shows have occurences that, for example, may be displayed in a calendar.  In the response, &#x60;items&#x60; is an array of objects representing occurences of scheduled shows.  You may optionally filter &#x60;items&#x60; to a datetime *range* by including in the request {start} and/or {end} parameters, both of which must be no more than one hour in the past. An occurence starting at {end} is included in the reponse.  &#x60;itmes&#x60; can include occurences that begin *or* end within the filter range. A show that goes on air before {start} appears in &#x60;items&#x60; if it ends *after* but not *at* {start}. An occurence starting at or before {end} is included.  If the request omits the {start} parameter, the server sets its value to the current time so that the filter range&#39;s start is always defined. If the request specifies {end} then the requested range is *bounded*, otherwise it is *unbounded*.  For a bounded request, &#x60;items&#x60; includes *every* occurence of all shows occuring in the range. The only difference between objects in &#x60;items&#x60; representing a given show will be the &#x60;start&#x60; field value.  For an unbounded request, &#x60;items&#x60; includes *only one* occurence per show, specifically, the next occurrence after {start} of all shows occuring after {start}.  Use an unbounded request to get a straight list all shows. Use a bounded request to get a calendar/agenda of shows expanded into occurrences by thir shedules and repetitions.  Objects in &#x60;items&#x60; are ordered first by &#x60;datetime&#x60; and then by &#x60;id&#x60;. 

    :param start: The datetime starting from items must be returned. Maximum 1 hour in past. 
    :type start: str
    :param end: The ending datetime. Maximum 1 hour in past. 
    :type end: str
    :param count: Amount of items to return
    :type count: int
    :param page: Offset, used together with count
    :type page: int
    :param fields: Allows to select only needed fields
    :type fields: List[str]
    :param expand: Allows to select extra fields
    :type expand: List[str]

    """
    start = util.deserialize_datetime(start)
    end = util.deserialize_datetime(end)
    return web.Response(status=200)


async def shows_id_get(request: web.Request, id, fields=None, expand=None) -> web.Response:
    """Get a Show by id

    The response object represents the next occurence of the show specified by {id}.  Status 404 is returned if a show with {id} does not exist or if it does but all its scheduled occurences elapsed in the past. 

    :param id: 
    :type id: int
    :param fields: Allows to select only needed fields
    :type fields: List[str]
    :param expand: Allows to select extra fields
    :type expand: List[str]

    """
    return web.Response(status=200)
