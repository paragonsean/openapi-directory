from typing import List, Dict
from aiohttp import web

from openapi_server.models.config_context import ConfigContext
from openapi_server.models.content_type import ContentType
from openapi_server.models.custom_field import CustomField
from openapi_server.models.custom_link import CustomLink
from openapi_server.models.export_template import ExportTemplate
from openapi_server.models.extras_config_contexts_list200_response import ExtrasConfigContextsList200Response
from openapi_server.models.extras_content_types_list200_response import ExtrasContentTypesList200Response
from openapi_server.models.extras_custom_fields_list200_response import ExtrasCustomFieldsList200Response
from openapi_server.models.extras_custom_links_list200_response import ExtrasCustomLinksList200Response
from openapi_server.models.extras_export_templates_list200_response import ExtrasExportTemplatesList200Response
from openapi_server.models.extras_image_attachments_list200_response import ExtrasImageAttachmentsList200Response
from openapi_server.models.extras_job_results_list200_response import ExtrasJobResultsList200Response
from openapi_server.models.extras_journal_entries_list200_response import ExtrasJournalEntriesList200Response
from openapi_server.models.extras_object_changes_list200_response import ExtrasObjectChangesList200Response
from openapi_server.models.extras_saved_filters_list200_response import ExtrasSavedFiltersList200Response
from openapi_server.models.extras_tags_list200_response import ExtrasTagsList200Response
from openapi_server.models.extras_webhooks_list200_response import ExtrasWebhooksList200Response
from openapi_server.models.image_attachment import ImageAttachment
from openapi_server.models.job_result import JobResult
from openapi_server.models.journal_entry import JournalEntry
from openapi_server.models.object_change import ObjectChange
from openapi_server.models.saved_filter import SavedFilter
from openapi_server.models.tag import Tag
from openapi_server.models.webhook import Webhook
from openapi_server.models.writable_config_context import WritableConfigContext
from openapi_server.models.writable_custom_field import WritableCustomField
from openapi_server.models.writable_journal_entry import WritableJournalEntry
from openapi_server import util


async def extras_config_contexts_bulk_delete(request: web.Request, ) -> web.Response:
    """extras_config_contexts_bulk_delete

    


    """
    return web.Response(status=200)


async def extras_config_contexts_bulk_partial_update(request: web.Request, body) -> web.Response:
    """extras_config_contexts_bulk_partial_update

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableConfigContext.from_dict(body)
    return web.Response(status=200)


async def extras_config_contexts_bulk_update(request: web.Request, body) -> web.Response:
    """extras_config_contexts_bulk_update

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableConfigContext.from_dict(body)
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


async def extras_config_contexts_list(request: web.Request, id=None, name=None, is_active=None, created=None, last_updated=None, q=None, region_id=None, region=None, site_group=None, site_group_id=None, site_id=None, site=None, location_id=None, location=None, device_type_id=None, role_id=None, role=None, platform_id=None, platform=None, cluster_type_id=None, cluster_type=None, cluster_group_id=None, cluster_group=None, cluster_id=None, tenant_group_id=None, tenant_group=None, tenant_id=None, tenant=None, tag_id=None, tag=None, id__n=None, id__lte=None, id__lt=None, id__gte=None, id__gt=None, name__n=None, name__ic=None, name__nic=None, name__iew=None, name__niew=None, name__isw=None, name__nisw=None, name__ie=None, name__nie=None, name__empty=None, created__n=None, created__lte=None, created__lt=None, created__gte=None, created__gt=None, last_updated__n=None, last_updated__lte=None, last_updated__lt=None, last_updated__gte=None, last_updated__gt=None, region_id__n=None, region__n=None, site_group__n=None, site_group_id__n=None, site_id__n=None, site__n=None, location_id__n=None, location__n=None, device_type_id__n=None, role_id__n=None, role__n=None, platform_id__n=None, platform__n=None, cluster_type_id__n=None, cluster_type__n=None, cluster_group_id__n=None, cluster_group__n=None, cluster_id__n=None, tenant_group_id__n=None, tenant_group__n=None, tenant_id__n=None, tenant__n=None, tag_id__n=None, tag__n=None, ordering=None, limit=None, offset=None) -> web.Response:
    """extras_config_contexts_list

    

    :param id: 
    :type id: str
    :param name: 
    :type name: str
    :param is_active: 
    :type is_active: str
    :param created: 
    :type created: str
    :param last_updated: 
    :type last_updated: str
    :param q: 
    :type q: str
    :param region_id: 
    :type region_id: str
    :param region: 
    :type region: str
    :param site_group: 
    :type site_group: str
    :param site_group_id: 
    :type site_group_id: str
    :param site_id: 
    :type site_id: str
    :param site: 
    :type site: str
    :param location_id: 
    :type location_id: str
    :param location: 
    :type location: str
    :param device_type_id: 
    :type device_type_id: str
    :param role_id: 
    :type role_id: str
    :param role: 
    :type role: str
    :param platform_id: 
    :type platform_id: str
    :param platform: 
    :type platform: str
    :param cluster_type_id: 
    :type cluster_type_id: str
    :param cluster_type: 
    :type cluster_type: str
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
    :param tag_id: 
    :type tag_id: str
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
    :param name__empty: 
    :type name__empty: str
    :param created__n: 
    :type created__n: str
    :param created__lte: 
    :type created__lte: str
    :param created__lt: 
    :type created__lt: str
    :param created__gte: 
    :type created__gte: str
    :param created__gt: 
    :type created__gt: str
    :param last_updated__n: 
    :type last_updated__n: str
    :param last_updated__lte: 
    :type last_updated__lte: str
    :param last_updated__lt: 
    :type last_updated__lt: str
    :param last_updated__gte: 
    :type last_updated__gte: str
    :param last_updated__gt: 
    :type last_updated__gt: str
    :param region_id__n: 
    :type region_id__n: str
    :param region__n: 
    :type region__n: str
    :param site_group__n: 
    :type site_group__n: str
    :param site_group_id__n: 
    :type site_group_id__n: str
    :param site_id__n: 
    :type site_id__n: str
    :param site__n: 
    :type site__n: str
    :param location_id__n: 
    :type location_id__n: str
    :param location__n: 
    :type location__n: str
    :param device_type_id__n: 
    :type device_type_id__n: str
    :param role_id__n: 
    :type role_id__n: str
    :param role__n: 
    :type role__n: str
    :param platform_id__n: 
    :type platform_id__n: str
    :param platform__n: 
    :type platform__n: str
    :param cluster_type_id__n: 
    :type cluster_type_id__n: str
    :param cluster_type__n: 
    :type cluster_type__n: str
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
    :param tag_id__n: 
    :type tag_id__n: str
    :param tag__n: 
    :type tag__n: str
    :param ordering: Which field to use when ordering the results.
    :type ordering: str
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


async def extras_content_types_list(request: web.Request, id=None, app_label=None, model=None, q=None, ordering=None, limit=None, offset=None) -> web.Response:
    """extras_content_types_list

    Read-only list of ContentTypes. Limit results to ContentTypes pertinent to NetBox objects.

    :param id: 
    :type id: 
    :param app_label: 
    :type app_label: str
    :param model: 
    :type model: str
    :param q: 
    :type q: str
    :param ordering: Which field to use when ordering the results.
    :type ordering: str
    :param limit: Number of results to return per page.
    :type limit: int
    :param offset: The initial index from which to return the results.
    :type offset: int

    """
    return web.Response(status=200)


async def extras_content_types_read(request: web.Request, id) -> web.Response:
    """extras_content_types_read

    Read-only list of ContentTypes. Limit results to ContentTypes pertinent to NetBox objects.

    :param id: A unique integer value identifying this content type.
    :type id: int

    """
    return web.Response(status=200)


async def extras_custom_fields_bulk_delete(request: web.Request, ) -> web.Response:
    """extras_custom_fields_bulk_delete

    


    """
    return web.Response(status=200)


async def extras_custom_fields_bulk_partial_update(request: web.Request, body) -> web.Response:
    """extras_custom_fields_bulk_partial_update

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableCustomField.from_dict(body)
    return web.Response(status=200)


