from typing import List, Dict
from aiohttp import web

from openapi_server.models.newsletter_input import NewsletterInput
from openapi_server.models.newsletterresponse import Newsletterresponse
from openapi_server.models.newsletters import Newsletters
from openapi_server import util


async def find_newsletters(request: web.Request, vestorly_auth, access_token=None) -> web.Response:
    """find_newsletters

    Returns all newsletters

    :param vestorly_auth: Vestorly Auth Token
    :type vestorly_auth: str
    :param access_token: OAuth Token
    :type access_token: str

    """
    return web.Response(status=200)


async def get_newsletter_by_id(request: web.Request, vestorly_auth, id, access_token=None) -> web.Response:
    """get_newsletter_by_id

    Get a newsletter by ID

    :param vestorly_auth: Vestorly Auth Token
    :type vestorly_auth: str
    :param id: Mongo ID of event to get
    :type id: str
    :param access_token: OAuth Token
    :type access_token: str

    """
    return web.Response(status=200)


async def update_newsletter_by_id(request: web.Request, vestorly_auth, id, newsletter, access_token=None) -> web.Response:
    """update_newsletter_by_id

    Updates a newsletter

    :param vestorly_auth: Vestorly Auth Token
    :type vestorly_auth: str
    :param id: Mongo ID of event to update
    :type id: str
    :param newsletter: Newsletter
    :type newsletter: dict | bytes
    :param access_token: OAuth Token
    :type access_token: str

    """
    newsletter = NewsletterInput.from_dict(newsletter)
    return web.Response(status=200)
