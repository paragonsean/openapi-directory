from typing import List, Dict
from aiohttp import web

from openapi_server.models.config_context import ConfigContext
from openapi_server.models.export_template import ExportTemplate
from openapi_server.models.extras_config_contexts_list200_response import ExtrasConfigContextsList200Response
from openapi_server.models.extras_export_templates_list200_response import ExtrasExportTemplatesList200Response
from openapi_server.models.extras_graphs_list200_response import ExtrasGraphsList200Response
from openapi_server.models.extras_image_attachments_list200_response import ExtrasImageAttachmentsList200Response
from openapi_server.models.extras_object_changes_list200_response import ExtrasObjectChangesList200Response
from openapi_server.models.extras_tags_list200_response import ExtrasTagsList200Response
from openapi_server.models.graph import Graph
from openapi_server.models.image_attachment import ImageAttachment
from openapi_server.models.object_change import ObjectChange
from openapi_server.models.tag import Tag
from openapi_server.models.writable_config_context import WritableConfigContext
from openapi_server.models.writable_export_template import WritableExportTemplate
from openapi_server import util


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


async def extras_config_contexts_list(request: web.Request, id=None, name=None, is_active=None, q=None, region_id=None, region=None, site_id=None, site=None, role_id=None, role=None, platform_id=None, platform=None, cluster_group_id=None, cluster_group=None, cluster_id=None, tenant_group_id=None, tenant_group=None, tenant_id=None, tenant=None, tag=None, id__n=None, id__lte=None, id__lt=None, id__gte=None, id__gt=None, name__n=None, name__ic=None, name__nic=None, name__iew=None, name__niew=None, name__isw=None, name__nisw=None, name__ie=None, name__nie=None, region_id__n=None, region__n=None, site_id__n=None, site__n=None, role_id__n=None, role__n=None, platform_id__n=None, platform__n=None, cluster_group_id__n=None, cluster_group__n=None, cluster_id__n=None, tenant_group_id__n=None, tenant_group__n=None, tenant_id__n=None, tenant__n=None, tag__n=None, limit=None, offset=None) -> web.Response:
    """extras_config_contexts_list

    Call to super to allow for caching

    :param id: 
    :type id: str
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
    :param cluster_group_id: 
    :type cluster_group_id: str
    :param cluster_group: 
    :type cluster_group: str
    :param cluster_id: 
    :type cluster_id: str
    :param tenant_group_id: 
    :type tenant_group_id: str
    :param tenant_group: 
    :type tenant_group: str
    :param tenant_id: 
    :type tenant_id: str
    :param tenant: 
    :type tenant: str
    :param tag: 
    :type tag: str
    :param id__n: 
    :type id__n: str
    :param id__lte: 
    :type id__lte: str
    :param id__lt: 
    :type id__lt: str
    :param id__gte: 
    :type id__gte: str
    :param id__gt: 
    :type id__gt: str
    :param name__n: 
    :type name__n: str
    :param name__ic: 
    :type name__ic: str
    :param name__nic: 
    :type name__nic: str
    :param name__iew: 
    :type name__iew: str
    :param name__niew: 
    :type name__niew: str
    :param name__isw: 
    :type name__isw: str
    :param name__nisw: 
    :type name__nisw: str
    :param name__ie: 
    :type name__ie: str
    :param name__nie: 
    :type name__nie: str
    :param region_id__n: 
    :type region_id__n: str
    :param region__n: 
    :type region__n: str
    :param site_id__n: 
    :type site_id__n: str
    :param site__n: 
    :type site__n: str
    :param role_id__n: 
    :type role_id__n: str
    :param role__n: 
    :type role__n: str
    :param platform_id__n: 
    :type platform_id__n: str
    :param platform__n: 
    :type platform__n: str
    :param cluster_group_id__n: 
    :type cluster_group_id__n: str
    :param cluster_group__n: 
    :type cluster_group__n: str
    :param cluster_id__n: 
    :type cluster_id__n: str
    :param tenant_group_id__n: 
    :type tenant_group_id__n: str
    :param tenant_group__n: 
    :type tenant_group__n: str
    :param tenant_id__n: 
    :type tenant_id__n: str
    :param tenant__n: 
    :type tenant__n: str
    :param tag__n: 
    :type tag__n: str
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

    Call to super to allow for caching

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


async def extras_custom_field_choices_list(request: web.Request, ) -> web.Response:
    """extras_custom_field_choices_list

    


    """
    return web.Response(status=200)


async def extras_custom_field_choices_read(request: web.Request, id) -> web.Response:
    """extras_custom_field_choices_read

    

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def extras_export_templates_create(request: web.Request, body) -> web.Response:
    """extras_export_templates_create

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableExportTemplate.from_dict(body)
    return web.Response(status=200)


async def extras_export_templates_delete(request: web.Request, id) -> web.Response:
    """extras_export_templates_delete

    

    :param id: A unique integer value identifying this export template.
    :type id: int

    """
    return web.Response(status=200)


async def extras_export_templates_list(request: web.Request, id=None, content_type=None, name=None, template_language=None, id__n=None, id__lte=None, id__lt=None, id__gte=None, id__gt=None, content_type__n=None, name__n=None, name__ic=None, name__nic=None, name__iew=None, name__niew=None, name__isw=None, name__nisw=None, name__ie=None, name__nie=None, template_language__n=None, limit=None, offset=None) -> web.Response:
    """extras_export_templates_list

    Call to super to allow for caching

    :param id: 
    :type id: str
    :param content_type: 
    :type content_type: str
    :param name: 
    :type name: str
    :param template_language: 
    :type template_language: str
    :param id__n: 
    :type id__n: str
    :param id__lte: 
    :type id__lte: str
    :param id__lt: 
    :type id__lt: str
    :param id__gte: 
    :type id__gte: str
    :param id__gt: 
    :type id__gt: str
    :param content_type__n: 
    :type content_type__n: str
    :param name__n: 
    :type name__n: str
    :param name__ic: 
    :type name__ic: str
    :param name__nic: 
    :type name__nic: str
    :param name__iew: 
    :type name__iew: str
    :param name__niew: 
    :type name__niew: str
    :param name__isw: 
    :type name__isw: str
    :param name__nisw: 
    :type name__nisw: str
    :param name__ie: 
    :type name__ie: str
    :param name__nie: 
    :type name__nie: str
    :param template_language__n: 
    :type template_language__n: str
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
    body = WritableExportTemplate.from_dict(body)
    return web.Response(status=200)