async def extras_custom_fields_bulk_update(request: web.Request, body) -> web.Response:
    """extras_custom_fields_bulk_update

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableCustomField.from_dict(body)
    return web.Response(status=200)


async def extras_custom_fields_create(request: web.Request, body) -> web.Response:
    """extras_custom_fields_create

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableCustomField.from_dict(body)
    return web.Response(status=200)


async def extras_custom_fields_delete(request: web.Request, id) -> web.Response:
    """extras_custom_fields_delete

    

    :param id: A unique integer value identifying this custom field.
    :type id: int

    """
    return web.Response(status=200)


async def extras_custom_fields_list(request: web.Request, id=None, content_types=None, name=None, group_name=None, required=None, search_weight=None, filter_logic=None, ui_visibility=None, weight=None, description=None, q=None, type=None, content_type_id=None, id__n=None, id__lte=None, id__lt=None, id__gte=None, id__gt=None, content_types__n=None, content_types__ic=None, content_types__nic=None, content_types__iew=None, content_types__niew=None, content_types__isw=None, content_types__nisw=None, content_types__ie=None, content_types__nie=None, name__n=None, name__ic=None, name__nic=None, name__iew=None, name__niew=None, name__isw=None, name__nisw=None, name__ie=None, name__nie=None, name__empty=None, group_name__n=None, group_name__ic=None, group_name__nic=None, group_name__iew=None, group_name__niew=None, group_name__isw=None, group_name__nisw=None, group_name__ie=None, group_name__nie=None, group_name__empty=None, search_weight__n=None, search_weight__lte=None, search_weight__lt=None, search_weight__gte=None, search_weight__gt=None, filter_logic__n=None, ui_visibility__n=None, weight__n=None, weight__lte=None, weight__lt=None, weight__gte=None, weight__gt=None, description__n=None, description__ic=None, description__nic=None, description__iew=None, description__niew=None, description__isw=None, description__nisw=None, description__ie=None, description__nie=None, description__empty=None, type__n=None, content_type_id__n=None, content_type_id__lte=None, content_type_id__lt=None, content_type_id__gte=None, content_type_id__gt=None, ordering=None, limit=None, offset=None) -> web.Response:
    """extras_custom_fields_list

    

    :param id: 
    :type id: str
    :param content_types: 
    :type content_types: str
    :param name: 
    :type name: str
    :param group_name: 
    :type group_name: str
    :param required: 
    :type required: str
    :param search_weight: 
    :type search_weight: str
    :param filter_logic: 
    :type filter_logic: str
    :param ui_visibility: 
    :type ui_visibility: str
    :param weight: 
    :type weight: str
    :param description: 
    :type description: str
    :param q: 
    :type q: str
    :param type: 
    :type type: str
    :param content_type_id: 
    :type content_type_id: str
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
    :param content_types__n: 
    :type content_types__n: str
    :param content_types__ic: 
    :type content_types__ic: str
    :param content_types__nic: 
    :type content_types__nic: str
    :param content_types__iew: 
    :type content_types__iew: str
    :param content_types__niew: 
    :type content_types__niew: str
    :param content_types__isw: 
    :type content_types__isw: str
    :param content_types__nisw: 
    :type content_types__nisw: str
    :param content_types__ie: 
    :type content_types__ie: str
    :param content_types__nie: 
    :type content_types__nie: str
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
    :param name__empty: 
    :type name__empty: str
    :param group_name__n: 
    :type group_name__n: str
    :param group_name__ic: 
    :type group_name__ic: str
    :param group_name__nic: 
    :type group_name__nic: str
    :param group_name__iew: 
    :type group_name__iew: str
    :param group_name__niew: 
    :type group_name__niew: str
    :param group_name__isw: 
    :type group_name__isw: str
    :param group_name__nisw: 
    :type group_name__nisw: str
    :param group_name__ie: 
    :type group_name__ie: str
    :param group_name__nie: 
    :type group_name__nie: str
    :param group_name__empty: 
    :type group_name__empty: str
    :param search_weight__n: 
    :type search_weight__n: str
    :param search_weight__lte: 
    :type search_weight__lte: str
    :param search_weight__lt: 
    :type search_weight__lt: str
    :param search_weight__gte: 
    :type search_weight__gte: str
    :param search_weight__gt: 
    :type search_weight__gt: str
    :param filter_logic__n: 
    :type filter_logic__n: str
    :param ui_visibility__n: 
    :type ui_visibility__n: str
    :param weight__n: 
    :type weight__n: str
    :param weight__lte: 
    :type weight__lte: str
    :param weight__lt: 
    :type weight__lt: str
    :param weight__gte: 
    :type weight__gte: str
    :param weight__gt: 
    :type weight__gt: str
    :param description__n: 
    :type description__n: str
    :param description__ic: 
    :type description__ic: str
    :param description__nic: 
    :type description__nic: str
    :param description__iew: 
    :type description__iew: str
    :param description__niew: 
    :type description__niew: str
    :param description__isw: 
    :type description__isw: str
    :param description__nisw: 
    :type description__nisw: str
    :param description__ie: 
    :type description__ie: str
    :param description__nie: 
    :type description__nie: str
    :param description__empty: 
    :type description__empty: str
    :param type__n: 
    :type type__n: str
    :param content_type_id__n: 
    :type content_type_id__n: str
    :param content_type_id__lte: 
    :type content_type_id__lte: str
    :param content_type_id__lt: 
    :type content_type_id__lt: str
    :param content_type_id__gte: 
    :type content_type_id__gte: str
    :param content_type_id__gt: 
    :type content_type_id__gt: str
    :param ordering: Which field to use when ordering the results.
    :type ordering: str
    :param limit: Number of results to return per page.
    :type limit: int
    :param offset: The initial index from which to return the results.
    :type offset: int

    """
    return web.Response(status=200)


