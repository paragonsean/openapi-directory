from typing import List, Dict
from aiohttp import web

from openapi_server.models.schema_response_actions import SchemaResponseActions
from openapi_server import util


async def schema_response_action_read(request: web.Request, schema_response_id) -> web.Response:
    """Retrieve a list of Schema Response Actions for a Schema Response

    This retrieves a paginated list of all Schema Response Actions created for a Schema Response. #### Returns Returns a JSON object with a &#x60;data&#x60; key containing the representation of the requested Schema Response Actions, if the request is successful. #### Errors If the request is unsuccessful, an &#x60;errors&#x60; key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

    :param schema_response_id: The unique identifier of the Registration Schema example &#x60;6176c9d45e01f100091d4f94&#x60;.
    :type schema_response_id: str

    """
    return web.Response(status=200)


async def schema_responses_schema_response_id_actions_post(request: web.Request, schema_response_id) -> web.Response:
    """Create a new Schema Response Action

    This creates a new Schema Response Action in order to trigger a state transition for a Schema Response. #### Returns Returns a JSON object with a &#x60;data&#x60; key containing the representation of the requested Schema Response Actions, if the request is successful. #### Errors If the request is unsuccessful, an &#x60;errors&#x60; key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

    :param schema_response_id: The unique identifier of the Registration Schema example &#x60;6176c9d45e01f100091d4f94&#x60;.
    :type schema_response_id: str

    """
    return web.Response(status=200)


async def schema_responses_schema_response_id_actions_schema_response_action_id_get(request: web.Request, schema_response_id, schema_response_action_id) -> web.Response:
    """A Schema Response Action from a Schema Response

    Retrieves a Schema Response Action by it&#39;s ID. #### Returns Returns a JSON object with a &#x60;data&#x60; key containing the representation of the requested Schema Response Actions, if the request is successful. #### Errors If the request is unsuccessful, an &#x60;errors&#x60; key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

    :param schema_response_id: The unique identifier of the Schema Response example &#x60;61b9cd62eb66180215222669&#x60;.
    :type schema_response_id: str
    :param schema_response_action_id: The unique identifier of the Schema Response Action example &#x60;61b9eae1a7d8ac025c4c46d3&#x60;.
    :type schema_response_action_id: str

    """
    return web.Response(status=200)
