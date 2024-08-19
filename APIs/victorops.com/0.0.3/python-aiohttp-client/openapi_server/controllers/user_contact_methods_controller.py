from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_public_v1_user_user_contact_methods_get200_response import ApiPublicV1UserUserContactMethodsGet200Response
from openapi_server.models.contact_device import ContactDevice
from openapi_server.models.contact_device_add import ContactDeviceAdd
from openapi_server.models.contact_email_add import ContactEmailAdd
from openapi_server.models.contact_phone_add import ContactPhoneAdd
from openapi_server.models.user_contact import UserContact
from openapi_server import util


async def api_public_v1_user_user_contact_methods_devices_contact_id_delete(request: web.Request, x_vo_api_id, x_vo_api_key, user, contact_id) -> web.Response:
    """Delete a contact device for a user

    Delete a contact device for a user  This API may be called a maximum of 60 times per minute. 

    :param x_vo_api_id: Your API ID
    :type x_vo_api_id: str
    :param x_vo_api_key: Your API Key
    :type x_vo_api_key: str
    :param user: The VictorOps user ID
    :type user: str
    :param contact_id: The unique contact identifier
    :type contact_id: str

    """
    return web.Response(status=200)


async def api_public_v1_user_user_contact_methods_devices_contact_id_get(request: web.Request, x_vo_api_id, x_vo_api_key, user, contact_id) -> web.Response:
    """Get the indicated contact device for a user

    Get the indicated contact device for a user  This API may be called a maximum of 60 times per minute. 

    :param x_vo_api_id: Your API ID
    :type x_vo_api_id: str
    :param x_vo_api_key: Your API Key
    :type x_vo_api_key: str
    :param user: The VictorOps user ID
    :type user: str
    :param contact_id: The unique contact identifier
    :type contact_id: str

    """
    return web.Response(status=200)


async def api_public_v1_user_user_contact_methods_devices_contact_id_put(request: web.Request, x_vo_api_id, x_vo_api_key, user, contact_id, body) -> web.Response:
    """Update a contact device for a user

    Update a contact device for a user  This API may be called a maximum of 60 times per minute. 

    :param x_vo_api_id: Your API ID
    :type x_vo_api_id: str
    :param x_vo_api_key: Your API Key
    :type x_vo_api_key: str
    :param user: The VictorOps user ID
    :type user: str
    :param contact_id: The unique contact identifier
    :type contact_id: str
    :param body: The contact device
    :type body: dict | bytes

    """
    body = ContactDeviceAdd.from_dict(body)
    return web.Response(status=200)


async def api_public_v1_user_user_contact_methods_devices_get(request: web.Request, x_vo_api_id, x_vo_api_key, user) -> web.Response:
    """Get a list of all contact devices for a user

    Get the contact methods for a user  This API may be called a maximum of 60 times per minute. 

    :param x_vo_api_id: Your API ID
    :type x_vo_api_id: str
    :param x_vo_api_key: Your API Key
    :type x_vo_api_key: str
    :param user: The VictorOps user ID
    :type user: str

    """
    return web.Response(status=200)


async def api_public_v1_user_user_contact_methods_emails_contact_id_delete(request: web.Request, x_vo_api_id, x_vo_api_key, user, contact_id) -> web.Response:
    """Delete a contact email for a user

    Delete the indicated contact email for the user  This API may be called a maximum of 60 times per minute. 

    :param x_vo_api_id: Your API ID
    :type x_vo_api_id: str
    :param x_vo_api_key: Your API Key
    :type x_vo_api_key: str
    :param user: The VictorOps user ID
    :type user: str
    :param contact_id: The unique contact identifier
    :type contact_id: str

    """
    return web.Response(status=200)


async def api_public_v1_user_user_contact_methods_emails_contact_id_get(request: web.Request, x_vo_api_id, x_vo_api_key, user, contact_id) -> web.Response:
    """Get the indicated contact email for a user

    Get the indicated contact email for a user  This API may be called a maximum of 60 times per minute. 

    :param x_vo_api_id: Your API ID
    :type x_vo_api_id: str
    :param x_vo_api_key: Your API Key
    :type x_vo_api_key: str
    :param user: The VictorOps user ID
    :type user: str
    :param contact_id: The unique contact identifier
    :type contact_id: str

    """
    return web.Response(status=200)


