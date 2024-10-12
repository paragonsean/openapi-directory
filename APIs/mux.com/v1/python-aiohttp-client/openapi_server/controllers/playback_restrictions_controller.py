from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_playback_restriction_request import CreatePlaybackRestrictionRequest
from openapi_server.models.list_playback_restrictions_response import ListPlaybackRestrictionsResponse
from openapi_server.models.playback_restriction_response import PlaybackRestrictionResponse
from openapi_server.models.update_referrer_domain_restriction_request import UpdateReferrerDomainRestrictionRequest
from openapi_server import util


async def create_playback_restriction(request: web.Request, body) -> web.Response:
    """Create a Playback Restriction

    Create a new Playback Restriction.

    :param body: 
    :type body: dict | bytes

    """
    body = CreatePlaybackRestrictionRequest.from_dict(body)
    return web.Response(status=200)


async def delete_playback_restriction(request: web.Request, playback_restriction_id) -> web.Response:
    """Delete a Playback Restriction

    Deletes a single Playback Restriction.

    :param playback_restriction_id: ID of the Playback Restriction.
    :type playback_restriction_id: str

    """
    return web.Response(status=200)


async def get_playback_restriction(request: web.Request, playback_restriction_id) -> web.Response:
    """Retrieve a Playback Restriction

    Retrieves a Playback Restriction associated with the unique identifier.

    :param playback_restriction_id: ID of the Playback Restriction.
    :type playback_restriction_id: str

    """
    return web.Response(status=200)


async def list_playback_restrictions(request: web.Request, page=None, limit=None) -> web.Response:
    """List Playback Restrictions

    Returns a list of all Playback Restrictions.

    :param page: Offset by this many pages, of the size of &#x60;limit&#x60;
    :type page: int
    :param limit: Number of items to include in the response
    :type limit: int

    """
    return web.Response(status=200)


async def update_referrer_domain_restriction(request: web.Request, playback_restriction_id, body) -> web.Response:
    """Update the Referrer Playback Restriction

    Allows you to modify the list of domains or change how Mux validates playback requests without the &#x60;Referer&#x60; HTTP header. The Referrer restriction fully replaces the old list with this new list of domains.

    :param playback_restriction_id: ID of the Playback Restriction.
    :type playback_restriction_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateReferrerDomainRestrictionRequest.from_dict(body)
    return web.Response(status=200)
