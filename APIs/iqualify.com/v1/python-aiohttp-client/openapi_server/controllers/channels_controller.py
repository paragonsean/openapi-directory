from typing import List, Dict
from aiohttp import web

from openapi_server.models.channel import Channel
from openapi_server.models.channel_required import ChannelRequired
from openapi_server.models.channel_response import ChannelResponse
from openapi_server.models.comment import Comment
from openapi_server.models.error import Error
from openapi_server.models.http_post import HttpPost
from openapi_server.models.offerings_offering_id_channels_channel_id_learners_post_request import OfferingsOfferingIdChannelsChannelIdLearnersPostRequest
from openapi_server import util


async def offerings_offering_id_analytics_channels_channel_id_comments_get(request: web.Request, offering_id, channel_id) -> web.Response:
    """Find comments

    Responds with a list of comments made in any posts in a specified channel, within an offering.

    :param offering_id: offering&#39;s id
    :type offering_id: str
    :param channel_id: channel&#39;s id
    :type channel_id: str

    """
    return web.Response(status=200)


async def offerings_offering_id_analytics_channels_channel_id_posts_get(request: web.Request, offering_id, channel_id) -> web.Response:
    """Find posts

    Responds with a list of posts made in a specified channel, within an offering.

    :param offering_id: offering&#39;s id
    :type offering_id: str
    :param channel_id: channel&#39;s id
    :type channel_id: str

    """
    return web.Response(status=200)


async def offerings_offering_id_analytics_channels_channel_id_replies_get(request: web.Request, offering_id, channel_id) -> web.Response:
    """Find replies

    Responds with a list of replies to comments in any posts in a specified channel, within an offering.

    :param offering_id: offering&#39;s id
    :type offering_id: str
    :param channel_id: channel&#39;s id
    :type channel_id: str

    """
    return web.Response(status=200)


async def offerings_offering_id_channels_channel_id_learners_delete(request: web.Request, offering_id, channel_id, body) -> web.Response:
    """Remove learners from a group channel

    Removes a learner from the specified group channel.

    :param offering_id: offering&#39;s id
    :type offering_id: str
    :param channel_id: channel&#39;s id
    :type channel_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = OfferingsOfferingIdChannelsChannelIdLearnersPostRequest.from_dict(body)
    return web.Response(status=200)


async def offerings_offering_id_channels_channel_id_learners_get(request: web.Request, offering_id, channel_id) -> web.Response:
    """Find learners in a group channel

    Finds all learners in a specified group channel.

    :param offering_id: offering&#39;s id
    :type offering_id: str
    :param channel_id: channel&#39;s id
    :type channel_id: str

    """
    return web.Response(status=200)


async def offerings_offering_id_channels_channel_id_learners_post(request: web.Request, offering_id, channel_id, body) -> web.Response:
    """Add learners to a group channel

    Adds a learner to a specified group channel.

    :param offering_id: offering&#39;s id
    :type offering_id: str
    :param channel_id: channel&#39;s id
    :type channel_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = OfferingsOfferingIdChannelsChannelIdLearnersPostRequest.from_dict(body)
    return web.Response(status=200)


async def offerings_offering_id_channels_channel_id_patch(request: web.Request, offering_id, channel_id, body) -> web.Response:
    """Update channel

    Updates a channel in an offering.

    :param offering_id: offering&#39;s id
    :type offering_id: str
    :param channel_id: channel&#39;s id
    :type channel_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = Channel.from_dict(body)
    return web.Response(status=200)


async def offerings_offering_id_channels_get(request: web.Request, offering_id) -> web.Response:
    """Find channels

    Responds with a list of channels in an offering.

    :param offering_id: offering&#39;s id
    :type offering_id: str

    """
    return web.Response(status=200)


async def offerings_offering_id_channels_post(request: web.Request, offering_id, body) -> web.Response:
    """Add channel

    Adds new channel to the specified offering.

    :param offering_id: offering&#39;s id
    :type offering_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = ChannelRequired.from_dict(body)
    return web.Response(status=200)