async def extras_custom_fields_partial_update(request: web.Request, id, body) -> web.Response:
    """extras_custom_fields_partial_update

    

    :param id: A unique integer value identifying this custom field.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = WritableCustomField.from_dict(body)
    return web.Response(status=200)


async def extras_custom_fields_read(request: web.Request, id) -> web.Response:
    """extras_custom_fields_read

    

    :param id: A unique integer value identifying this custom field.
    :type id: int

    """
    return web.Response(status=200)


async def extras_custom_fields_update(request: web.Request, id, body) -> web.Response:
    """extras_custom_fields_update

    

    :param id: A unique integer value identifying this custom field.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = WritableCustomField.from_dict(body)
    return web.Response(status=200)


async def extras_custom_links_bulk_delete(request: web.Request, ) -> web.Response:
    """extras_custom_links_bulk_delete

    


    """
    return web.Response(status=200)


async def extras_custom_links_bulk_partial_update(request: web.Request, body) -> web.Response:
    """extras_custom_links_bulk_partial_update

    

    :param body: 
    :type body: dict | bytes

    """
    body = CustomLink.from_dict(body)
    return web.Response(status=200)


async def extras_custom_links_bulk_update(request: web.Request, body) -> web.Response:
    """extras_custom_links_bulk_update

    

    :param body: 
    :type body: dict | bytes

    """
    body = CustomLink.from_dict(body)
    return web.Response(status=200)


async def extras_custom_links_create(request: web.Request, body) -> web.Response:
    """extras_custom_links_create

    

    :param body: 
    :type body: dict | bytes

    """
    body = CustomLink.from_dict(body)
    return web.Response(status=200)


async def extras_custom_links_delete(request: web.Request, id) -> web.Response:
    """extras_custom_links_delete

    

    :param id: A unique integer value identifying this custom link.
    :type id: int

    """
    return web.Response(status=200)


async def extras_custom_links_list(request: web.Request, id=None, content_types=None, name=None, enabled=None, link_text=None, link_url=None, weight=None, group_name=None, new_window=None, q=None, content_type_id=None, id__n=None, id__lte=None, id__lt=None, id__gte=None, id__gt=None, content_types__n=None, content_types__ic=None, content_types__nic=None, content_types__iew=None, content_types__niew=None, content_types__isw=None, content_types__nisw=None, content_types__ie=None, content_types__nie=None, name__n=None, name__ic=None, name__nic=None, name__iew=None, name__niew=None, name__isw=None, name__nisw=None, name__ie=None, name__nie=None, name__empty=None, link_text__n=None, link_text__ic=None, link_text__nic=None, link_text__iew=None, link_text__niew=None, link_text__isw=None, link_text__nisw=None, link_text__ie=None, link_text__nie=None, link_url__n=None, link_url__ic=None, link_url__nic=None, link_url__iew=None, link_url__niew=None, link_url__isw=None, link_url__nisw=None, link_url__ie=None, link_url__nie=None, weight__n=None, weight__lte=None, weight__lt=None, weight__gte=None, weight__gt=None, group_name__n=None, group_name__ic=None, group_name__nic=None, group_name__iew=None, group_name__niew=None, group_name__isw=None, group_name__nisw=None, group_name__ie=None, group_name__nie=None, group_name__empty=None, content_type_id__n=None, content_type_id__lte=None, content_type_id__lt=None, content_type_id__gte=None, content_type_id__gt=None, ordering=None, limit=None, offset=None) -> web.Response:
    """extras_custom_links_list

    

    :param id: 
    :type id: str
    :param content_types: 
    :type content_types: str
    :param name: 
    :type name: str
    :param enabled: 
    :type enabled: str
    :param link_text: 
    :type link_text: str
    :param link_url: 
    :type link_url: str
    :param weight: 
    :type weight: str
    :param group_name: 
    :type group_name: str
    :param new_window: 
    :type new_window: str
    :param q: 
    :type q: str
    :param content_type_id: 
    :type content_type_id: str
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
    :param content_types__n: 
    :type content_types__n: str
    :param content_types__ic: 
    :type content_types__ic: str
    :param content_types__nic: 
    :type content_types__nic: str
    :param content_types__iew: 
    :type content_types__iew: str
    :param content_types__niew: 
    :type content_types__niew: str
    :param content_types__isw: 
    :type content_types__isw: str
    :param content_types__nisw: 
    :type content_types__nisw: str
    :param content_types__ie: 
    :type content_types__ie: str
    :param content_types__nie: 
    :type content_types__nie: str
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
    :param name__empty: 
    :type name__empty: str
    :param link_text__n: 
    :type link_text__n: str
    :param link_text__ic: 
    :type link_text__ic: str
    :param link_text__nic: 
    :type link_text__nic: str
    :param link_text__iew: 
    :type link_text__iew: str
    :param link_text__niew: 
    :type link_text__niew: str
    :param link_text__isw: 
    :type link_text__isw: str
    :param link_text__nisw: 
    :type link_text__nisw: str
    :param link_text__ie: 
    :type link_text__ie: str
    :param link_text__nie: 
    :type link_text__nie: str
    :param link_url__n: 
    :type link_url__n: str
    :param link_url__ic: 
    :type link_url__ic: str
    :param link_url__nic: 
    :type link_url__nic: str
    :param link_url__iew: 
    :type link_url__iew: str
    :param link_url__niew: 
    :type link_url__niew: str
    :param link_url__isw: 
    :type link_url__isw: str
    :param link_url__nisw: 
    :type link_url__nisw: str
    :param link_url__ie: 
    :type link_url__ie: str
    :param link_url__nie: 
    :type link_url__nie: str
    :param weight__n: 
    :type weight__n: str
    :param weight__lte: 
    :type weight__lte: str
    :param weight__lt: 
    :type weight__lt: str
    :param weight__gte: 
    :type weight__gte: str
    :param weight__gt: 
    :type weight__gt: str
    :param group_name__n: 
    :type group_name__n: str
    :param group_name__ic: 
    :type group_name__ic: str
    :param group_name__nic: 
    :type group_name__nic: str
    :param group_name__iew: 
    :type group_name__iew: str
    :param group_name__niew: 
    :type group_name__niew: str
    :param group_name__isw: 
    :type group_name__isw: str
    :param group_name__nisw: 
    :type group_name__nisw: str
    :param group_name__ie: 
    :type group_name__ie: str
    :param group_name__nie: 
    :type group_name__nie: str
    :param group_name__empty: 
    :type group_name__empty: str
    :param content_type_id__n: 
    :type content_type_id__n: str
    :param content_type_id__lte: 
    :type content_type_id__lte: str
    :param content_type_id__lt: 
    :type content_type_id__lt: str
    :param content_type_id__gte: 
    :type content_type_id__gte: str
    :param content_type_id__gt: 
    :type content_type_id__gt: str
    :param ordering: Which field to use when ordering the results.
    :type ordering: str
    :param limit: Number of results to return per page.
    :type limit: int
    :param offset: The initial index from which to return the results.
    :type offset: int

    """
    return web.Response(status=200)


