from typing import List, Dict
from aiohttp import web

from openapi_server.models.address_to_validate import AddressToValidate
from openapi_server.models.address_validation_result import AddressValidationResult
from openapi_server.models.error_response_body import ErrorResponseBody
from openapi_server.models.parse_address_request_body import ParseAddressRequestBody
from openapi_server.models.parse_address_response_body import ParseAddressResponseBody
from openapi_server import util


async def parse_address(request: web.Request, body) -> web.Response:
    """Parse an address

    The address-recognition API makes it easy for you to extract address data from unstructured text, including the recipient name, line 1, line 2, city, postal code, and more.  Data often enters your system as unstructured text (for example: emails, SMS messages, support tickets, or other documents). ShipEngine&#39;s address-recognition API helps you extract meaningful, structured data from this unstructured text. The parsed address data is returned in the same structure that&#39;s used for other ShipEngine APIs, such as address validation, rate quotes, and shipping labels.  &gt; **Note:** Address recognition is currently supported for the United States, Canada, Australia, New Zealand, the United Kingdom, and Ireland. 

    :param body: The only required field is &#x60;text&#x60;, which is the text to be parsed. You can optionally also provide an &#x60;address&#x60; containing already-known values. For example, you may already know the recipient&#39;s name, city, and country, and only want to parse the street address into separate lines. 
    :type body: dict | bytes

    """
    body = ParseAddressRequestBody.from_dict(body)
    return web.Response(status=200)


async def validate_address(request: web.Request, body) -> web.Response:
    """Validate An Address

    Address validation ensures accurate addresses and can lead to reduced shipping costs by preventing address correction surcharges. ShipEngine cross references multiple databases to validate addresses and identify potential deliverability issues. 

    :param body: 
    :type body: list | bytes

    """
    body = [AddressToValidate.from_dict(d) for d in body]
    return web.Response(status=200)
