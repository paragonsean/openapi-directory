from typing import List, Dict
from aiohttp import web

from openapi_server.models.associate_field_configurations_with_issue_types_request import AssociateFieldConfigurationsWithIssueTypesRequest
from openapi_server.models.error_collection import ErrorCollection
from openapi_server.models.field_configuration import FieldConfiguration
from openapi_server.models.field_configuration_details import FieldConfigurationDetails
from openapi_server.models.field_configuration_items_details import FieldConfigurationItemsDetails
from openapi_server.models.field_configuration_scheme import FieldConfigurationScheme
from openapi_server.models.field_configuration_scheme_project_association import FieldConfigurationSchemeProjectAssociation
from openapi_server.models.issue_type_ids_to_remove import IssueTypeIdsToRemove
from openapi_server.models.page_bean_field_configuration_details import PageBeanFieldConfigurationDetails
from openapi_server.models.page_bean_field_configuration_issue_type_item import PageBeanFieldConfigurationIssueTypeItem
from openapi_server.models.page_bean_field_configuration_item import PageBeanFieldConfigurationItem
from openapi_server.models.page_bean_field_configuration_scheme import PageBeanFieldConfigurationScheme
from openapi_server.models.page_bean_field_configuration_scheme_projects import PageBeanFieldConfigurationSchemeProjects
from openapi_server.models.update_field_configuration_scheme_details import UpdateFieldConfigurationSchemeDetails
from openapi_server import util


async def assign_field_configuration_scheme_to_project(request: web.Request, body) -> web.Response:
    """Assign field configuration scheme to project

    Assigns a field configuration scheme to a project. If the field configuration scheme ID is &#x60;null&#x60;, the operation assigns the default field configuration scheme.  Field configuration schemes can only be assigned to classic projects.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    :param body: 
    :type body: dict | bytes

    """
    body = FieldConfigurationSchemeProjectAssociation.from_dict(body)
    return web.Response(status=200)


async def create_field_configuration(request: web.Request, body) -> web.Response:
    """Create field configuration

    Creates a field configuration. The field configuration is created with the same field properties as the default configuration, with all the fields being optional.  This operation can only create configurations for use in company-managed (classic) projects.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    :param body: 
    :type body: dict | bytes

    """
    body = FieldConfigurationDetails.from_dict(body)
    return web.Response(status=200)


async def create_field_configuration_scheme(request: web.Request, body) -> web.Response:
    """Create field configuration scheme

    Creates a field configuration scheme.  This operation can only create field configuration schemes used in company-managed (classic) projects.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    :param body: The details of the field configuration scheme.
    :type body: dict | bytes

    """
    body = UpdateFieldConfigurationSchemeDetails.from_dict(body)
    return web.Response(status=200)


async def delete_field_configuration(request: web.Request, id) -> web.Response:
    """Delete field configuration

    Deletes a field configuration.  This operation can only delete configurations used in company-managed (classic) projects.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    :param id: The ID of the field configuration.
    :type id: int

    """
    return web.Response(status=200)


async def delete_field_configuration_scheme(request: web.Request, id) -> web.Response:
    """Delete field configuration scheme

    Deletes a field configuration scheme.  This operation can only delete field configuration schemes used in company-managed (classic) projects.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    :param id: The ID of the field configuration scheme.
    :type id: int

    """
    return web.Response(status=200)


async def get_all_field_configuration_schemes(request: web.Request, start_at=None, max_results=None, id=None) -> web.Response:
    """Get all field configuration schemes

    Returns a [paginated](#pagination) list of field configuration schemes.  Only field configuration schemes used in classic projects are returned.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    :param start_at: The index of the first item to return in a page of results (page offset).
    :type start_at: int
    :param max_results: The maximum number of items to return per page.
    :type max_results: int
    :param id: The list of field configuration scheme IDs. To include multiple IDs, provide an ampersand-separated list. For example, &#x60;id&#x3D;10000&amp;id&#x3D;10001&#x60;.
    :type id: List[int]

    """
    return web.Response(status=200)


async def get_all_field_configurations(request: web.Request, start_at=None, max_results=None, id=None, is_default=None, query=None) -> web.Response:
    """Get all field configurations

    Returns a [paginated](#pagination) list of field configurations. The list can be for all field configurations or a subset determined by any combination of these criteria:   *  a list of field configuration item IDs.  *  whether the field configuration is a default.  *  whether the field configuration name or description contains a query string.  Only field configurations used in company-managed (classic) projects are returned.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    :param start_at: The index of the first item to return in a page of results (page offset).
    :type start_at: int
    :param max_results: The maximum number of items to return per page.
    :type max_results: int
    :param id: The list of field configuration IDs. To include multiple IDs, provide an ampersand-separated list. For example, &#x60;id&#x3D;10000&amp;id&#x3D;10001&#x60;.
    :type id: List[int]
    :param is_default: If *true* returns default field configurations only.
    :type is_default: bool
    :param query: The query string used to match against field configuration names and descriptions.
    :type query: str

    """
    return web.Response(status=200)


