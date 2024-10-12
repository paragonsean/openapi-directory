from typing import List, Dict
from aiohttp import web

from openapi_server.models.invalid_input_exception_info import InvalidInputExceptionInfo
from openapi_server.models.not_found_known_exception_info import NotFoundKnownExceptionInfo
from openapi_server.models.source_definition_id_with_workspace_id import SourceDefinitionIdWithWorkspaceId
from openapi_server.models.source_definition_specification_read import SourceDefinitionSpecificationRead
from openapi_server import util


async def get_source_definition_specification(request: web.Request, body) -> web.Response:
    """Get specification for a SourceDefinition.

    

    :param body: 
    :type body: dict | bytes

    """
    body = SourceDefinitionIdWithWorkspaceId.from_dict(body)
    return web.Response(status=200)
