from typing import List, Dict
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.pipeline_template_definition_list_result import PipelineTemplateDefinitionListResult
from openapi_server import util


async def pipeline_template_definitions_list(request: web.Request, api_version) -> web.Response:
    """pipeline_template_definitions_list

    Lists all pipeline templates which can be used to configure an Azure Pipeline.

    :param api_version: API version to be used with the HTTP request.
    :type api_version: str

    """
    return web.Response(status=200)
