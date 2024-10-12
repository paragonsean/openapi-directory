from typing import List, Dict
from aiohttp import web

from openapi_server.models.config_context import ConfigContext
from openapi_server.models.export_template import ExportTemplate
from openapi_server.models.extras_config_contexts_list200_response import ExtrasConfigContextsList200Response
from openapi_server.models.extras_export_templates_list200_response import ExtrasExportTemplatesList200Response
from openapi_server.models.extras_graphs_list200_response import ExtrasGraphsList200Response
from openapi_server.models.extras_image_attachments_list200_response import ExtrasImageAttachmentsList200Response
from openapi_server.models.extras_object_changes_list200_response import ExtrasObjectChangesList200Response
from openapi_server.models.extras_recent_activity_list200_response import ExtrasRecentActivityList200Response
from openapi_server.models.extras_tags_list200_response import ExtrasTagsList200Response
from openapi_server.models.extras_topology_maps_list200_response import ExtrasTopologyMapsList200Response
from openapi_server.models.graph import Graph
from openapi_server.models.image_attachment import ImageAttachment
from openapi_server.models.object_change import ObjectChange
from openapi_server.models.tag import Tag
from openapi_server.models.topology_map import TopologyMap
from openapi_server.models.user_action import UserAction
from openapi_server.models.writable_config_context import WritableConfigContext
from openapi_server.models.writable_graph import WritableGraph
from openapi_server.models.writable_topology_map import WritableTopologyMap
from openapi_server import util


async def extras_choices_list(request: web.Request, ) -> web.Response:
    """extras_choices_list

    


    """
    return web.Response(status=200)


async def extras_choices_read(request: web.Request, id) -> web.Response:
    """extras_choices_read

    

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def extras_config_contexts_create(request: web.Request, body) -> web.Response:
    """extras_config_contexts_create

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableConfigContext.from_dict(body)
    return web.Response(status=200)


async def extras_config_contexts_delete(request: web.Request, id) -> web.Response:
    """extras_config_contexts_delete

    

    :param id: A unique integer value identifying this config context.
    :type id: int

    """
    return web.Response(status=200)


async def extras_config_contexts_list(request: web.Request, name=None, is_active=None, q=None, region_id=None, region=None, site_id=None, site=None, role_id=None, role=None, platform_id=None, platform=None, tenant_group_id=None, tenant_group=None, tenant_id=None, tenant=None, limit=None, offset=None) -> web.Response:
    """extras_config_contexts_list

    

    :param name: 
    :type name: str
    :param is_active: 
    :type is_active: str
    :param q: 
    :type q: str
    :param region_id: 
    :type region_id: str
    :param region: 
    :type region: str
    :param site_id: 
    :type site_id: str
    :param site: 
    :type site: str
    :param role_id: 
    :type role_id: str
    :param role: 
    :type role: str
    :param platform_id: 
    :type platform_id: str
    :param platform: 
    :type platform: str
    :param tenant_group_id: 
    :type tenant_group_id: str
    :param tenant_group: 
    :type tenant_group: str
    :param tenant_id: 
    :type tenant_id: str
    :param tenant: 
    :type tenant: str
    :param limit: Number of results to return per page.
    :type limit: int
    :param offset: The initial index from which to return the results.
    :type offset: int

    """
    return web.Response(status=200)


async def extras_config_contexts_partial_update(request: web.Request, id, body) -> web.Response:
    """extras_config_contexts_partial_update

    

    :param id: A unique integer value identifying this config context.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = WritableConfigContext.from_dict(body)
    return web.Response(status=200)


async def extras_config_contexts_read(request: web.Request, id) -> web.Response:
    """extras_config_contexts_read

    

    :param id: A unique integer value identifying this config context.
    :type id: int

    """
    return web.Response(status=200)


async def extras_config_contexts_update(request: web.Request, id, body) -> web.Response:
    """extras_config_contexts_update

    

    :param id: A unique integer value identifying this config context.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = WritableConfigContext.from_dict(body)
    return web.Response(status=200)


async def extras_export_templates_create(request: web.Request, body) -> web.Response:
    """extras_export_templates_create

    

    :param body: 
    :type body: dict | bytes

    """
    body = ExportTemplate.from_dict(body)
    return web.Response(status=200)


async def extras_export_templates_delete(request: web.Request, id) -> web.Response:
    """extras_export_templates_delete

    

    :param id: A unique integer value identifying this export template.
    :type id: int

    """
    return web.Response(status=200)


