from typing import List, Dict
from aiohttp import web

from openapi_server.models.add_coupons200_response import AddCoupons200Response
from openapi_server.models.add_coupons_request import AddCouponsRequest
from openapi_server.models.cart_simulation200_response import CartSimulation200Response
from openapi_server.models.cart_simulation_request import CartSimulationRequest
from openapi_server.models.ignore_profile_data_request import IgnoreProfileDataRequest
from openapi_server.models.items200_response import Items200Response
from openapi_server.models.items_request import ItemsRequest
from openapi_server.models.items_update200_response import ItemsUpdate200Response
from openapi_server.models.items_update_request import ItemsUpdateRequest
from openapi_server.models.price_change_request import PriceChangeRequest
from openapi_server import util


async def add_coupons(request: web.Request, order_form_id, content_type, accept, body) -> web.Response:
    """Add coupons to the cart

    Use this request to add coupons to a given shopping cart.

    :param order_form_id: ID of the orderForm that will receive coupon information.
    :type order_form_id: str
    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param body: 
    :type body: dict | bytes

    """
    body = AddCouponsRequest.from_dict(body)
    return web.Response(status=200)


async def cart_simulation(request: web.Request, content_type, accept, rnb_behavior=None, sc=None, body=None) -> web.Response:
    """Cart simulation

    This endpoint is used to simulate a cart in VTEX Checkout.    It receives an **SKU ID**, the **quantity** of items in the cart and the ID of the **Seller**.    It sends back all information about the cart, such as the selling price of each item, rates and benefits data, payment and logistics info.    This is useful whenever you need to know the availability of fulfilling an order for a specific cart setting, since the API response will let you know the updated price, inventory and shipping data.    **Important**: The fields (&#x60;sku id&#x60;, &#x60;quantity&#x60;, &#x60;seller&#x60;, &#x60;country&#x60;, &#x60;postalCode&#x60; and &#x60;geoCoordinates&#x60;) are just examples of content that you can simulate in your cart. You can add more fields to the request as per your need. Access the [orderForm](https://developers.vtex.com/docs/guides/orderform-fields) guide to check the available fields.

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param rnb_behavior: This parameter defines which promotions apply to the simulation. Use &#x60;0&#x60; for simulations at cart stage, which means all promotions apply. In case of window simulation use &#x60;1&#x60;, which indicates promotions that apply nominal discounts over the total purchase value shouldn&#39;t be considered on the simulation.    Note that if this not sent, the parameter is &#x60;1&#x60;.
    :type rnb_behavior: int
    :param sc: Trade Policy (Sales Channel) identification.
    :type sc: int
    :param body: 
    :type body: dict | bytes

    """
    body = CartSimulationRequest.from_dict(body)
    return web.Response(status=200)


async def create_a_new_cart(request: web.Request, content_type, accept, force_new_cart=None) -> web.Response:
    """Get current or create a new cart

    You can use this request to get your current shopping cart information (&#x60;orderFormId&#x60;) or to create a new cart.    **Important**: To create a new empty shopping cart you need to send this request with the query param &#x60;forceNewCart&#x3D;true&#x60;.    The [orderForm](https://developers.vtex.com/docs/guides/orderform-fields) is the data structure which represents a shopping cart and contains all information pertaining to it. Hence, the &#x60;orderFormId&#x60; obtained in response is the identification code of the newly created cart.    &gt; This request has a time out of 45 seconds.

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param force_new_cart: Use this query parameter to create a new empty shopping cart.
    :type force_new_cart: bool

    """
    return web.Response(status=200)


async def get_cart_information_by_id(request: web.Request, order_form_id, content_type, accept, refresh_outdated_data=None) -> web.Response:
    """Get cart information by ID

    Use this request to get all information associated to a given shopping  cart.    The [orderForm](https://developers.vtex.com/docs/guides/orderform-fields) is the data structure which represents a shopping cart and contains all information pertaining to it. Hence, the &#x60;orderFormId&#x60; is the identification code of a given cart.    &gt; This request has a time out of 45 seconds.

    :param order_form_id: ID of the orderForm corresponding to the cart whose information you want to retrieve.
    :type order_form_id: str
    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param refresh_outdated_data: It is possible to use the [Update cart items request](https://developers.vtex.com/vtex-rest-api/reference/cart-update#itemsupdate) so as to allow outdated information in the &#x60;orderForm&#x60;, which may improve performance in some cases. To guarantee that all cart information is updated, send this request with this parameter as &#x60;true&#x60;. We recommend doing this in the final stages of the shopping experience, starting from the checkout page.
    :type refresh_outdated_data: bool

    """
    return web.Response(status=200)


