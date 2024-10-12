from typing import List, Dict
from aiohttp import web

from openapi_server.models.registration_schema_block import RegistrationSchemaBlock
from openapi_server import util


async def schema_response_blocks_read(request: web.Request, schema_response_id) -> web.Response:
    """Retrieve a list of Registration Schema Blocks for a Schema Response

    This returns a list of all the Registration Schema Blocks are contained in Registration Schema. #### Returns Returns a JSON object with a &#x60;data&#x60; key containing the representation of the requested Registration Schemas, if the request is successful. #### Errors If the request is unsuccessful, an &#x60;errors&#x60; key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

    :param schema_response_id: The unique identifier of the Registration Schema example &#x60;6176c9d45e01f100091d4f94&#x60;.
    :type schema_response_id: str

    """
    return web.Response(status=200)


async def schema_responses_schema_response_id_schema_blocks_schema_response_block_id_get(request: web.Request, schema_response_id, schema_response_block_id) -> web.Response:
    """Retrieve a Registration Schema Block

    This returns a Registration Schema Block by it&#39;s ID. #### Returns Returns a JSON object with a &#x60;data&#x60; key containing the representation of the requested Registration Schemas, if the request is successful. #### Errors If the request is unsuccessful, an &#x60;errors&#x60; key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

    :param schema_response_id: The unique identifier of the Registration Schema example &#x60;6176c9d45e01f100091d4f94&#x60;.
    :type schema_response_id: str
    :param schema_response_block_id: The unique identifier of the Schema Response Block example &#x60;61b79f9eadbb5701424a2d5e&#x60;.
    :type schema_response_block_id: str

    """
    return web.Response(status=200)
