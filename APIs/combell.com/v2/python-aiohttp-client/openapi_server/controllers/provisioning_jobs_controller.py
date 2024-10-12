from typing import List, Dict
from aiohttp import web

from openapi_server.models.provisioning_job_completion import ProvisioningJobCompletion
from openapi_server.models.provisioning_job_info import ProvisioningJobInfo
from openapi_server import util


async def provisioningjobs_job_id_get(request: web.Request, job_id, job_id2) -> web.Response:
    """Detail of a provisioning job

    Provisioning failures may occur. Contact support in the event of a failure or wait for error resolution.&lt;br /&gt;  Do NOT retry provisioning until the job reports finished or cancelled.

    :param job_id: 
    :type job_id: str
    :type job_id: str
    :param job_id2: Automatically added
    :type job_id2: str

    """
    return web.Response(status=200)