async def get_cart_installments(request: web.Request, order_form_id, payment_system, content_type, accept) -> web.Response:
    """Cart installments

    Retrieves possible amount of installments and respective values for a given cart with a given payment method.    The [orderForm](https://developers.vtex.com/docs/guides/orderform-fields) is the data structure which represents a shopping cart and contains all information pertaining to it. Hence, the &#x60;orderFormId&#x60; is the identification code of a given cart.    This endpoint can be used to get the installment options for only one payment method at a time.    This endpoint should be called only after the selected &#x60;orderForm&#x60; already has a &#x60;paymentData&#x60;.

    :param order_form_id: ID of the &#x60;orderForm&#x60; to be consulted for installments.
    :type order_form_id: str
    :param payment_system: ID of the payment method to be consulted for installments.
    :type payment_system: int
    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str

    """
    return web.Response(status=200)


async def ignore_profile_data(request: web.Request, order_form_id, content_type, accept, body) -> web.Response:
    """Ignore profile data

    When a shopper provides an email address at Checkout, the platform tries to retrieve existing profile information for that email and add it to the shopping cart information. Use this request if you want to change this behavior for a given cart, meaning profile information will not be included in the order automattically.    The [orderForm](https://developers.vtex.com/docs/guides/orderform-fields) is the data structure which represents a shopping cart and contains all information pertaining to it. Hence, the &#x60;orderFormId&#x60; is the identification code of a given cart.    Note that this request will only work if you have not sent the &#x60;clientProfileData&#x60; to the cart yet. Sending it to a cart that already has a &#x60;clientProfileData&#x60; should return a status &#x60;403 Forbidden&#x60; error, with an &#x60;Access denied&#x60; message.

    :param order_form_id: ID of the orderForm corresponding to the cart whose items will have the price changed.
    :type order_form_id: str
    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param body: 
    :type body: dict | bytes

    """
    body = IgnoreProfileDataRequest.from_dict(body)
    return web.Response(status=200)


async def items(request: web.Request, content_type, accept, order_form_id, body, allowed_outdated_data=None) -> web.Response:
    """Add cart items

    Use this request to add a new item to the shopping cart.    The [orderForm](https://developers.vtex.com/docs/guides/orderform-fields) is the data structure which represents a shopping cart and contains all information pertaining to it. Hence, the &#x60;orderFormId&#x60; is the identification code of a given cart.    &gt; This request has a time out of 45 seconds.

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param order_form_id: ID of the orderForm corresponding to the cart in which the new item will be added.
    :type order_form_id: str
    :param body: 
    :type body: dict | bytes
    :param allowed_outdated_data: In order to optimize performance, this parameter allows some information to not be updated when there are changes in the minicart. For instance, if a shopper adds another unit of a given SKU to the cart, it may not be necessary to recalculate payment information, which could impact performance.    This array accepts strings and currently the only possible value is &#x60;”paymentData”&#x60;.
    :type allowed_outdated_data: List[]

    """
    body = ItemsRequest.from_dict(body)
    return web.Response(status=200)


