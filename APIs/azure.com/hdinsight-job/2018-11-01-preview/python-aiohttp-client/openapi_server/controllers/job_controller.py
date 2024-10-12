from typing import List, Dict
from aiohttp import web

from openapi_server.models.app_state import AppState
from openapi_server.models.job_detail_root_json_object import JobDetailRootJsonObject
from openapi_server.models.job_list_json_object import JobListJsonObject
from openapi_server.models.job_operations_error_response import JobOperationsErrorResponse
from openapi_server.models.job_submission_json_response import JobSubmissionJsonResponse
from openapi_server import util


async def job_get(request: web.Request, user_name, job_id, fields) -> web.Response:
    """job_get

    Gets job details from the specified HDInsight cluster.

    :param user_name: The user name used for running job.
    :type user_name: str
    :param job_id: The id of the job.
    :type job_id: str
    :param fields: If fields set to &#39;*&#39;, the request will return full details of the job. Currently the value can only be &#39;*&#39;.
    :type fields: str

    """
    return web.Response(status=200)


async def job_get_app_state(request: web.Request, app_id) -> web.Response:
    """job_get_app_state

    Gets application state from the specified HDInsight cluster.

    :param app_id: The id of the job.
    :type app_id: str

    """
    return web.Response(status=200)


async def job_kill(request: web.Request, user_name, job_id) -> web.Response:
    """job_kill

    Initiates cancel on given running job in the specified HDInsight.

    :param user_name: The user name used for running job.
    :type user_name: str
    :param job_id: The id of the job.
    :type job_id: str

    """
    return web.Response(status=200)


async def job_list(request: web.Request, user_name, showall, fields) -> web.Response:
    """job_list

    Gets the list of jobs from the specified HDInsight cluster.

    :param user_name: The user name used for running job.
    :type user_name: str
    :param showall: If showall is set to &#39;true&#39;, the request will return all jobs the user has permission to view, not only the jobs belonging to the user.
    :type showall: str
    :param fields: If fields set to &#39;*&#39;, the request will return full details of the job. Currently the value can only be &#39;*&#39;.
    :type fields: str

    """
    return web.Response(status=200)


async def job_list_after_job_id(request: web.Request, user_name, showall, fields, jobid=None, numrecords=None) -> web.Response:
    """job_list_after_job_id

    Gets numrecords Of Jobs after jobid from the specified HDInsight cluster.

    :param user_name: The user name used for running job.
    :type user_name: str
    :param showall: If showall is set to &#39;true&#39;, the request will return all jobs the user has permission to view, not only the jobs belonging to the user.
    :type showall: str
    :param fields: If fields set to &#39;*&#39;, the request will return full details of the job. Currently the value can only be &#39;*&#39;.
    :type fields: str
    :param jobid: JobId from where to list jobs.
    :type jobid: str
    :param numrecords: Number of jobs to fetch.
    :type numrecords: int

    """
    return web.Response(status=200)


async def job_submit_hive_job(request: web.Request, user_name, content) -> web.Response:
    """job_submit_hive_job

    Submits a Hive job to an HDInsight cluster.

    :param user_name: The user name used for running job.
    :type user_name: str
    :param content: The content of the Hive job request.
    :type content: 

    """
    return web.Response(status=200)


async def job_submit_map_reduce_job(request: web.Request, user_name, content) -> web.Response:
    """job_submit_map_reduce_job

    Submits a MapReduce job to an HDInsight cluster.

    :param user_name: The user name used for running job.
    :type user_name: str
    :param content: The content of the MapReduce job request.
    :type content: 

    """
    return web.Response(status=200)


async def job_submit_map_reduce_streaming_job(request: web.Request, user_name, content) -> web.Response:
    """job_submit_map_reduce_streaming_job

    Submits a MapReduce streaming job to an HDInsight cluster.

    :param user_name: The user name used for running job.
    :type user_name: str
    :param content: The content of the MapReduce job request.
    :type content: 

    """
    return web.Response(status=200)


async def job_submit_pig_job(request: web.Request, user_name, content) -> web.Response:
    """job_submit_pig_job

    Submits a Pig job to an HDInsight cluster.

    :param user_name: The user name used for running job.
    :type user_name: str
    :param content: The content of the Pig job request.
    :type content: 

    """
    return web.Response(status=200)


async def job_submit_sqoop_job(request: web.Request, user_name, content) -> web.Response:
    """job_submit_sqoop_job

    Submits a Sqoop job to an HDInsight cluster.

    :param user_name: The user name used for running job.
    :type user_name: str
    :param content: The content of the Sqoop job request.
    :type content: 

    """
    return web.Response(status=200)