async def api_public_v1_user_user_contact_methods_emails_get(request: web.Request, x_vo_api_id, x_vo_api_key, user) -> web.Response:
    """Get a list of all contact emails for a user

    Get the contact emails for a user  This API may be called a maximum of 60 times per minute. 

    :param x_vo_api_id: Your API ID
    :type x_vo_api_id: str
    :param x_vo_api_key: Your API Key
    :type x_vo_api_key: str
    :param user: The VictorOps user ID
    :type user: str

    """
    return web.Response(status=200)


async def api_public_v1_user_user_contact_methods_emails_post(request: web.Request, x_vo_api_id, x_vo_api_key, user, body) -> web.Response:
    """Create a contact emails for a user

    Create a contact email for a user  This API may be called a maximum of 60 times per minute. 

    :param x_vo_api_id: Your API ID
    :type x_vo_api_id: str
    :param x_vo_api_key: Your API Key
    :type x_vo_api_key: str
    :param user: The VictorOps user ID
    :type user: str
    :param body: The contact email
    :type body: dict | bytes

    """
    body = ContactEmailAdd.from_dict(body)
    return web.Response(status=200)


async def api_public_v1_user_user_contact_methods_get(request: web.Request, x_vo_api_id, x_vo_api_key, user) -> web.Response:
    """Get a list of all contact methods for a user

    Get the contact methods for a user  This API may be called a maximum of 60 times per minute. 

    :param x_vo_api_id: Your API ID
    :type x_vo_api_id: str
    :param x_vo_api_key: Your API Key
    :type x_vo_api_key: str
    :param user: The VictorOps user ID
    :type user: str

    """
    return web.Response(status=200)


async def api_public_v1_user_user_contact_methods_phones_contact_id_delete(request: web.Request, x_vo_api_id, x_vo_api_key, user, contact_id) -> web.Response:
    """Delete a contact phone for a user

    Delete the indicated contact phone for the user  This API may be called a maximum of 60 times per minute. 

    :param x_vo_api_id: Your API ID
    :type x_vo_api_id: str
    :param x_vo_api_key: Your API Key
    :type x_vo_api_key: str
    :param user: The VictorOps user ID
    :type user: str
    :param contact_id: The unique contact identifier
    :type contact_id: str

    """
    return web.Response(status=200)


async def api_public_v1_user_user_contact_methods_phones_contact_id_get(request: web.Request, x_vo_api_id, x_vo_api_key, user, contact_id) -> web.Response:
    """Get the indicated contact phone for a user

    Get the indicated contact phone for a user  This API may be called a maximum of 60 times per minute. 

    :param x_vo_api_id: Your API ID
    :type x_vo_api_id: str
    :param x_vo_api_key: Your API Key
    :type x_vo_api_key: str
    :param user: The VictorOps user ID
    :type user: str
    :param contact_id: The unique contact identifier
    :type contact_id: str

    """
    return web.Response(status=200)


async def api_public_v1_user_user_contact_methods_phones_get(request: web.Request, x_vo_api_id, x_vo_api_key, user) -> web.Response:
    """Get a list of all contact phones for a user

    Get the contact phones for a user  This API may be called a maximum of 60 times per minute. 

    :param x_vo_api_id: Your API ID
    :type x_vo_api_id: str
    :param x_vo_api_key: Your API Key
    :type x_vo_api_key: str
    :param user: The VictorOps user ID
    :type user: str

    """
    return web.Response(status=200)


async def api_public_v1_user_user_contact_methods_phones_post(request: web.Request, x_vo_api_id, x_vo_api_key, user, body) -> web.Response:
    """Create a contact phones for a user

    Create a contact phone for a user  This API may be called a maximum of 60 times per minute. 

    :param x_vo_api_id: Your API ID
    :type x_vo_api_id: str
    :param x_vo_api_key: Your API Key
    :type x_vo_api_key: str
    :param user: The VictorOps user ID
    :type user: str
    :param body: The contact phone
    :type body: dict | bytes

    """
    body = ContactPhoneAdd.from_dict(body)
    return web.Response(status=200)