async def extras_custom_links_partial_update(request: web.Request, id, body) -> web.Response:
    """extras_custom_links_partial_update

    

    :param id: A unique integer value identifying this custom link.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = CustomLink.from_dict(body)
    return web.Response(status=200)


async def extras_custom_links_read(request: web.Request, id) -> web.Response:
    """extras_custom_links_read

    

    :param id: A unique integer value identifying this custom link.
    :type id: int

    """
    return web.Response(status=200)


async def extras_custom_links_update(request: web.Request, id, body) -> web.Response:
    """extras_custom_links_update

    

    :param id: A unique integer value identifying this custom link.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = CustomLink.from_dict(body)
    return web.Response(status=200)


async def extras_export_templates_bulk_delete(request: web.Request, ) -> web.Response:
    """extras_export_templates_bulk_delete

    


    """
    return web.Response(status=200)


async def extras_export_templates_bulk_partial_update(request: web.Request, body) -> web.Response:
    """extras_export_templates_bulk_partial_update

    

    :param body: 
    :type body: dict | bytes

    """
    body = ExportTemplate.from_dict(body)
    return web.Response(status=200)


async def extras_export_templates_bulk_update(request: web.Request, body) -> web.Response:
    """extras_export_templates_bulk_update

    

    :param body: 
    :type body: dict | bytes

    """
    body = ExportTemplate.from_dict(body)
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


async def extras_export_templates_list(request: web.Request, id=None, content_types=None, name=None, description=None, q=None, content_type_id=None, id__n=None, id__lte=None, id__lt=None, id__gte=None, id__gt=None, content_types__n=None, content_types__ic=None, content_types__nic=None, content_types__iew=None, content_types__niew=None, content_types__isw=None, content_types__nisw=None, content_types__ie=None, content_types__nie=None, name__n=None, name__ic=None, name__nic=None, name__iew=None, name__niew=None, name__isw=None, name__nisw=None, name__ie=None, name__nie=None, name__empty=None, description__n=None, description__ic=None, description__nic=None, description__iew=None, description__niew=None, description__isw=None, description__nisw=None, description__ie=None, description__nie=None, description__empty=None, content_type_id__n=None, content_type_id__lte=None, content_type_id__lt=None, content_type_id__gte=None, content_type_id__gt=None, ordering=None, limit=None, offset=None) -> web.Response:
    """extras_export_templates_list

    

    :param id: 
    :type id: str
    :param content_types: 
    :type content_types: str
    :param name: 
    :type name: str
    :param description: 
    :type description: str
    :param q: 
    :type q: str
    :param content_type_id: 
    :type content_type_id: str
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
    :param content_types__n: 
    :type content_types__n: str
    :param content_types__ic: 
    :type content_types__ic: str
    :param content_types__nic: 
    :type content_types__nic: str
    :param content_types__iew: 
    :type content_types__iew: str
    :param content_types__niew: 
    :type content_types__niew: str
    :param content_types__isw: 
    :type content_types__isw: str
    :param content_types__nisw: 
    :type content_types__nisw: str
    :param content_types__ie: 
    :type content_types__ie: str
    :param content_types__nie: 
    :type content_types__nie: str
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
    :param name__empty: 
    :type name__empty: str
    :param description__n: 
    :type description__n: str
    :param description__ic: 
    :type description__ic: str
    :param description__nic: 
    :type description__nic: str
    :param description__iew: 
    :type description__iew: str
    :param description__niew: 
    :type description__niew: str
    :param description__isw: 
    :type description__isw: str
    :param description__nisw: 
    :type description__nisw: str
    :param description__ie: 
    :type description__ie: str
    :param description__nie: 
    :type description__nie: str
    :param description__empty: 
    :type description__empty: str
    :param content_type_id__n: 
    :type content_type_id__n: str
    :param content_type_id__lte: 
    :type content_type_id__lte: str
    :param content_type_id__lt: 
    :type content_type_id__lt: str
    :param content_type_id__gte: 
    :type content_type_id__gte: str
    :param content_type_id__gt: 
    :type content_type_id__gt: str
    :param ordering: Which field to use when ordering the results.
    :type ordering: str
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


async def extras_image_attachments_bulk_delete(request: web.Request, ) -> web.Response:
    """extras_image_attachments_bulk_delete

    


    """
    return web.Response(status=200)


async def extras_image_attachments_bulk_partial_update(request: web.Request, body) -> web.Response:
    """extras_image_attachments_bulk_partial_update

    

    :param body: 
    :type body: dict | bytes

    """
    body = ImageAttachment.from_dict(body)
    return web.Response(status=200)


async def extras_image_attachments_bulk_update(request: web.Request, body) -> web.Response:
    """extras_image_attachments_bulk_update

    

    :param body: 
    :type body: dict | bytes

    """
    body = ImageAttachment.from_dict(body)
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


async def extras_image_attachments_list(request: web.Request, id=None, content_type_id=None, object_id=None, name=None, q=None, created=None, content_type=None, id__n=None, id__lte=None, id__lt=None, id__gte=None, id__gt=None, content_type_id__n=None, object_id__n=None, object_id__lte=None, object_id__lt=None, object_id__gte=None, object_id__gt=None, name__n=None, name__ic=None, name__nic=None, name__iew=None, name__niew=None, name__isw=None, name__nisw=None, name__ie=None, name__nie=None, name__empty=None, content_type__n=None, ordering=None, limit=None, offset=None) -> web.Response:
    """extras_image_attachments_list

    

    :param id: 
    :type id: str
    :param content_type_id: 
    :type content_type_id: str
    :param object_id: 
    :type object_id: str
    :param name: 
    :type name: str
    :param q: 
    :type q: str
    :param created: 
    :type created: str
    :param content_type: 
    :type content_type: str
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
    :param content_type_id__n: 
    :type content_type_id__n: str
    :param object_id__n: 
    :type object_id__n: str
    :param object_id__lte: 
    :type object_id__lte: str
    :param object_id__lt: 
    :type object_id__lt: str
    :param object_id__gte: 
    :type object_id__gte: str
    :param object_id__gt: 
    :type object_id__gt: str
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
    :param name__empty: 
    :type name__empty: str
    :param content_type__n: 
    :type content_type__n: str
    :param ordering: Which field to use when ordering the results.
    :type ordering: str
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


