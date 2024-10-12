from typing import List, Dict
from aiohttp import web

from openapi_server.models.ip_messaging_v1_service import IpMessagingV1Service
from openapi_server.models.list_service_response import ListServiceResponse
from openapi_server import util


async def create_service(request: web.Request, friendly_name) -> web.Response:
    """create_service

    

    :param friendly_name: 
    :type friendly_name: str

    """
    return web.Response(status=200)


async def delete_service(request: web.Request, sid) -> web.Response:
    """delete_service

    

    :param sid: 
    :type sid: str

    """
    return web.Response(status=200)


async def fetch_service(request: web.Request, sid) -> web.Response:
    """fetch_service

    

    :param sid: 
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

    

    :param sid: 
    :type sid: str
    :param consumption_report_interval: 
    :type consumption_report_interval: int
    :param default_channel_creator_role_sid: 
    :type default_channel_creator_role_sid: str
    :param default_channel_role_sid: 
    :type default_channel_role_sid: str
    :param default_service_role_sid: 
    :type default_service_role_sid: str
    :param friendly_name: 
    :type friendly_name: str
    :param limits_channel_members: 
    :type limits_channel_members: int
    :param limits_user_channels: 
    :type limits_user_channels: int
    :param notifications_added_to_channel_enabled: 
    :type notifications_added_to_channel_enabled: bool
    :param notifications_added_to_channel_template: 
    :type notifications_added_to_channel_template: str
    :param notifications_invited_to_channel_enabled: 
    :type notifications_invited_to_channel_enabled: bool
    :param notifications_invited_to_channel_template: 
    :type notifications_invited_to_channel_template: str
    :param notifications_new_message_enabled: 
    :type notifications_new_message_enabled: bool
    :param notifications_new_message_template: 
    :type notifications_new_message_template: str
    :param notifications_removed_from_channel_enabled: 
    :type notifications_removed_from_channel_enabled: bool
    :param notifications_removed_from_channel_template: 
    :type notifications_removed_from_channel_template: str
    :param post_webhook_url: 
    :type post_webhook_url: str
    :param pre_webhook_url: 
    :type pre_webhook_url: str
    :param reachability_enabled: 
    :type reachability_enabled: bool
    :param read_status_enabled: 
    :type read_status_enabled: bool
    :param typing_indicator_timeout: 
    :type typing_indicator_timeout: int
    :param webhook_filters: 
    :type webhook_filters: List[str]
    :param webhook_method: 
    :type webhook_method: str
    :param webhooks_on_channel_add_method: 
    :type webhooks_on_channel_add_method: str
    :param webhooks_on_channel_add_url: 
    :type webhooks_on_channel_add_url: str
    :param webhooks_on_channel_added_method: 
    :type webhooks_on_channel_added_method: str
    :param webhooks_on_channel_added_url: 
    :type webhooks_on_channel_added_url: str
    :param webhooks_on_channel_destroy_method: 
    :type webhooks_on_channel_destroy_method: str
    :param webhooks_on_channel_destroy_url: 
    :type webhooks_on_channel_destroy_url: str
    :param webhooks_on_channel_destroyed_method: 
    :type webhooks_on_channel_destroyed_method: str
    :param webhooks_on_channel_destroyed_url: 
    :type webhooks_on_channel_destroyed_url: str
    :param webhooks_on_channel_update_method: 
    :type webhooks_on_channel_update_method: str
    :param webhooks_on_channel_update_url: 
    :type webhooks_on_channel_update_url: str
    :param webhooks_on_channel_updated_method: 
    :type webhooks_on_channel_updated_method: str
    :param webhooks_on_channel_updated_url: 
    :type webhooks_on_channel_updated_url: str
    :param webhooks_on_member_add_method: 
    :type webhooks_on_member_add_method: str
    :param webhooks_on_member_add_url: 
    :type webhooks_on_member_add_url: str
    :param webhooks_on_member_added_method: 
    :type webhooks_on_member_added_method: str
    :param webhooks_on_member_added_url: 
    :type webhooks_on_member_added_url: str
    :param webhooks_on_member_remove_method: 
    :type webhooks_on_member_remove_method: str
    :param webhooks_on_member_remove_url: 
    :type webhooks_on_member_remove_url: str
    :param webhooks_on_member_removed_method: 
    :type webhooks_on_member_removed_method: str
    :param webhooks_on_member_removed_url: 
    :type webhooks_on_member_removed_url: str
    :param webhooks_on_message_remove_method: 
    :type webhooks_on_message_remove_method: str
    :param webhooks_on_message_remove_url: 
    :type webhooks_on_message_remove_url: str
    :param webhooks_on_message_removed_method: 
    :type webhooks_on_message_removed_method: str
    :param webhooks_on_message_removed_url: 
    :type webhooks_on_message_removed_url: str
    :param webhooks_on_message_send_method: 
    :type webhooks_on_message_send_method: str
    :param webhooks_on_message_send_url: 
    :type webhooks_on_message_send_url: str
    :param webhooks_on_message_sent_method: 
    :type webhooks_on_message_sent_method: str
    :param webhooks_on_message_sent_url: 
    :type webhooks_on_message_sent_url: str
    :param webhooks_on_message_update_method: 
    :type webhooks_on_message_update_method: str
    :param webhooks_on_message_update_url: 
    :type webhooks_on_message_update_url: str
    :param webhooks_on_message_updated_method: 
    :type webhooks_on_message_updated_method: str
    :param webhooks_on_message_updated_url: 
    :type webhooks_on_message_updated_url: str

    """
    return web.Response(status=200)
