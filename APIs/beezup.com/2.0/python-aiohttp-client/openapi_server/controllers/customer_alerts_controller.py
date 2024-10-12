from typing import List, Dict
from aiohttp import web

from openapi_server.models.beez_up_common_error_response_message import BeezUPCommonErrorResponseMessage
from openapi_server.models.save_store_alert_request import SaveStoreAlertRequest
from openapi_server.models.store_alerts import StoreAlerts
from openapi_server import util


async def get_store_alerts(request: web.Request, store_id, if_none_match=None) -> web.Response:
    """Get store&#39;s alerts

    

    :param store_id: Your store identifier
    :type store_id: str
    :param if_none_match: ETag value to identify the last known version of requested resource.\\ To avoid useless exchange, we recommend you to indicate the ETag you previously got from this operation.\\ If the ETag value does not match the response will be 200 to give you a new content, otherwise the response will be: 304 Not Modified, without any content.\\ For more details go to this link: http://tools.ietf.org/html/rfc7232#section-2.3 
    :type if_none_match: str

    """
    return web.Response(status=200)


async def save_store_alerts(request: web.Request, store_id, body) -> web.Response:
    """Save store alerts

    You just have to send the alert you want to update, does not need all alerts. (PARTIAL UPDATE ACCEPTED)

    :param store_id: Your store identifier
    :type store_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = {k: SaveStoreAlertRequest.from_dict(v) for k, v in body}
    return web.Response(status=200)