async def extras_job_results_list(request: web.Request, id=None, interval=None, status=None, user=None, obj_type=None, name=None, q=None, created=None, created__before=None, created__after=None, scheduled=None, scheduled__before=None, scheduled__after=None, started=None, started__before=None, started__after=None, completed=None, completed__before=None, completed__after=None, id__n=None, id__lte=None, id__lt=None, id__gte=None, id__gt=None, interval__n=None, interval__lte=None, interval__lt=None, interval__gte=None, interval__gt=None, status__n=None, user__n=None, obj_type__n=None, name__n=None, name__ic=None, name__nic=None, name__iew=None, name__niew=None, name__isw=None, name__nisw=None, name__ie=None, name__nie=None, name__empty=None, ordering=None, limit=None, offset=None) -> web.Response:
    """extras_job_results_list

    Retrieve a list of job results

    :param id: 
    :type id: str
    :param interval: 
    :type interval: str
    :param status: 
    :type status: str
    :param user: 
    :type user: str
    :param obj_type: 
    :type obj_type: str
    :param name: 
    :type name: str
    :param q: 
    :type q: str
    :param created: 
    :type created: str
    :param created__before: 
    :type created__before: str
    :param created__after: 
    :type created__after: str
    :param scheduled: 
    :type scheduled: str
    :param scheduled__before: 
    :type scheduled__before: str
    :param scheduled__after: 
    :type scheduled__after: str
    :param started: 
    :type started: str
    :param started__before: 
    :type started__before: str
    :param started__after: 
    :type started__after: str
    :param completed: 
    :type completed: str
    :param completed__before: 
    :type completed__before: str
    :param completed__after: 
    :type completed__after: str
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
    :param interval__n: 
    :type interval__n: str
    :param interval__lte: 
    :type interval__lte: str
    :param interval__lt: 
    :type interval__lt: str
    :param interval__gte: 
    :type interval__gte: str
    :param interval__gt: 
    :type interval__gt: str
    :param status__n: 
    :type status__n: str
    :param user__n: 
    :type user__n: str
    :param obj_type__n: 
    :type obj_type__n: str
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
    :param name__empty: 
    :type name__empty: str
    :param ordering: Which field to use when ordering the results.
    :type ordering: str
    :param limit: Number of results to return per page.
    :type limit: int
    :param offset: The initial index from which to return the results.
    :type offset: int

    """
    return web.Response(status=200)


async def extras_job_results_read(request: web.Request, id) -> web.Response:
    """extras_job_results_read

    Retrieve a list of job results

    :param id: A unique integer value identifying this job result.
    :type id: int

    """
    return web.Response(status=200)


async def extras_journal_entries_bulk_delete(request: web.Request, ) -> web.Response:
    """extras_journal_entries_bulk_delete

    


    """
    return web.Response(status=200)


async def extras_journal_entries_bulk_partial_update(request: web.Request, body) -> web.Response:
    """extras_journal_entries_bulk_partial_update

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableJournalEntry.from_dict(body)
    return web.Response(status=200)


async def extras_journal_entries_bulk_update(request: web.Request, body) -> web.Response:
    """extras_journal_entries_bulk_update

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableJournalEntry.from_dict(body)
    return web.Response(status=200)


async def extras_journal_entries_create(request: web.Request, body) -> web.Response:
    """extras_journal_entries_create

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableJournalEntry.from_dict(body)
    return web.Response(status=200)


async def extras_journal_entries_delete(request: web.Request, id) -> web.Response:
    """extras_journal_entries_delete

    

    :param id: A unique integer value identifying this journal entry.
    :type id: int

    """
    return web.Response(status=200)


async def extras_journal_entries_list(request: web.Request, id=None, assigned_object_type_id=None, assigned_object_id=None, created=None, kind=None, last_updated=None, q=None, tag=None, assigned_object_type=None, created_by_id=None, created_by=None, id__n=None, id__lte=None, id__lt=None, id__gte=None, id__gt=None, assigned_object_type_id__n=None, assigned_object_id__n=None, assigned_object_id__lte=None, assigned_object_id__lt=None, assigned_object_id__gte=None, assigned_object_id__gt=None, kind__n=None, last_updated__n=None, last_updated__lte=None, last_updated__lt=None, last_updated__gte=None, last_updated__gt=None, tag__n=None, assigned_object_type__n=None, created_by_id__n=None, created_by__n=None, ordering=None, limit=None, offset=None) -> web.Response:
    """extras_journal_entries_list

    

    :param id: 
    :type id: str
    :param assigned_object_type_id: 
    :type assigned_object_type_id: str
    :param assigned_object_id: 
    :type assigned_object_id: str
    :param created: 
    :type created: str
    :param kind: 
    :type kind: str
    :param last_updated: 
    :type last_updated: str
    :param q: 
    :type q: str
    :param tag: 
    :type tag: str
    :param assigned_object_type: 
    :type assigned_object_type: str
    :param created_by_id: 
    :type created_by_id: str
    :param created_by: 
    :type created_by: str
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
    :param assigned_object_type_id__n: 
    :type assigned_object_type_id__n: str
    :param assigned_object_id__n: 
    :type assigned_object_id__n: str
    :param assigned_object_id__lte: 
    :type assigned_object_id__lte: str
    :param assigned_object_id__lt: 
    :type assigned_object_id__lt: str
    :param assigned_object_id__gte: 
    :type assigned_object_id__gte: str
    :param assigned_object_id__gt: 
    :type assigned_object_id__gt: str
    :param kind__n: 
    :type kind__n: str
    :param last_updated__n: 
    :type last_updated__n: str
    :param last_updated__lte: 
    :type last_updated__lte: str
    :param last_updated__lt: 
    :type last_updated__lt: str
    :param last_updated__gte: 
    :type last_updated__gte: str
    :param last_updated__gt: 
    :type last_updated__gt: str
    :param tag__n: 
    :type tag__n: str
    :param assigned_object_type__n: 
    :type assigned_object_type__n: str
    :param created_by_id__n: 
    :type created_by_id__n: str
    :param created_by__n: 
    :type created_by__n: str
    :param ordering: Which field to use when ordering the results.
    :type ordering: str
    :param limit: Number of results to return per page.
    :type limit: int
    :param offset: The initial index from which to return the results.
    :type offset: int

    """
    return web.Response(status=200)


async def extras_journal_entries_partial_update(request: web.Request, id, body) -> web.Response:
    """extras_journal_entries_partial_update

    

    :param id: A unique integer value identifying this journal entry.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = WritableJournalEntry.from_dict(body)
    return web.Response(status=200)


