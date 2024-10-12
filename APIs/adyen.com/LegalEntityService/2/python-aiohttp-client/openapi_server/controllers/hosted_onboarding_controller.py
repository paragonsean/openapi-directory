from typing import List, Dict
from aiohttp import web

from openapi_server.models.onboarding_link import OnboardingLink
from openapi_server.models.onboarding_link_info import OnboardingLinkInfo
from openapi_server.models.onboarding_theme import OnboardingTheme
from openapi_server.models.onboarding_themes import OnboardingThemes
from openapi_server.models.service_error import ServiceError
from openapi_server import util


async def get_themes(request: web.Request, ) -> web.Response:
    """Get a list of hosted onboarding page themes

    Returns a list of hosted onboarding page themes.  &gt;If you are using hosted onboarding and just beginning your integration, use v3 for your API requests. Otherwise, use v2.  


    """
    return web.Response(status=200)


async def get_themes_id(request: web.Request, id) -> web.Response:
    """Get an onboarding link theme

    Returns the details of the theme identified in the path.&gt;If you are using hosted onboarding and just beginning your integration, use v3 for your API requests. Otherwise, use v2.  

    :param id: The unique identifier of the theme
    :type id: str

    """
    return web.Response(status=200)


async def post_legal_entities_id_onboarding_links(request: web.Request, id, body=None) -> web.Response:
    """Get a link to an Adyen-hosted onboarding page

    Returns a link to an Adyen-hosted onboarding page where you need to redirect your user.  &gt;If you are using hosted onboarding and just beginning your integration, use v3 for your API requests. Otherwise, use v2.  

    :param id: The unique identifier of the legal entity
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = OnboardingLinkInfo.from_dict(body)
    return web.Response(status=200)
