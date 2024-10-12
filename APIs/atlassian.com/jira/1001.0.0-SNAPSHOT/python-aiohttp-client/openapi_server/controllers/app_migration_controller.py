from typing import List, Dict
from aiohttp import web

from openapi_server.models.connect_custom_field_values import ConnectCustomFieldValues
from openapi_server.models.entity_property_details import EntityPropertyDetails
from openapi_server.models.workflow_rules_search import WorkflowRulesSearch
from openapi_server.models.workflow_rules_search_details import WorkflowRulesSearchDetails
from openapi_server import util


async def app_issue_field_value_update_resource_update_issue_fields_put(request: web.Request, atlassian_transfer_id, body) -> web.Response:
    """Bulk update custom field value

    Updates the value of a custom field added by Connect apps on one or more issues. The values of up to 200 custom fields can be updated.  **[Permissions](#permissions) required:** Only Connect apps can make this request.

    :param atlassian_transfer_id: The ID of the transfer.
    :type atlassian_transfer_id: str
    :type atlassian_transfer_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = ConnectCustomFieldValues.from_dict(body)
    return web.Response(status=200)


async def migration_resource_update_entity_properties_value_put(request: web.Request, atlassian_transfer_id, entity_type, body) -> web.Response:
    """Bulk update entity properties

    Updates the values of multiple entity properties for an object, up to 50 updates per request. This operation is for use by Connect apps during app migration.

    :param atlassian_transfer_id: The app migration transfer ID.
    :type atlassian_transfer_id: str
    :type atlassian_transfer_id: str
    :param entity_type: The type indicating the object that contains the entity properties.
    :type entity_type: str
    :param body: 
    :type body: list | bytes

    """
    body = [EntityPropertyDetails.from_dict(d) for d in body]
    return web.Response(status=200)


async def migration_resource_workflow_rule_search_post(request: web.Request, atlassian_transfer_id, body) -> web.Response:
    """Get workflow transition rule configurations

    Returns configurations for workflow transition rules migrated from server to cloud and owned by the calling Connect app.

    :param atlassian_transfer_id: The app migration transfer ID.
    :type atlassian_transfer_id: str
    :type atlassian_transfer_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = WorkflowRulesSearch.from_dict(body)
    return web.Response(status=200)
