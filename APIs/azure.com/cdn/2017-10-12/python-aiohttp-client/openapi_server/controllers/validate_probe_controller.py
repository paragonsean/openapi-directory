from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.validate_probe_input import ValidateProbeInput
from openapi_server.models.validate_probe_output import ValidateProbeOutput
from openapi_server import util


async def validate_probe(request: web.Request, subscription_id, api_version, validate_probe_input) -> web.Response:
    """validate_probe

    Check if the probe path is a valid path and the file can be accessed. Probe path is the path to a file hosted on the origin server to help accelerate the delivery of dynamic content via the CDN endpoint. This path is relative to the origin path specified in the endpoint configuration.

    :param subscription_id: Azure Subscription ID.
    :type subscription_id: str
    :param api_version: Version of the API to be used with the client request. Current version is 2017-04-02.
    :type api_version: str
    :param validate_probe_input: Input to check.
    :type validate_probe_input: dict | bytes

    """
    validate_probe_input = ValidateProbeInput.from_dict(validate_probe_input)
    return web.Response(status=200)
