from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def session_controller_change_password(request: web.Request, short_name, token, old_password, new_password) -> web.Response:
    """Change the password of a customer given their existing and new password.

    

    :param short_name: The unique client short-name
    :type short_name: str
    :param token: The login token returned from the /session POST call
    :type token: str
    :param old_password: The customer&#39;s existing password.
    :type old_password: str
    :param new_password: The customer&#39;s new password.
    :type new_password: str

    """
    return web.Response(status=200)


async def session_controller_create_landlord_login(request: web.Request, short_name, email, title, forename, surname, property_address, contact_details, branch_id=None) -> web.Response:
    """Send a request to the in-tray to create a landlord login.

    

    :param short_name: The unique client short-name
    :type short_name: str
    :param email: The email address of the landlord
    :type email: str
    :param title: The title of the landlord
    :type title: str
    :param forename: The forename of the landlord
    :type forename: str
    :param surname: The surname of the landlord
    :type surname: str
    :param property_address: Address of the property linked to the landlord
    :type property_address: str
    :param contact_details: Contact details of the landlord
    :type contact_details: str
    :param branch_id: (Optional) The branch ID linked to the login. This will determine which in tray the request display in
    :type branch_id: str

    """
    return web.Response(status=200)


async def session_controller_get_session_info(request: web.Request, short_name, token) -> web.Response:
    """Gets information about the currently logged on customer.

    

    :param short_name: The unique client short-name
    :type short_name: str
    :param token: The login token returned from the /session POST call
    :type token: str

    """
    return web.Response(status=200)


async def session_controller_login(request: web.Request, short_name, username, password) -> web.Response:
    """Login as a customer given their username and password.

    

    :param short_name: The unique client short-name
    :type short_name: str
    :param username: The user&#39;s username.
    :type username: str
    :param password: The user&#39;s password.
    :type password: str

    """
    return web.Response(status=200)


async def session_controller_logout(request: web.Request, short_name, token) -> web.Response:
    """Logout a customer previously logged in via the Login endpoint.

    

    :param short_name: The unique client short-name
    :type short_name: str
    :param token: The login token returned from the /session POST call
    :type token: str

    """
    return web.Response(status=200)


async def session_controller_reset_password(request: web.Request, short_name, email) -> web.Response:
    """Reset the customer&#39;s password. An email will be sent out to reset.

    

    :param short_name: The unique client short-name
    :type short_name: str
    :param email: The login Email Address.
    :type email: str

    """
    return web.Response(status=200)