async def extras_journal_entries_read(request: web.Request, id) -> web.Response:
    """extras_journal_entries_read

    

    :param id: A unique integer value identifying this journal entry.
    :type id: int

    """
    return web.Response(status=200)


async def extras_journal_entries_update(request: web.Request, id, body) -> web.Response:
    """extras_journal_entries_update

    

    :param id: A unique integer value identifying this journal entry.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = WritableJournalEntry.from_dict(body)
    return web.Response(status=200)


async def extras_object_changes_list(request: web.Request, id=None, user=None, user_name=None, request_id=None, action=None, changed_object_type_id=None, changed_object_id=None, object_repr=None, q=None, time=None, changed_object_type=None, user_id=None, id__n=None, id__lte=None, id__lt=None, id__gte=None, id__gt=None, user__n=None, user_name__n=None, user_name__ic=None, user_name__nic=None, user_name__iew=None, user_name__niew=None, user_name__isw=None, user_name__nisw=None, user_name__ie=None, user_name__nie=None, user_name__empty=None, action__n=None, changed_object_type_id__n=None, changed_object_id__n=None, changed_object_id__lte=None, changed_object_id__lt=None, changed_object_id__gte=None, changed_object_id__gt=None, object_repr__n=None, object_repr__ic=None, object_repr__nic=None, object_repr__iew=None, object_repr__niew=None, object_repr__isw=None, object_repr__nisw=None, object_repr__ie=None, object_repr__nie=None, object_repr__empty=None, changed_object_type__n=None, user_id__n=None, ordering=None, limit=None, offset=None) -> web.Response:
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
    :param changed_object_type_id: 
    :type changed_object_type_id: str
    :param changed_object_id: 
    :type changed_object_id: str
    :param object_repr: 
    :type object_repr: str
    :param q: 
    :type q: str
    :param time: 
    :type time: str
    :param changed_object_type: 
    :type changed_object_type: str
    :param user_id: 
    :type user_id: str
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
    :param user_name__empty: 
    :type user_name__empty: str
    :param action__n: 
    :type action__n: str
    :param changed_object_type_id__n: 
    :type changed_object_type_id__n: str
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
    :param object_repr__empty: 
    :type object_repr__empty: str
    :param changed_object_type__n: 
    :type changed_object_type__n: str
    :param user_id__n: 
    :type user_id__n: str
    :param ordering: Which field to use when ordering the results.
    :type ordering: str
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

    Run a Report identified as \&quot;&lt;module&gt;.&lt;script&gt;\&quot; and return the pending JobResult as the result

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def extras_saved_filters_bulk_delete(request: web.Request, ) -> web.Response:
    """extras_saved_filters_bulk_delete

    


    """
    return web.Response(status=200)


async def extras_saved_filters_bulk_partial_update(request: web.Request, body) -> web.Response:
    """extras_saved_filters_bulk_partial_update

    

    :param body: 
    :type body: dict | bytes

    """
    body = SavedFilter.from_dict(body)
    return web.Response(status=200)


async def extras_saved_filters_bulk_update(request: web.Request, body) -> web.Response:
    """extras_saved_filters_bulk_update

    

    :param body: 
    :type body: dict | bytes

    """
    body = SavedFilter.from_dict(body)
    return web.Response(status=200)


async def extras_saved_filters_create(request: web.Request, body) -> web.Response:
    """extras_saved_filters_create

    

    :param body: 
    :type body: dict | bytes

    """
    body = SavedFilter.from_dict(body)
    return web.Response(status=200)


async def extras_saved_filters_delete(request: web.Request, id) -> web.Response:
    """extras_saved_filters_delete

    

    :param id: A unique integer value identifying this saved filter.
    :type id: int

    """
    return web.Response(status=200)


async def extras_saved_filters_list(request: web.Request, id=None, content_types=None, name=None, slug=None, description=None, enabled=None, shared=None, weight=None, q=None, content_type_id=None, user_id=None, user=None, usable=None, id__n=None, id__lte=None, id__lt=None, id__gte=None, id__gt=None, content_types__n=None, content_types__ic=None, content_types__nic=None, content_types__iew=None, content_types__niew=None, content_types__isw=None, content_types__nisw=None, content_types__ie=None, content_types__nie=None, name__n=None, name__ic=None, name__nic=None, name__iew=None, name__niew=None, name__isw=None, name__nisw=None, name__ie=None, name__nie=None, name__empty=None, slug__n=None, slug__ic=None, slug__nic=None, slug__iew=None, slug__niew=None, slug__isw=None, slug__nisw=None, slug__ie=None, slug__nie=None, slug__empty=None, description__n=None, description__ic=None, description__nic=None, description__iew=None, description__niew=None, description__isw=None, description__nisw=None, description__ie=None, description__nie=None, description__empty=None, weight__n=None, weight__lte=None, weight__lt=None, weight__gte=None, weight__gt=None, content_type_id__n=None, content_type_id__lte=None, content_type_id__lt=None, content_type_id__gte=None, content_type_id__gt=None, user_id__n=None, user__n=None, ordering=None, limit=None, offset=None) -> web.Response:
    """extras_saved_filters_list

    

    :param id: 
    :type id: str
    :param content_types: 
    :type content_types: str
    :param name: 
    :type name: str
    :param slug: 
    :type slug: str
    :param description: 
    :type description: str
    :param enabled: 
    :type enabled: str
    :param shared: 
    :type shared: str
    :param weight: 
    :type weight: str
    :param q: 
    :type q: str
    :param content_type_id: 
    :type content_type_id: str
    :param user_id: 
    :type user_id: str
    :param user: 
    :type user: str
    :param usable: 
    :type usable: str
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
    :param content_types__n: 
    :type content_types__n: str
    :param content_types__ic: 
    :type content_types__ic: str
    :param content_types__nic: 
    :type content_types__nic: str
    :param content_types__iew: 
    :type content_types__iew: str
    :param content_types__niew: 
    :type content_types__niew: str
    :param content_types__isw: 
    :type content_types__isw: str
    :param content_types__nisw: 
    :type content_types__nisw: str
    :param content_types__ie: 
    :type content_types__ie: str
    :param content_types__nie: 
    :type content_types__nie: str
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
    :param name__empty: 
    :type name__empty: str
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
    :param slug__empty: 
    :type slug__empty: str
    :param description__n: 
    :type description__n: str
    :param description__ic: 
    :type description__ic: str
    :param description__nic: 
    :type description__nic: str
    :param description__iew: 
    :type description__iew: str
    :param description__niew: 
    :type description__niew: str
    :param description__isw: 
    :type description__isw: str
    :param description__nisw: 
    :type description__nisw: str
    :param description__ie: 
    :type description__ie: str
    :param description__nie: 
    :type description__nie: str
    :param description__empty: 
    :type description__empty: str
    :param weight__n: 
    :type weight__n: str
    :param weight__lte: 
    :type weight__lte: str
    :param weight__lt: 
    :type weight__lt: str
    :param weight__gte: 
    :type weight__gte: str
    :param weight__gt: 
    :type weight__gt: str
    :param content_type_id__n: 
    :type content_type_id__n: str
    :param content_type_id__lte: 
    :type content_type_id__lte: str
    :param content_type_id__lt: 
    :type content_type_id__lt: str
    :param content_type_id__gte: 
    :type content_type_id__gte: str
    :param content_type_id__gt: 
    :type content_type_id__gt: str
    :param user_id__n: 
    :type user_id__n: str
    :param user__n: 
    :type user__n: str
    :param ordering: Which field to use when ordering the results.
    :type ordering: str
    :param limit: Number of results to return per page.
    :type limit: int
    :param offset: The initial index from which to return the results.
    :type offset: int

    """
    return web.Response(status=200)


async def extras_saved_filters_partial_update(request: web.Request, id, body) -> web.Response:
    """extras_saved_filters_partial_update

    

    :param id: A unique integer value identifying this saved filter.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = SavedFilter.from_dict(body)
    return web.Response(status=200)


