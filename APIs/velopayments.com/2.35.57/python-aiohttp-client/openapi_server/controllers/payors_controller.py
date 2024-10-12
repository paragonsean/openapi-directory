from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.inline_response400 import InlineResponse400
from openapi_server.models.inline_response403 import InlineResponse403
from openapi_server.models.inline_response404 import InlineResponse404
from openapi_server.models.inline_response409 import InlineResponse409
from openapi_server.models.payor_branding_response import PayorBrandingResponse
from openapi_server.models.payor_create_api_key_request import PayorCreateApiKeyRequest
from openapi_server.models.payor_create_api_key_response import PayorCreateApiKeyResponse
from openapi_server.models.payor_create_application_request import PayorCreateApplicationRequest
from openapi_server.models.payor_email_opt_out_request import PayorEmailOptOutRequest
from openapi_server.models.payor_v1 import PayorV1
from openapi_server.models.payor_v2 import PayorV2
from openapi_server import util


async def get_payor_by_id_v1(request: web.Request, payor_id) -> web.Response:
    """Get Payor

    &lt;p&gt;Get a Single Payor by Id.&lt;/p&gt; &lt;p&gt;deprecated since v2.10 - Use /v2/payors 

    :param payor_id: The Payor Id
    :type payor_id: str
    :type payor_id: str

    """
    return web.Response(status=200)


async def get_payor_by_id_v2(request: web.Request, payor_id) -> web.Response:
    """Get Payor

    Get a Single Payor by Id. 

    :param payor_id: The Payor Id
    :type payor_id: str
    :type payor_id: str

    """
    return web.Response(status=200)


async def payor_add_payor_logo_v1(request: web.Request, payor_id, logo=None) -> web.Response:
    """Add Logo

    &lt;p&gt;Add Payor Logo&lt;/p&gt; &lt;p&gt;Logo file is used in your branding and emails sent to payees&lt;/p&gt; 

    :param payor_id: The Payor Id
    :type payor_id: str
    :type payor_id: str
    :param logo: 
    :type logo: str

    """
    return web.Response(status=200)


async def payor_create_api_key_v1(request: web.Request, payor_id, application_id, body) -> web.Response:
    """Create API Key

    &lt;p&gt;Create an an API key for the given payor Id and application Id&lt;/p&gt; &lt;p&gt;You can create multiple API Keys for a given application&lt;/p&gt; &lt;p&gt;API Keys are programmatic users for integrating your application with the Velo platform&lt;/p&gt; 

    :param payor_id: The Payor Id
    :type payor_id: str
    :type payor_id: str
    :param application_id: Application ID
    :type application_id: str
    :type application_id: str
    :param body: Details of application API key to create
    :type body: dict | bytes

    """
    body = PayorCreateApiKeyRequest.from_dict(body)
    return web.Response(status=200)


async def payor_create_application_v1(request: web.Request, payor_id, body) -> web.Response:
    """Create Application

    &lt;p&gt;Create an application for the given Payor ID.&lt;/p&gt; &lt;p&gt;Applications provide a means to group your API Keys&lt;/p&gt; &lt;p&gt;For example you might have an SAP application that you wish to integrate with Velo&lt;/p&gt; &lt;p&gt;You can create an application and then create one or more API keys for the application&lt;/p&gt; 

    :param payor_id: The Payor Id
    :type payor_id: str
    :type payor_id: str
    :param body: Details of application to create
    :type body: dict | bytes

    """
    body = PayorCreateApplicationRequest.from_dict(body)
    return web.Response(status=200)


async def payor_email_opt_out(request: web.Request, payor_id, body) -> web.Response:
    """Reminder Email Opt-Out

    Update the emailRemindersOptOut field for a Payor. This API can be used to opt out or opt into Payor Reminder emails. These emails are typically around payee events such as payees registering and onboarding. 

    :param payor_id: The Payor Id
    :type payor_id: str
    :type payor_id: str
    :param body: Reminder Emails Opt-Out Request
    :type body: dict | bytes

    """
    body = PayorEmailOptOutRequest.from_dict(body)
    return web.Response(status=200)


async def payor_get_branding(request: web.Request, payor_id) -> web.Response:
    """Get Branding

    Get the payor branding details.

    :param payor_id: The Payor Id
    :type payor_id: str
    :type payor_id: str

    """
    return web.Response(status=200)
