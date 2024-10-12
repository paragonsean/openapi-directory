from typing import List, Dict
from aiohttp import web

from openapi_server.models.controllers_advisories_response import ControllersAdvisoriesResponse
from openapi_server.models.controllers_advisories_systems_response import ControllersAdvisoriesSystemsResponse
from openapi_server.models.controllers_advisory_detail_response import ControllersAdvisoryDetailResponse
from openapi_server.models.controllers_advisory_inline_item import ControllersAdvisoryInlineItem
from openapi_server.models.controllers_advisory_systems_response import ControllersAdvisorySystemsResponse
from openapi_server.models.controllers_package_detail_response import ControllersPackageDetailResponse
from openapi_server.models.controllers_package_item import ControllersPackageItem
from openapi_server.models.controllers_package_system_item import ControllersPackageSystemItem
from openapi_server.models.controllers_package_systems_response import ControllersPackageSystemsResponse
from openapi_server.models.controllers_package_versions_response import ControllersPackageVersionsResponse
from openapi_server.models.controllers_packages_response import ControllersPackagesResponse
from openapi_server.models.controllers_system_advisories_db_lookup import ControllersSystemAdvisoriesDBLookup
from openapi_server.models.controllers_system_advisories_response import ControllersSystemAdvisoriesResponse
from openapi_server.models.controllers_system_detail_response import ControllersSystemDetailResponse
from openapi_server.models.controllers_system_inline_item import ControllersSystemInlineItem
from openapi_server.models.controllers_system_package_inline import ControllersSystemPackageInline
from openapi_server.models.controllers_system_package_response import ControllersSystemPackageResponse
from openapi_server.models.controllers_systems_advisories_request import ControllersSystemsAdvisoriesRequest
from openapi_server.models.controllers_systems_advisories_response import ControllersSystemsAdvisoriesResponse
from openapi_server.models.controllers_systems_response import ControllersSystemsResponse
from openapi_server import util


async def deletesystem(request: web.Request, inventory_id) -> web.Response:
    """Delete system by inventory id

    Delete system by inventory id

    :param inventory_id: Inventory ID
    :type inventory_id: str

    """
    return web.Response(status=200)


async def detail_advisory(request: web.Request, advisory_id) -> web.Response:
    """Show me details an advisory by given advisory name

    Show me details an advisory by given advisory name

    :param advisory_id: Advisory ID
    :type advisory_id: str

    """
    return web.Response(status=200)


async def detail_system(request: web.Request, inventory_id) -> web.Response:
    """Show me details about a system by given inventory id

    Show me details about a system by given inventory id

    :param inventory_id: Inventory ID
    :type inventory_id: str

    """
    return web.Response(status=200)


async def export_advisories(request: web.Request, search=None, filter_id=None, filter_description=None, filter_public_date=None, filter_synopsis=None, filter_advisory_type=None, filter_severity=None, filter_applicable_systems=None) -> web.Response:
    """Export applicable advisories for all my systems

    Export applicable advisories for all my systems

    :param search: Find matching text
    :type search: str
    :param filter_id: Filter
    :type filter_id: str
    :param filter_description: Filter
    :type filter_description: str
    :param filter_public_date: Filter
    :type filter_public_date: str
    :param filter_synopsis: Filter
    :type filter_synopsis: str
    :param filter_advisory_type: Filter
    :type filter_advisory_type: str
    :param filter_severity: Filter
    :type filter_severity: str
    :param filter_applicable_systems: Filter
    :type filter_applicable_systems: str

    """
    return web.Response(status=200)