async def extras_export_templates_read(request: web.Request, id) -> web.Response:
    """extras_export_templates_read

    Call to super to allow for caching

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
    body = WritableExportTemplate.from_dict(body)
    return web.Response(status=200)


async def extras_graphs_create(request: web.Request, body) -> web.Response:
    """extras_graphs_create

    

    :param body: 
    :type body: dict | bytes

    """
    body = Graph.from_dict(body)
    return web.Response(status=200)


async def extras_graphs_delete(request: web.Request, id) -> web.Response:
    """extras_graphs_delete

    

    :param id: A unique integer value identifying this graph.
    :type id: int

    """
    return web.Response(status=200)


async def extras_graphs_list(request: web.Request, id=None, type=None, name=None, template_language=None, id__n=None, id__lte=None, id__lt=None, id__gte=None, id__gt=None, type__n=None, name__n=None, name__ic=None, name__nic=None, name__iew=None, name__niew=None, name__isw=None, name__nisw=None, name__ie=None, name__nie=None, template_language__n=None, limit=None, offset=None) -> web.Response:
    """extras_graphs_list

    Call to super to allow for caching

    :param id: 
    :type id: str
    :param type: 
    :type type: str
    :param name: 
    :type name: str
    :param template_language: 
    :type template_language: str
    :param id__n: 
    :type id__n: str
    :param id__lte: 
    :type id__lte: str
    :param id__lt: 
    :type id__lt: str
    :param id__gte: 
    :type id__gte: str
    :param id__gt: 
    :type id__gt: str
    :param type__n: 
    :type type__n: str
    :param name__n: 
    :type name__n: str
    :param name__ic: 
    :type name__ic: str
    :param name__nic: 
    :type name__nic: str
    :param name__iew: 
    :type name__iew: str
    :param name__niew: 
    :type name__niew: str
    :param name__isw: 
    :type name__isw: str
    :param name__nisw: 
    :type name__nisw: str
    :param name__ie: 
    :type name__ie: str
    :param name__nie: 
    :type name__nie: str
    :param template_language__n: 
    :type template_language__n: str
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
    body = Graph.from_dict(body)
    return web.Response(status=200)


