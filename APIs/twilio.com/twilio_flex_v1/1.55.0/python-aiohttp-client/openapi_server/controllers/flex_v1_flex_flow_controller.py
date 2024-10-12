from typing import List, Dict
from aiohttp import web

from openapi_server.models.flex_flow_enum_channel_type import FlexFlowEnumChannelType
from openapi_server.models.flex_flow_enum_integration_type import FlexFlowEnumIntegrationType
from openapi_server.models.flex_v1_flex_flow import FlexV1FlexFlow
from openapi_server.models.list_flex_flow_response import ListFlexFlowResponse
from openapi_server import util


async def create_flex_flow(request: web.Request, channel_type, chat_service_sid, friendly_name, contact_identity=None, enabled=None, integration_channel=None, integration_creation_on_message=None, integration_flow_sid=None, integration_priority=None, integration_retry_count=None, integration_timeout=None, integration_url=None, integration_workflow_sid=None, integration_workspace_sid=None, integration_type=None, janitor_enabled=None, long_lived=None) -> web.Response:
    """create_flex_flow

    

    :param channel_type: 
    :type channel_type: str
    :param chat_service_sid: The SID of the chat service.
    :type chat_service_sid: str
    :param friendly_name: A descriptive string that you create to describe the Flex Flow resource.
    :type friendly_name: str
    :param contact_identity: The channel contact&#39;s Identity.
    :type contact_identity: str
    :param enabled: Whether the new Flex Flow is enabled.
    :type enabled: bool
    :param integration_channel: The Task Channel SID (TCXXXX) or unique name (e.g., &#x60;sms&#x60;) to use for the Task that will be created. Applicable and required when &#x60;integrationType&#x60; is &#x60;task&#x60;. The default value is &#x60;default&#x60;.
    :type integration_channel: str
    :param integration_creation_on_message: In the context of outbound messaging, defines whether to create a Task immediately (and therefore reserve the conversation to current agent), or delay Task creation until the customer sends the first response. Set to false to create immediately, true to delay Task creation. This setting is only applicable for outbound messaging.
    :type integration_creation_on_message: bool
    :param integration_flow_sid: The SID of the Studio Flow. Required when &#x60;integrationType&#x60; is &#x60;studio&#x60;.
    :type integration_flow_sid: str
    :param integration_priority: The Task priority of a new Task. The default priority is 0. Optional when &#x60;integrationType&#x60; is &#x60;task&#x60;, not applicable otherwise.
    :type integration_priority: int
    :param integration_retry_count: The number of times to retry the Studio Flow or webhook in case of failure. Takes integer values from 0 to 3 with the default being 3. Optional when &#x60;integrationType&#x60; is &#x60;studio&#x60; or &#x60;external&#x60;, not applicable otherwise.
    :type integration_retry_count: int
    :param integration_timeout: The Task timeout in seconds for a new Task. Default is 86,400 seconds (24 hours). Optional when &#x60;integrationType&#x60; is &#x60;task&#x60;, not applicable otherwise.
    :type integration_timeout: int
    :param integration_url: The URL of the external webhook. Required when &#x60;integrationType&#x60; is &#x60;external&#x60;.
    :type integration_url: str
    :param integration_workflow_sid: The Workflow SID for a new Task. Required when &#x60;integrationType&#x60; is &#x60;task&#x60;.
    :type integration_workflow_sid: str
    :param integration_workspace_sid: The Workspace SID for a new Task. Required when &#x60;integrationType&#x60; is &#x60;task&#x60;.
    :type integration_workspace_sid: str
    :param integration_type: 
    :type integration_type: str
    :param janitor_enabled: When enabled, the Messaging Channel Janitor will remove active Proxy sessions if the associated Task is deleted outside of the Flex UI. Defaults to &#x60;false&#x60;.
    :type janitor_enabled: bool
    :param long_lived: When enabled, Flex will keep the chat channel active so that it may be used for subsequent interactions with a contact identity. Defaults to &#x60;false&#x60;.
    :type long_lived: bool

    """
    return web.Response(status=200)


async def delete_flex_flow(request: web.Request, sid) -> web.Response:
    """delete_flex_flow

    

    :param sid: The SID of the Flex Flow resource to delete.
    :type sid: str

    """
    return web.Response(status=200)