async def export_advisory_systems(request: web.Request, advisory_id, search=None, filter_id=None, filter_display_name=None, filter_last_evaluation=None, filter_last_upload=None, filter_rhsa_count=None, filter_rhba_count=None, filter_rhea_count=None, filter_other_count=None, filter_stale=None, filter_packages_installed=None, filter_packages_updatable=None, filter_system_profile_sap_system=None, filter_system_profile_sap_sids_in=None, tags=None) -> web.Response:
    """Export systems for my account

    Export systems for my account

    :param advisory_id: Advisory ID
    :type advisory_id: str
    :param search: Find matching text
    :type search: str
    :param filter_id: Filter
    :type filter_id: str
    :param filter_display_name: Filter
    :type filter_display_name: str
    :param filter_last_evaluation: Filter
    :type filter_last_evaluation: str
    :param filter_last_upload: Filter
    :type filter_last_upload: str
    :param filter_rhsa_count: Filter
    :type filter_rhsa_count: str
    :param filter_rhba_count: Filter
    :type filter_rhba_count: str
    :param filter_rhea_count: Filter
    :type filter_rhea_count: str
    :param filter_other_count: Filter
    :type filter_other_count: str
    :param filter_stale: Filter
    :type filter_stale: str
    :param filter_packages_installed: Filter
    :type filter_packages_installed: str
    :param filter_packages_updatable: Filter
    :type filter_packages_updatable: str
    :param filter_system_profile_sap_system: Filter only SAP systems
    :type filter_system_profile_sap_system: str
    :param filter_system_profile_sap_sids_in: Filter systems by their SAP SIDs
    :type filter_system_profile_sap_sids_in: List[str]
    :param tags: Tag filter
    :type tags: List[str]

    """
    return web.Response(status=200)


async def export_package_systems(request: web.Request, package_name, filter_system_profile_sap_system=None, filter_system_profile_sap_sids_in=None, tags=None) -> web.Response:
    """Show me all my systems which have a package installed

    Show me all my systems which have a package installed

    :param package_name: Package name
    :type package_name: str
    :param filter_system_profile_sap_system: Filter only SAP systems
    :type filter_system_profile_sap_system: str
    :param filter_system_profile_sap_sids_in: Filter systems by their SAP SIDs
    :type filter_system_profile_sap_sids_in: List[str]
    :param tags: Tag filter
    :type tags: List[str]

    """
    return web.Response(status=200)


async def export_packages(request: web.Request, sort=None, search=None, filter_name=None, filter_systems_installed=None, filter_systems_updatable=None, filter_summary=None) -> web.Response:
    """Show me all installed packages across my systems

    Show me all installed packages across my systems

    :param sort: Sort field
    :type sort: str
    :param search: Find matching text
    :type search: str
    :param filter_name: Filter
    :type filter_name: str
    :param filter_systems_installed: Filter
    :type filter_systems_installed: str
    :param filter_systems_updatable: Filter
    :type filter_systems_updatable: str
    :param filter_summary: Filter
    :type filter_summary: str

    """
    return web.Response(status=200)


async def export_system_advisories(request: web.Request, inventory_id, search=None, filter_id=None, filter_description=None, filter_public_date=None, filter_synopsis=None, filter_advisory_type=None, filter_severity=None) -> web.Response:
    """Export applicable advisories for all my systems

    Export applicable advisories for all my systems

    :param inventory_id: Inventory ID
    :type inventory_id: str
    :param search: Find matching text
    :type search: str
    :param filter_id: Filter
    :type filter_id: str
    :param filter_description: Filter
    :type filter_description: str
    :param filter_public_date: Filter
    :type filter_public_date: str
    :param filter_synopsis: Filter
    :type filter_synopsis: str
    :param filter_advisory_type: Filter
    :type filter_advisory_type: str
    :param filter_severity: Filter
    :type filter_severity: str

    """
    return web.Response(status=200)


async def export_system_packages(request: web.Request, inventory_id, search=None, filter_name=None, filter_description=None, filter_evra=None, filter_summary=None, filter_updatable=None) -> web.Response:
    """Show me details about a system packages by given inventory id

    Show me details about a system packages by given inventory id

    :param inventory_id: Inventory ID
    :type inventory_id: str
    :param search: Find matching text
    :type search: str
    :param filter_name: Filter
    :type filter_name: str
    :param filter_description: Filter
    :type filter_description: str
    :param filter_evra: Filter
    :type filter_evra: str
    :param filter_summary: Filter
    :type filter_summary: str
    :param filter_updatable: Filter
    :type filter_updatable: bool

    """
    return web.Response(status=200)


