# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.exception_model import ExceptionModel
from openapi_server.models.license_user_type import LicenseUserType
from openapi_server.models.resource_allocation_criteria_model import ResourceAllocationCriteriaModel
from openapi_server.models.resource_allocation_output_model import ResourceAllocationOutputModel
from openapi_server.models.role_allocation_output_model import RoleAllocationOutputModel
from openapi_server.models.sales_progress import SalesProgress


pytestmark = pytest.mark.asyncio

async def test_resource_allocations_get_resource_allocation(client):
    """Test case for resource_allocations_get_resource_allocation

    Get resource allocation by ID
    """
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/resourceallocations/{guid}'.format(guid='guid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_resource_allocations_get_resource_allocations(client):
    """Test case for resource_allocations_get_resource_allocations

    Get resource allocations
    """
    params = [('rowCount', 56),
                    ('pageToken', 'page_token_example'),
                    ('changedSince', '2013-10-20T19:20:30+01:00')]
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/resourceallocations',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_resource_allocations_get_resource_allocations_by_phase_guid(client):
    """Test case for resource_allocations_get_resource_allocations_by_phase_guid

    Get resource allocations for a phase with required filters (startDate and endDate or changedSince, max 30 days to be fetched at once)
    """
    params = [('startDate', '2013-10-20T19:20:30+01:00'),
                    ('endDate', '2013-10-20T19:20:30+01:00'),
                    ('changedSince', '2013-10-20T19:20:30+01:00'),
                    ('userLicenseTypes', [openapi_server.LicenseUserType()]),
                    ('projectGuid', 'project_guid_example'),
                    ('userGuid', 'user_guid_example'),
                    ('projectBusinessUnitGuid', 'project_business_unit_guid_example'),
                    ('userBusinessUnitGuid', 'user_business_unit_guid_example'),
                    ('projectManagerUserGuid', 'project_manager_user_guid_example'),
                    ('userTagGuid', 'user_tag_guid_example'),
                    ('useSalesProbability', True),
                    ('projectStatusTypeGuid', 'project_status_type_guid_example'),
                    ('projectTagGuid', 'project_tag_guid_example'),
                    ('superiorUserGuid', 'superior_user_guid_example'),
                    ('salesStatusTypeGuid', 'sales_status_type_guid_example'),
                    ('resourceAllocationGuid', 'resource_allocation_guid_example'),
                    ('salesProgress', openapi_server.SalesProgress()),
                    ('rowCount', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/phases/{phase_guid}/resourceallocations/allocations'.format(phase_guid='phase_guid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_resource_allocations_get_resource_allocations_by_project_guid(client):
    """Test case for resource_allocations_get_resource_allocations_by_project_guid

    Get resource allocations for a project with required filters (startDate and endDate or changedSince, max 30 days to be fetched at once)
    """
    params = [('startDate', '2013-10-20T19:20:30+01:00'),
                    ('endDate', '2013-10-20T19:20:30+01:00'),
                    ('changedSince', '2013-10-20T19:20:30+01:00'),
                    ('userLicenseTypes', [openapi_server.LicenseUserType()]),
                    ('phaseGuid', 'phase_guid_example'),
                    ('userGuid', 'user_guid_example'),
                    ('projectBusinessUnitGuid', 'project_business_unit_guid_example'),
                    ('userBusinessUnitGuid', 'user_business_unit_guid_example'),
                    ('projectManagerUserGuid', 'project_manager_user_guid_example'),
                    ('userTagGuid', 'user_tag_guid_example'),
                    ('useSalesProbability', True),
                    ('projectStatusTypeGuid', 'project_status_type_guid_example'),
                    ('projectTagGuid', 'project_tag_guid_example'),
                    ('superiorUserGuid', 'superior_user_guid_example'),
                    ('salesStatusTypeGuid', 'sales_status_type_guid_example'),
                    ('resourceAllocationGuid', 'resource_allocation_guid_example'),
                    ('salesProgress', openapi_server.SalesProgress()),
                    ('rowCount', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/projects/{project_guid}/resourceallocations/allocations'.format(project_guid='project_guid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_resource_allocations_get_resource_allocations_by_user_guid(client):
    """Test case for resource_allocations_get_resource_allocations_by_user_guid

    Get resource allocations for a user with required filters (startDate and endDate or changedSince, max 30 days to be fetched at once)
    """
    params = [('startDate', '2013-10-20T19:20:30+01:00'),
                    ('endDate', '2013-10-20T19:20:30+01:00'),
                    ('changedSince', '2013-10-20T19:20:30+01:00'),
                    ('userLicenseTypes', [openapi_server.LicenseUserType()]),
                    ('phaseGuid', 'phase_guid_example'),
                    ('projectGuid', 'project_guid_example'),
                    ('projectBusinessUnitGuid', 'project_business_unit_guid_example'),
                    ('userBusinessUnitGuid', 'user_business_unit_guid_example'),
                    ('projectManagerUserGuid', 'project_manager_user_guid_example'),
                    ('userTagGuid', 'user_tag_guid_example'),
                    ('useSalesProbability', True),
                    ('projectStatusTypeGuid', 'project_status_type_guid_example'),
                    ('projectTagGuid', 'project_tag_guid_example'),
                    ('superiorUserGuid', 'superior_user_guid_example'),
                    ('salesStatusTypeGuid', 'sales_status_type_guid_example'),
                    ('resourceAllocationGuid', 'resource_allocation_guid_example'),
                    ('salesProgress', openapi_server.SalesProgress()),
                    ('rowCount', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/users/{user_guid}/resourceallocations/allocations'.format(user_guid='user_guid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_resource_allocations_post_resource_allocations(client):
    """Test case for resource_allocations_post_resource_allocations

    Get resource allocations (its POST because of being able to accommodate more filters)
    """
    body = {"projectManagerUserGuids":["projectManagerUserGuids","projectManagerUserGuids"],"userBusinessUnitGuids":["userBusinessUnitGuids","userBusinessUnitGuids"],"endDate":"2000-01-23T04:56:07.000+00:00","superiorUserGuids":["superiorUserGuids","superiorUserGuids"],"userLicenseTypes":["FullUser","FullUser"],"phaseGuids":["phaseGuids","phaseGuids"],"projectStatusTypeGuids":["projectStatusTypeGuids","projectStatusTypeGuids"],"salesStatusTypeGuids":["salesStatusTypeGuids","salesStatusTypeGuids"],"projectTagGuids":["projectTagGuids","projectTagGuids"],"projectBusinessUnitGuids":["projectBusinessUnitGuids","projectBusinessUnitGuids"],"resourceAllocationGuids":["resourceAllocationGuids","resourceAllocationGuids"],"includeAbsences":True,"userGuids":["userGuids","userGuids"],"salesProgresses":["None","None"],"useSalesProbability":True,"userTagGuids":["userTagGuids","userTagGuids"],"projectGuids":["projectGuids","projectGuids"],"startDate":"2000-01-23T04:56:07.000+00:00"}
    params = [('rowCount', 56),
                    ('pageToken', 'page_token_example'),
                    ('changedSince', '2013-10-20T19:20:30+01:00')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/rest-api/v1/resourceallocations/allocations',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_role_allocations_get_role_allocation(client):
    """Test case for role_allocations_get_role_allocation

    Get role allocation by GUID.
    """
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/roleallocations/{guid}'.format(guid='guid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_role_allocations_get_role_allocations(client):
    """Test case for role_allocations_get_role_allocations

    Get role allocations.
    """
    params = [('startDate', '2013-10-20T19:20:30+01:00'),
                    ('endDate', '2013-10-20T19:20:30+01:00'),
                    ('pageToken', 'page_token_example'),
                    ('rowCount', 56),
                    ('useSalesProbability', True),
                    ('roleGuids', ['role_guids_example']),
                    ('phaseGuids', ['phase_guids_example']),
                    ('projectGuids', ['project_guids_example'])]
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/roleallocations',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

