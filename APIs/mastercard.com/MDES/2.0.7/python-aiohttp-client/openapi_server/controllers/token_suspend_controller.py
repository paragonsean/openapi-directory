from typing import List, Dict
from aiohttp import web

from openapi_server.models.errors_response import ErrorsResponse
from openapi_server.models.token_suspend_request_schema import TokenSuspendRequestSchema
from openapi_server.models.token_suspend_response_schema import TokenSuspendResponseSchema
from openapi_server import util


async def token_suspend_post(request: web.Request, token_suspend_request_schema=None) -> web.Response:
    """token_suspend_post

    Used to suspend an active token so that it may not initiate any new transactions. All authorizations for a SUSPENDED token will be declined. Tokens may be suspended by multiple parties (suspenders) concurrently. The token status is updated from ACTIVE to SUSPENDED when the first suspender triggers a suspend action. Additional suspenders can add their suspend action to the list of suspenders. Suspenders can unsuspend only their own suspend action. All suspenders need to perform an unsuspend action to move a token from SUSPENDED to ACTIVE. The token status will only change when the last suspender has unsuspended the token. &lt;br&gt;For CoF tokens, the only two supported suspenders are issuer and token requestor. &lt;br&gt;For Apple Pay tokens, there are some differences in behavior versus the general principles. An issuer may add themselves as a suspender to a token already suspended by a cardholder, as above. However, a cardholder cannot suspend a token already suspended by the issuer. As a special case for Apple Pay, an issuer may unsuspend (override) a token already suspended by a cardholder. However, a cardholder cannot unsuspend a token already suspended by the issuer. 

    :param token_suspend_request_schema: Contains the details of the request message.
    :type token_suspend_request_schema: dict | bytes

    """
    token_suspend_request_schema = TokenSuspendRequestSchema.from_dict(token_suspend_request_schema)
    return web.Response(status=200)
