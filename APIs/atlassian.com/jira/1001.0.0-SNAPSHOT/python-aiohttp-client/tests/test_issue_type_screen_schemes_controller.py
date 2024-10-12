# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.issue_type_ids import IssueTypeIds
from openapi_server.models.issue_type_screen_scheme_details import IssueTypeScreenSchemeDetails
from openapi_server.models.issue_type_screen_scheme_id import IssueTypeScreenSchemeId
from openapi_server.models.issue_type_screen_scheme_mapping_details import IssueTypeScreenSchemeMappingDetails
from openapi_server.models.issue_type_screen_scheme_project_association import IssueTypeScreenSchemeProjectAssociation
from openapi_server.models.issue_type_screen_scheme_update_details import IssueTypeScreenSchemeUpdateDetails
from openapi_server.models.page_bean_issue_type_screen_scheme import PageBeanIssueTypeScreenScheme
from openapi_server.models.page_bean_issue_type_screen_scheme_item import PageBeanIssueTypeScreenSchemeItem
from openapi_server.models.page_bean_issue_type_screen_schemes_projects import PageBeanIssueTypeScreenSchemesProjects
from openapi_server.models.page_bean_project_details import PageBeanProjectDetails
from openapi_server.models.update_default_screen_scheme import UpdateDefaultScreenScheme


pytestmark = pytest.mark.asyncio

async def test_append_mappings_for_issue_type_screen_scheme(client):
    """Test case for append_mappings_for_issue_type_screen_scheme

    Append mappings to issue type screen scheme
    """
    body = {"issueTypeMappings":[{"issueTypeId":"issueTypeId","screenSchemeId":"screenSchemeId"},{"issueTypeId":"issueTypeId","screenSchemeId":"screenSchemeId"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PUT',
        path='/rest/api/3/issuetypescreenscheme/{issue_type_screen_scheme_id}/mapping'.format(issue_type_screen_scheme_id='issue_type_screen_scheme_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_assign_issue_type_screen_scheme_to_project(client):
    """Test case for assign_issue_type_screen_scheme_to_project

    Assign issue type screen scheme to project
    """
    body = {"issueTypeScreenSchemeId":"issueTypeScreenSchemeId","projectId":"projectId"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PUT',
        path='/rest/api/3/issuetypescreenscheme/project',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_issue_type_screen_scheme(client):
    """Test case for create_issue_type_screen_scheme

    Create issue type screen scheme
    """
    body = {"name":"name","description":"description","issueTypeMappings":[{"issueTypeId":"issueTypeId","screenSchemeId":"screenSchemeId"},{"issueTypeId":"issueTypeId","screenSchemeId":"screenSchemeId"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/rest/api/3/issuetypescreenscheme',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_issue_type_screen_scheme(client):
    """Test case for delete_issue_type_screen_scheme

    Delete issue type screen scheme
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/rest/api/3/issuetypescreenscheme/{issue_type_screen_scheme_id}'.format(issue_type_screen_scheme_id='issue_type_screen_scheme_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_issue_type_screen_scheme_mappings(client):
    """Test case for get_issue_type_screen_scheme_mappings

    Get issue type screen scheme items
    """
    params = [('startAt', 0),
                    ('maxResults', 50),
                    ('issueTypeScreenSchemeId', [56])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/issuetypescreenscheme/mapping',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_issue_type_screen_scheme_project_associations(client):
    """Test case for get_issue_type_screen_scheme_project_associations

    Get issue type screen schemes for projects
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
        path='/rest/api/3/issuetypescreenscheme/project',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_issue_type_screen_schemes(client):
    """Test case for get_issue_type_screen_schemes

    Get issue type screen schemes
    """
    params = [('startAt', 0),
                    ('maxResults', 50),
                    ('id', [56]),
                    ('queryString', ''),
                    ('orderBy', id),
                    ('expand', '')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/issuetypescreenscheme',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_projects_for_issue_type_screen_scheme(client):
    """Test case for get_projects_for_issue_type_screen_scheme

    Get issue type screen scheme projects
    """
    params = [('startAt', 0),
                    ('maxResults', 50),
                    ('query', '')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/issuetypescreenscheme/{issue_type_screen_scheme_id}/project'.format(issue_type_screen_scheme_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remove_mappings_from_issue_type_screen_scheme(client):
    """Test case for remove_mappings_from_issue_type_screen_scheme

    Remove mappings from issue type screen scheme
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
        path='/rest/api/3/issuetypescreenscheme/{issue_type_screen_scheme_id}/mapping/remove'.format(issue_type_screen_scheme_id='issue_type_screen_scheme_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_default_screen_scheme(client):
    """Test case for update_default_screen_scheme

    Update issue type screen scheme default screen scheme
    """
    body = {"screenSchemeId":"screenSchemeId"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PUT',
        path='/rest/api/3/issuetypescreenscheme/{issue_type_screen_scheme_id}/mapping/default'.format(issue_type_screen_scheme_id='issue_type_screen_scheme_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_issue_type_screen_scheme(client):
    """Test case for update_issue_type_screen_scheme

    Update issue type screen scheme
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
        path='/rest/api/3/issuetypescreenscheme/{issue_type_screen_scheme_id}'.format(issue_type_screen_scheme_id='issue_type_screen_scheme_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

