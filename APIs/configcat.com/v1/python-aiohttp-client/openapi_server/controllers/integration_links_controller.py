from typing import List, Dict
from aiohttp import web

from openapi_server.models.add_or_update_integration_link_model import AddOrUpdateIntegrationLinkModel
from openapi_server.models.add_or_update_jira_integration_link_model import AddOrUpdateJiraIntegrationLinkModel
from openapi_server.models.connect_request import ConnectRequest
from openapi_server.models.delete_integration_link_model import DeleteIntegrationLinkModel
from openapi_server.models.integration_link_details_model import IntegrationLinkDetailsModel
from openapi_server.models.integration_link_model import IntegrationLinkModel
from openapi_server.models.integration_link_type import IntegrationLinkType
from openapi_server import util


async def add_or_update_integration_link(request: web.Request, environment_id, setting_id, integration_link_type, key, body=None) -> web.Response:
    """Add or update Integration link

    

    :param environment_id: The identifier of the Environment.
    :type environment_id: str
    :type environment_id: str
    :param setting_id: The id of the Setting.
    :type setting_id: int
    :param integration_link_type: The integration link&#39;s type.
    :type integration_link_type: dict | bytes
    :param key: The key of the integration link.
    :type key: str
    :param body: 
    :type body: dict | bytes

    """
    integration_link_type = .from_dict(integration_link_type)
    body = AddOrUpdateIntegrationLinkModel.from_dict(body)
    return web.Response(status=200)


async def delete_integration_link(request: web.Request, environment_id, setting_id, integration_link_type, key) -> web.Response:
    """Delete Integration link

    

    :param environment_id: The identifier of the Environment.
    :type environment_id: str
    :type environment_id: str
    :param setting_id: The id of the Setting.
    :type setting_id: int
    :param integration_link_type: The integration&#39;s type.
    :type integration_link_type: dict | bytes
    :param key: The key of the integration link.
    :type key: str

    """
    integration_link_type = .from_dict(integration_link_type)
    return web.Response(status=200)


async def get_integration_link_details(request: web.Request, integration_link_type, key) -> web.Response:
    """Get Integration link

    

    :param integration_link_type: The integration link&#39;s type.
    :type integration_link_type: dict | bytes
    :param key: The key of the integration link.
    :type key: str

    """
    integration_link_type = .from_dict(integration_link_type)
    return web.Response(status=200)


async def jira_add_or_update_integration_link(request: web.Request, environment_id, setting_id, key, body=None) -> web.Response:
    """jira_add_or_update_integration_link

    

    :param environment_id: The identifier of the Environment.
    :type environment_id: str
    :type environment_id: str
    :param setting_id: The id of the Setting.
    :type setting_id: int
    :param key: The key of the integration link.
    :type key: str
    :param body: 
    :type body: dict | bytes

    """
    body = AddOrUpdateJiraIntegrationLinkModel.from_dict(body)
    return web.Response(status=200)


async def v1_jira_connect_post(request: web.Request, body=None) -> web.Response:
    """v1_jira_connect_post

    

    :param body: 
    :type body: dict | bytes

    """
    body = ConnectRequest.from_dict(body)
    return web.Response(status=200)