async def extras_export_templates_list(request: web.Request, content_type=None, name=None, limit=None, offset=None) -> web.Response:
    """extras_export_templates_list

    

    :param content_type: 
    :type content_type: str
    :param name: 
    :type name: str
    :param limit: Number of results to return per page.
    :type limit: int
    :param offset: The initial index from which to return the results.
    :type offset: int

    """
    return web.Response(status=200)


async def extras_export_templates_partial_update(request: web.Request, id, body) -> web.Response:
    """extras_export_templates_partial_update

    

    :param id: A unique integer value identifying this export template.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = ExportTemplate.from_dict(body)
    return web.Response(status=200)


async def extras_export_templates_read(request: web.Request, id) -> web.Response:
    """extras_export_templates_read

    

    :param id: A unique integer value identifying this export template.
    :type id: int

    """
    return web.Response(status=200)


async def extras_export_templates_update(request: web.Request, id, body) -> web.Response:
    """extras_export_templates_update

    

    :param id: A unique integer value identifying this export template.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = ExportTemplate.from_dict(body)
    return web.Response(status=200)


async def extras_graphs_create(request: web.Request, body) -> web.Response:
    """extras_graphs_create

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableGraph.from_dict(body)
    return web.Response(status=200)


async def extras_graphs_delete(request: web.Request, id) -> web.Response:
    """extras_graphs_delete

    

    :param id: A unique integer value identifying this graph.
    :type id: int

    """
    return web.Response(status=200)


async def extras_graphs_list(request: web.Request, type=None, name=None, limit=None, offset=None) -> web.Response:
    """extras_graphs_list

    

    :param type: 
    :type type: str
    :param name: 
    :type name: str
    :param limit: Number of results to return per page.
    :type limit: int
    :param offset: The initial index from which to return the results.
    :type offset: int

    """
    return web.Response(status=200)


async def extras_graphs_partial_update(request: web.Request, id, body) -> web.Response:
    """extras_graphs_partial_update

    

    :param id: A unique integer value identifying this graph.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = WritableGraph.from_dict(body)
    return web.Response(status=200)


async def extras_graphs_read(request: web.Request, id) -> web.Response:
    """extras_graphs_read

    

    :param id: A unique integer value identifying this graph.
    :type id: int

    """
    return web.Response(status=200)


async def extras_graphs_update(request: web.Request, id, body) -> web.Response:
    """extras_graphs_update

    

    :param id: A unique integer value identifying this graph.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = WritableGraph.from_dict(body)
    return web.Response(status=200)


async def extras_image_attachments_create(request: web.Request, body) -> web.Response:
    """extras_image_attachments_create

    

    :param body: 
    :type body: dict | bytes

    """
    body = ImageAttachment.from_dict(body)
    return web.Response(status=200)


async def extras_image_attachments_delete(request: web.Request, id) -> web.Response:
    """extras_image_attachments_delete

    

    :param id: A unique integer value identifying this image attachment.
    :type id: int

    """
    return web.Response(status=200)


async def extras_image_attachments_list(request: web.Request, limit=None, offset=None) -> web.Response:
    """extras_image_attachments_list

    

    :param limit: Number of results to return per page.
    :type limit: int
    :param offset: The initial index from which to return the results.
    :type offset: int

    """
    return web.Response(status=200)


async def extras_image_attachments_partial_update(request: web.Request, id, body) -> web.Response:
    """extras_image_attachments_partial_update

    

    :param id: A unique integer value identifying this image attachment.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = ImageAttachment.from_dict(body)
    return web.Response(status=200)


async def extras_image_attachments_read(request: web.Request, id) -> web.Response:
    """extras_image_attachments_read

    

    :param id: A unique integer value identifying this image attachment.
    :type id: int

    """
    return web.Response(status=200)


