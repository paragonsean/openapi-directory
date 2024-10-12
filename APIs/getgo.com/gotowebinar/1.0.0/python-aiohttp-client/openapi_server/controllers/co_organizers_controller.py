from typing import List, Dict
from aiohttp import web

from openapi_server.models.coorganizer import Coorganizer
from openapi_server.models.coorganizer_req_create import CoorganizerReqCreate
from openapi_server import util


async def create_coorganizers(request: web.Request, authorization, organizer_key, webinar_key, body) -> web.Response:
    """Create co-organizers

    Creates co-organizers for the specified webinar. For co-organizers that have a GoToWebinar account you have to set the parameter &#39;external&#39; to &#39;false&#39;. In this case you have to pass the parameter &#39;organizerKey&#39; only. For co-organizers that have no GoToWebinar account you have to set the parameter &#39;external&#39; to &#39;true&#39;. In this case you have to pass the parameters &#39;givenName&#39; and &#39;email&#39;. Since there is no parameter for &#39;surname&#39; you should pass first and last name to the parameter &#39;givenName&#39;.

    :param authorization: Access token
    :type authorization: str
    :param organizer_key: The key of the organizer
    :type organizer_key: int
    :param webinar_key: The key of the webinar
    :type webinar_key: int
    :param body: The co-organizer details
    :type body: list | bytes

    """
    body = [CoorganizerReqCreate.from_dict(d) for d in body]
    return web.Response(status=200)


async def delete_coorganizer(request: web.Request, authorization, organizer_key, webinar_key, coorganizer_key, external=None) -> web.Response:
    """Delete co-organizer

    Deletes an internal co-organizer specified by the coorganizerKey (memberKey).

    :param authorization: Access token
    :type authorization: str
    :param organizer_key: The key of the organizer
    :type organizer_key: int
    :param webinar_key: The key of the webinar
    :type webinar_key: int
    :param coorganizer_key: The key of the internal or external co-organizer (memberKey)
    :type coorganizer_key: int
    :param external: By default only internal co-organizers (with a GoToWebinar account) can be deleted. If you want to use this call for external co-organizers you have to set this parameter to &#39;true&#39;.
    :type external: bool

    """
    return web.Response(status=200)


async def get_coorganizers(request: web.Request, authorization, organizer_key, webinar_key) -> web.Response:
    """Get co-organizers

    Returns the co-organizers for the specified webinar. The original organizer who created the webinar is filtered out of the list. If the webinar has no co-organizers, an empty array is returned. Co-organizers that do not have a GoToWebinar account are returned as external co-organizers. For those organizers no surname is returned.

    :param authorization: Access token
    :type authorization: str
    :param organizer_key: The key of the organizer
    :type organizer_key: int
    :param webinar_key: The key of the webinar
    :type webinar_key: int

    """
    return web.Response(status=200)


async def resend_coorganizer_invitation(request: web.Request, authorization, organizer_key, webinar_key, coorganizer_key, external=None) -> web.Response:
    """Resend invitation

    Resends an invitation email to the specified co-organizer

    :param authorization: Access token
    :type authorization: str
    :param organizer_key: The key of the organizer
    :type organizer_key: int
    :param webinar_key: The key of the webinar
    :type webinar_key: int
    :param coorganizer_key: The key of the internal or external co-organizer (memberKey)
    :type coorganizer_key: int
    :param external: By default only internal co-organizers (with a GoToWebinar account) will retrieve the resent invitation email. If you want to use this call for external co-organizers you have to set this parameter to &#39;true&#39;.
    :type external: bool

    """
    return web.Response(status=200)
