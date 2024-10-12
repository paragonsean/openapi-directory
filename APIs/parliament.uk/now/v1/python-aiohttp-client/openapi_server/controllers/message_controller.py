from typing import List, Dict
from aiohttp import web

from openapi_server.models.annunciator_message_type import AnnunciatorMessageType
from openapi_server.models.message_view_model import MessageViewModel
from openapi_server import util


async def api_message_message_annunciator_current_get(request: web.Request, annunciator) -> web.Response:
    """Return the current message by annunciator type

    

    :param annunciator: Current message by annunciator
    :type annunciator: dict | bytes

    """
    annunciator = .from_dict(annunciator)
    return web.Response(status=200)


async def api_message_message_annunciator_date_get(request: web.Request, annunciator, _date) -> web.Response:
    """Return the most recent message by annunciator after date time specified

    

    :param annunciator: Message by annunciator type
    :type annunciator: dict | bytes
    :param _date: First message after date time specified
    :type _date: str

    """
    annunciator = .from_dict(annunciator)
    _date = util.deserialize_datetime(_date)
    return web.Response(status=200)
