from typing import List, Dict
from aiohttp import web

from openapi_server.models.attraction import Attraction
from openapi_server.models.augmentation_data import AugmentationData
from openapi_server.models.entitlement import Entitlement
from openapi_server.models.event import Event
from openapi_server.models.extension_data import ExtensionData
from openapi_server.models.ingestion_result import IngestionResult
from openapi_server.models.venue import Venue
from openapi_server.models.video import Video
from openapi_server import util


async def patch_attraction(request: web.Request, id, tmps_correlation_id, body) -> web.Response:
    """Publish a patch on an attraction

    Since 1.0.0

    :param id: ID of the attraction the patch will be applied
    :type id: str
    :param tmps_correlation_id: Unique correlation id to be able to trace the request in our system
    :type tmps_correlation_id: str
    :param body: Patch to apply
    :type body: dict | bytes

    """
    body = AugmentationData.from_dict(body)
    return web.Response(status=200)


async def patch_event(request: web.Request, id, tmps_correlation_id, body) -> web.Response:
    """Publish a patch on an event

    Since 1.0.0

    :param id: ID of the event the patch will be applied
    :type id: str
    :param tmps_correlation_id: Unique correlation id to be able to trace the request in our system
    :type tmps_correlation_id: str
    :param body: Patch to apply
    :type body: dict | bytes

    """
    body = AugmentationData.from_dict(body)
    return web.Response(status=200)


async def patch_venue(request: web.Request, id, tmps_correlation_id, body) -> web.Response:
    """Publish a patch on a venue

    Since 1.0.0

    :param id: ID of the venue the patch will be applied
    :type id: str
    :param tmps_correlation_id: Unique correlation id to be able to trace the request in our system
    :type tmps_correlation_id: str
    :param body: Patch to apply
    :type body: dict | bytes

    """
    body = AugmentationData.from_dict(body)
    return web.Response(status=200)


async def publish_attraction(request: web.Request, tmps_correlation_id, body) -> web.Response:
    """Publish an attractions

    Since 1.0.0

    :param tmps_correlation_id: Unique correlation id to be able to trace the request in our system
    :type tmps_correlation_id: str
    :param body: Attraction
    :type body: dict | bytes

    """
    body = Attraction.from_dict(body)
    return web.Response(status=200)


async def publish_attraction_videos(request: web.Request, id, tmps_correlation_id, body) -> web.Response:
    """Publish a video on an attraction

    Since 1.0.0

    :param id: ID of the attraction the video is linked to
    :type id: str
    :param tmps_correlation_id: Unique correlation id to be able to trace the request in our system
    :type tmps_correlation_id: str
    :param body: Video data
    :type body: dict | bytes

    """
    body = Video.from_dict(body)
    return web.Response(status=200)


async def publish_entitlements(request: web.Request, tmps_correlation_id, body) -> web.Response:
    """Publish entitlements on an entity

    Since 2.0.0

    :param tmps_correlation_id: Unique correlation id to be able to trace the request in our system
    :type tmps_correlation_id: str
    :param body: Entitlements information to add to the entity
    :type body: dict | bytes

    """
    body = Entitlement.from_dict(body)
    return web.Response(status=200)


async def publish_event(request: web.Request, tmps_correlation_id, body) -> web.Response:
    """Publish an event

    Since 1.0.0

    :param tmps_correlation_id: Unique correlation id to be able to trace the request in our system
    :type tmps_correlation_id: str
    :param body: Event
    :type body: dict | bytes

    """
    body = Event.from_dict(body)
    return web.Response(status=200)


async def publish_event_videos(request: web.Request, id, tmps_correlation_id, body) -> web.Response:
    """Publish a video on an event

    Since 1.0.0

    :param id: ID of the event the video is linked to
    :type id: str
    :param tmps_correlation_id: Unique correlation id to be able to trace the request in our system
    :type tmps_correlation_id: str
    :param body: Video data
    :type body: dict | bytes

    """
    body = Video.from_dict(body)
    return web.Response(status=200)


async def publish_extension(request: web.Request, tmps_correlation_id, body) -> web.Response:
    """Publish extension on an entity

    Since 1.0.0

    :param tmps_correlation_id: Unique correlation id to be able to trace the request in our system
    :type tmps_correlation_id: str
    :param body: Extension information to add to the entity
    :type body: dict | bytes

    """
    body = ExtensionData.from_dict(body)
    return web.Response(status=200)


async def publish_venue(request: web.Request, tmps_correlation_id, body) -> web.Response:
    """Publish a venue

    Since 1.0.0

    :param tmps_correlation_id: Unique correlation id to be able to trace the request in our system
    :type tmps_correlation_id: str
    :param body: Venue
    :type body: dict | bytes

    """
    body = Venue.from_dict(body)
    return web.Response(status=200)
