from typing import List, Dict
from aiohttp import web

from openapi_server.models.destination_definition_id_with_workspace_id import DestinationDefinitionIdWithWorkspaceId
from openapi_server.models.destination_definition_specification_read import DestinationDefinitionSpecificationRead
from openapi_server.models.invalid_input_exception_info import InvalidInputExceptionInfo
from openapi_server.models.not_found_known_exception_info import NotFoundKnownExceptionInfo
from openapi_server import util


async def get_destination_definition_specification(request: web.Request, body) -> web.Response:
    """Get specification for a destinationDefinition

    

    :param body: 
    :type body: dict | bytes

    """
    body = DestinationDefinitionIdWithWorkspaceId.from_dict(body)
    return web.Response(status=200)