async def extras_graphs_read(request: web.Request, id) -> web.Response:
    """extras_graphs_read

    Call to super to allow for caching

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
    body = Graph.from_dict(body)
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

    Call to super to allow for caching

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

    Call to super to allow for caching

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


async def extras_object_changes_list(request: web.Request, id=None, user=None, user_name=None, request_id=None, action=None, changed_object_type=None, changed_object_id=None, object_repr=None, q=None, time=None, id__n=None, id__lte=None, id__lt=None, id__gte=None, id__gt=None, user__n=None, user_name__n=None, user_name__ic=None, user_name__nic=None, user_name__iew=None, user_name__niew=None, user_name__isw=None, user_name__nisw=None, user_name__ie=None, user_name__nie=None, action__n=None, changed_object_type__n=None, changed_object_id__n=None, changed_object_id__lte=None, changed_object_id__lt=None, changed_object_id__gte=None, changed_object_id__gt=None, object_repr__n=None, object_repr__ic=None, object_repr__nic=None, object_repr__iew=None, object_repr__niew=None, object_repr__isw=None, object_repr__nisw=None, object_repr__ie=None, object_repr__nie=None, limit=None, offset=None) -> web.Response:
    """extras_object_changes_list

    Retrieve a list of recent changes.

    :param id: 
    :type id: str
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
    :param changed_object_id: 
    :type changed_object_id: str
    :param object_repr: 
    :type object_repr: str
    :param q: 
    :type q: str
    :param time: 
    :type time: str
    :param id__n: 
    :type id__n: str
    :param id__lte: 
    :type id__lte: str
    :param id__lt: 
    :type id__lt: str
    :param id__gte: 
    :type id__gte: str
    :param id__gt: 
    :type id__gt: str
    :param user__n: 
    :type user__n: str
    :param user_name__n: 
    :type user_name__n: str
    :param user_name__ic: 
    :type user_name__ic: str
    :param user_name__nic: 
    :type user_name__nic: str
    :param user_name__iew: 
    :type user_name__iew: str
    :param user_name__niew: 
    :type user_name__niew: str
    :param user_name__isw: 
    :type user_name__isw: str
    :param user_name__nisw: 
    :type user_name__nisw: str
    :param user_name__ie: 
    :type user_name__ie: str
    :param user_name__nie: 
    :type user_name__nie: str
    :param action__n: 
    :type action__n: str
    :param changed_object_type__n: 
    :type changed_object_type__n: str
    :param changed_object_id__n: 
    :type changed_object_id__n: str
    :param changed_object_id__lte: 
    :type changed_object_id__lte: str
    :param changed_object_id__lt: 
    :type changed_object_id__lt: str
    :param changed_object_id__gte: 
    :type changed_object_id__gte: str
    :param changed_object_id__gt: 
    :type changed_object_id__gt: str
    :param object_repr__n: 
    :type object_repr__n: str
    :param object_repr__ic: 
    :type object_repr__ic: str
    :param object_repr__nic: 
    :type object_repr__nic: str
    :param object_repr__iew: 
    :type object_repr__iew: str
    :param object_repr__niew: 
    :type object_repr__niew: str
    :param object_repr__isw: 
    :type object_repr__isw: str
    :param object_repr__nisw: 
    :type object_repr__nisw: str
    :param object_repr__ie: 
    :type object_repr__ie: str
    :param object_repr__nie: 
    :type object_repr__nie: str
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


async def extras_reports_list(request: web.Request, ) -> web.Response:
    """extras_reports_list

    Compile all reports and their related results (if any). Result data is deferred in the list view.


    """
    return web.Response(status=200)