async def extras_image_attachments_update(request: web.Request, id, body) -> web.Response:
    """extras_image_attachments_update

    

    :param id: A unique integer value identifying this image attachment.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = ImageAttachment.from_dict(body)
    return web.Response(status=200)


async def extras_object_changes_list(request: web.Request, user=None, user_name=None, request_id=None, action=None, changed_object_type=None, object_repr=None, q=None, time=None, limit=None, offset=None) -> web.Response:
    """extras_object_changes_list

    Retrieve a list of recent changes.

    :param user: 
    :type user: str
    :param user_name: 
    :type user_name: str
    :param request_id: 
    :type request_id: str
    :param action: 
    :type action: str
    :param changed_object_type: 
    :type changed_object_type: str
    :param object_repr: 
    :type object_repr: str
    :param q: 
    :type q: str
    :param time: 
    :type time: str
    :param limit: Number of results to return per page.
    :type limit: int
    :param offset: The initial index from which to return the results.
    :type offset: int

    """
    return web.Response(status=200)


async def extras_object_changes_read(request: web.Request, id) -> web.Response:
    """extras_object_changes_read

    Retrieve a list of recent changes.

    :param id: A unique integer value identifying this object change.
    :type id: int

    """
    return web.Response(status=200)


async def extras_recent_activity_list(request: web.Request, user=None, username=None, limit=None, offset=None) -> web.Response:
    """extras_recent_activity_list

    

    :param user: 
    :type user: str
    :param username: 
    :type username: str
    :param limit: Number of results to return per page.
    :type limit: int
    :param offset: The initial index from which to return the results.
    :type offset: int

    """
    return web.Response(status=200)


async def extras_recent_activity_read(request: web.Request, id) -> web.Response:
    """extras_recent_activity_read

    

    :param id: A unique integer value identifying this user action.
    :type id: int

    """
    return web.Response(status=200)


async def extras_tags_create(request: web.Request, body) -> web.Response:
    """extras_tags_create

    

    :param body: 
    :type body: dict | bytes

    """
    body = Tag.from_dict(body)
    return web.Response(status=200)


async def extras_tags_delete(request: web.Request, id) -> web.Response:
    """extras_tags_delete

    

    :param id: A unique integer value identifying this Tag.
    :type id: int

    """
    return web.Response(status=200)


async def extras_tags_list(request: web.Request, name=None, slug=None, q=None, limit=None, offset=None) -> web.Response:
    """extras_tags_list

    

    :param name: 
    :type name: str
    :param slug: 
    :type slug: str
    :param q: 
    :type q: str
    :param limit: Number of results to return per page.
    :type limit: int
    :param offset: The initial index from which to return the results.
    :type offset: int

    """
    return web.Response(status=200)


async def extras_tags_partial_update(request: web.Request, id, body) -> web.Response:
    """extras_tags_partial_update

    

    :param id: A unique integer value identifying this Tag.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = Tag.from_dict(body)
    return web.Response(status=200)


async def extras_tags_read(request: web.Request, id) -> web.Response:
    """extras_tags_read

    

    :param id: A unique integer value identifying this Tag.
    :type id: int

    """
    return web.Response(status=200)


async def extras_tags_update(request: web.Request, id, body) -> web.Response:
    """extras_tags_update

    

    :param id: A unique integer value identifying this Tag.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = Tag.from_dict(body)
    return web.Response(status=200)


async def extras_topology_maps_create(request: web.Request, body) -> web.Response:
    """extras_topology_maps_create

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableTopologyMap.from_dict(body)
    return web.Response(status=200)


async def extras_topology_maps_delete(request: web.Request, id) -> web.Response:
    """extras_topology_maps_delete

    

    :param id: A unique integer value identifying this topology map.
    :type id: int

    """
    return web.Response(status=200)


async def extras_topology_maps_list(request: web.Request, name=None, slug=None, site_id=None, site=None, limit=None, offset=None) -> web.Response:
    """extras_topology_maps_list

    

    :param name: 
    :type name: str
    :param slug: 
    :type slug: str
    :param site_id: 
    :type site_id: str
    :param site: 
    :type site: str
    :param limit: Number of results to return per page.
    :type limit: int
    :param offset: The initial index from which to return the results.
    :type offset: int

    """
    return web.Response(status=200)


async def extras_topology_maps_partial_update(request: web.Request, id, body) -> web.Response:
    """extras_topology_maps_partial_update

    

    :param id: A unique integer value identifying this topology map.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = WritableTopologyMap.from_dict(body)
    return web.Response(status=200)


async def extras_topology_maps_read(request: web.Request, id) -> web.Response:
    """extras_topology_maps_read

    

    :param id: A unique integer value identifying this topology map.
    :type id: int

    """
    return web.Response(status=200)


async def extras_topology_maps_render(request: web.Request, id) -> web.Response:
    """extras_topology_maps_render

    

    :param id: A unique integer value identifying this topology map.
    :type id: int

    """
    return web.Response(status=200)


async def extras_topology_maps_update(request: web.Request, id, body) -> web.Response:
    """extras_topology_maps_update

    

    :param id: A unique integer value identifying this topology map.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = WritableTopologyMap.from_dict(body)
    return web.Response(status=200)
