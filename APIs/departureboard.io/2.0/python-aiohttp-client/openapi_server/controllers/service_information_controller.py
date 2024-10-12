from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def get_service_details_by_id(request: web.Request, service_id, api_key) -> web.Response:
    """getServiceDetailsByID is used to get information on a service, by the Service ID. This will typically return a train service, but will also return a bus and ferry services. The Service ID must be provided in the serviceIDUrlSafe format that is provided in the response for Arrival and Departure Boards. A service ID is specific to a station, and can only be looked up for a short time after a train/bus/ferry arrives at, or departs from a station. This is a National Rail limitation.

    

    :param service_id: The Service ID for the Train Service you wish to look up in the URL Safe format. For example \&quot;qsec4O8LW7k8ITcOt_ir4Q--\&quot;.
    :type service_id: str
    :param api_key: The National Rail OpenLDBWS API Key to use for looking up service information. You must register with National Rail to obtain this key and whitelist it with us. See https://api.departureboard.io/docs/registration for more information.
    :type api_key: str

    """
    return web.Response(status=200)
