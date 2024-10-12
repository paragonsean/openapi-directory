from typing import List, Dict
from aiohttp import web

from openapi_server.models.netlicensing import Netlicensing
from openapi_server import util


async def create_token(request: web.Request, token_type, action=None, api_key_role=None, cancel_url=None, cancel_url_title=None, license_template_number=None, licensee_number=None, predefined_shopping_item=None, private_key=None, product_number=None, success_url=None, success_url_title=None, type=None) -> web.Response:
    """Create token

    Create token by &#39;tokenType&#39; and additional token parameters

    :param token_type: Token type to be generated
    :type token_type: str
    :param action: For &lt;i&gt;type&#x3D;ACTION&lt;/i&gt; only; defines token action to be perfromed
    :type action: str
    :param api_key_role: For &lt;i&gt;tokenType&#x3D;APIKEY&lt;/i&gt; only (default: ROLE_APIKEY_LICENSEE); defines token RoleID
    :type api_key_role: str
    :param cancel_url: For &lt;i&gt;tokenType&#x3D;SHOP&lt;/i&gt; only; take customers to this URL when they cancel their checkout
    :type cancel_url: str
    :param cancel_url_title: For &lt;i&gt;tokenType&#x3D;SHOP&lt;/i&gt; only; shop link title for cancel checkout process
    :type cancel_url_title: str
    :param license_template_number: For &lt;i&gt;tokenType&#x3D;SHOP&lt;/i&gt; only; identifies LicenseTemplate that will be assigned to the shop token
    :type license_template_number: str
    :param licensee_number: For &lt;i&gt;tokenType&#x3D;SHOP&lt;/i&gt; or &lt;i&gt;type&#x3D;ACTION&lt;/i&gt; only (mandatory); identifies Licensee that will be assigned to the shop token
    :type licensee_number: str
    :param predefined_shopping_item: For &lt;i&gt;tokenType&#x3D;SHOP&lt;/i&gt; only; identifies Shopping Item name that will be shown to the customer
    :type predefined_shopping_item: str
    :param private_key: For &lt;i&gt;tokenType&#x3D;APIKEY&lt;/i&gt; only (optional); defines PrivateKey to be used with the validate method&lt;br/&gt;&lt;strong&gt;Please Note:&lt;/strong&gt; PrivateKey need to be provided as one line without spaces
    :type private_key: str
    :param product_number: For &lt;i&gt;tokenType&#x3D;SHOP&lt;/i&gt; only (mandatory); identifies Product that will be assigned to the shop token
    :type product_number: str
    :param success_url: For &lt;i&gt;tokenType&#x3D;SHOP&lt;/i&gt; only; take customers to this URL when they finish checkout
    :type success_url: str
    :param success_url_title: For &lt;i&gt;tokenType&#x3D;SHOP&lt;/i&gt; only; shop link title for successful checkout process
    :type success_url_title: str
    :param type: For &lt;i&gt;tokenType&#x3D;DEFAULT&lt;/i&gt; only; action type to be set
    :type type: str

    """
    return web.Response(status=200)


async def delete_token(request: web.Request, token_number) -> web.Response:
    """Delete token

    Delete a token by &#39;number&#39;

    :param token_number: Token number
    :type token_number: str

    """
    return web.Response(status=200)


async def get_token(request: web.Request, token_number) -> web.Response:
    """Get token

    Return a token by &#39;tokenNumber&#39;

    :param token_number: Token number
    :type token_number: str

    """
    return web.Response(status=200)


async def list_tokens(request: web.Request, ) -> web.Response:
    """List Tokens

    Return a list of all tokens for the current Vendor


    """
    return web.Response(status=200)
