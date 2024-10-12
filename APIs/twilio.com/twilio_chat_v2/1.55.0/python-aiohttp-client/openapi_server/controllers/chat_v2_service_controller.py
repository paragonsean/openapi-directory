from typing import List, Dict
from aiohttp import web

from openapi_server.models.chat_v2_service import ChatV2Service
from openapi_server.models.list_service_response import ListServiceResponse
from openapi_server import util


async def create_service(request: web.Request, friendly_name) -> web.Response:
    """create_service

    

    :param friendly_name: A descriptive string that you create to describe the new resource.
    :type friendly_name: str

    """
    return web.Response(status=200)


async def delete_service(request: web.Request, sid) -> web.Response:
    """delete_service

    

    :param sid: The SID of the Service resource to delete.
    :type sid: str

    """
    return web.Response(status=200)


async def fetch_service(request: web.Request, sid) -> web.Response:
    """fetch_service

    

    :param sid: The SID of the Service resource to fetch.
    :type sid: str

    """
    return web.Response(status=200)


async def list_service(request: web.Request, page_size=None, page=None, page_token=None) -> web.Response:
    """list_service

    

    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)


async def update_service(request: web.Request, sid, consumption_report_interval=None, default_channel_creator_role_sid=None, default_channel_role_sid=None, default_service_role_sid=None, friendly_name=None, limits_channel_members=None, limits_user_channels=None, media_compatibility_message=None, notifications_added_to_channel_enabled=None, notifications_added_to_channel_sound=None, notifications_added_to_channel_template=None, notifications_invited_to_channel_enabled=None, notifications_invited_to_channel_sound=None, notifications_invited_to_channel_template=None, notifications_log_enabled=None, notifications_new_message_badge_count_enabled=None, notifications_new_message_enabled=None, notifications_new_message_sound=None, notifications_new_message_template=None, notifications_removed_from_channel_enabled=None, notifications_removed_from_channel_sound=None, notifications_removed_from_channel_template=None, post_webhook_retry_count=None, post_webhook_url=None, pre_webhook_retry_count=None, pre_webhook_url=None, reachability_enabled=None, read_status_enabled=None, typing_indicator_timeout=None, webhook_filters=None, webhook_method=None) -> web.Response:
    """update_service

    

    :param sid: The SID of the Service resource to update.
    :type sid: str
    :param consumption_report_interval: DEPRECATED. The interval in seconds between consumption reports submission batches from client endpoints.
    :type consumption_report_interval: int
    :param default_channel_creator_role_sid: The channel role assigned to a channel creator when they join a new channel. See the [Role resource](https://www.twilio.com/docs/chat/rest/role-resource) for more info about roles.
    :type default_channel_creator_role_sid: str
    :param default_channel_role_sid: The channel role assigned to users when they are added to a channel. See the [Role resource](https://www.twilio.com/docs/chat/rest/role-resource) for more info about roles.
    :type default_channel_role_sid: str
    :param default_service_role_sid: The service role assigned to users when they are added to the service. See the [Role resource](https://www.twilio.com/docs/chat/rest/role-resource) for more info about roles.
    :type default_service_role_sid: str
    :param friendly_name: A descriptive string that you create to describe the resource.
    :type friendly_name: str
    :param limits_channel_members: The maximum number of Members that can be added to Channels within this Service. Can be up to 1,000.
    :type limits_channel_members: int
    :param limits_user_channels: The maximum number of Channels Users can be a Member of within this Service. Can be up to 1,000.
    :type limits_user_channels: int
    :param media_compatibility_message: The message to send when a media message has no text. Can be used as placeholder message.
    :type media_compatibility_message: str
    :param notifications_added_to_channel_enabled: Whether to send a notification when a member is added to a channel. The default is &#x60;false&#x60;.
    :type notifications_added_to_channel_enabled: bool
    :param notifications_added_to_channel_sound: The name of the sound to play when a member is added to a channel and &#x60;notifications.added_to_channel.enabled&#x60; is &#x60;true&#x60;.
    :type notifications_added_to_channel_sound: str
    :param notifications_added_to_channel_template: The template to use to create the notification text displayed when a member is added to a channel and &#x60;notifications.added_to_channel.enabled&#x60; is &#x60;true&#x60;.
    :type notifications_added_to_channel_template: str
    :param notifications_invited_to_channel_enabled: Whether to send a notification when a user is invited to a channel. The default is &#x60;false&#x60;.
    :type notifications_invited_to_channel_enabled: bool
    :param notifications_invited_to_channel_sound: The name of the sound to play when a user is invited to a channel and &#x60;notifications.invited_to_channel.enabled&#x60; is &#x60;true&#x60;.
    :type notifications_invited_to_channel_sound: str
    :param notifications_invited_to_channel_template: The template to use to create the notification text displayed when a user is invited to a channel and &#x60;notifications.invited_to_channel.enabled&#x60; is &#x60;true&#x60;.
    :type notifications_invited_to_channel_template: str
    :param notifications_log_enabled: Whether to log notifications. The default is &#x60;false&#x60;.
    :type notifications_log_enabled: bool
    :param notifications_new_message_badge_count_enabled: Whether the new message badge is enabled. The default is &#x60;false&#x60;.
    :type notifications_new_message_badge_count_enabled: bool
    :param notifications_new_message_enabled: Whether to send a notification when a new message is added to a channel. The default is &#x60;false&#x60;.
    :type notifications_new_message_enabled: bool
    :param notifications_new_message_sound: The name of the sound to play when a new message is added to a channel and &#x60;notifications.new_message.enabled&#x60; is &#x60;true&#x60;.
    :type notifications_new_message_sound: str
    :param notifications_new_message_template: The template to use to create the notification text displayed when a new message is added to a channel and &#x60;notifications.new_message.enabled&#x60; is &#x60;true&#x60;.
    :type notifications_new_message_template: str
    :param notifications_removed_from_channel_enabled: Whether to send a notification to a user when they are removed from a channel. The default is &#x60;false&#x60;.
    :type notifications_removed_from_channel_enabled: bool
    :param notifications_removed_from_channel_sound: The name of the sound to play to a user when they are removed from a channel and &#x60;notifications.removed_from_channel.enabled&#x60; is &#x60;true&#x60;.
    :type notifications_removed_from_channel_sound: str
    :param notifications_removed_from_channel_template: The template to use to create the notification text displayed to a user when they are removed from a channel and &#x60;notifications.removed_from_channel.enabled&#x60; is &#x60;true&#x60;.
    :type notifications_removed_from_channel_template: str
    :param post_webhook_retry_count: The number of times to retry a call to the &#x60;post_webhook_url&#x60; if the request times out (after 5 seconds) or it receives a 429, 503, or 504 HTTP response. The default is 0, which means the call won&#39;t be retried.
    :type post_webhook_retry_count: int
    :param post_webhook_url: The URL for post-event webhooks, which are called by using the &#x60;webhook_method&#x60;. See [Webhook Events](https://www.twilio.com/docs/chat/webhook-events) for more details.
    :type post_webhook_url: str
    :param pre_webhook_retry_count: The number of times to retry a call to the &#x60;pre_webhook_url&#x60; if the request times out (after 5 seconds) or it receives a 429, 503, or 504 HTTP response. Default retry count is 0 times, which means the call won&#39;t be retried.
    :type pre_webhook_retry_count: int
    :param pre_webhook_url: The URL for pre-event webhooks, which are called by using the &#x60;webhook_method&#x60;. See [Webhook Events](https://www.twilio.com/docs/chat/webhook-events) for more details.
    :type pre_webhook_url: str
    :param reachability_enabled: Whether to enable the [Reachability Indicator](https://www.twilio.com/docs/chat/reachability-indicator) for this Service instance. The default is &#x60;false&#x60;.
    :type reachability_enabled: bool
    :param read_status_enabled: Whether to enable the [Message Consumption Horizon](https://www.twilio.com/docs/chat/consumption-horizon) feature. The default is &#x60;true&#x60;.
    :type read_status_enabled: bool
    :param typing_indicator_timeout: How long in seconds after a &#x60;started typing&#x60; event until clients should assume that user is no longer typing, even if no &#x60;ended typing&#x60; message was received.  The default is 5 seconds.
    :type typing_indicator_timeout: int
    :param webhook_filters: The list of webhook events that are enabled for this Service instance. See [Webhook Events](https://www.twilio.com/docs/chat/webhook-events) for more details.
    :type webhook_filters: List[str]
    :param webhook_method: The HTTP method to use for calls to the &#x60;pre_webhook_url&#x60; and &#x60;post_webhook_url&#x60; webhooks.  Can be: &#x60;POST&#x60; or &#x60;GET&#x60; and the default is &#x60;POST&#x60;. See [Webhook Events](https://www.twilio.com/docs/chat/webhook-events) for more details.
    :type webhook_method: str

    """
    return web.Response(status=200)