async def export_systems(request: web.Request, search=None, filter_id=None, filter_display_name=None, filter_last_evaluation=None, filter_last_upload=None, filter_rhsa_count=None, filter_rhba_count=None, filter_rhea_count=None, filter_other_count=None, filter_stale=None, filter_packages_installed=None, filter_packages_updatable=None, filter_system_profile_sap_system=None, filter_system_profile_sap_sids_in=None, tags=None) -> web.Response:
    """Export systems for my account

    Export systems for my account

    :param search: Find matching text
    :type search: str
    :param filter_id: Filter
    :type filter_id: str
    :param filter_display_name: Filter
    :type filter_display_name: str
    :param filter_last_evaluation: Filter
    :type filter_last_evaluation: str
    :param filter_last_upload: Filter
    :type filter_last_upload: str
    :param filter_rhsa_count: Filter
    :type filter_rhsa_count: str
    :param filter_rhba_count: Filter
    :type filter_rhba_count: str
    :param filter_rhea_count: Filter
    :type filter_rhea_count: str
    :param filter_other_count: Filter
    :type filter_other_count: str
    :param filter_stale: Filter
    :type filter_stale: str
    :param filter_packages_installed: Filter
    :type filter_packages_installed: str
    :param filter_packages_updatable: Filter
    :type filter_packages_updatable: str
    :param filter_system_profile_sap_system: Filter only SAP systems
    :type filter_system_profile_sap_system: str
    :param filter_system_profile_sap_sids_in: Filter systems by their SAP SIDs
    :type filter_system_profile_sap_sids_in: List[str]
    :param tags: Tag filter
    :type tags: List[str]

    """
    return web.Response(status=200)


async def latest_package(request: web.Request, package_name) -> web.Response:
    """Show me metadata of selected package

    Show me metadata of selected package

    :param package_name: package_name - latest, nevra - exact version
    :type package_name: str

    """
    return web.Response(status=200)


async def list_advisories(request: web.Request, limit=None, offset=None, sort=None, search=None, filter_id=None, filter_description=None, filter_public_date=None, filter_synopsis=None, filter_advisory_type=None, filter_severity=None, filter_applicable_systems=None, tags=None, filter_system_profile_sap_system=None, filter_system_profile_sap_sids_in=None) -> web.Response:
    """Show me all applicable advisories for all my systems

    Show me all applicable advisories for all my systems

    :param limit: Limit for paging, set -1 to return all
    :type limit: int
    :param offset: Offset for paging
    :type offset: int
    :param sort: Sort field
    :type sort: str
    :param search: Find matching text
    :type search: str
    :param filter_id: Filter 
    :type filter_id: str
    :param filter_description: Filter
    :type filter_description: str
    :param filter_public_date: Filter
    :type filter_public_date: str
    :param filter_synopsis: Filter
    :type filter_synopsis: str
    :param filter_advisory_type: Filter
    :type filter_advisory_type: str
    :param filter_severity: Filter
    :type filter_severity: str
    :param filter_applicable_systems: Filter
    :type filter_applicable_systems: str
    :param tags: Tag filter
    :type tags: List[str]
    :param filter_system_profile_sap_system: Filter only SAP systems
    :type filter_system_profile_sap_system: str
    :param filter_system_profile_sap_sids_in: Filter systems by their SAP SIDs
    :type filter_system_profile_sap_sids_in: List[str]

    """
    return web.Response(status=200)


async def list_advisory_systems(request: web.Request, advisory_id, limit=None, offset=None, sort=None, search=None, filter_id=None, filter_insights_id=None, filter_display_name=None, filter_last_evaluation=None, filter_last_upload=None, filter_rhsa_count=None, filter_rhba_count=None, filter_rhea_count=None, filter_other_count=None, filter_stale=None, filter_stale_timestamp=None, filter_stale_warning_timestamp=None, filter_culled_timestamp=None, filter_created=None, tags=None, filter_system_profile_sap_system=None, filter_system_profile_sap_sids_in=None) -> web.Response:
    """Show me systems on which the given advisory is applicable

    Show me systems on which the given advisory is applicable

    :param advisory_id: Advisory ID
    :type advisory_id: str
    :param limit: Limit for paging, set -1 to return all
    :type limit: int
    :param offset: Offset for paging
    :type offset: int
    :param sort: Sort field
    :type sort: str
    :param search: Find matching text
    :type search: str
    :param filter_id: Filter
    :type filter_id: str
    :param filter_insights_id: Filter
    :type filter_insights_id: str
    :param filter_display_name: Filter
    :type filter_display_name: str
    :param filter_last_evaluation: Filter
    :type filter_last_evaluation: str
    :param filter_last_upload: Filter
    :type filter_last_upload: str
    :param filter_rhsa_count: Filter
    :type filter_rhsa_count: str
    :param filter_rhba_count: Filter
    :type filter_rhba_count: str
    :param filter_rhea_count: Filter
    :type filter_rhea_count: str
    :param filter_other_count: Filter
    :type filter_other_count: str
    :param filter_stale: Filter
    :type filter_stale: str
    :param filter_stale_timestamp: Filter
    :type filter_stale_timestamp: str
    :param filter_stale_warning_timestamp: Filter
    :type filter_stale_warning_timestamp: str
    :param filter_culled_timestamp: Filter
    :type filter_culled_timestamp: str
    :param filter_created: Filter
    :type filter_created: str
    :param tags: Tag filter
    :type tags: List[str]
    :param filter_system_profile_sap_system: Filter only SAP systems
    :type filter_system_profile_sap_system: str
    :param filter_system_profile_sap_sids_in: Filter systems by their SAP SIDs
    :type filter_system_profile_sap_sids_in: List[str]

    """
    return web.Response(status=200)


