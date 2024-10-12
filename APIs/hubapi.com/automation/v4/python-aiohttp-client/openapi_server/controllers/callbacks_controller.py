from typing import List, Dict
from aiohttp import web

from openapi_server.models.batch_input_callback_completion_batch_request import BatchInputCallbackCompletionBatchRequest
from openapi_server.models.callback_completion_request import CallbackCompletionRequest
from openapi_server.models.error import Error
from openapi_server import util


async def post_automation_v4_actions_callbacks_callback_id_complete_complete(request: web.Request, callback_id, body) -> web.Response:
    """Completes a single callback

    

    :param callback_id: 
    :type callback_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CallbackCompletionRequest.from_dict(body)
    return web.Response(status=200)


async def post_automation_v4_actions_callbacks_complete_complete_batch(request: web.Request, body) -> web.Response:
    """Completes a batch of callbacks

    

    :param body: 
    :type body: dict | bytes

    """
    body = BatchInputCallbackCompletionBatchRequest.from_dict(body)
    return web.Response(status=200)
