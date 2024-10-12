from typing import List, Dict
from aiohttp import web

from openapi_server.models.position import Position
from openapi_server import util


async def positions_get(request: web.Request, device_id=None, _from=None, to=None, id=None) -> web.Response:
    """Fetches a list of Positions

    We strongly recommend using [Traccar WebSocket API](https://www.traccar.org/traccar-api/) instead of periodically polling positions endpoint. Without any params, it returns a list of last known positions for all the user&#39;s Devices. _from_ and _to_ fields are not required with _id_.

    :param device_id: _deviceId_ is optional, but requires the _from_ and _to_ parameters when used
    :type device_id: int
    :param _from: in IS0 8601 format. eg. &#x60;1963-11-22T18:30:00Z&#x60;
    :type _from: str
    :param to: in IS0 8601 format. eg. &#x60;1963-11-22T18:30:00Z&#x60;
    :type to: str
    :param id: To fetch one or more positions. Multiple params can be passed like &#x60;id&#x3D;31&amp;id&#x3D;42&#x60;
    :type id: int

    """
    _from = util.deserialize_datetime(_from)
    to = util.deserialize_datetime(to)
    return web.Response(status=200)
