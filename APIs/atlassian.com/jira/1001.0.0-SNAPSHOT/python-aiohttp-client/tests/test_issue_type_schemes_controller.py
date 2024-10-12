# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.issue_type_ids import IssueTypeIds
from openapi_server.models.issue_type_scheme_details import IssueTypeSchemeDetails
from openapi_server.models.issue_type_scheme_id import IssueTypeSchemeID
from openapi_server.models.issue_type_scheme_project_association import IssueTypeSchemeProjectAssociation
from openapi_server.models.issue_type_scheme_update_details import IssueTypeSchemeUpdateDetails
from openapi_server.models.order_of_issue_types import OrderOfIssueTypes
from openapi_server.models.page_bean_issue_type_scheme import PageBeanIssueTypeScheme
from openapi_server.models.page_bean_issue_type_scheme_mapping import PageBeanIssueTypeSchemeMapping
from openapi_server.models.page_bean_issue_type_scheme_projects import PageBeanIssueTypeSchemeProjects


pytestmark = pytest.mark.asyncio

async def test_add_issue_types_to_issue_type_scheme(client):
    """Test case for add_issue_types_to_issue_type_scheme

    Add issue types to issue type scheme
    """
    body = {"issueTypeIds":["issueTypeIds","issueTypeIds"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PUT',
        path='/rest/api/3/issuetypescheme/{issue_type_scheme_id}/issuetype'.format(issue_type_scheme_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_assign_issue_type_scheme_to_project(client):
    """Test case for assign_issue_type_scheme_to_project

    Assign issue type scheme to project
    """
    body = {"issueTypeSchemeId":"issueTypeSchemeId","projectId":"projectId"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PUT',
        path='/rest/api/3/issuetypescheme/project',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_issue_type_scheme(client):
    """Test case for create_issue_type_scheme

    Create issue type scheme
    """
    body = {"defaultIssueTypeId":"defaultIssueTypeId","issueTypeIds":["issueTypeIds","issueTypeIds"],"name":"name","description":"description"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/rest/api/3/issuetypescheme',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_issue_type_scheme(client):
    """Test case for delete_issue_type_scheme

    Delete issue type scheme
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/rest/api/3/issuetypescheme/{issue_type_scheme_id}'.format(issue_type_scheme_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_all_issue_type_schemes(client):
    """Test case for get_all_issue_type_schemes

    Get all issue type schemes
    """
    params = [('startAt', 0),
                    ('maxResults', 50),
                    ('id', [56]),
                    ('orderBy', id),
                    ('expand', ''),
                    ('queryString', '')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/issuetypescheme',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_issue_type_scheme_for_projects(client):
    """Test case for get_issue_type_scheme_for_projects

    Get issue type schemes for projects
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
        path='/rest/api/3/issuetypescheme/project',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_issue_type_schemes_mapping(client):
    """Test case for get_issue_type_schemes_mapping

    Get issue type scheme items
    """
    params = [('startAt', 0),
                    ('maxResults', 50),
                    ('issueTypeSchemeId', [56])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/issuetypescheme/mapping',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remove_issue_type_from_issue_type_scheme(client):
    """Test case for remove_issue_type_from_issue_type_scheme

    Remove issue type from issue type scheme
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/rest/api/3/issuetypescheme/{issue_type_scheme_id}/issuetype/{issue_type_id}'.format(issue_type_scheme_id=56, issue_type_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reorder_issue_types_in_issue_type_scheme(client):
    """Test case for reorder_issue_types_in_issue_type_scheme

    Change order of issue types
    """
    body = {"issueTypeIds":["issueTypeIds","issueTypeIds"],"after":"after","position":"First"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PUT',
        path='/rest/api/3/issuetypescheme/{issue_type_scheme_id}/issuetype/move'.format(issue_type_scheme_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_issue_type_scheme(client):
    """Test case for update_issue_type_scheme

    Update issue type scheme
    """
    body = {"defaultIssueTypeId":"defaultIssueTypeId","name":"name","description":"description"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PUT',
        path='/rest/api/3/issuetypescheme/{issue_type_scheme_id}'.format(issue_type_scheme_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

