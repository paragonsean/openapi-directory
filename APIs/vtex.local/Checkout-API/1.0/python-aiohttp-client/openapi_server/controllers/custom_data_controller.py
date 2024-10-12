from typing import List, Dict
from aiohttp import web

from openapi_server.models.setsinglecustomfieldvalue_request import SetsinglecustomfieldvalueRequest
from openapi_server import util


async def removesinglecustomfieldvalue(request: web.Request, content_type, accept, order_form_id, app_id, app_field_name) -> web.Response:
    """Remove single custom field value

    Your account may create &#x60;apps&#x60;, which contain custom fields, through the [Update orderForm configuration](https://developers.vtex.com/reference#updateorderformconfiguration) request. The value of a specific custom field can be removed by this request.    To do that, you need to inform in the URL the ID of the app you created with the configuration API (&#x60;appId&#x60;).    You also need to iform the specific field created in this app (identified by the &#x60;appFieldName&#x60; parameter, also passed through the URL) whose value you want to remove.

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param order_form_id: The ID of the orderForm from which you want to remove the custom field value.
    :type order_form_id: str
    :param app_id: ID of the app created through the Update orderForm Configuration endpoint.
    :type app_id: str
    :param app_field_name: Name of the app&#39;s field created through the Update orderForm Configuration endpoint and which will be deleted.
    :type app_field_name: str

    """
    return web.Response(status=200)


async def set_multiple_custom_field_values(request: web.Request, order_form_id, content_type, accept, app_id, body) -> web.Response:
    """Set multiple custom field values

    Your account may create &#x60;apps&#x60;, which contain custom fields, through the [Update orderForm configuration](https://developers.vtex.com/reference/configuration#updateorderformconfiguration) request. The values of these custom fields can then be updated by this request.    To do that, you need to inform the ID of the app you created with the configuration API (&#x60;appId&#x60;).    In the body of the request, for each field created in this app (&#x60;appFieldName&#x60;) you will inform a value (&#x60;appFieldValue&#x60;).    The [orderForm](https://developers.vtex.com/docs/guides/orderform-fields) is the data structure which represents a shopping cart and contains all information pertaining to it. Hence, the &#x60;orderFormId&#x60; is the identification code of a given cart.

    :param order_form_id: ID of the orderForm that will receive the new custom field values.
    :type order_form_id: str
    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param app_id: ID of the app created with the configuration API.
    :type app_id: str
    :param body: 
    :type body: Dict[str, ]

    """
    return web.Response(status=200)


async def set_single_custom_field_value(request: web.Request, order_form_id, app_id, app_field_name, content_type, accept, body) -> web.Response:
    """Set single custom field value

    Your account may create &#x60;apps&#x60;, which contain custom fields, through the [Update orderForm configuration](https://developers.vtex.com/reference#updateorderformconfiguration) request. The value of a specific custom field can then be updated by this request.    To do that, you need to inform in the URL the ID of the app you created with the configuration API (&#x60;appId&#x60;).    In the body of the request, you will inform the new value (&#x60;appFieldValue&#x60;, passed through the body) of the specific field created in this app (identified by the &#x60;appFieldName&#x60; parameter, passed through the URL).    The [orderForm](https://developers.vtex.com/docs/guides/orderform-fields) is the data structure which represents a shopping cart and contains all information pertaining to it. Hence, the &#x60;orderFormId&#x60; is the identification code of a given cart.

    :param order_form_id: The ID of the orderForm whose custom field&#39;s value you want to change.
    :type order_form_id: str
    :param app_id: ID of the app created through the Update orderForm Configuration endpoint.
    :type app_id: str
    :param app_field_name: Name of the app&#39;s field created through the Update orderForm Configuration endpoint.
    :type app_field_name: str
    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param body: 
    :type body: dict | bytes

    """
    body = SetsinglecustomfieldvalueRequest.from_dict(body)
    return web.Response(status=200)
