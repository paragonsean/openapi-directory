from typing import List, Dict
from aiohttp import web

from openapi_server.models.bulkexports_v1_export_configuration import BulkexportsV1ExportConfiguration
from openapi_server import util


async def fetch_export_configuration(request: web.Request, resource_type) -> web.Response:
    """fetch_export_configuration

    Fetch a specific Export Configuration.

    :param resource_type: The type of communication – Messages, Calls, Conferences, and Participants
    :type resource_type: str

    """
    return web.Response(status=200)


async def update_export_configuration(request: web.Request, resource_type, enabled=None, webhook_method=None, webhook_url=None) -> web.Response:
    """update_export_configuration

    Update a specific Export Configuration.

    :param resource_type: The type of communication – Messages, Calls, Conferences, and Participants
    :type resource_type: str
    :param enabled: If true, Twilio will automatically generate every day&#39;s file when the day is over.
    :type enabled: bool
    :param webhook_method: Sets whether Twilio should call a webhook URL when the automatic generation is complete, using GET or POST. The actual destination is set in the webhook_url
    :type webhook_method: str
    :param webhook_url: Stores the URL destination for the method specified in webhook_method.
    :type webhook_url: str

    """
    return web.Response(status=200)
