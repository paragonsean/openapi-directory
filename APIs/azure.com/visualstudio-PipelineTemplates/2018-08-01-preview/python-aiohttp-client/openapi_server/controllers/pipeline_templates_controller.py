from typing import List, Dict
from aiohttp import web

from openapi_server.models.pipeline_template_resource_list_result import PipelineTemplateResourceListResult
from openapi_server import util


async def pipeline_templates_list(request: web.Request, api_version) -> web.Response:
    """PipelineTemplates_List

    Gets all pipeline templates which can be used to configure a CI/CD pipeline in a new or an existing Team Services project.

    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)
