from typing import List, Dict
from aiohttp import web

from openapi_server.models.newsletter_settings import NewsletterSettings
from openapi_server.models.newsletter_settings_input import NewsletterSettingsInput
from openapi_server.models.newslettersettingresponse import Newslettersettingresponse
from openapi_server import util


async def find_newsletter_settings(request: web.Request, vestorly_auth, access_token=None) -> web.Response:
    """find_newsletter_settings

    Returns all newsletter settings

    :param vestorly_auth: Vestorly Auth Token
    :type vestorly_auth: str
    :param access_token: OAuth Token
    :type access_token: str

    """
    return web.Response(status=200)


async def find_newsletter_settings_by_id(request: web.Request, id, vestorly_auth, access_token=None) -> web.Response:
    """find_newsletter_settings_by_id

    Returns a single newsletter settings if the user has access

    :param id: Mongo ID of newsletter settings to fetch
    :type id: str
    :param vestorly_auth: Vestorly Auth Token
    :type vestorly_auth: str
    :param access_token: OAuth Token
    :type access_token: str

    """
    return web.Response(status=200)


async def update_newsletter_settings_by_id(request: web.Request, id, vestorly_auth, newsletter_setting, access_token=None) -> web.Response:
    """update_newsletter_settings_by_id

    Update a single newsletter setting by ID

    :param id: Mongo ID of newsletter settings to update
    :type id: str
    :param vestorly_auth: Vestorly Auth Token
    :type vestorly_auth: str
    :param newsletter_setting: newsletter settings
    :type newsletter_setting: dict | bytes
    :param access_token: OAuth Token
    :type access_token: str

    """
    newsletter_setting = NewsletterSettingsInput.from_dict(newsletter_setting)
    return web.Response(status=200)