async def fetch_flex_flow(request: web.Request, sid) -> web.Response:
    """fetch_flex_flow

    

    :param sid: The SID of the Flex Flow resource to fetch.
    :type sid: str

    """
    return web.Response(status=200)


async def list_flex_flow(request: web.Request, friendly_name=None, page_size=None, page=None, page_token=None) -> web.Response:
    """list_flex_flow

    

    :param friendly_name: The &#x60;friendly_name&#x60; of the Flex Flow resources to read.
    :type friendly_name: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)


async def update_flex_flow(request: web.Request, sid, channel_type=None, chat_service_sid=None, contact_identity=None, enabled=None, friendly_name=None, integration_channel=None, integration_creation_on_message=None, integration_flow_sid=None, integration_priority=None, integration_retry_count=None, integration_timeout=None, integration_url=None, integration_workflow_sid=None, integration_workspace_sid=None, integration_type=None, janitor_enabled=None, long_lived=None) -> web.Response:
    """update_flex_flow

    

    :param sid: The SID of the Flex Flow resource to update.
    :type sid: str
    :param channel_type: 
    :type channel_type: str
    :param chat_service_sid: The SID of the chat service.
    :type chat_service_sid: str
    :param contact_identity: The channel contact&#39;s Identity.
    :type contact_identity: str
    :param enabled: Whether the new Flex Flow is enabled.
    :type enabled: bool
    :param friendly_name: A descriptive string that you create to describe the Flex Flow resource.
    :type friendly_name: str
    :param integration_channel: The Task Channel SID (TCXXXX) or unique name (e.g., &#x60;sms&#x60;) to use for the Task that will be created. Applicable and required when &#x60;integrationType&#x60; is &#x60;task&#x60;. The default value is &#x60;default&#x60;.
    :type integration_channel: str
    :param integration_creation_on_message: In the context of outbound messaging, defines whether to create a Task immediately (and therefore reserve the conversation to current agent), or delay Task creation until the customer sends the first response. Set to false to create immediately, true to delay Task creation. This setting is only applicable for outbound messaging.
    :type integration_creation_on_message: bool
    :param integration_flow_sid: The SID of the Studio Flow. Required when &#x60;integrationType&#x60; is &#x60;studio&#x60;.
    :type integration_flow_sid: str
    :param integration_priority: The Task priority of a new Task. The default priority is 0. Optional when &#x60;integrationType&#x60; is &#x60;task&#x60;, not applicable otherwise.
    :type integration_priority: int
    :param integration_retry_count: The number of times to retry the Studio Flow or webhook in case of failure. Takes integer values from 0 to 3 with the default being 3. Optional when &#x60;integrationType&#x60; is &#x60;studio&#x60; or &#x60;external&#x60;, not applicable otherwise.
    :type integration_retry_count: int
    :param integration_timeout: The Task timeout in seconds for a new Task. Default is 86,400 seconds (24 hours). Optional when &#x60;integrationType&#x60; is &#x60;task&#x60;, not applicable otherwise.
    :type integration_timeout: int
    :param integration_url: The URL of the external webhook. Required when &#x60;integrationType&#x60; is &#x60;external&#x60;.
    :type integration_url: str
    :param integration_workflow_sid: The Workflow SID for a new Task. Required when &#x60;integrationType&#x60; is &#x60;task&#x60;.
    :type integration_workflow_sid: str
    :param integration_workspace_sid: The Workspace SID for a new Task. Required when &#x60;integrationType&#x60; is &#x60;task&#x60;.
    :type integration_workspace_sid: str
    :param integration_type: 
    :type integration_type: str
    :param janitor_enabled: When enabled, the Messaging Channel Janitor will remove active Proxy sessions if the associated Task is deleted outside of the Flex UI. Defaults to &#x60;false&#x60;.
    :type janitor_enabled: bool
    :param long_lived: When enabled, Flex will keep the chat channel active so that it may be used for subsequent interactions with a contact identity. Defaults to &#x60;false&#x60;.
    :type long_lived: bool

    """
    return web.Response(status=200)
