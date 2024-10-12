from typing import List, Dict
from aiohttp import web

from openapi_server.models.account_response import AccountResponse
from openapi_server.models.blend_response import BlendResponse
from openapi_server.models.button_response import ButtonResponse
from openapi_server.models.button_response_error_upscaled import ButtonResponseErrorUpscaled
from openapi_server.models.describe_response import DescribeResponse
from openapi_server.models.imagine_response import ImagineResponse
from openapi_server.models.imagine_response_moderated import ImagineResponseModerated
from openapi_server.models.job_cancel_response import JobCancelResponse
from openapi_server.models.job_response import JobResponse
from openapi_server.models.jobs_blend_post_request import JobsBlendPostRequest
from openapi_server.models.jobs_button_post_request import JobsButtonPostRequest
from openapi_server.models.jobs_describe_post_request import JobsDescribePostRequest
from openapi_server.models.jobs_imagine_post_request import JobsImaginePostRequest
from openapi_server.models.response_error import ResponseError
from openapi_server.models.response_max_jobs import ResponseMaxJobs
from openapi_server import util


async def account_get(request: web.Request, ) -> web.Response:
    """account_get

    Retrieve account information


    """
    return web.Response(status=200)


async def jobs_blend_post(request: web.Request, body) -> web.Response:
    """jobs_blend_post

    Submit the Midjourney /blend command

    :param body: 
    :type body: dict | bytes

    """
    body = JobsBlendPostRequest.from_dict(body)
    return web.Response(status=200)


async def jobs_button_post(request: web.Request, body) -> web.Response:
    """jobs_button_post

    Submit the Midjourney /imagine command

    :param body: 
    :type body: dict | bytes

    """
    body = JobsButtonPostRequest.from_dict(body)
    return web.Response(status=200)


async def jobs_cancel_get(request: web.Request, jobid) -> web.Response:
    """jobs_cancel_get

    Cancel execution of job created by jobs/imagine, jobs/button, jobs/blend or jobs/describe

    :param jobid: jobid value returned by jobs/imagine, jobs/button, jobs/blend or jobs/describe
    :type jobid: str

    """
    return web.Response(status=200)


async def jobs_describe_post(request: web.Request, body) -> web.Response:
    """jobs_describe_post

    Submit the Midjourney /describe command

    :param body: 
    :type body: dict | bytes

    """
    body = JobsDescribePostRequest.from_dict(body)
    return web.Response(status=200)


async def jobs_get(request: web.Request, ) -> web.Response:
    """jobs_get

    Get list of currently executing jobs


    """
    return web.Response(status=200)


async def jobs_get_0(request: web.Request, jobid) -> web.Response:
    """jobs_get_0

    Retrieve status and results of jobs/imagine, jobs/button, jobs/blend or jobs/describe

    :param jobid: jobid value returned by jobs/imagine, jobs/button, jobs/blend or jobs/describe
    :type jobid: str

    """
    return web.Response(status=200)


async def jobs_imagine_post(request: web.Request, body) -> web.Response:
    """jobs_imagine_post

    Submit the Midjourney /imagine command

    :param body: 
    :type body: dict | bytes

    """
    body = JobsImaginePostRequest.from_dict(body)
    return web.Response(status=200)
