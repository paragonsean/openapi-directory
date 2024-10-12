from typing import List, Dict
from aiohttp import web

from openapi_server.models.clearorder_form_messages200_response import ClearorderFormMessages200Response
from openapi_server.models.updateorder_formconfiguration_request import UpdateorderFormconfigurationRequest
from openapi_server.models.waiting_time import WaitingTime
from openapi_server import util


async def clearorder_form_messages(request: web.Request, order_form_id, content_type, accept, body=None) -> web.Response:
    """Clear orderForm messages

    This request removes all messages from the &#x60;messages&#x60; field of the orderForm , leaving it empty.    You must send an empty JSON in the body of the request.    The [orderForm](https://developers.vtex.com/docs/guides/orderform-fields) is the data structure which represents a shopping cart and contains all information pertaining to it. Hence, the &#x60;orderFormId&#x60; is the identification code of a given cart.    **Important**: **Request Body** must always be sent with empty value \&quot;{ }\&quot; in this endpoint.

    :param order_form_id: ID of the orderForm corresponding to the cart whose messages you want to remove.
    :type order_form_id: str
    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param body: 
    :type body: 

    """
    return web.Response(status=200)


async def get_window_to_change_seller(request: web.Request, content_type, accept) -> web.Response:
    """Get window to change seller

    Retrieves a marketplace’s window to change seller, that is, the period when it is possible to choose another seller to fulfill a given order after the original seller has canceled it.    The default period for this window is of 2 days, but it can be configured by the request Update window to change seller.

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str

    """
    return web.Response(status=200)


async def getorder_formconfiguration(request: web.Request, content_type, accept) -> web.Response:
    """Get orderForm configuration

    Retrieves the settings that are currently applied to every orderForm in the account.    These settings are defined by the request [Update orderForm configuration](https://developers.vtex.com/reference/configuration#updateorderformconfiguration).    Always use this request to retrieve the current configuration before performing an update. By doing so you ensure that you are modifying only the properties you want.

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str

    """
    return web.Response(status=200)


async def update_window_to_change_seller(request: web.Request, content_type, accept, body) -> web.Response:
    """Update window to change seller

    Updates a marketplace’s window to change seller, that is, the period when it is possible to choose another seller to fulfill a given order after the original seller has canceled it.    It is possible to check the current window using the request Get window to change seller.

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param body: 
    :type body: dict | bytes

    """
    body = WaitingTime.from_dict(body)
    return web.Response(status=200)


async def updateorder_formconfiguration(request: web.Request, content_type, accept, body) -> web.Response:
    """Update orderForm configuration

    Determines settings that will apply to every orderForm in the account.    For example, if you create an app using this request, every orderForm of this account will have the custom fields created though it.    **Important**: always retrieve the current configuration before performing an update to ensure that you are modifying only the properties you want. Otherwise, old values can be overwritten. To retrieve the current configuration, use the request [Get orderForm configuration](https://developers.vtex.com/reference#getorderformconfiguration).

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateorderFormconfigurationRequest.from_dict(body)
    return web.Response(status=200)
