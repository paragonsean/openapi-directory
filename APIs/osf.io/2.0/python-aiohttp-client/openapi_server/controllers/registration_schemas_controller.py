from typing import List, Dict
from aiohttp import web

from openapi_server.models.registration_schema import RegistrationSchema
from openapi_server import util


async def registration_schema_read(request: web.Request, registration_schema_id) -> web.Response:
    """Retrieve a Registration Schema

    Retrieves the details of a given Registration Schema. Registration Schemas defines the desired supplemental information that should accompany be included in a Registration. Registration Schemas are Read-only to API users. #### Returns Returns a JSON object with a &#x60;data&#x60; key containing the representation of the requested Registration Schemas, if the request is successful. #### Errors If the request is unsuccessful, an &#x60;errors&#x60; key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

    :param registration_schema_id: The unique identifier of the Registration Schema example &#x60;6176c9d45e01f100091d4f94&#x60;.
    :type registration_schema_id: str

    """
    return web.Response(status=200)


async def registration_schemas_list(request: web.Request, ) -> web.Response:
    """Retrieve a list of Registration Schemas

    Retrieve a paginated list of all active Registration Schemas. Registration Schemas describe the supplemental questions that accompany a registration. Registration Schemas are read-only for API users. #### Returns Returns a JSON object containing &#x60;data&#x60; and &#x60;links&#x60; keys. The &#x60;data&#x60; key contains an array of 10 Registration Schemas. Each resource in the array is a separate Registration Schemas object. The &#x60;links&#x60; key contains a dictionary of links that can be used for [pagination](#tag/Pagination). #### Errors This request should never return an error.


    """
    return web.Response(status=200)
