# coding: utf-8

import pytest
import json
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


pytestmark = pytest.mark.asyncio

async def test_deletesystem(client):
    """Test case for deletesystem

    Delete system by inventory id
    """
    headers = { 
        'RhIdentity': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/patch/v1/systems/{inventory_id}'.format(inventory_id='inventory_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_detail_advisory(client):
    """Test case for detail_advisory

    Show me details an advisory by given advisory name
    """
    headers = { 
        'Accept': 'application/json',
        'RhIdentity': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/patch/v1/advisories/{advisory_id}'.format(advisory_id='advisory_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_detail_system(client):
    """Test case for detail_system

    Show me details about a system by given inventory id
    """
    headers = { 
        'Accept': 'application/json',
        'RhIdentity': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/patch/v1/systems/{inventory_id}'.format(inventory_id='inventory_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_export_advisories(client):
    """Test case for export_advisories

    Export applicable advisories for all my systems
    """
    params = [('search', 'search_example'),
                    ('filter[id]', 'filter_id_example'),
                    ('filter[description]', 'filter_description_example'),
                    ('filter[public_date]', 'filter_public_date_example'),
                    ('filter[synopsis]', 'filter_synopsis_example'),
                    ('filter[advisory_type]', 'filter_advisory_type_example'),
                    ('filter[severity]', 'filter_severity_example'),
                    ('filter[applicable_systems]', 'filter_applicable_systems_example')]
    headers = { 
        'Accept': 'application/json',
        'RhIdentity': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/patch/v1/export/advisories',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_export_advisory_systems(client):
    """Test case for export_advisory_systems

    Export systems for my account
    """
    params = [('search', 'search_example'),
                    ('filter[id]', 'filter_id_example'),
                    ('filter[display_name]', 'filter_display_name_example'),
                    ('filter[last_evaluation]', 'filter_last_evaluation_example'),
                    ('filter[last_upload]', 'filter_last_upload_example'),
                    ('filter[rhsa_count]', 'filter_rhsa_count_example'),
                    ('filter[rhba_count]', 'filter_rhba_count_example'),
                    ('filter[rhea_count]', 'filter_rhea_count_example'),
                    ('filter[other_count]', 'filter_other_count_example'),
                    ('filter[stale]', 'filter_stale_example'),
                    ('filter[packages_installed]', 'filter_packages_installed_example'),
                    ('filter[packages_updatable]', 'filter_packages_updatable_example'),
                    ('filter[system_profile][sap_system]', 'filter_system_profile_sap_system_example'),
                    ('filter[system_profile][sap_sids][in]', ['filter_system_profile_sap_sids_in_example']),
                    ('tags', ['tags_example'])]
    headers = { 
        'Accept': 'application/json',
        'RhIdentity': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/patch/v1/export/advisories/{advisory_id}/systems'.format(advisory_id='advisory_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_export_package_systems(client):
    """Test case for export_package_systems

    Show me all my systems which have a package installed
    """
    params = [('filter[system_profile][sap_system]', 'filter_system_profile_sap_system_example'),
                    ('filter[system_profile][sap_sids][in]', ['filter_system_profile_sap_sids_in_example']),
                    ('tags', ['tags_example'])]
    headers = { 
        'Accept': 'application/json',
        'RhIdentity': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/patch/v1/export/packages/{package_name}/systems'.format(package_name='package_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_export_packages(client):
    """Test case for export_packages

    Show me all installed packages across my systems
    """
    params = [('sort', 'sort_example'),
                    ('search', 'search_example'),
                    ('filter[name]', 'filter_name_example'),
                    ('filter[systems_installed]', 'filter_systems_installed_example'),
                    ('filter[systems_updatable]', 'filter_systems_updatable_example'),
                    ('filter[summary]', 'filter_summary_example')]
    headers = { 
        'Accept': 'application/json',
        'RhIdentity': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/patch/v1/export/packages',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_export_system_advisories(client):
    """Test case for export_system_advisories

    Export applicable advisories for all my systems
    """
    params = [('search', 'search_example'),
                    ('filter[id]', 'filter_id_example'),
                    ('filter[description]', 'filter_description_example'),
                    ('filter[public_date]', 'filter_public_date_example'),
                    ('filter[synopsis]', 'filter_synopsis_example'),
                    ('filter[advisory_type]', 'filter_advisory_type_example'),
                    ('filter[severity]', 'filter_severity_example')]
    headers = { 
        'Accept': 'application/json',
        'RhIdentity': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/patch/v1/export/systems/{inventory_id}/advisories'.format(inventory_id='inventory_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_export_system_packages(client):
    """Test case for export_system_packages

    Show me details about a system packages by given inventory id
    """
    params = [('search', 'search_example'),
                    ('filter[name]', 'filter_name_example'),
                    ('filter[description]', 'filter_description_example'),
                    ('filter[evra]', 'filter_evra_example'),
                    ('filter[summary]', 'filter_summary_example'),
                    ('filter[updatable]', True)]
    headers = { 
        'Accept': 'application/json',
        'RhIdentity': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/patch/v1/export/systems/{inventory_id}/packages'.format(inventory_id='inventory_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_export_systems(client):
    """Test case for export_systems

    Export systems for my account
    """
    params = [('search', 'search_example'),
                    ('filter[id]', 'filter_id_example'),
                    ('filter[display_name]', 'filter_display_name_example'),
                    ('filter[last_evaluation]', 'filter_last_evaluation_example'),
                    ('filter[last_upload]', 'filter_last_upload_example'),
                    ('filter[rhsa_count]', 'filter_rhsa_count_example'),
                    ('filter[rhba_count]', 'filter_rhba_count_example'),
                    ('filter[rhea_count]', 'filter_rhea_count_example'),
                    ('filter[other_count]', 'filter_other_count_example'),
                    ('filter[stale]', 'filter_stale_example'),
                    ('filter[packages_installed]', 'filter_packages_installed_example'),
                    ('filter[packages_updatable]', 'filter_packages_updatable_example'),
                    ('filter[system_profile][sap_system]', 'filter_system_profile_sap_system_example'),
                    ('filter[system_profile][sap_sids][in]', ['filter_system_profile_sap_sids_in_example']),
                    ('tags', ['tags_example'])]
    headers = { 
        'Accept': 'application/json',
        'RhIdentity': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/patch/v1/export/systems',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_latest_package(client):
    """Test case for latest_package

    Show me metadata of selected package
    """
    headers = { 
        'Accept': 'application/json',
        'RhIdentity': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/patch/v1/packages/{package_name}'.format(package_name='package_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_advisories(client):
    """Test case for list_advisories

    Show me all applicable advisories for all my systems
    """
    params = [('limit', 56),
                    ('offset', 56),
                    ('sort', 'sort_example'),
                    ('search', 'search_example'),
                    ('filter[id]', 'filter_id_example'),
                    ('filter[description]', 'filter_description_example'),
                    ('filter[public_date]', 'filter_public_date_example'),
                    ('filter[synopsis]', 'filter_synopsis_example'),
                    ('filter[advisory_type]', 'filter_advisory_type_example'),
                    ('filter[severity]', 'filter_severity_example'),
                    ('filter[applicable_systems]', 'filter_applicable_systems_example'),
                    ('tags', ['tags_example']),
                    ('filter[system_profile][sap_system]', 'filter_system_profile_sap_system_example'),
                    ('filter[system_profile][sap_sids][in]', ['filter_system_profile_sap_sids_in_example'])]
    headers = { 
        'Accept': 'application/json',
        'RhIdentity': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/patch/v1/advisories',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_advisory_systems(client):
    """Test case for list_advisory_systems

    Show me systems on which the given advisory is applicable
    """
    params = [('limit', 56),
                    ('offset', 56),
                    ('sort', 'sort_example'),
                    ('search', 'search_example'),
                    ('filter[id]', 'filter_id_example'),
                    ('filter[insights_id]', 'filter_insights_id_example'),
                    ('filter[display_name]', 'filter_display_name_example'),
                    ('filter[last_evaluation]', 'filter_last_evaluation_example'),
                    ('filter[last_upload]', 'filter_last_upload_example'),
                    ('filter[rhsa_count]', 'filter_rhsa_count_example'),
                    ('filter[rhba_count]', 'filter_rhba_count_example'),
                    ('filter[rhea_count]', 'filter_rhea_count_example'),
                    ('filter[other_count]', 'filter_other_count_example'),
                    ('filter[stale]', 'filter_stale_example'),
                    ('filter[stale_timestamp]', 'filter_stale_timestamp_example'),
                    ('filter[stale_warning_timestamp]', 'filter_stale_warning_timestamp_example'),
                    ('filter[culled_timestamp]', 'filter_culled_timestamp_example'),
                    ('filter[created]', 'filter_created_example'),
                    ('tags', ['tags_example']),
                    ('filter[system_profile][sap_system]', 'filter_system_profile_sap_system_example'),
                    ('filter[system_profile][sap_sids][in]', ['filter_system_profile_sap_sids_in_example'])]
    headers = { 
        'Accept': 'application/json',
        'RhIdentity': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/patch/v1/advisories/{advisory_id}/systems'.format(advisory_id='advisory_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_packages(client):
    """Test case for list_packages

    Show me all installed packages across my systems
    """
    params = [('limit', 56),
                    ('offset', 56),
                    ('sort', 'sort_example'),
                    ('search', 'search_example'),
                    ('filter[name]', 'filter_name_example'),
                    ('filter[systems_installed]', 'filter_systems_installed_example'),
                    ('filter[systems_updatable]', 'filter_systems_updatable_example'),
                    ('filter[summary]', 'filter_summary_example'),
                    ('tags', ['tags_example']),
                    ('filter[system_profile][sap_system]', 'filter_system_profile_sap_system_example'),
                    ('filter[system_profile][sap_sids][in]', ['filter_system_profile_sap_sids_in_example'])]
    headers = { 
        'Accept': 'application/json',
        'RhIdentity': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/patch/v1/packages/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_system_advisories(client):
    """Test case for list_system_advisories

    Show me advisories for a system by given inventory id
    """
    params = [('limit', 56),
                    ('offset', 56),
                    ('sort', 'sort_example'),
                    ('search', 'search_example'),
                    ('filter[id]', 'filter_id_example'),
                    ('filter[description]', 'filter_description_example'),
                    ('filter[public_date]', 'filter_public_date_example'),
                    ('filter[synopsis]', 'filter_synopsis_example'),
                    ('filter[advisory_type]', 'filter_advisory_type_example'),
                    ('filter[severity]', 'filter_severity_example')]
    headers = { 
        'Accept': 'application/json',
        'RhIdentity': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/patch/v1/systems/{inventory_id}/advisories'.format(inventory_id='inventory_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_systems(client):
    """Test case for list_systems

    Show me all my systems
    """
    params = [('limit', 56),
                    ('offset', 56),
                    ('sort', 'sort_example'),
                    ('search', 'search_example'),
                    ('filter[insights_id]', 'filter_insights_id_example'),
                    ('filter[id]', 'filter_id_example'),
                    ('filter[display_name]', 'filter_display_name_example'),
                    ('filter[last_evaluation]', 'filter_last_evaluation_example'),
                    ('filter[last_upload]', 'filter_last_upload_example'),
                    ('filter[rhsa_count]', 'filter_rhsa_count_example'),
                    ('filter[rhba_count]', 'filter_rhba_count_example'),
                    ('filter[rhea_count]', 'filter_rhea_count_example'),
                    ('filter[other_count]', 'filter_other_count_example'),
                    ('filter[stale]', 'filter_stale_example'),
                    ('filter[packages_installed]', 'filter_packages_installed_example'),
                    ('filter[packages_updatable]', 'filter_packages_updatable_example'),
                    ('filter[stale_timestamp]', 'filter_stale_timestamp_example'),
                    ('filter[stale_warning_timestamp]', 'filter_stale_warning_timestamp_example'),
                    ('filter[culled_timestamp]', 'filter_culled_timestamp_example'),
                    ('filter[created]', 'filter_created_example'),
                    ('tags', ['tags_example']),
                    ('filter[system_profile][sap_system]', 'filter_system_profile_sap_system_example'),
                    ('filter[system_profile][sap_sids][in]', ['filter_system_profile_sap_sids_in_example'])]
    headers = { 
        'Accept': 'application/json',
        'RhIdentity': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/patch/v1/systems',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_package_systems(client):
    """Test case for package_systems

    Show me all my systems which have a package installed
    """
    params = [('limit', 56),
                    ('offset', 56),
                    ('tags', ['tags_example']),
                    ('filter[system_profile][sap_system]', 'filter_system_profile_sap_system_example'),
                    ('filter[system_profile][sap_sids][in]', ['filter_system_profile_sap_sids_in_example'])]
    headers = { 
        'Accept': 'application/json',
        'RhIdentity': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/patch/v1/packages/{package_name}/systems'.format(package_name='package_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_package_versions(client):
    """Test case for package_versions

    Show me all package versions installed on some system
    """
    params = [('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
        'RhIdentity': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/patch/v1/packages/{package_name}/versions'.format(package_name='package_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_system_packages(client):
    """Test case for system_packages

    Show me details about a system packages by given inventory id
    """
    params = [('limit', 56),
                    ('offset', 56),
                    ('search', 'search_example'),
                    ('filter[name]', 'filter_name_example'),
                    ('filter[description]', 'filter_description_example'),
                    ('filter[evra]', 'filter_evra_example'),
                    ('filter[summary]', 'filter_summary_example'),
                    ('filter[updatable]', True)]
    headers = { 
        'Accept': 'application/json',
        'RhIdentity': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/patch/v1/systems/{inventory_id}/packages'.format(inventory_id='inventory_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_view_advisories_systems(client):
    """Test case for view_advisories_systems

    View advisory-system pairs for selected systems and advisories
    """
    body = openapi_server.ControllersSystemsAdvisoriesRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'RhIdentity': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/patch/v1/views/advisories/systems',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_view_systems_advisories(client):
    """Test case for view_systems_advisories

    View system-advisory pairs for selected systems and advisories
    """
    body = openapi_server.ControllersSystemsAdvisoriesRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'RhIdentity': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/patch/v1/views/systems/advisories',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

