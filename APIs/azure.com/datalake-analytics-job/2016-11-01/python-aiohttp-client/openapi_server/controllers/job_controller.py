from typing import List, Dict
from aiohttp import web

from openapi_server.models.build_job_parameters import BuildJobParameters
from openapi_server.models.create_job_parameters import CreateJobParameters
from openapi_server.models.job_data_path import JobDataPath
from openapi_server.models.job_info_list_result import JobInfoListResult
from openapi_server.models.job_information import JobInformation
from openapi_server.models.job_statistics import JobStatistics
from openapi_server import util


async def job_build(request: web.Request, api_version, parameters) -> web.Response:
    """job_build

    Builds (compiles) the specified job in the specified Data Lake Analytics account for job correctness and validation.

    :param api_version: Client Api Version.
    :type api_version: str
    :param parameters: The parameters to build a job.
    :type parameters: dict | bytes

    """
    parameters = BuildJobParameters.from_dict(parameters)
    return web.Response(status=200)


async def job_cancel(request: web.Request, job_identity, api_version) -> web.Response:
    """job_cancel

    Cancels the running job specified by the job ID.

    :param job_identity: Job identifier. Uniquely identifies the job across all jobs submitted to the service.
    :type job_identity: str
    :type job_identity: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def job_create(request: web.Request, job_identity, api_version, parameters) -> web.Response:
    """job_create

    Submits a job to the specified Data Lake Analytics account.

    :param job_identity: Job identifier. Uniquely identifies the job across all jobs submitted to the service.
    :type job_identity: str
    :type job_identity: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param parameters: The parameters to submit a job.
    :type parameters: dict | bytes

    """
    parameters = CreateJobParameters.from_dict(parameters)
    return web.Response(status=200)


async def job_get(request: web.Request, job_identity, api_version) -> web.Response:
    """job_get

    Gets the job information for the specified job ID.

    :param job_identity: JobInfo ID.
    :type job_identity: str
    :type job_identity: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def job_get_debug_data_path(request: web.Request, job_identity, api_version) -> web.Response:
    """job_get_debug_data_path

    Gets the job debug data information specified by the job ID.

    :param job_identity: Job identifier. Uniquely identifies the job across all jobs submitted to the service.
    :type job_identity: str
    :type job_identity: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def job_get_statistics(request: web.Request, job_identity, api_version) -> web.Response:
    """job_get_statistics

    Gets statistics of the specified job.

    :param job_identity: Job Information ID.
    :type job_identity: str
    :type job_identity: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def job_list(request: web.Request, api_version, filter=None, top=None, skip=None, select=None, orderby=None, count=None) -> web.Response:
    """job_list

    Lists the jobs, if any, associated with the specified Data Lake Analytics account. The response includes a link to the next page of results, if any.

    :param api_version: Client Api Version.
    :type api_version: str
    :param filter: OData filter. Optional.
    :type filter: str
    :param top: The number of items to return. Optional.
    :type top: int
    :param skip: The number of items to skip over before returning elements. Optional.
    :type skip: int
    :param select: OData Select statement. Limits the properties on each entry to just those requested, e.g. Categories?$select&#x3D;CategoryName,Description. Optional.
    :type select: str
    :param orderby: OrderBy clause. One or more comma-separated expressions with an optional \&quot;asc\&quot; (the default) or \&quot;desc\&quot; depending on the order you&#39;d like the values sorted, e.g. Categories?$orderby&#x3D;CategoryName desc. Optional.
    :type orderby: str
    :param count: The Boolean value of true or false to request a count of the matching resources included with the resources in the response, e.g. Categories?$count&#x3D;true. Optional.
    :type count: bool

    """
    return web.Response(status=200)
