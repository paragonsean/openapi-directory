from typing import List, Dict
from aiohttp import web

from openapi_server.models.event_record import EventRecord
from openapi_server import util


async def get_events(request: web.Request, company=None, site=None, deal=None, type=None, nexttoken=None, queryexecutionid=None) -> web.Response:
    """get events for analytics

    By passing in the company, site or deal Id a set of user interaction event records is returned. For pagination of a large result set use queryexecutionid and nexttoken instead. 

    :param company: pass an optional company Id
    :type company: str
    :param site: pass an optional site Id
    :type site: str
    :param deal: pass an optional deal Id
    :type deal: str
    :param type: type of records to return
    :type type: str
    :param nexttoken: next token to start returning records from
    :type nexttoken: str
    :param queryexecutionid: id of execution to get more records based on next token
    :type queryexecutionid: str

    """
    return web.Response(status=200)
