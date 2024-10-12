from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_compliance_job_request import CreateComplianceJobRequest
from openapi_server.models.create_compliance_job_response import CreateComplianceJobResponse
from openapi_server.models.error import Error
from openapi_server.models.get2_compliance_jobs_id_response import Get2ComplianceJobsIdResponse
from openapi_server.models.get2_compliance_jobs_response import Get2ComplianceJobsResponse
from openapi_server.models.problem import Problem
from openapi_server.models.tweet_compliance_stream_response import TweetComplianceStreamResponse
from openapi_server.models.tweet_label_stream_response import TweetLabelStreamResponse
from openapi_server.models.user_compliance_stream_response import UserComplianceStreamResponse
from openapi_server import util


async def create_batch_compliance_job(request: web.Request, body) -> web.Response:
    """Create compliance job

    Creates a compliance for the given job type

    :param body: 
    :type body: dict | bytes

    """
    body = CreateComplianceJobRequest.from_dict(body)
    return web.Response(status=200)


async def get_batch_compliance_job(request: web.Request, id, compliance_job_fields=None) -> web.Response:
    """Get Compliance Job

    Returns a single Compliance Job by ID

    :param id: The ID of the Compliance Job to retrieve.
    :type id: str
    :param compliance_job_fields: A comma separated list of ComplianceJob fields to display.
    :type compliance_job_fields: List[str]

    """
    return web.Response(status=200)


async def get_tweets_compliance_stream(request: web.Request, partition, backfill_minutes=None, start_time=None, end_time=None) -> web.Response:
    """Tweets Compliance stream

    Streams 100% of compliance data for Tweets

    :param partition: The partition number.
    :type partition: int
    :param backfill_minutes: The number of minutes of backfill requested.
    :type backfill_minutes: int
    :param start_time: YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp from which the Tweet Compliance events will be provided.
    :type start_time: str
    :param end_time: YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp to which the Tweet Compliance events will be provided.
    :type end_time: str

    """
    start_time = util.deserialize_datetime(start_time)
    end_time = util.deserialize_datetime(end_time)
    return web.Response(status=200)


async def get_tweets_label_stream(request: web.Request, backfill_minutes=None, start_time=None, end_time=None) -> web.Response:
    """Tweets Label stream

    Streams 100% of labeling events applied to Tweets

    :param backfill_minutes: The number of minutes of backfill requested.
    :type backfill_minutes: int
    :param start_time: YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp from which the Tweet labels will be provided.
    :type start_time: str
    :param end_time: YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp from which the Tweet labels will be provided.
    :type end_time: str

    """
    start_time = util.deserialize_datetime(start_time)
    end_time = util.deserialize_datetime(end_time)
    return web.Response(status=200)


async def get_users_compliance_stream(request: web.Request, partition, backfill_minutes=None, start_time=None, end_time=None) -> web.Response:
    """Users Compliance stream

    Streams 100% of compliance data for Users

    :param partition: The partition number.
    :type partition: int
    :param backfill_minutes: The number of minutes of backfill requested.
    :type backfill_minutes: int
    :param start_time: YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp from which the User Compliance events will be provided.
    :type start_time: str
    :param end_time: YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp from which the User Compliance events will be provided.
    :type end_time: str

    """
    start_time = util.deserialize_datetime(start_time)
    end_time = util.deserialize_datetime(end_time)
    return web.Response(status=200)


async def list_batch_compliance_jobs(request: web.Request, type, status=None, compliance_job_fields=None) -> web.Response:
    """List Compliance Jobs

    Returns recent Compliance Jobs for a given job type and optional job status

    :param type: Type of Compliance Job to list.
    :type type: str
    :param status: Status of Compliance Job to list.
    :type status: str
    :param compliance_job_fields: A comma separated list of ComplianceJob fields to display.
    :type compliance_job_fields: List[str]

    """
    return web.Response(status=200)
