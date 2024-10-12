from typing import List, Dict
from aiohttp import web

from openapi_server.models.flow_validate_enum_status import FlowValidateEnumStatus
from openapi_server.models.studio_v2_flow_validate import StudioV2FlowValidate
from openapi_server import util


async def update_flow_validate(request: web.Request, definition, friendly_name, status, commit_message=None) -> web.Response:
    """update_flow_validate

    Validate flow JSON definition

    :param definition: JSON representation of flow definition.
    :type definition: dict | bytes
    :param friendly_name: The string that you assigned to describe the Flow.
    :type friendly_name: str
    :param status: 
    :type status: str
    :param commit_message: Description of change made in the revision.
    :type commit_message: str

    """
    definition = object.from_dict(definition)
    return web.Response(status=200)
