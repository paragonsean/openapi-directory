from typing import List, Dict
from aiohttp import web

from openapi_server.models.bulkexports_v1_export_export_custom_job import BulkexportsV1ExportExportCustomJob
from openapi_server.models.list_export_custom_job_response import ListExportCustomJobResponse
from openapi_server import util


async def create_export_custom_job(request: web.Request, resource_type, end_day, friendly_name, start_day, email=None, webhook_method=None, webhook_url=None) -> web.Response:
    """create_export_custom_job

    

    :param resource_type: The type of communication – Messages or Calls, Conferences, and Participants
    :type resource_type: str
    :param end_day: The end day for the custom export specified as a string in the format of yyyy-mm-dd. End day is inclusive and must be 2 days earlier than the current UTC day.
    :type end_day: str
    :param friendly_name: The friendly name specified when creating the job
    :type friendly_name: str
    :param start_day: The start day for the custom export specified as a string in the format of yyyy-mm-dd
    :type start_day: str
    :param email: The optional email to send the completion notification to. You can set both webhook, and email, or one or the other. If you set neither, the job will run but you will have to query to determine your job&#39;s status.
    :type email: str
    :param webhook_method: This is the method used to call the webhook on completion of the job. If this is supplied, &#x60;WebhookUrl&#x60; must also be supplied.
    :type webhook_method: str
    :param webhook_url: The optional webhook url called on completion of the job. If this is supplied, &#x60;WebhookMethod&#x60; must also be supplied. If you set neither webhook nor email, you will have to check your job&#39;s status manually.
    :type webhook_url: str

    """
    return web.Response(status=200)


async def list_export_custom_job(request: web.Request, resource_type, page_size=None, page=None, page_token=None) -> web.Response:
    """list_export_custom_job

    

    :param resource_type: The type of communication – Messages, Calls, Conferences, and Participants
    :type resource_type: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)
