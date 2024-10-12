from typing import List, Dict
from aiohttp import web

from openapi_server.models.add_client_preferences_request import AddClientPreferencesRequest
from openapi_server.models.add_client_profile_request import AddClientProfileRequest
from openapi_server.models.add_marketing_data_request import AddMarketingDataRequest
from openapi_server.models.add_merchant_context_data200_response import AddMerchantContextData200Response
from openapi_server.models.add_merchant_context_data_request import AddMerchantContextDataRequest
from openapi_server.models.add_payment_data_request import AddPaymentDataRequest
from openapi_server.models.add_shipping_address_request import AddShippingAddressRequest
from openapi_server.models.get_client_profile_by_email200_response import GetClientProfileByEmail200Response
from openapi_server import util


async def add_client_preferences(request: web.Request, content_type, accept, order_form_id, body) -> web.Response:
    """Add client preferences

    Use this request to include client preferences information to a given shopping cart.    The [orderForm](https://developers.vtex.com/docs/guides/orderform-fields) is the data structure which represents a shopping cart and contains all information pertaining to it. Hence, the &#x60;orderFormId&#x60; is the identification code of a given cart.    &gt; This request has a time out of 12 seconds.

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param order_form_id: ID of the orderForm that will receive client profile information.
    :type order_form_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = AddClientPreferencesRequest.from_dict(body)
    return web.Response(status=200)


async def add_client_profile(request: web.Request, content_type, accept, order_form_id, body) -> web.Response:
    """Add client profile

    Use this request to include client profile information to a given shopping cart.    The [orderForm](https://developers.vtex.com/docs/guides/orderform-fields) is the data structure which represents a shopping cart and contains all information pertaining to it. Hence, the &#x60;orderFormId&#x60; is the identification code of a given cart.    &gt; This request has a time out of 12 seconds.    &gt;⚠️ The authentication of this endpoint can change depending on the customer context. If you are modifying information from a customer with a complete profile on the store, the response will return the customer&#39;s data masked. You can only access the customer data with an authenticated request.

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param order_form_id: ID of the orderForm that will receive client profile information.
    :type order_form_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = AddClientProfileRequest.from_dict(body)
    return web.Response(status=200)


async def add_marketing_data(request: web.Request, content_type, accept, order_form_id, body) -> web.Response:
    """Add marketing data

    Use this request to include marketing information to a given shopping cart.    The [orderForm](https://developers.vtex.com/docs/guides/orderform-fields) is the data structure which represents a shopping cart and contains all information pertaining to it. Hence, the &#x60;orderFormId&#x60; is the identification code of a given cart.    &gt; This request has a time out of 12 seconds.

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param order_form_id: ID of the orderForm that will receive client profile information.
    :type order_form_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = AddMarketingDataRequest.from_dict(body)
    return web.Response(status=200)


async def add_merchant_context_data(request: web.Request, content_type, accept, order_form_id, body) -> web.Response:
    """Add merchant context data

    This endpoint is used for the merchant to add to the cart any relevant information that is related to the context of a specific order.    The [orderForm](https://developers.vtex.com/docs/guides/orderform-fields) is the data structure which represents a shopping cart and contains all information pertaining to it. Hence, the &#x60;orderFormId&#x60; is the identification code of a given cart.    &gt; This request has a time out of 12 seconds.

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param order_form_id: ID of the orderForm that will receive the relevant information added by the merchant.
    :type order_form_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = AddMerchantContextDataRequest.from_dict(body)
    return web.Response(status=200)


async def add_payment_data(request: web.Request, content_type, accept, order_form_id, body) -> web.Response:
    """Add payment data

    Use this request to include payment information to a given shopping cart. The payment information attachment in the shopping cart does not determine the final order payment method in itself. However, it allows tha platform to update any relevant information that may be impacted by the payment method.    The [orderForm](https://developers.vtex.com/docs/guides/orderform-fields) is the data structure which represents a shopping cart and contains all information pertaining to it. Hence, the &#x60;orderFormId&#x60; is the identification code of a given cart.    &gt; This request has a time out of 12 seconds.

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param order_form_id: ID of the orderForm that will receive client profile information.
    :type order_form_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = AddPaymentDataRequest.from_dict(body)
    return web.Response(status=200)


async def add_shipping_address(request: web.Request, content_type, accept, order_form_id, body) -> web.Response:
    """Add shipping address and select delivery option

    Use this request to include shipping information and/or selected delivery option to a given shopping cart.    To add shipping addresses send the &#x60;selectedAddresses&#x60; array. For delivery option use the &#x60;logisticsInfo&#x60; array.    The [orderForm](https://developers.vtex.com/docs/guides/orderform-fields) is the data structure which represents a shopping cart and contains all information pertaining to it. Hence, the &#x60;orderFormId&#x60; is the identification code of a given cart.    &gt; This request has a time out of 12 seconds.    &gt;⚠️ The authentication of this endpoint can change depending on the customer context. If you are modifying information from a customer with a complete profile on the store, the response will return the customer&#39;s data masked. You can only access the customer data with an authenticated request.

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param order_form_id: ID of the orderForm that will receive client profile information.
    :type order_form_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = AddShippingAddressRequest.from_dict(body)
    return web.Response(status=200)


async def get_client_profile_by_email(request: web.Request, content_type, accept, email) -> web.Response:
    """Get client profile by email

    Retrieve a client&#39;s profile information by providing an email address.    If the response body fields are empty, the following situations may have occurred:    1. There is no client registered with the email address provided in your store, or;  2. Client profile is invalid or incomplete. For more information, see [SmartCheckout - Customer information automatic fill-in](https://help.vtex.com/en/tutorial/smartcheckout-customer-information-automatic-fill-in--2Nuu3xAFzdhIzJIldAdtan).    &gt;⚠️ The authentication of this endpoint can change depending on the customer context. If you are consulting information from a customer with a complete profile on the store, the response will return the customer&#39;s data masked. You can only access the customer data with an authenticated request.

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param email: Client&#39;s email address to be searched.
    :type email: str

    """
    return web.Response(status=200)
