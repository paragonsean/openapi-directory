from typing import List, Dict
from aiohttp import web

from openapi_server.models.configuration_address_enum_auto_creation_type import ConfigurationAddressEnumAutoCreationType
from openapi_server.models.configuration_address_enum_method import ConfigurationAddressEnumMethod
from openapi_server.models.configuration_address_enum_type import ConfigurationAddressEnumType
from openapi_server.models.conversations_v1_configuration_address import ConversationsV1ConfigurationAddress
from openapi_server.models.list_configuration_address_response import ListConfigurationAddressResponse
from openapi_server import util


async def create_configuration_address(request: web.Request, address, type, address_country=None, auto_creation_conversation_service_sid=None, auto_creation_enabled=None, auto_creation_studio_flow_sid=None, auto_creation_studio_retry_count=None, auto_creation_type=None, auto_creation_webhook_filters=None, auto_creation_webhook_method=None, auto_creation_webhook_url=None, friendly_name=None) -> web.Response:
    """create_configuration_address

    Create a new address configuration

    :param address: The unique address to be configured. The address can be a whatsapp address or phone number
    :type address: str
    :param type: 
    :type type: str
    :param address_country: An ISO 3166-1 alpha-2n country code which the address belongs to. This is currently only applicable to short code addresses.
    :type address_country: str
    :param auto_creation_conversation_service_sid: Conversation Service for the auto-created conversation. If not set, the conversation is created in the default service.
    :type auto_creation_conversation_service_sid: str
    :param auto_creation_enabled: Enable/Disable auto-creating conversations for messages to this address
    :type auto_creation_enabled: bool
    :param auto_creation_studio_flow_sid: For type &#x60;studio&#x60;, the studio flow SID where the webhook should be sent to.
    :type auto_creation_studio_flow_sid: str
    :param auto_creation_studio_retry_count: For type &#x60;studio&#x60;, number of times to retry the webhook request
    :type auto_creation_studio_retry_count: int
    :param auto_creation_type: 
    :type auto_creation_type: str
    :param auto_creation_webhook_filters: The list of events, firing webhook event for this Conversation. Values can be any of the following: &#x60;onMessageAdded&#x60;, &#x60;onMessageUpdated&#x60;, &#x60;onMessageRemoved&#x60;, &#x60;onConversationUpdated&#x60;, &#x60;onConversationStateUpdated&#x60;, &#x60;onConversationRemoved&#x60;, &#x60;onParticipantAdded&#x60;, &#x60;onParticipantUpdated&#x60;, &#x60;onParticipantRemoved&#x60;, &#x60;onDeliveryUpdated&#x60;
    :type auto_creation_webhook_filters: List[str]
    :param auto_creation_webhook_method: 
    :type auto_creation_webhook_method: str
    :param auto_creation_webhook_url: For type &#x60;webhook&#x60;, the url for the webhook request.
    :type auto_creation_webhook_url: str
    :param friendly_name: The human-readable name of this configuration, limited to 256 characters. Optional.
    :type friendly_name: str

    """
    return web.Response(status=200)


async def delete_configuration_address(request: web.Request, sid) -> web.Response:
    """delete_configuration_address

    Remove an existing address configuration

    :param sid: The SID of the Address Configuration resource. This value can be either the &#x60;sid&#x60; or the &#x60;address&#x60; of the configuration
    :type sid: str

    """
    return web.Response(status=200)


async def fetch_configuration_address(request: web.Request, sid) -> web.Response:
    """fetch_configuration_address

    Fetch an address configuration 

    :param sid: The SID of the Address Configuration resource. This value can be either the &#x60;sid&#x60; or the &#x60;address&#x60; of the configuration
    :type sid: str

    """
    return web.Response(status=200)


async def list_configuration_address(request: web.Request, type=None, page_size=None, page=None, page_token=None) -> web.Response:
    """list_configuration_address

    Retrieve a list of address configurations for an account

    :param type: Filter the address configurations by its type. This value can be one of: &#x60;whatsapp&#x60;, &#x60;sms&#x60;.
    :type type: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)


async def update_configuration_address(request: web.Request, sid, auto_creation_conversation_service_sid=None, auto_creation_enabled=None, auto_creation_studio_flow_sid=None, auto_creation_studio_retry_count=None, auto_creation_type=None, auto_creation_webhook_filters=None, auto_creation_webhook_method=None, auto_creation_webhook_url=None, friendly_name=None) -> web.Response:
    """update_configuration_address

    Update an existing address configuration

    :param sid: The SID of the Address Configuration resource. This value can be either the &#x60;sid&#x60; or the &#x60;address&#x60; of the configuration
    :type sid: str
    :param auto_creation_conversation_service_sid: Conversation Service for the auto-created conversation. If not set, the conversation is created in the default service.
    :type auto_creation_conversation_service_sid: str
    :param auto_creation_enabled: Enable/Disable auto-creating conversations for messages to this address
    :type auto_creation_enabled: bool
    :param auto_creation_studio_flow_sid: For type &#x60;studio&#x60;, the studio flow SID where the webhook should be sent to.
    :type auto_creation_studio_flow_sid: str
    :param auto_creation_studio_retry_count: For type &#x60;studio&#x60;, number of times to retry the webhook request
    :type auto_creation_studio_retry_count: int
    :param auto_creation_type: 
    :type auto_creation_type: str
    :param auto_creation_webhook_filters: The list of events, firing webhook event for this Conversation. Values can be any of the following: &#x60;onMessageAdded&#x60;, &#x60;onMessageUpdated&#x60;, &#x60;onMessageRemoved&#x60;, &#x60;onConversationUpdated&#x60;, &#x60;onConversationStateUpdated&#x60;, &#x60;onConversationRemoved&#x60;, &#x60;onParticipantAdded&#x60;, &#x60;onParticipantUpdated&#x60;, &#x60;onParticipantRemoved&#x60;, &#x60;onDeliveryUpdated&#x60;
    :type auto_creation_webhook_filters: List[str]
    :param auto_creation_webhook_method: 
    :type auto_creation_webhook_method: str
    :param auto_creation_webhook_url: For type &#x60;webhook&#x60;, the url for the webhook request.
    :type auto_creation_webhook_url: str
    :param friendly_name: The human-readable name of this configuration, limited to 256 characters. Optional.
    :type friendly_name: str

    """
    return web.Response(status=200)
