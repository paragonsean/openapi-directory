from typing import List, Dict
from aiohttp import web

from openapi_server.models.add_cart_item_input import AddCartItemInput
from openapi_server.models.remote_shopcart_response import RemoteShopcartResponse
from openapi_server.models.remove_cart_item_input import RemoveCartItemInput
from openapi_server.models.update_cart_item_input import UpdateCartItemInput
from openapi_server import util


async def add_item(request: web.Request, body=None) -> web.Response:
    """add_item

    This is an Experimental method. This method creates an eBay cart for the eBay member, if one does not exist, and adds items to that cart. Because a cart never expires, any item added to the cart will remain in the cart until it is removed. To use this method, you must submit a RESTful item ID and the quantity of the item. If the quantity value is greater than the number of available, the quantity value is changed to the number available and a warning is returned. For example, if there are 15 baseballs available and you set the quantity value to 50, the service automatically changes the value of quantity to 15. The response returns all the items in the eBay member&#39;s cart; items added to the cart while on ebay.com as well as items added to the cart using the Browse API. The quantity and state of an item changes often. If the item becomes &amp;quot;unavailable&amp;quot; such as, when the listing has ended or the item is out of stock, whether it has just been added to the cart or has been in the cart for some time, the item will be returned in the unavailableCartItems container. Note: There are differences between how legacy APIs, such as Finding, and RESTful APIs, such as Browse, return the identifier of an &amp;quot;item&amp;quot; and what the item ID represents. If you have an item ID from one of the legacy APIs, you can use the legacy item ID with the getItemByLegacyId method to retrieve the RESTful ID for that item. For more information about how to use legacy IDs with the Buy APIs, see Legacy API compatibility in the Buying Integration guide. URLs for this method Production URL: https://api.ebay.com/buy/browse/v1/shopping_cart/ Sandbox URL: https://api.sandbox.ebay.com/buy/browse/v1/shopping_cart/ Note: This method is not available in the eBay API Explorer. Restrictions This method can be used only for eBay members. You can add only items with a FIXED_PRICE that accept PayPal as a payment. For a list of supported sites and other restrictions, see API Restrictions.

    :param body: 
    :type body: dict | bytes

    """
    body = AddCartItemInput.from_dict(body)
    return web.Response(status=200)


async def get_shopping_cart(request: web.Request, ) -> web.Response:
    """get_shopping_cart

    This is an experimental method. This method retrieves all the items in the eBay member&#39;s cart; items added to the cart while on ebay.com as well as items added to the cart using the Browse API. There are no URI parameters or request payload. The response returns the summary details of all the items in the eBay member&#39;s cart; items added to the cart while on ebay.com as well as items added to the cart using the Browse API. If the cart is empty, the response is HTTP 204. The quantity and state of an item changes often. If the item becomes &amp;quot;unavailable&amp;quot; such as, when the listing has ended or the item is out of stock, the item will be returned in the unavailableCartItems container. URLs for this method Production URL: https://api.ebay.com/buy/browse/v1/shopping_cart/ Sandbox URL: https://api.sandbox.ebay.com/buy/browse/v1/shopping_cart/ Note: This method is not available in the eBay API Explorer. Restrictions This method can be used only for eBay members. For a list of supported sites and other restrictions, see API Restrictions.


    """
    return web.Response(status=200)


async def remove_item(request: web.Request, body=None) -> web.Response:
    """remove_item

    This is an experimental method. This method removes a specific item from the eBay member&#39;s cart. You specify the ID of the item in the cart (cartItemId) that you want to remove. The response returns all the items in the eBay member&#39;s cart; items added to the cart while on ebay.com as well as items added to the cart using the Browse API. If you remove the last item in the cart, the response is HTTP 204. The quantity and state of an item changes often. If the item becomes &amp;quot;unavailable&amp;quot; such as, when the listing has ended or the item is out of stock, the item will be returned in the unavailableCartItems container. Note: The cartItemId is not the same as the item ID. The cartItemId is the identifier of a specific item in the cart and is generated when the item was added to the cart. URLs for this method Production URL: https://api.ebay.com/buy/browse/v1/shopping_cart/ Sandbox URL: https://api.sandbox.ebay.com/buy/browse/v1/shopping_cart/ Note: This method is not available in the eBay API Explorer. Restrictions This method can be used only for eBay members. For a list of supported sites and other restrictions, see API Restrictions.

    :param body: 
    :type body: dict | bytes

    """
    body = RemoveCartItemInput.from_dict(body)
    return web.Response(status=200)


async def update_quantity(request: web.Request, body=None) -> web.Response:
    """update_quantity

    This is an experimental method. This method updates the quantity value of a specific item in the eBay member&#39;s cart. You specify the ID of the item in the cart (cartItemId) and the new value for the quantity. If the quantity value is greater than the number of available, the quantity value is changed to the number available and a warning is returned. For example, if there are 15 baseballs available and you set the quantity value to 50, the service automatically changes the value of quantity to 15. The response returns all the items in the eBay member&#39;s cart; items added to the cart while on ebay.com as well as items added to the cart using the Browse API. The quantity and state of an item changes often. If the item becomes &amp;quot;unavailable&amp;quot; such as, the listing has ended or the item is out of stock, the item will be returned in the unavailableCartItems container. Note: The cartItemId is not the same as the item ID. The cartItemId is the identifier of a specific item in the cart and is generated when the item was added to the cart. URLs for this method Production URL: https://api.ebay.com/buy/browse/v1/shopping_cart/ Sandbox URL: https://api.sandbox.ebay.com/buy/browse/v1/shopping_cart/ Note: This method is not available in the eBay API Explorer. Restrictions This method can be used only for eBay members. For a list of supported sites and other restrictions, see API Restrictions.

    :param body: 
    :type body: dict | bytes

    """
    body = UpdateCartItemInput.from_dict(body)
    return web.Response(status=200)
