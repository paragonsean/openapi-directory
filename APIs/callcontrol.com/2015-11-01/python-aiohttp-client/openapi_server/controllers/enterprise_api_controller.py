from typing import List, Dict
from aiohttp import web

from openapi_server.models.call_control_user import CallControlUser
from openapi_server import util


async def enterprise_api_get_user(request: web.Request, phone_number) -> web.Response:
    """Enterprise  GET: GetUser  Returns the current information from the user;  try 12066194123 as demo

    

    :param phone_number: 
    :type phone_number: str

    """
    return web.Response(status=200)


async def enterprise_api_should_block(request: web.Request, phone_number, user_phone_number) -> web.Response:
    """Enterprise  GET: ShouldBlock  Simple Enteprise which returns a call block proceed decision.

    This returns information required to perform basic call blocking behaviors              Try with api_key &#39;demo&#39; and phone numbers 18008472911, 13157244022, 17275567300, 18008276655, and 12061231234 (last one not spam)

    :param phone_number: phone number to search
    :type phone_number: str
    :param user_phone_number: (OPTIONAL) phone number of user to look up block rules
    :type user_phone_number: str

    """
    return web.Response(status=200)


async def enterprise_api_upsert_user(request: web.Request, user) -> web.Response:
    """UpsertUser: insert or update all properties from a user  PhoneNumber  WhiteList (list of phone numbers to whitelist)  BlackList (list of phone numbers to blacklist)  QuietHourList (list of quiet hour objects)  UseCommunityBlacklist (enable / disable community blacklist) default true  BreakThroughQhWithMultipleCalls (break through quiet hours with two calls in 3 minutes)  WhiteListBreaksQh (break through quiet hours for whitelist)

    

    :param user: [FromBody] User               &lt;remarks&gt;This returns information required to perform basic call blocking behaviors.  The demo key will return ok, but will not save the data.&lt;br /&gt;&lt;/remarks&gt;
    :type user: dict | bytes

    """
    user = CallControlUser.from_dict(user)
    return web.Response(status=200)