async def extras_saved_filters_read(request: web.Request, id) -> web.Response:
    """extras_saved_filters_read

    

    :param id: A unique integer value identifying this saved filter.
    :type id: int

    """
    return web.Response(status=200)


async def extras_saved_filters_update(request: web.Request, id, body) -> web.Response:
    """extras_saved_filters_update

    

    :param id: A unique integer value identifying this saved filter.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = SavedFilter.from_dict(body)
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


async def extras_tags_bulk_delete(request: web.Request, ) -> web.Response:
    """extras_tags_bulk_delete

    


    """
    return web.Response(status=200)


async def extras_tags_bulk_partial_update(request: web.Request, body) -> web.Response:
    """extras_tags_bulk_partial_update

    

    :param body: 
    :type body: dict | bytes

    """
    body = Tag.from_dict(body)
    return web.Response(status=200)


async def extras_tags_bulk_update(request: web.Request, body) -> web.Response:
    """extras_tags_bulk_update

    

    :param body: 
    :type body: dict | bytes

    """
    body = Tag.from_dict(body)
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


async def extras_tags_list(request: web.Request, id=None, name=None, slug=None, color=None, description=None, created=None, last_updated=None, q=None, content_type=None, content_type_id=None, id__n=None, id__lte=None, id__lt=None, id__gte=None, id__gt=None, name__n=None, name__ic=None, name__nic=None, name__iew=None, name__niew=None, name__isw=None, name__nisw=None, name__ie=None, name__nie=None, name__empty=None, slug__n=None, slug__ic=None, slug__nic=None, slug__iew=None, slug__niew=None, slug__isw=None, slug__nisw=None, slug__ie=None, slug__nie=None, slug__empty=None, color__n=None, color__ic=None, color__nic=None, color__iew=None, color__niew=None, color__isw=None, color__nisw=None, color__ie=None, color__nie=None, color__empty=None, description__n=None, description__ic=None, description__nic=None, description__iew=None, description__niew=None, description__isw=None, description__nisw=None, description__ie=None, description__nie=None, description__empty=None, created__n=None, created__lte=None, created__lt=None, created__gte=None, created__gt=None, last_updated__n=None, last_updated__lte=None, last_updated__lt=None, last_updated__gte=None, last_updated__gt=None, ordering=None, limit=None, offset=None) -> web.Response:
    """extras_tags_list

    

    :param id: 
    :type id: str
    :param name: 
    :type name: str
    :param slug: 
    :type slug: str
    :param color: 
    :type color: str
    :param description: 
    :type description: str
    :param created: 
    :type created: str
    :param last_updated: 
    :type last_updated: str
    :param q: 
    :type q: str
    :param content_type: 
    :type content_type: str
    :param content_type_id: 
    :type content_type_id: str
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
    :param name__empty: 
    :type name__empty: str
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
    :param slug__empty: 
    :type slug__empty: str
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
    :param color__empty: 
    :type color__empty: str
    :param description__n: 
    :type description__n: str
    :param description__ic: 
    :type description__ic: str
    :param description__nic: 
    :type description__nic: str
    :param description__iew: 
    :type description__iew: str
    :param description__niew: 
    :type description__niew: str
    :param description__isw: 
    :type description__isw: str
    :param description__nisw: 
    :type description__nisw: str
    :param description__ie: 
    :type description__ie: str
    :param description__nie: 
    :type description__nie: str
    :param description__empty: 
    :type description__empty: str
    :param created__n: 
    :type created__n: str
    :param created__lte: 
    :type created__lte: str
    :param created__lt: 
    :type created__lt: str
    :param created__gte: 
    :type created__gte: str
    :param created__gt: 
    :type created__gt: str
    :param last_updated__n: 
    :type last_updated__n: str
    :param last_updated__lte: 
    :type last_updated__lte: str
    :param last_updated__lt: 
    :type last_updated__lt: str
    :param last_updated__gte: 
    :type last_updated__gte: str
    :param last_updated__gt: 
    :type last_updated__gt: str
    :param ordering: Which field to use when ordering the results.
    :type ordering: str
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


async def extras_webhooks_bulk_delete(request: web.Request, ) -> web.Response:
    """extras_webhooks_bulk_delete

    


    """
    return web.Response(status=200)


async def extras_webhooks_bulk_partial_update(request: web.Request, body) -> web.Response:
    """extras_webhooks_bulk_partial_update

    

    :param body: 
    :type body: dict | bytes

    """
    body = Webhook.from_dict(body)
    return web.Response(status=200)


async def extras_webhooks_bulk_update(request: web.Request, body) -> web.Response:
    """extras_webhooks_bulk_update

    

    :param body: 
    :type body: dict | bytes

    """
    body = Webhook.from_dict(body)
    return web.Response(status=200)


async def extras_webhooks_create(request: web.Request, body) -> web.Response:
    """extras_webhooks_create

    

    :param body: 
    :type body: dict | bytes

    """
    body = Webhook.from_dict(body)
    return web.Response(status=200)


async def extras_webhooks_delete(request: web.Request, id) -> web.Response:
    """extras_webhooks_delete

    

    :param id: A unique integer value identifying this webhook.
    :type id: int

    """
    return web.Response(status=200)