async def get_field_configuration_items(request: web.Request, id, start_at=None, max_results=None) -> web.Response:
    """Get field configuration items

    Returns a [paginated](#pagination) list of all fields for a configuration.  Only the fields from configurations used in company-managed (classic) projects are returned.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    :param id: The ID of the field configuration.
    :type id: int
    :param start_at: The index of the first item to return in a page of results (page offset).
    :type start_at: int
    :param max_results: The maximum number of items to return per page.
    :type max_results: int

    """
    return web.Response(status=200)


async def get_field_configuration_scheme_mappings(request: web.Request, start_at=None, max_results=None, field_configuration_scheme_id=None) -> web.Response:
    """Get field configuration issue type items

    Returns a [paginated](#pagination) list of field configuration issue type items.  Only items used in classic projects are returned.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    :param start_at: The index of the first item to return in a page of results (page offset).
    :type start_at: int
    :param max_results: The maximum number of items to return per page.
    :type max_results: int
    :param field_configuration_scheme_id: The list of field configuration scheme IDs. To include multiple field configuration schemes separate IDs with ampersand: &#x60;fieldConfigurationSchemeId&#x3D;10000&amp;fieldConfigurationSchemeId&#x3D;10001&#x60;.
    :type field_configuration_scheme_id: List[int]

    """
    return web.Response(status=200)


async def get_field_configuration_scheme_project_mapping(request: web.Request, project_id, start_at=None, max_results=None) -> web.Response:
    """Get field configuration schemes for projects

    Returns a [paginated](#pagination) list of field configuration schemes and, for each scheme, a list of the projects that use it.  The list is sorted by field configuration scheme ID. The first item contains the list of project IDs assigned to the default field configuration scheme.  Only field configuration schemes used in classic projects are returned.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    :param project_id: The list of project IDs. To include multiple projects, separate IDs with ampersand: &#x60;projectId&#x3D;10000&amp;projectId&#x3D;10001&#x60;.
    :type project_id: List[int]
    :param start_at: The index of the first item to return in a page of results (page offset).
    :type start_at: int
    :param max_results: The maximum number of items to return per page.
    :type max_results: int

    """
    return web.Response(status=200)


async def remove_issue_types_from_global_field_configuration_scheme(request: web.Request, id, body) -> web.Response:
    """Remove issue types from field configuration scheme

    Removes issue types from the field configuration scheme.  This operation can only modify field configuration schemes used in company-managed (classic) projects.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    :param id: The ID of the field configuration scheme.
    :type id: int
    :param body: The issue type IDs to remove.
    :type body: dict | bytes

    """
    body = IssueTypeIdsToRemove.from_dict(body)
    return web.Response(status=200)


async def set_field_configuration_scheme_mapping(request: web.Request, id, body) -> web.Response:
    """Assign issue types to field configurations

    Assigns issue types to field configurations on field configuration scheme.  This operation can only modify field configuration schemes used in company-managed (classic) projects.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    :param id: The ID of the field configuration scheme.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = AssociateFieldConfigurationsWithIssueTypesRequest.from_dict(body)
    return web.Response(status=200)


async def update_field_configuration(request: web.Request, id, body) -> web.Response:
    """Update field configuration

    Updates a field configuration. The name and the description provided in the request override the existing values.  This operation can only update configurations used in company-managed (classic) projects.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    :param id: The ID of the field configuration.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = FieldConfigurationDetails.from_dict(body)
    return web.Response(status=200)


async def update_field_configuration_items(request: web.Request, id, body) -> web.Response:
    """Update field configuration items

    Updates fields in a field configuration. The properties of the field configuration fields provided override the existing values.  This operation can only update field configurations used in company-managed (classic) projects.  The operation can set the renderer for text fields to the default text renderer (&#x60;text-renderer&#x60;) or wiki style renderer (&#x60;wiki-renderer&#x60;). However, the renderer cannot be updated for fields using the autocomplete renderer (&#x60;autocomplete-renderer&#x60;).  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    :param id: The ID of the field configuration.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = FieldConfigurationItemsDetails.from_dict(body)
    return web.Response(status=200)


async def update_field_configuration_scheme(request: web.Request, id, body) -> web.Response:
    """Update field configuration scheme

    Updates a field configuration scheme.  This operation can only update field configuration schemes used in company-managed (classic) projects.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    :param id: The ID of the field configuration scheme.
    :type id: int
    :param body: The details of the field configuration scheme.
    :type body: dict | bytes

    """
    body = UpdateFieldConfigurationSchemeDetails.from_dict(body)
    return web.Response(status=200)
