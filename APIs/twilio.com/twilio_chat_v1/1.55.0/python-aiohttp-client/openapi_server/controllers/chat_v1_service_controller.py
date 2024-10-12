from typing import List, Dict
from aiohttp import web

from openapi_server.models.chat_v1_service import ChatV1Service
from openapi_server.models.list_service_response import ListServiceResponse
from openapi_server import util


async def create_service(request: web.Request, friendly_name) -> web.Response:
    """create_service

    

    :param friendly_name: A descriptive string that you create to describe the resource. It can be up to 64 characters long.
    :type friendly_name: str

    """
    return web.Response(status=200)


async def delete_service(request: web.Request, sid) -> web.Response:
    """delete_service

    

    :param sid: The Twilio-provided string that uniquely identifies the Service resource to delete.
    :type sid: str

    """
    return web.Response(status=200)


async def fetch_service(request: web.Request, sid) -> web.Response:
    """fetch_service

    

    :param sid: The Twilio-provided string that uniquely identifies the Service resource to fetch.
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


async def update_service(request: web.Request, sid, consumption_report_interval=None, default_channel_creator_role_sid=None, default_channel_role_sid=None, default_service_role_sid=None, friendly_name=None, limits_channel_members=None, limits_user_channels=None, notifications_added_to_channel_enabled=None, notifications_added_to_channel_template=None, notifications_invited_to_channel_enabled=None, notifications_invited_to_channel_template=None, notifications_new_message_enabled=None, notifications_new_message_template=None, notifications_removed_from_channel_enabled=None, notifications_removed_from_channel_template=None, post_webhook_url=None, pre_webhook_url=None, reachability_enabled=None, read_status_enabled=None, typing_indicator_timeout=None, webhook_filters=None, webhook_method=None, webhooks_on_channel_add_method=None, webhooks_on_channel_add_url=None, webhooks_on_channel_added_method=None, webhooks_on_channel_added_url=None, webhooks_on_channel_destroy_method=None, webhooks_on_channel_destroy_url=None, webhooks_on_channel_destroyed_method=None, webhooks_on_channel_destroyed_url=None, webhooks_on_channel_update_method=None, webhooks_on_channel_update_url=None, webhooks_on_channel_updated_method=None, webhooks_on_channel_updated_url=None, webhooks_on_member_add_method=None, webhooks_on_member_add_url=None, webhooks_on_member_added_method=None, webhooks_on_member_added_url=None, webhooks_on_member_remove_method=None, webhooks_on_member_remove_url=None, webhooks_on_member_removed_method=None, webhooks_on_member_removed_url=None, webhooks_on_message_remove_method=None, webhooks_on_message_remove_url=None, webhooks_on_message_removed_method=None, webhooks_on_message_removed_url=None, webhooks_on_message_send_method=None, webhooks_on_message_send_url=None, webhooks_on_message_sent_method=None, webhooks_on_message_sent_url=None, webhooks_on_message_update_method=None, webhooks_on_message_update_url=None, webhooks_on_message_updated_method=None, webhooks_on_message_updated_url=None) -> web.Response:
    """update_service

    

    :param sid: The Twilio-provided string that uniquely identifies the Service resource to update.
    :type sid: str
    :param consumption_report_interval: DEPRECATED. The interval in seconds between consumption reports submission batches from client endpoints.
    :type consumption_report_interval: int
    :param default_channel_creator_role_sid: The channel role assigned to a channel creator when they join a new channel. See the [Roles endpoint](https://www.twilio.com/docs/chat/api/roles) for more details.
    :type default_channel_creator_role_sid: str
    :param default_channel_role_sid: The channel role assigned to users when they are added to a channel. See the [Roles endpoint](https://www.twilio.com/docs/chat/api/roles) for more details.
    :type default_channel_role_sid: str
    :param default_service_role_sid: The service role assigned to users when they are added to the service. See the [Roles endpoint](https://www.twilio.com/docs/chat/api/roles) for more details.
    :type default_service_role_sid: str
    :param friendly_name: A descriptive string that you create to describe the resource. It can be up to 64 characters long.
    :type friendly_name: str
    :param limits_channel_members: The maximum number of Members that can be added to Channels within this Service. Can be up to 1,000.
    :type limits_channel_members: int
    :param limits_user_channels: The maximum number of Channels Users can be a Member of within this Service. Can be up to 1,000.
    :type limits_user_channels: int
    :param notifications_added_to_channel_enabled: Whether to send a notification when a member is added to a channel. Can be: &#x60;true&#x60; or &#x60;false&#x60; and the default is &#x60;false&#x60;.
    :type notifications_added_to_channel_enabled: bool
    :param notifications_added_to_channel_template: The template to use to create the notification text displayed when a member is added to a channel and &#x60;notifications.added_to_channel.enabled&#x60; is &#x60;true&#x60;.
    :type notifications_added_to_channel_template: str
    :param notifications_invited_to_channel_enabled: Whether to send a notification when a user is invited to a channel. Can be: &#x60;true&#x60; or &#x60;false&#x60; and the default is &#x60;false&#x60;.
    :type notifications_invited_to_channel_enabled: bool
    :param notifications_invited_to_channel_template: The template to use to create the notification text displayed when a user is invited to a channel and &#x60;notifications.invited_to_channel.enabled&#x60; is &#x60;true&#x60;.
    :type notifications_invited_to_channel_template: str
    :param notifications_new_message_enabled: Whether to send a notification when a new message is added to a channel. Can be: &#x60;true&#x60; or &#x60;false&#x60; and the default is &#x60;false&#x60;.
    :type notifications_new_message_enabled: bool
    :param notifications_new_message_template: The template to use to create the notification text displayed when a new message is added to a channel and &#x60;notifications.new_message.enabled&#x60; is &#x60;true&#x60;.
    :type notifications_new_message_template: str
    :param notifications_removed_from_channel_enabled: Whether to send a notification to a user when they are removed from a channel. Can be: &#x60;true&#x60; or &#x60;false&#x60; and the default is &#x60;false&#x60;.
    :type notifications_removed_from_channel_enabled: bool
    :param notifications_removed_from_channel_template: The template to use to create the notification text displayed to a user when they are removed from a channel and &#x60;notifications.removed_from_channel.enabled&#x60; is &#x60;true&#x60;.
    :type notifications_removed_from_channel_template: str
    :param post_webhook_url: The URL for post-event webhooks, which are called by using the &#x60;webhook_method&#x60;. See [Webhook Events](https://www.twilio.com/docs/api/chat/webhooks) for more details.
    :type post_webhook_url: str
    :param pre_webhook_url: The URL for pre-event webhooks, which are called by using the &#x60;webhook_method&#x60;. See [Webhook Events](https://www.twilio.com/docs/api/chat/webhooks) for more details.
    :type pre_webhook_url: str
    :param reachability_enabled: Whether to enable the [Reachability Indicator](https://www.twilio.com/docs/chat/reachability-indicator) for this Service instance. The default is &#x60;false&#x60;.
    :type reachability_enabled: bool
    :param read_status_enabled: Whether to enable the [Message Consumption Horizon](https://www.twilio.com/docs/chat/consumption-horizon) feature. The default is &#x60;true&#x60;.
    :type read_status_enabled: bool
    :param typing_indicator_timeout: How long in seconds after a &#x60;started typing&#x60; event until clients should assume that user is no longer typing, even if no &#x60;ended typing&#x60; message was received.  The default is 5 seconds.
    :type typing_indicator_timeout: int
    :param webhook_filters: The list of WebHook events that are enabled for this Service instance. See [Webhook Events](https://www.twilio.com/docs/chat/webhook-events) for more details.
    :type webhook_filters: List[str]
    :param webhook_method: The HTTP method to use for calls to the &#x60;pre_webhook_url&#x60; and &#x60;post_webhook_url&#x60; webhooks.  Can be: &#x60;POST&#x60; or &#x60;GET&#x60; and the default is &#x60;POST&#x60;. See [Webhook Events](https://www.twilio.com/docs/chat/webhook-events) for more details.
    :type webhook_method: str
    :param webhooks_on_channel_add_method: The HTTP method to use when calling the &#x60;webhooks.on_channel_add.url&#x60;.
    :type webhooks_on_channel_add_method: str
    :param webhooks_on_channel_add_url: The URL of the webhook to call in response to the &#x60;on_channel_add&#x60; event using the &#x60;webhooks.on_channel_add.method&#x60; HTTP method.
    :type webhooks_on_channel_add_url: str
    :param webhooks_on_channel_added_method: The URL of the webhook to call in response to the &#x60;on_channel_added&#x60; event&#x60;.
    :type webhooks_on_channel_added_method: str
    :param webhooks_on_channel_added_url: The URL of the webhook to call in response to the &#x60;on_channel_added&#x60; event using the &#x60;webhooks.on_channel_added.method&#x60; HTTP method.
    :type webhooks_on_channel_added_url: str
    :param webhooks_on_channel_destroy_method: The HTTP method to use when calling the &#x60;webhooks.on_channel_destroy.url&#x60;.
    :type webhooks_on_channel_destroy_method: str
    :param webhooks_on_channel_destroy_url: The URL of the webhook to call in response to the &#x60;on_channel_destroy&#x60; event using the &#x60;webhooks.on_channel_destroy.method&#x60; HTTP method.
    :type webhooks_on_channel_destroy_url: str
    :param webhooks_on_channel_destroyed_method: The HTTP method to use when calling the &#x60;webhooks.on_channel_destroyed.url&#x60;.
    :type webhooks_on_channel_destroyed_method: str
    :param webhooks_on_channel_destroyed_url: The URL of the webhook to call in response to the &#x60;on_channel_added&#x60; event using the &#x60;webhooks.on_channel_destroyed.method&#x60; HTTP method.
    :type webhooks_on_channel_destroyed_url: str
    :param webhooks_on_channel_update_method: The HTTP method to use when calling the &#x60;webhooks.on_channel_update.url&#x60;.
    :type webhooks_on_channel_update_method: str
    :param webhooks_on_channel_update_url: The URL of the webhook to call in response to the &#x60;on_channel_update&#x60; event using the &#x60;webhooks.on_channel_update.method&#x60; HTTP method.
    :type webhooks_on_channel_update_url: str
    :param webhooks_on_channel_updated_method: The HTTP method to use when calling the &#x60;webhooks.on_channel_updated.url&#x60;.
    :type webhooks_on_channel_updated_method: str
    :param webhooks_on_channel_updated_url: The URL of the webhook to call in response to the &#x60;on_channel_updated&#x60; event using the &#x60;webhooks.on_channel_updated.method&#x60; HTTP method.
    :type webhooks_on_channel_updated_url: str
    :param webhooks_on_member_add_method: The HTTP method to use when calling the &#x60;webhooks.on_member_add.url&#x60;.
    :type webhooks_on_member_add_method: str
    :param webhooks_on_member_add_url: The URL of the webhook to call in response to the &#x60;on_member_add&#x60; event using the &#x60;webhooks.on_member_add.method&#x60; HTTP method.
    :type webhooks_on_member_add_url: str
    :param webhooks_on_member_added_method: The HTTP method to use when calling the &#x60;webhooks.on_channel_updated.url&#x60;.
    :type webhooks_on_member_added_method: str
    :param webhooks_on_member_added_url: The URL of the webhook to call in response to the &#x60;on_channel_updated&#x60; event using the &#x60;webhooks.on_channel_updated.method&#x60; HTTP method.
    :type webhooks_on_member_added_url: str
    :param webhooks_on_member_remove_method: The HTTP method to use when calling the &#x60;webhooks.on_member_remove.url&#x60;.
    :type webhooks_on_member_remove_method: str
    :param webhooks_on_member_remove_url: The URL of the webhook to call in response to the &#x60;on_member_remove&#x60; event using the &#x60;webhooks.on_member_remove.method&#x60; HTTP method.
    :type webhooks_on_member_remove_url: str
    :param webhooks_on_member_removed_method: The HTTP method to use when calling the &#x60;webhooks.on_member_removed.url&#x60;.
    :type webhooks_on_member_removed_method: str
    :param webhooks_on_member_removed_url: The URL of the webhook to call in response to the &#x60;on_member_removed&#x60; event using the &#x60;webhooks.on_member_removed.method&#x60; HTTP method.
    :type webhooks_on_member_removed_url: str
    :param webhooks_on_message_remove_method: The HTTP method to use when calling the &#x60;webhooks.on_message_remove.url&#x60;.
    :type webhooks_on_message_remove_method: str
    :param webhooks_on_message_remove_url: The URL of the webhook to call in response to the &#x60;on_message_remove&#x60; event using the &#x60;webhooks.on_message_remove.method&#x60; HTTP method.
    :type webhooks_on_message_remove_url: str
    :param webhooks_on_message_removed_method: The HTTP method to use when calling the &#x60;webhooks.on_message_removed.url&#x60;.
    :type webhooks_on_message_removed_method: str
    :param webhooks_on_message_removed_url: The URL of the webhook to call in response to the &#x60;on_message_removed&#x60; event using the &#x60;webhooks.on_message_removed.method&#x60; HTTP method.
    :type webhooks_on_message_removed_url: str
    :param webhooks_on_message_send_method: The HTTP method to use when calling the &#x60;webhooks.on_message_send.url&#x60;.
    :type webhooks_on_message_send_method: str
    :param webhooks_on_message_send_url: The URL of the webhook to call in response to the &#x60;on_message_send&#x60; event using the &#x60;webhooks.on_message_send.method&#x60; HTTP method.
    :type webhooks_on_message_send_url: str
    :param webhooks_on_message_sent_method: The URL of the webhook to call in response to the &#x60;on_message_sent&#x60; event&#x60;.
    :type webhooks_on_message_sent_method: str
    :param webhooks_on_message_sent_url: The URL of the webhook to call in response to the &#x60;on_message_sent&#x60; event using the &#x60;webhooks.on_message_sent.method&#x60; HTTP method.
    :type webhooks_on_message_sent_url: str
    :param webhooks_on_message_update_method: The HTTP method to use when calling the &#x60;webhooks.on_message_update.url&#x60;.
    :type webhooks_on_message_update_method: str
    :param webhooks_on_message_update_url: The URL of the webhook to call in response to the &#x60;on_message_update&#x60; event using the &#x60;webhooks.on_message_update.method&#x60; HTTP method.
    :type webhooks_on_message_update_url: str
    :param webhooks_on_message_updated_method: The HTTP method to use when calling the &#x60;webhooks.on_message_updated.url&#x60;.
    :type webhooks_on_message_updated_method: str
    :param webhooks_on_message_updated_url: The URL of the webhook to call in response to the &#x60;on_message_updated&#x60; event using the &#x60;webhooks.on_message_updated.method&#x60; HTTP method.
    :type webhooks_on_message_updated_url: str

    """
    return web.Response(status=200)
