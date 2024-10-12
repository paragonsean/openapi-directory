from typing import List, Dict
from aiohttp import web

from openapi_server.models.add_media_intent_handling_invocation import AddMediaIntentHandlingInvocation
from openapi_server.models.add_media_intent_handling_invocation_response import AddMediaIntentHandlingInvocationResponse
from openapi_server.models.play_media_intent_handling_invocation import PlayMediaIntentHandlingInvocation
from openapi_server.models.play_media_intent_handling_invocation_response import PlayMediaIntentHandlingInvocationResponse
from openapi_server.models.update_media_affinity_intent_handling_invocation import UpdateMediaAffinityIntentHandlingInvocation
from openapi_server.models.update_media_affinity_intent_handling_invocation_response import UpdateMediaAffinityIntentHandlingInvocationResponse
from openapi_server import util


async def add_media_intent_handling(request: web.Request, x_applecloudextension_session_id, request_timeout, user_agent, accept_language, x_applecloudextension_retry_count=None, body=None) -> web.Response:
    """addMedia

    

    :param x_applecloudextension_session_id: 
    :type x_applecloudextension_session_id: str
    :param request_timeout: 
    :type request_timeout: 
    :param user_agent: 
    :type user_agent: str
    :param accept_language: 
    :type accept_language: str
    :param x_applecloudextension_retry_count: 
    :type x_applecloudextension_retry_count: 
    :param body: 
    :type body: list | bytes

    """
    body = [AddMediaIntentHandlingInvocation.from_dict(d) for d in body]
    return web.Response(status=200)


async def play_media_intent_handling(request: web.Request, x_applecloudextension_session_id, request_timeout, user_agent, accept_language, x_applecloudextension_retry_count=None, body=None) -> web.Response:
    """playMedia

    

    :param x_applecloudextension_session_id: 
    :type x_applecloudextension_session_id: str
    :param request_timeout: 
    :type request_timeout: 
    :param user_agent: 
    :type user_agent: str
    :param accept_language: 
    :type accept_language: str
    :param x_applecloudextension_retry_count: 
    :type x_applecloudextension_retry_count: 
    :param body: 
    :type body: list | bytes

    """
    body = [PlayMediaIntentHandlingInvocation.from_dict(d) for d in body]
    return web.Response(status=200)


async def update_media_affinity_intent_handling(request: web.Request, x_applecloudextension_session_id, request_timeout, user_agent, accept_language, x_applecloudextension_retry_count=None, body=None) -> web.Response:
    """updateMediaAffinity

    

    :param x_applecloudextension_session_id: 
    :type x_applecloudextension_session_id: str
    :param request_timeout: 
    :type request_timeout: 
    :param user_agent: 
    :type user_agent: str
    :param accept_language: 
    :type accept_language: str
    :param x_applecloudextension_retry_count: 
    :type x_applecloudextension_retry_count: 
    :param body: 
    :type body: list | bytes

    """
    body = [UpdateMediaAffinityIntentHandlingInvocation.from_dict(d) for d in body]
    return web.Response(status=200)