async def extras_webhooks_list(request: web.Request, id=None, name=None, type_create=None, type_update=None, type_delete=None, payload_url=None, enabled=None, http_method=None, http_content_type=None, secret=None, ssl_verification=None, ca_file_path=None, q=None, content_type_id=None, content_types=None, id__n=None, id__lte=None, id__lt=None, id__gte=None, id__gt=None, name__n=None, name__ic=None, name__nic=None, name__iew=None, name__niew=None, name__isw=None, name__nisw=None, name__ie=None, name__nie=None, name__empty=None, payload_url__n=None, payload_url__ic=None, payload_url__nic=None, payload_url__iew=None, payload_url__niew=None, payload_url__isw=None, payload_url__nisw=None, payload_url__ie=None, payload_url__nie=None, payload_url__empty=None, http_method__n=None, http_content_type__n=None, http_content_type__ic=None, http_content_type__nic=None, http_content_type__iew=None, http_content_type__niew=None, http_content_type__isw=None, http_content_type__nisw=None, http_content_type__ie=None, http_content_type__nie=None, http_content_type__empty=None, secret__n=None, secret__ic=None, secret__nic=None, secret__iew=None, secret__niew=None, secret__isw=None, secret__nisw=None, secret__ie=None, secret__nie=None, secret__empty=None, ca_file_path__n=None, ca_file_path__ic=None, ca_file_path__nic=None, ca_file_path__iew=None, ca_file_path__niew=None, ca_file_path__isw=None, ca_file_path__nisw=None, ca_file_path__ie=None, ca_file_path__nie=None, ca_file_path__empty=None, content_type_id__n=None, content_type_id__lte=None, content_type_id__lt=None, content_type_id__gte=None, content_type_id__gt=None, content_types__n=None, content_types__ic=None, content_types__nic=None, content_types__iew=None, content_types__niew=None, content_types__isw=None, content_types__nisw=None, content_types__ie=None, content_types__nie=None, ordering=None, limit=None, offset=None) -> web.Response:
    """extras_webhooks_list

    

    :param id: 
    :type id: str
    :param name: 
    :type name: str
    :param type_create: 
    :type type_create: str
    :param type_update: 
    :type type_update: str
    :param type_delete: 
    :type type_delete: str
    :param payload_url: 
    :type payload_url: str
    :param enabled: 
    :type enabled: str
    :param http_method: 
    :type http_method: str
    :param http_content_type: 
    :type http_content_type: str
    :param secret: 
    :type secret: str
    :param ssl_verification: 
    :type ssl_verification: str
    :param ca_file_path: 
    :type ca_file_path: str
    :param q: 
    :type q: str
    :param content_type_id: 
    :type content_type_id: str
    :param content_types: 
    :type content_types: str
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
    :param name__empty: 
    :type name__empty: str
    :param payload_url__n: 
    :type payload_url__n: str
    :param payload_url__ic: 
    :type payload_url__ic: str
    :param payload_url__nic: 
    :type payload_url__nic: str
    :param payload_url__iew: 
    :type payload_url__iew: str
    :param payload_url__niew: 
    :type payload_url__niew: str
    :param payload_url__isw: 
    :type payload_url__isw: str
    :param payload_url__nisw: 
    :type payload_url__nisw: str
    :param payload_url__ie: 
    :type payload_url__ie: str
    :param payload_url__nie: 
    :type payload_url__nie: str
    :param payload_url__empty: 
    :type payload_url__empty: str
    :param http_method__n: 
    :type http_method__n: str
    :param http_content_type__n: 
    :type http_content_type__n: str
    :param http_content_type__ic: 
    :type http_content_type__ic: str
    :param http_content_type__nic: 
    :type http_content_type__nic: str
    :param http_content_type__iew: 
    :type http_content_type__iew: str
    :param http_content_type__niew: 
    :type http_content_type__niew: str
    :param http_content_type__isw: 
    :type http_content_type__isw: str
    :param http_content_type__nisw: 
    :type http_content_type__nisw: str
    :param http_content_type__ie: 
    :type http_content_type__ie: str
    :param http_content_type__nie: 
    :type http_content_type__nie: str
    :param http_content_type__empty: 
    :type http_content_type__empty: str
    :param secret__n: 
    :type secret__n: str
    :param secret__ic: 
    :type secret__ic: str
    :param secret__nic: 
    :type secret__nic: str
    :param secret__iew: 
    :type secret__iew: str
    :param secret__niew: 
    :type secret__niew: str
    :param secret__isw: 
    :type secret__isw: str
    :param secret__nisw: 
    :type secret__nisw: str
    :param secret__ie: 
    :type secret__ie: str
    :param secret__nie: 
    :type secret__nie: str
    :param secret__empty: 
    :type secret__empty: str
    :param ca_file_path__n: 
    :type ca_file_path__n: str
    :param ca_file_path__ic: 
    :type ca_file_path__ic: str
    :param ca_file_path__nic: 
    :type ca_file_path__nic: str
    :param ca_file_path__iew: 
    :type ca_file_path__iew: str
    :param ca_file_path__niew: 
    :type ca_file_path__niew: str
    :param ca_file_path__isw: 
    :type ca_file_path__isw: str
    :param ca_file_path__nisw: 
    :type ca_file_path__nisw: str
    :param ca_file_path__ie: 
    :type ca_file_path__ie: str
    :param ca_file_path__nie: 
    :type ca_file_path__nie: str
    :param ca_file_path__empty: 
    :type ca_file_path__empty: str
    :param content_type_id__n: 
    :type content_type_id__n: str
    :param content_type_id__lte: 
    :type content_type_id__lte: str
    :param content_type_id__lt: 
    :type content_type_id__lt: str
    :param content_type_id__gte: 
    :type content_type_id__gte: str
    :param content_type_id__gt: 
    :type content_type_id__gt: str
    :param content_types__n: 
    :type content_types__n: str
    :param content_types__ic: 
    :type content_types__ic: str
    :param content_types__nic: 
    :type content_types__nic: str
    :param content_types__iew: 
    :type content_types__iew: str
    :param content_types__niew: 
    :type content_types__niew: str
    :param content_types__isw: 
    :type content_types__isw: str
    :param content_types__nisw: 
    :type content_types__nisw: str
    :param content_types__ie: 
    :type content_types__ie: str
    :param content_types__nie: 
    :type content_types__nie: str
    :param ordering: Which field to use when ordering the results.
    :type ordering: str
    :param limit: Number of results to return per page.
    :type limit: int
    :param offset: The initial index from which to return the results.
    :type offset: int

    """
    return web.Response(status=200)


async def extras_webhooks_partial_update(request: web.Request, id, body) -> web.Response:
    """extras_webhooks_partial_update

    

    :param id: A unique integer value identifying this webhook.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = Webhook.from_dict(body)
    return web.Response(status=200)


async def extras_webhooks_read(request: web.Request, id) -> web.Response:
    """extras_webhooks_read

    

    :param id: A unique integer value identifying this webhook.
    :type id: int

    """
    return web.Response(status=200)


async def extras_webhooks_update(request: web.Request, id, body) -> web.Response:
    """extras_webhooks_update

    

    :param id: A unique integer value identifying this webhook.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = Webhook.from_dict(body)
    return web.Response(status=200)