async def extras_reports_read(request: web.Request, id) -> web.Response:
    """extras_reports_read

    Retrieve a single Report identified as \&quot;&lt;module&gt;.&lt;report&gt;\&quot;.

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def extras_reports_run(request: web.Request, id) -> web.Response:
    """extras_reports_run

    Run a Report and create a new ReportResult, overwriting any previous result for the Report.

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def extras_scripts_list(request: web.Request, ) -> web.Response:
    """extras_scripts_list

    


    """
    return web.Response(status=200)


async def extras_scripts_read(request: web.Request, id) -> web.Response:
    """extras_scripts_read

    

    :param id: 
    :type id: str

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

    

    :param id: A unique integer value identifying this tag.
    :type id: int

    """
    return web.Response(status=200)


async def extras_tags_list(request: web.Request, id=None, name=None, slug=None, color=None, q=None, id__n=None, id__lte=None, id__lt=None, id__gte=None, id__gt=None, name__n=None, name__ic=None, name__nic=None, name__iew=None, name__niew=None, name__isw=None, name__nisw=None, name__ie=None, name__nie=None, slug__n=None, slug__ic=None, slug__nic=None, slug__iew=None, slug__niew=None, slug__isw=None, slug__nisw=None, slug__ie=None, slug__nie=None, color__n=None, color__ic=None, color__nic=None, color__iew=None, color__niew=None, color__isw=None, color__nisw=None, color__ie=None, color__nie=None, limit=None, offset=None) -> web.Response:
    """extras_tags_list

    Call to super to allow for caching

    :param id: 
    :type id: str
    :param name: 
    :type name: str
    :param slug: 
    :type slug: str
    :param color: 
    :type color: str
    :param q: 
    :type q: str
    :param id__n: 
    :type id__n: str
    :param id__lte: 
    :type id__lte: str
    :param id__lt: 
    :type id__lt: str
    :param id__gte: 
    :type id__gte: str
    :param id__gt: 
    :type id__gt: str
    :param name__n: 
    :type name__n: str
    :param name__ic: 
    :type name__ic: str
    :param name__nic: 
    :type name__nic: str
    :param name__iew: 
    :type name__iew: str
    :param name__niew: 
    :type name__niew: str
    :param name__isw: 
    :type name__isw: str
    :param name__nisw: 
    :type name__nisw: str
    :param name__ie: 
    :type name__ie: str
    :param name__nie: 
    :type name__nie: str
    :param slug__n: 
    :type slug__n: str
    :param slug__ic: 
    :type slug__ic: str
    :param slug__nic: 
    :type slug__nic: str
    :param slug__iew: 
    :type slug__iew: str
    :param slug__niew: 
    :type slug__niew: str
    :param slug__isw: 
    :type slug__isw: str
    :param slug__nisw: 
    :type slug__nisw: str
    :param slug__ie: 
    :type slug__ie: str
    :param slug__nie: 
    :type slug__nie: str
    :param color__n: 
    :type color__n: str
    :param color__ic: 
    :type color__ic: str
    :param color__nic: 
    :type color__nic: str
    :param color__iew: 
    :type color__iew: str
    :param color__niew: 
    :type color__niew: str
    :param color__isw: 
    :type color__isw: str
    :param color__nisw: 
    :type color__nisw: str
    :param color__ie: 
    :type color__ie: str
    :param color__nie: 
    :type color__nie: str
    :param limit: Number of results to return per page.
    :type limit: int
    :param offset: The initial index from which to return the results.
    :type offset: int

    """
    return web.Response(status=200)


async def extras_tags_partial_update(request: web.Request, id, body) -> web.Response:
    """extras_tags_partial_update

    

    :param id: A unique integer value identifying this tag.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = Tag.from_dict(body)
    return web.Response(status=200)


async def extras_tags_read(request: web.Request, id) -> web.Response:
    """extras_tags_read

    Call to super to allow for caching

    :param id: A unique integer value identifying this tag.
    :type id: int

    """
    return web.Response(status=200)


async def extras_tags_update(request: web.Request, id, body) -> web.Response:
    """extras_tags_update

    

    :param id: A unique integer value identifying this tag.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = Tag.from_dict(body)
    return web.Response(status=200)
