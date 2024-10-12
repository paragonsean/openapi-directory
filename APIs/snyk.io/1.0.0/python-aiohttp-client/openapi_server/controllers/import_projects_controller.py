from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_import_job_details200_response import GetImportJobDetails200Response
from openapi_server.models.import_targets_request import ImportTargetsRequest
from openapi_server import util


async def get_import_job_details(request: web.Request, org_id, integration_id, job_id) -> web.Response:
    """Get import job details

    

    :param org_id: The organization ID. The &#x60;API_KEY&#x60; must have admin access to this organization.
    :type org_id: str
    :param integration_id: The unique identifier for the configured integration. This can be found on the [Integration page in the Settings area](https://app.snyk.io/manage/integrations) for all integrations that have been configured.
    :type integration_id: str
    :param job_id: The ID of the job. This can be found in the Location response header from the corresponding POST request that triggered the import job.
    :type job_id: str

    """
    return web.Response(status=200)


async def import_targets(request: web.Request, org_id, integration_id, body=None) -> web.Response:
    """Import targets

    

    :param org_id: The organization ID. The &#x60;API_KEY&#x60; must have admin access to this organization.
    :type org_id: str
    :param integration_id: The unique identifier for the configured integration. This can be found on the [Integration page in the Settings area](https://app.snyk.io/manage/integrations) for all integrations that have been configured.
    :type integration_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = ImportTargetsRequest.from_dict(body)
    return web.Response(status=200)