async def items_update(request: web.Request, content_type, accept, order_form_id, body, allowed_outdated_data=None) -> web.Response:
    """Update cart items

    You can use this request to:    1. Change the quantity of one or more items in a specific cart.  2. Remove an item from the cart (by sending the &#x60;quantity&#x60; value &#x3D; &#x60;0&#x60; in the request body).    **Important**: To remove all items from the cart at the same time, use the [Remove all items](https://developers.vtex.com/vtex-rest-api/reference/removeallitems) endpoint.    The [orderForm](https://developers.vtex.com/docs/guides/orderform-fields) is the data structure that represents a shopping cart and contains all information pertaining to it. Hence, the &#x60;orderFormId&#x60; is the identification code of a given cart.    &gt; This request has a time out of 45 seconds.

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param order_form_id: ID of the &#x60;orderForm&#x60; corresponding to the cart whose items you want to update.
    :type order_form_id: str
    :param body: 
    :type body: dict | bytes
    :param allowed_outdated_data: In order to optimize performance, this parameter allows some information to not be updated when there are changes in the minicart. For instance, if a shopper adds another unit of a given SKU to the cart, it may not be necessary to recalculate payment information, which could impact performance.    This array accepts strings and currently the only possible value is &#x60;”paymentData”&#x60;.
    :type allowed_outdated_data: List[]

    """
    body = ItemsUpdateRequest.from_dict(body)
    return web.Response(status=200)


async def price_change(request: web.Request, order_form_id, item_index, content_type, accept, body) -> web.Response:
    """Change price

    This request changes the price of an SKU in a cart. You can also perform type of bulk price change with the [Update cart items request](https://developers.vtex.com/vtex-rest-api/reference/shopping-cart#itemsupdate)    The [orderForm](https://developers.vtex.com/docs/guides/orderform-fields) is the data structure which represents a shopping cart and contains all information pertaining to it. Hence, the &#x60;orderFormId&#x60; is the identification code of a given cart.    You need to inform which cart you are referring to, by sending its &#x60;orderFormId&#x60;; and what is the item whose price you want to change, by sending its &#x60;itemIndex&#x60;.    You also need to pass the new price value in the body.    Remember that, to use this endpoint, the feature of *manual price* must be active. To check if it&#39;s active, use the [Get orderForm configuration](https://developers.vtex.com/reference#getorderformconfiguration) endpoint. To make it active, use the [Update orderForm configuration](https://developers.vtex.com/reference#updateorderformconfiguration) endpoint, making the &#x60;allowManualPrice&#x60; field &#x60;true&#x60;.    &gt; Whenever you use this request to change the price of an item, all items in that cart with the same SKU are affected by this change. This applies even to items that share the SKU but have been separated into different objects in the &#x60;items&#x60; array due to customizations or attachments, for example.

    :param order_form_id: ID of the orderForm corresponding to the cart whose items will have the price changed.
    :type order_form_id: str
    :param item_index: The index of the item in the cart. Each cart item is identified by an index, starting in 0.
    :type item_index: str
    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param body: 
    :type body: dict | bytes

    """
    body = PriceChangeRequest.from_dict(body)
    return web.Response(status=200)


async def remove_all_items(request: web.Request, order_form_id, content_type, accept, body=None) -> web.Response:
    """Remove all items

    This request removes all items from a given cart, leaving it empty.    You must send an empty JSON in the body of the request.    The [orderForm](https://developers.vtex.com/docs/guides/orderform-fields) is the data structure which represents a shopping cart and contains all information pertaining to it. Hence, the &#x60;orderFormId&#x60; is the identification code of a given cart.    **Important**: **Request Body** must always be sent with empty value \&quot;{ }\&quot; in this endpoint.

    :param order_form_id: ID of the orderForm corresponding to the cart whose items you want to remove.
    :type order_form_id: str
    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param body: 
    :type body: 

    """
    return web.Response(status=200)


async def removeallpersonaldata(request: web.Request, content_type, accept, order_form_id) -> web.Response:
    """Remove all personal data

    This call removes all user information, making a cart anonymous while leaving the items.    The [orderForm](https://developers.vtex.com/docs/guides/orderform-fields) is the data structure that represents a shopping cart and contains all information about it. Hence, the &#x60;orderFormId&#x60; is the identification code of a given cart.    This call works by creating a new orderForm, setting a new cookie, and returning a redirect 302 to the cart URL (&#x60;/checkout/#/orderform&#x60;).

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param order_form_id: ID of the orderForm corresponding to the cart whose user&#39;s personal data you want to remove.
    :type order_form_id: str

    """
    return web.Response(status=200)
