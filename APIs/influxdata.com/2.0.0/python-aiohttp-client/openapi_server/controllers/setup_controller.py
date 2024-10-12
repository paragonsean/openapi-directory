from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.is_onboarding import IsOnboarding
from openapi_server.models.onboarding_request import OnboardingRequest
from openapi_server.models.onboarding_response import OnboardingResponse
from openapi_server import util


async def get_setup(request: web.Request, zap_trace_span=None) -> web.Response:
    """Check if database has default user, org, bucket

    Returns &#x60;true&#x60; if no default user, organization, or bucket has been created.

    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str

    """
    return web.Response(status=200)


async def post_setup(request: web.Request, body, zap_trace_span=None) -> web.Response:
    """Set up initial user, org and bucket

    Post an onboarding request to set up initial user, org and bucket.

    :param body: Source to create
    :type body: dict | bytes
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str

    """
    body = OnboardingRequest.from_dict(body)
    return web.Response(status=200)
