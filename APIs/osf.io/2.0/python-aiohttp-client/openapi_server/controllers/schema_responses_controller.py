from typing import List, Dict
from aiohttp import web

from openapi_server.models.schema_responses import SchemaResponses
from openapi_server import util


async def schema_response_delete(request: web.Request, schema_response_id) -> web.Response:
    """Delete a Incomplete Schema Response

    This endpoint deletes a new Schema Response. Schema Responses can only be deleted in the &#x60;in_progress&#x60; state. Once a Schema Response is transitioned to an &#x60;approved&#x60; it is immutable and another Schema Response must be created to update the Schema Response for that registration. #### Returns Returns a JSON object with a &#x60;data&#x60; key containing an updated representation of the requested Schema Response, if the request is successful. #### Errors If the request is unsuccessful, an &#x60;errors&#x60; key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

    :param schema_response_id: The unique identifier of the Registration Schema example &#x60;6176c9d45e01f100091d4f94&#x60;.
    :type schema_response_id: str

    """
    return web.Response(status=200)


async def schema_response_patch(request: web.Request, schema_response_id, body) -> web.Response:
    """Update a Registration&#39;s Schema Response

    Patching to this endpoint allows one to directly edit the revision responses on the Schema Response of a Registration if that Schema Response is in an &#x60;in_progress&#x60; state. #### Returns Returns a JSON object with a &#x60;data&#x60; key containing an updated representation of the requested Schema Response, if the request is successful. #### Errors If the request is unsuccessful, an &#x60;errors&#x60; key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

    :param schema_response_id: The unique identifier of the Registration Schema example &#x60;6176c9d45e01f100091d4f94&#x60;.
    :type schema_response_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = SchemaResponses.from_dict(body)
    return web.Response(status=200)


async def schema_response_ppost(request: web.Request, body) -> web.Response:
    """Create a new Schema Response

    This endpoint creates a new Schema Response with an &#x60;in_progress&#x60; state. A new response can only be created if the current schema response is in an &#x60;approved&#x60; state. #### Returns Returns a JSON object with a &#x60;data&#x60; key containing an updated representation of the requested Schema Response, if the request is successful. #### Errors If the request is unsuccessful, an &#x60;errors&#x60; key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

    :param body: 
    :type body: dict | bytes

    """
    body = SchemaResponses.from_dict(body)
    return web.Response(status=200)


async def schema_responses_list(request: web.Request, ) -> web.Response:
    """List all Schema Responses

    This retrieves a paginated list of all active Schema Responses that are public. #### Returns Returns a JSON object containing &#x60;data&#x60; and &#x60;links&#x60; keys. The &#x60;data&#x60; key contains an array of 10 Schema Responses. Each resource in the array is a separate Registration Schemas object. The &#x60;links&#x60; key contains a dictionary of links that can be used for [pagination](#tag/Pagination). #### Errors This request should never return an error.


    """
    return web.Response(status=200)


async def schema_responses_read(request: web.Request, schema_response_id) -> web.Response:
    """Retrieve a Schema Response

    This retrieves a single Schema response using it&#39;s id. #### Returns Returns a JSON object with a &#x60;data&#x60; key containing the representation of the requested Schema Response, if the request is successful. #### Errors If the request is unsuccessful, an &#x60;errors&#x60; key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

    :param schema_response_id: The unique identifier of the Registration Schema example &#x60;6176c9d45e01f100091d4f94&#x60;.
    :type schema_response_id: str

    """
    return web.Response(status=200)
