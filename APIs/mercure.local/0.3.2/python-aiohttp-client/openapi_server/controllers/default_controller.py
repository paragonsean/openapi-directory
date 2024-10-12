from typing import List, Dict
from aiohttp import web

from openapi_server.models.subscriptions import Subscriptions
from openapi_server import util


async def well_known_mercure_get(request: web.Request, topic, last_event_id=None, last_event_id2=None) -> web.Response:
    """Subscribe to updates

    

    :param topic: The topic to get updates from, can be a URI template (RFC6570).
    :type topic: List[str]
    :param last_event_id: The last received event id, to retrieve missed events.
    :type last_event_id: str
    :param last_event_id2: The last received event id, to retrieve missed events, takes precedence over the query parameter.
    :type last_event_id2: str

    """
    return web.Response(status=200)


async def well_known_mercure_post(request: web.Request, data, topic, id=None, private=None, retry=None, type=None) -> web.Response:
    """Publish an update

    

    :param data: The content of the new version of this topic.
    :type data: str
    :param topic: IRIs of the updated topic. If this key is present several times, the first occurrence is considered to be the canonical URL of the topic, and other ones are considered to be alternate URLs.
    :type topic: List[str]
    :param id: The topic&#39;s revision identifier: it will be used as the SSE&#39;s &#x60;id&#x60; property.
    :type id: str
    :param private: To mark an update as private. If not provided, this update will be public.
    :type private: bool
    :param retry: The SSE&#39;s &#x60;retry&#x60; property (the reconnection time).
    :type retry: int
    :param type: The SSE&#39;s &#x60;event&#x60; property (a specific event type).
    :type type: str

    """
    return web.Response(status=200)


async def well_known_mercure_subscriptions_get(request: web.Request, ) -> web.Response:
    """Active subscriptions

    


    """
    return web.Response(status=200)


async def well_known_mercure_subscriptions_topic_get(request: web.Request, topic) -> web.Response:
    """Active subscriptions for the given topic

    

    :param topic: 
    :type topic: str

    """
    return web.Response(status=200)


async def well_known_mercure_subscriptions_topic_subscriber_get(request: web.Request, topic, subscriber) -> web.Response:
    """Active subscription for the given topic and subscriber

    

    :param topic: 
    :type topic: str
    :param subscriber: 
    :type subscriber: str

    """
    return web.Response(status=200)
