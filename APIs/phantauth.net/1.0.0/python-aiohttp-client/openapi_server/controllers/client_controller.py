from typing import List, Dict
from aiohttp import web

from openapi_server.models.client_client_id_get200_response import ClientClientIdGet200Response
from openapi_server.models.client_post_request import ClientPostRequest
from openapi_server import util


async def client_client_id_get(request: web.Request, client_id) -> web.Response:
    """Get a Client

    Use this endpoint to generate a random client. The client is generated in a deterministic way, on the bases of the client ID given as a path parameter. In the case of identical client IDs, the endpoint will generate the same client object. The properties of the generated client object are randomly generated on the basis of the client ID. In lack of a client ID, all calls generate a different client object to the randomly generated client ID.  By providing an email address as the &#x60;client_id&#x60; parameter, you can customize the client logo by the use of the gravatar associated with the email address.  If the &#x60;client_id&#x60; parameter contains minimum one dot (&#x60;.&#x60;) or space (&#x60; &#x60;) character, the client_name is produced from the parameter, rather than being generated.&#x60;  The result is always a client object. If you want to generate multiple clients in one single step, you can do it by the use of *Fleet* generation. The members of a fleet are clients randomly generated from the fleet name.

    :param client_id: A client ID or email.
    :type client_id: str

    """
    return web.Response(status=200)


async def client_client_id_token_kind_get(request: web.Request, client_id, kind) -> web.Response:
    """Get a Client Token

    It is used to generate a OpenID Connect token as a path parameter to a client of a given client ID.  It is primarily used for testing purposes, when, for example, the token from the standard authentication flow is not available to the test code.

    :param client_id: A client ID or email.
    :type client_id: str
    :param kind: Token type
    :type kind: str

    """
    return web.Response(status=200)


async def client_post(request: web.Request, body=None) -> web.Response:
    """Create a Client Selfie

    To create a selfie token from the client data, you need an opaqe string token, which contains the encoded client properties sent in the request. Later, the selfie token can be used as a client ID. In this case, the client data is included in the selfie token, that is, the client properties are taken from the token. By the use of a selfie token, you can use your own client objects in the authentication process.

    :param body: 
    :type body: dict | bytes

    """
    body = ClientPostRequest.from_dict(body)
    return web.Response(status=200)