async def list_packages(request: web.Request, limit=None, offset=None, sort=None, search=None, filter_name=None, filter_systems_installed=None, filter_systems_updatable=None, filter_summary=None, tags=None, filter_system_profile_sap_system=None, filter_system_profile_sap_sids_in=None) -> web.Response:
    """Show me all installed packages across my systems

    Show me all installed packages across my systems

    :param limit: Limit for paging, set -1 to return all
    :type limit: int
    :param offset: Offset for paging
    :type offset: int
    :param sort: Sort field
    :type sort: str
    :param search: Find matching text
    :type search: str
    :param filter_name: Filter
    :type filter_name: str
    :param filter_systems_installed: Filter
    :type filter_systems_installed: str
    :param filter_systems_updatable: Filter
    :type filter_systems_updatable: str
    :param filter_summary: Filter
    :type filter_summary: str
    :param tags: Tag filter
    :type tags: List[str]
    :param filter_system_profile_sap_system: Filter only SAP systems
    :type filter_system_profile_sap_system: str
    :param filter_system_profile_sap_sids_in: Filter systems by their SAP SIDs
    :type filter_system_profile_sap_sids_in: List[str]

    """
    return web.Response(status=200)


async def list_system_advisories(request: web.Request, inventory_id, limit=None, offset=None, sort=None, search=None, filter_id=None, filter_description=None, filter_public_date=None, filter_synopsis=None, filter_advisory_type=None, filter_severity=None) -> web.Response:
    """Show me advisories for a system by given inventory id

    Show me advisories for a system by given inventory id

    :param inventory_id: Inventory ID
    :type inventory_id: str
    :param limit: Limit for paging, set -1 to return all
    :type limit: int
    :param offset: Offset for paging
    :type offset: int
    :param sort: Sort field
    :type sort: str
    :param search: Find matching text
    :type search: str
    :param filter_id: Filter
    :type filter_id: str
    :param filter_description: Filter
    :type filter_description: str
    :param filter_public_date: Filter
    :type filter_public_date: str
    :param filter_synopsis: Filter
    :type filter_synopsis: str
    :param filter_advisory_type: Filter
    :type filter_advisory_type: str
    :param filter_severity: Filter
    :type filter_severity: str

    """
    return web.Response(status=200)


