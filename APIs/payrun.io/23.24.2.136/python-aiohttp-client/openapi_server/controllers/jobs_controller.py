from typing import List, Dict
from aiohttp import web

from openapi_server.models.batch_job_instruction import BatchJobInstruction
from openapi_server.models.cis_job_instruction_base import CisJobInstructionBase
from openapi_server.models.dps_job_instruction import DpsJobInstruction
from openapi_server.models.error_model import ErrorModel
from openapi_server.models.job_info import JobInfo
from openapi_server.models.link import Link
from openapi_server.models.link_collection import LinkCollection
from openapi_server.models.pay_run_job_instruction import PayRunJobInstruction
from openapi_server.models.rti_job_instruction import RtiJobInstruction
from openapi_server.models.third_party_job_instruction import ThirdPartyJobInstruction
from openapi_server import util


async def delete_batch_job(request: web.Request, job_id, authorization, api_version) -> web.Response:
    """Delete the Batch job

    Deletes the the Batch job

    :param job_id: The job unique identifier.
    :type job_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def delete_cis_job(request: web.Request, job_id, authorization, api_version) -> web.Response:
    """Delete the CIS job

    Deletes the the CIS job

    :param job_id: The job unique identifier.
    :type job_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def delete_dps_job(request: web.Request, job_id, authorization, api_version) -> web.Response:
    """Delete the DPS job

    Deletes the the DPS job

    :param job_id: The job unique identifier.
    :type job_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def delete_pay_run_job(request: web.Request, job_id, authorization, api_version) -> web.Response:
    """Delete the pay run job

    Deletes the the payrun job

    :param job_id: The job unique identifier.
    :type job_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def delete_rti_job(request: web.Request, job_id, authorization, api_version) -> web.Response:
    """Delete the RTI job

    Deletes the the RTI job

    :param job_id: The job unique identifier.
    :type job_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def delete_third_party_job(request: web.Request, job_id, authorization, api_version) -> web.Response:
    """Delete the Third Party job

    Deletes the the Third Party job

    :param job_id: The job unique identifier.
    :type job_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_batch_job_info(request: web.Request, job_id, authorization, api_version) -> web.Response:
    """Get the Batch job information

    Return the the Batch job information

    :param job_id: The job unique identifier.
    :type job_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_batch_job_progress(request: web.Request, job_id, authorization, api_version) -> web.Response:
    """Get the Batch job progress

    Return the the Batch job progress

    :param job_id: The job unique identifier.
    :type job_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_batch_job_status(request: web.Request, job_id, authorization, api_version) -> web.Response:
    """Get the Batch job status

    Return the the Batch job status

    :param job_id: The job unique identifier.
    :type job_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_batch_jobs(request: web.Request, authorization, api_version) -> web.Response:
    """Get all Batch jobs

    Gets all the Batch jobs

    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_cis_job_info(request: web.Request, job_id, authorization, api_version) -> web.Response:
    """Get the CIS job information

    Return the the CIS job information

    :param job_id: The job unique identifier.
    :type job_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_cis_job_progress(request: web.Request, job_id, authorization, api_version) -> web.Response:
    """Get the CIS job progress

    Return the the CIS job progress

    :param job_id: The job unique identifier.
    :type job_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_cis_job_status(request: web.Request, job_id, authorization, api_version) -> web.Response:
    """Get the CIS job status

    Return the the CIS job status

    :param job_id: The job unique identifier.
    :type job_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_cis_jobs(request: web.Request, authorization, api_version) -> web.Response:
    """Get all CIS jobs

    Gets all the CIS jobs

    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_dps_job_info(request: web.Request, job_id, authorization, api_version) -> web.Response:
    """Get the DPS job information

    Return the the DPS job information

    :param job_id: The job unique identifier.
    :type job_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_dps_job_progress(request: web.Request, job_id, authorization, api_version) -> web.Response:
    """Get the DPS job progress

    Return the the DPS job progress

    :param job_id: The job unique identifier.
    :type job_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_dps_job_status(request: web.Request, job_id, authorization, api_version) -> web.Response:
    """Get the DPS job status

    Return the the DPS job status

    :param job_id: The job unique identifier.
    :type job_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_dps_jobs(request: web.Request, authorization, api_version) -> web.Response:
    """Get all DPS jobs

    Gets all the DPS jobs

    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_employer_jobs(request: web.Request, employer_id, authorization, api_version) -> web.Response:
    """Gets all jobs relating to the employer.

    Returns all job information objects for the specified employer.

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_pay_run_job_info(request: web.Request, job_id, authorization, api_version) -> web.Response:
    """Get the pay run job information

    Return the the payrun job information

    :param job_id: The job unique identifier.
    :type job_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_pay_run_job_progress(request: web.Request, job_id, authorization, api_version) -> web.Response:
    """Get the pay run job progress

    Return the the payrun job progress

    :param job_id: The job unique identifier.
    :type job_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_pay_run_job_status(request: web.Request, job_id, authorization, api_version) -> web.Response:
    """Get the pay run job status

    Return the the payrun job status

    :param job_id: The job unique identifier.
    :type job_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_pay_run_jobs(request: web.Request, authorization, api_version) -> web.Response:
    """Get all PayRun jobs

    Gets all the pay run jobs

    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_rti_job_info(request: web.Request, job_id, authorization, api_version) -> web.Response:
    """Get the RTI job information

    Return the the RTI job information

    :param job_id: The job unique identifier.
    :type job_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_rti_job_progress(request: web.Request, job_id, authorization, api_version) -> web.Response:
    """Get the RTI job progress

    Return the the RTI job progress

    :param job_id: The job unique identifier.
    :type job_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_rti_job_status(request: web.Request, job_id, authorization, api_version) -> web.Response:
    """Get the RTI job status

    Return the the RTI job status

    :param job_id: The job unique identifier.
    :type job_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_rti_jobs(request: web.Request, authorization, api_version) -> web.Response:
    """Get all RTI jobs

    Gets all the RTI jobs

    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_third_party_job_info(request: web.Request, job_id, authorization, api_version) -> web.Response:
    """Get the Third Party job information

    Return the the Third Party job information

    :param job_id: The job unique identifier.
    :type job_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_third_party_job_progress(request: web.Request, job_id, authorization, api_version) -> web.Response:
    """Get the Third Party job progress

    Return the the Third Party job progress

    :param job_id: The job unique identifier.
    :type job_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_third_party_job_status(request: web.Request, job_id, authorization, api_version) -> web.Response:
    """Get the Third Party job status

    Return the the Third Party job status

    :param job_id: The job unique identifier.
    :type job_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_third_party_jobs(request: web.Request, authorization, api_version) -> web.Response:
    """Get all Third Party jobs

    Gets all the Third Party jobs

    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def post_new_batch_job(request: web.Request, authorization, api_version, body) -> web.Response:
    """Create new Batch job

    Adds a new Batch job to the queue and returns the job info

    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str
    :param body: The the batch job instruction object.
    :type body: dict | bytes

    """
    body = BatchJobInstruction.from_dict(body)
    return web.Response(status=200)


async def post_new_cis_job(request: web.Request, authorization, api_version, body) -> web.Response:
    """Create new CIS job

    Adds a new CIS job to the queue and returns the job info

    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str
    :param body: The the CIS job instruction object.
    :type body: dict | bytes

    """
    body = CisJobInstructionBase.from_dict(body)
    return web.Response(status=200)


async def post_new_dps_job(request: web.Request, authorization, api_version, body) -> web.Response:
    """Create new DPS job

    Creates the new DPS job to the queue and returns the job info

    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str
    :param body: The the DPS job instruction object.
    :type body: dict | bytes

    """
    body = DpsJobInstruction.from_dict(body)
    return web.Response(status=200)


async def post_new_pay_run_job(request: web.Request, authorization, api_version, body) -> web.Response:
    """Create new PayRun job

    Creates the new pay run job to the queue and returns the job info

    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str
    :param body: The pay run job instruction object.
    :type body: dict | bytes

    """
    body = PayRunJobInstruction.from_dict(body)
    return web.Response(status=200)


async def post_new_rti_job(request: web.Request, authorization, api_version, body) -> web.Response:
    """Create new RTI job

    Creates the new RTI job to the queue and returns the job info

    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str
    :param body: The the RTI job instruction object.
    :type body: dict | bytes

    """
    body = RtiJobInstruction.from_dict(body)
    return web.Response(status=200)


async def post_new_third_party_job(request: web.Request, authorization, api_version, body) -> web.Response:
    """Create new Third Party job

    Adds a new Third Party job to the queue and returns the job info

    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str
    :param body: The the third party job instruction object.
    :type body: dict | bytes

    """
    body = ThirdPartyJobInstruction.from_dict(body)
    return web.Response(status=200)
