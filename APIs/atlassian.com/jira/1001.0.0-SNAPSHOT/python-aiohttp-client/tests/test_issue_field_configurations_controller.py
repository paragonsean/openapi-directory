# coding: utf-8

import pytest
import json
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


pytestmark = pytest.mark.asyncio

async def test_assign_field_configuration_scheme_to_project(client):
    """Test case for assign_field_configuration_scheme_to_project

    Assign field configuration scheme to project
    """
    body = {"fieldConfigurationSchemeId":"fieldConfigurationSchemeId","projectId":"projectId"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PUT',
        path='/rest/api/3/fieldconfigurationscheme/project',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_field_configuration(client):
    """Test case for create_field_configuration

    Create field configuration
    """
    body = {"name":"name","description":"description"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/rest/api/3/fieldconfiguration',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_field_configuration_scheme(client):
    """Test case for create_field_configuration_scheme

    Create field configuration scheme
    """
    body = {"name":"name","description":"description"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/rest/api/3/fieldconfigurationscheme',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_field_configuration(client):
    """Test case for delete_field_configuration

    Delete field configuration
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/rest/api/3/fieldconfiguration/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_field_configuration_scheme(client):
    """Test case for delete_field_configuration_scheme

    Delete field configuration scheme
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/rest/api/3/fieldconfigurationscheme/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_all_field_configuration_schemes(client):
    """Test case for get_all_field_configuration_schemes

    Get all field configuration schemes
    """
    params = [('startAt', 0),
                    ('maxResults', 50),
                    ('id', [56])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/fieldconfigurationscheme',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_all_field_configurations(client):
    """Test case for get_all_field_configurations

    Get all field configurations
    """
    params = [('startAt', 0),
                    ('maxResults', 50),
                    ('id', [56]),
                    ('isDefault', False),
                    ('query', '')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/fieldconfiguration',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_field_configuration_items(client):
    """Test case for get_field_configuration_items

    Get field configuration items
    """
    params = [('startAt', 0),
                    ('maxResults', 50)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/fieldconfiguration/{id}/fields'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_field_configuration_scheme_mappings(client):
    """Test case for get_field_configuration_scheme_mappings

    Get field configuration issue type items
    """
    params = [('startAt', 0),
                    ('maxResults', 50),
                    ('fieldConfigurationSchemeId', [56])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/fieldconfigurationscheme/mapping',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_field_configuration_scheme_project_mapping(client):
    """Test case for get_field_configuration_scheme_project_mapping

    Get field configuration schemes for projects
    """
    params = [('startAt', 0),
                    ('maxResults', 50),
                    ('projectId', [56])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/fieldconfigurationscheme/project',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remove_issue_types_from_global_field_configuration_scheme(client):
    """Test case for remove_issue_types_from_global_field_configuration_scheme

    Remove issue types from field configuration scheme
    """
    body = {"issueTypeIds":["issueTypeIds","issueTypeIds"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/rest/api/3/fieldconfigurationscheme/{id}/mapping/delete'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_set_field_configuration_scheme_mapping(client):
    """Test case for set_field_configuration_scheme_mapping

    Assign issue types to field configurations
    """
    body = {"mappings":[{"issueTypeId":"issueTypeId","fieldConfigurationId":"fieldConfigurationId"},{"issueTypeId":"issueTypeId","fieldConfigurationId":"fieldConfigurationId"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PUT',
        path='/rest/api/3/fieldconfigurationscheme/{id}/mapping'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_field_configuration(client):
    """Test case for update_field_configuration

    Update field configuration
    """
    body = {"name":"name","description":"description"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PUT',
        path='/rest/api/3/fieldconfiguration/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_field_configuration_items(client):
    """Test case for update_field_configuration_items

    Update field configuration items
    """
    body = {"fieldConfigurationItems":[{"isRequired":True,"renderer":"renderer","description":"description","id":"id","isHidden":True},{"isRequired":True,"renderer":"renderer","description":"description","id":"id","isHidden":True}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PUT',
        path='/rest/api/3/fieldconfiguration/{id}/fields'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_field_configuration_scheme(client):
    """Test case for update_field_configuration_scheme

    Update field configuration scheme
    """
    body = {"name":"name","description":"description"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PUT',
        path='/rest/api/3/fieldconfigurationscheme/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

