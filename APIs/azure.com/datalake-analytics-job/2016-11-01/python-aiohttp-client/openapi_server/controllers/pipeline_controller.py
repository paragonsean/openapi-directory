from typing import List, Dict
from aiohttp import web

from openapi_server.models.job_pipeline_information import JobPipelineInformation
from openapi_server.models.job_pipeline_information_list_result import JobPipelineInformationListResult
from openapi_server import util


async def pipeline_get(request: web.Request, pipeline_identity, api_version, start_date_time=None, end_date_time=None) -> web.Response:
    """pipeline_get

    Gets the Pipeline information for the specified pipeline ID.

    :param pipeline_identity: Pipeline ID.
    :type pipeline_identity: str
    :type pipeline_identity: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param start_date_time: The start date for when to get the pipeline and aggregate its data. The startDateTime and endDateTime can be no more than 30 days apart.
    :type start_date_time: str
    :param end_date_time: The end date for when to get the pipeline and aggregate its data. The startDateTime and endDateTime can be no more than 30 days apart.
    :type end_date_time: str

    """
    start_date_time = util.deserialize_datetime(start_date_time)
    end_date_time = util.deserialize_datetime(end_date_time)
    return web.Response(status=200)


async def pipeline_list(request: web.Request, api_version, start_date_time=None, end_date_time=None) -> web.Response:
    """pipeline_list

    Lists all pipelines.

    :param api_version: Client Api Version.
    :type api_version: str
    :param start_date_time: The start date for when to get the list of pipelines. The startDateTime and endDateTime can be no more than 30 days apart.
    :type start_date_time: str
    :param end_date_time: The end date for when to get the list of pipelines. The startDateTime and endDateTime can be no more than 30 days apart.
    :type end_date_time: str

    """
    start_date_time = util.deserialize_datetime(start_date_time)
    end_date_time = util.deserialize_datetime(end_date_time)
    return web.Response(status=200)
