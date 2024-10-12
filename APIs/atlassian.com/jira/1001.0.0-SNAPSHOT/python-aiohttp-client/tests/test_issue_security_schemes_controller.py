# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.add_security_scheme_levels_request_bean import AddSecuritySchemeLevelsRequestBean
from openapi_server.models.create_issue_security_scheme_details import CreateIssueSecuritySchemeDetails
from openapi_server.models.error_collection import ErrorCollection
from openapi_server.models.page_bean_issue_security_scheme_to_project_mapping import PageBeanIssueSecuritySchemeToProjectMapping
from openapi_server.models.page_bean_security_level import PageBeanSecurityLevel
from openapi_server.models.page_bean_security_level_member import PageBeanSecurityLevelMember
from openapi_server.models.page_bean_security_scheme_with_projects import PageBeanSecuritySchemeWithProjects
from openapi_server.models.security_scheme import SecurityScheme
from openapi_server.models.security_scheme_id import SecuritySchemeId
from openapi_server.models.security_scheme_members_request import SecuritySchemeMembersRequest
from openapi_server.models.security_schemes import SecuritySchemes
from openapi_server.models.set_default_levels_request import SetDefaultLevelsRequest
from openapi_server.models.task_progress_bean_object import TaskProgressBeanObject
from openapi_server.models.update_issue_security_level_details import UpdateIssueSecurityLevelDetails
from openapi_server.models.update_issue_security_scheme_request_bean import UpdateIssueSecuritySchemeRequestBean


pytestmark = pytest.mark.asyncio

async def test_add_security_level(client):
    """Test case for add_security_level

    Add issue security levels
    """
    body = {"levels":[{"isDefault":True,"members":[{"parameter":"parameter","type":"type"},{"parameter":"parameter","type":"type"}],"name":"name","description":"description"},{"isDefault":True,"members":[{"parameter":"parameter","type":"type"},{"parameter":"parameter","type":"type"}],"name":"name","description":"description"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PUT',
        path='/rest/api/3/issuesecurityschemes/{scheme_id}/level'.format(scheme_id='scheme_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_add_security_level_members(client):
    """Test case for add_security_level_members

    Add issue security level members
    """
    body = {"members":[{"parameter":"parameter","type":"type"},{"parameter":"parameter","type":"type"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PUT',
        path='/rest/api/3/issuesecurityschemes/{scheme_id}/level/{level_id}/member'.format(scheme_id='scheme_id_example', level_id='level_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_issue_security_scheme(client):
    """Test case for create_issue_security_scheme

    Create issue security scheme
    """
    body = {"name":"name","description":"description","levels":[{"isDefault":True,"members":[{"parameter":"parameter","type":"type"},{"parameter":"parameter","type":"type"}],"name":"name","description":"description"},{"isDefault":True,"members":[{"parameter":"parameter","type":"type"},{"parameter":"parameter","type":"type"}],"name":"name","description":"description"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/rest/api/3/issuesecurityschemes',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_security_scheme(client):
    """Test case for delete_security_scheme

    Delete issue security scheme
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/rest/api/3/issuesecurityschemes/{scheme_id}'.format(scheme_id='scheme_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_issue_security_scheme(client):
    """Test case for get_issue_security_scheme

    Get issue security scheme
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/issuesecurityschemes/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_issue_security_schemes(client):
    """Test case for get_issue_security_schemes

    Get issue security schemes
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/issuesecurityschemes',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_security_level_members(client):
    """Test case for get_security_level_members

    Get issue security level members
    """
    params = [('startAt', '0'),
                    ('maxResults', '50'),
                    ('id', ['id_example']),
                    ('schemeId', ['scheme_id_example']),
                    ('levelId', ['level_id_example']),
                    ('expand', 'expand_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/issuesecurityschemes/level/member',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_security_levels(client):
    """Test case for get_security_levels

    Get issue security levels
    """
    params = [('startAt', '0'),
                    ('maxResults', '50'),
                    ('id', ['id_example']),
                    ('schemeId', ['scheme_id_example']),
                    ('onlyDefault', False)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/issuesecurityschemes/level',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remove_level(client):
    """Test case for remove_level

    Remove issue security level
    """
    params = [('replaceWith', 'replace_with_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/rest/api/3/issuesecurityschemes/{scheme_id}/level/{level_id}'.format(scheme_id='scheme_id_example', level_id='level_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remove_member_from_security_level(client):
    """Test case for remove_member_from_security_level

    Remove member from issue security level
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/rest/api/3/issuesecurityschemes/{scheme_id}/level/{level_id}/member/{member_id}'.format(scheme_id='scheme_id_example', level_id='level_id_example', member_id='member_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_projects_using_security_schemes(client):
    """Test case for search_projects_using_security_schemes

    Get projects using issue security schemes
    """
    params = [('startAt', '0'),
                    ('maxResults', '50'),
                    ('issueSecuritySchemeId', ['issue_security_scheme_id_example']),
                    ('projectId', ['project_id_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/issuesecurityschemes/project',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_security_schemes(client):
    """Test case for search_security_schemes

    Search issue security schemes
    """
    params = [('startAt', '0'),
                    ('maxResults', '50'),
                    ('id', ['id_example']),
                    ('projectId', ['project_id_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/issuesecurityschemes/search',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_set_default_levels(client):
    """Test case for set_default_levels

    Set default issue security levels
    """
    body = {"defaultValues":[{"issueSecuritySchemeId":"issueSecuritySchemeId","defaultLevelId":"defaultLevelId"},{"issueSecuritySchemeId":"issueSecuritySchemeId","defaultLevelId":"defaultLevelId"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PUT',
        path='/rest/api/3/issuesecurityschemes/level/default',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_issue_security_scheme(client):
    """Test case for update_issue_security_scheme

    Update issue security scheme
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
        path='/rest/api/3/issuesecurityschemes/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_security_level(client):
    """Test case for update_security_level

    Update issue security level
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
        path='/rest/api/3/issuesecurityschemes/{scheme_id}/level/{level_id}'.format(scheme_id='scheme_id_example', level_id='level_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