async def list_systems(request: web.Request, limit=None, offset=None, sort=None, search=None, filter_insights_id=None, filter_id=None, filter_display_name=None, filter_last_evaluation=None, filter_last_upload=None, filter_rhsa_count=None, filter_rhba_count=None, filter_rhea_count=None, filter_other_count=None, filter_stale=None, filter_packages_installed=None, filter_packages_updatable=None, filter_stale_timestamp=None, filter_stale_warning_timestamp=None, filter_culled_timestamp=None, filter_created=None, tags=None, filter_system_profile_sap_system=None, filter_system_profile_sap_sids_in=None) -> web.Response:
    """Show me all my systems

    Show me all my systems

    :param limit: Limit for paging, set -1 to return all
    :type limit: int
    :param offset: Offset for paging
    :type offset: int
    :param sort: Sort field
    :type sort: str
    :param search: Find matching text
    :type search: str
    :param filter_insights_id: Filter
    :type filter_insights_id: str
    :param filter_id: Filter
    :type filter_id: str
    :param filter_display_name: Filter
    :type filter_display_name: str
    :param filter_last_evaluation: Filter
    :type filter_last_evaluation: str
    :param filter_last_upload: Filter
    :type filter_last_upload: str
    :param filter_rhsa_count: Filter
    :type filter_rhsa_count: str
    :param filter_rhba_count: Filter
    :type filter_rhba_count: str
    :param filter_rhea_count: Filter
    :type filter_rhea_count: str
    :param filter_other_count: Filter
    :type filter_other_count: str
    :param filter_stale: Filter
    :type filter_stale: str
    :param filter_packages_installed: Filter
    :type filter_packages_installed: str
    :param filter_packages_updatable: Filter
    :type filter_packages_updatable: str
    :param filter_stale_timestamp: Filter
    :type filter_stale_timestamp: str
    :param filter_stale_warning_timestamp: Filter
    :type filter_stale_warning_timestamp: str
    :param filter_culled_timestamp: Filter
    :type filter_culled_timestamp: str
    :param filter_created: Filter
    :type filter_created: str
    :param tags: Tag filter
    :type tags: List[str]
    :param filter_system_profile_sap_system: Filter only SAP systems
    :type filter_system_profile_sap_system: str
    :param filter_system_profile_sap_sids_in: Filter systems by their SAP SIDs
    :type filter_system_profile_sap_sids_in: List[str]

    """
    return web.Response(status=200)


async def package_systems(request: web.Request, package_name, limit=None, offset=None, tags=None, filter_system_profile_sap_system=None, filter_system_profile_sap_sids_in=None) -> web.Response:
    """Show me all my systems which have a package installed

    Show me all my systems which have a package installed

    :param package_name: Package name
    :type package_name: str
    :param limit: Limit for paging, set -1 to return all
    :type limit: int
    :param offset: Offset for paging
    :type offset: int
    :param tags: Tag filter
    :type tags: List[str]
    :param filter_system_profile_sap_system: Filter only SAP systems
    :type filter_system_profile_sap_system: str
    :param filter_system_profile_sap_sids_in: Filter systems by their SAP SIDs
    :type filter_system_profile_sap_sids_in: List[str]

    """
    return web.Response(status=200)


async def package_versions(request: web.Request, package_name, limit=None, offset=None) -> web.Response:
    """Show me all package versions installed on some system

    Show me all package versions installed on some system

    :param package_name: Package name
    :type package_name: str
    :param limit: Limit for paging, set -1 to return all
    :type limit: int
    :param offset: Offset for paging
    :type offset: int

    """
    return web.Response(status=200)


async def system_packages(request: web.Request, inventory_id, limit=None, offset=None, search=None, filter_name=None, filter_description=None, filter_evra=None, filter_summary=None, filter_updatable=None) -> web.Response:
    """Show me details about a system packages by given inventory id

    Show me details about a system packages by given inventory id

    :param inventory_id: Inventory ID
    :type inventory_id: str
    :param limit: Limit for paging, set -1 to return all
    :type limit: int
    :param offset: Offset for paging
    :type offset: int
    :param search: Find matching text
    :type search: str
    :param filter_name: Filter
    :type filter_name: str
    :param filter_description: Filter
    :type filter_description: str
    :param filter_evra: Filter
    :type filter_evra: str
    :param filter_summary: Filter
    :type filter_summary: str
    :param filter_updatable: Filter
    :type filter_updatable: bool

    """
    return web.Response(status=200)


async def view_advisories_systems(request: web.Request, body) -> web.Response:
    """View advisory-system pairs for selected systems and advisories

    View advisory-system pairs for selected systems and advisories

    :param body: Request body
    :type body: dict | bytes

    """
    body = ControllersSystemsAdvisoriesRequest.from_dict(body)
    return web.Response(status=200)


async def view_systems_advisories(request: web.Request, body) -> web.Response:
    """View system-advisory pairs for selected systems and advisories

    View system-advisory pairs for selected systems and advisories

    :param body: Request body
    :type body: dict | bytes

    """
    body = ControllersSystemsAdvisoriesRequest.from_dict(body)
    return web.Response(status=200)
