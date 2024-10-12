# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.analysis_category import AnalysisCategory
from openapi_server.models.errors import Errors
from openapi_server.models.items_security_entry import ItemsSecurityEntry
from openapi_server.models.items_security_rights import ItemsSecurityRights
from openapi_server.models.security_entry import SecurityEntry


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_analysis_category_create_security_entry(client):
    """Test case for analysis_category_create_security_entry

    Create a security entry owned by the analysis category.
    """
    security_entry = {"WebException":{"Errors":["An error has occurred."],"StatusCode":500},"AllowRights":["Read","ReadData"],"DenyRights":["Write","Execute","Admin"],"Links":{"SecurableObject":"SecurableObject","SecurityIdentity":"SecurityIdentity","Self":"Self"},"SecurityIdentityName":"domain\\user1","Name":"domain\\user1"}
    params = [('applyToChildren', True),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/piwebapi/analysiscategories/{web_id}/securityentries'.format(web_id='web_id_example'),
        headers=headers,
        json=security_entry,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_analysis_category_delete(client):
    """Test case for analysis_category_delete

    Delete an analysis category.
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/piwebapi/analysiscategories/{web_id}'.format(web_id='web_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_analysis_category_delete_security_entry(client):
    """Test case for analysis_category_delete_security_entry

    Delete a security entry owned by the analysis category.
    """
    params = [('applyToChildren', True)]
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/piwebapi/analysiscategories/{web_id}/securityentries/{name}'.format(name='name_example', web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_analysis_category_get(client):
    """Test case for analysis_category_get

    Retrieve an analysis category.
    """
    params = [('selectedFields', 'selected_fields_example'),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/analysiscategories/{web_id}'.format(web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_analysis_category_get_by_path(client):
    """Test case for analysis_category_get_by_path

    Retrieve an analysis category by path.
    """
    params = [('path', 'path_example'),
                    ('selectedFields', 'selected_fields_example'),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/analysiscategories',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_analysis_category_get_security(client):
    """Test case for analysis_category_get_security

    Get the security information of the specified security item associated with the analysis category for a specified user.
    """
    params = [('userIdentity', ['user_identity_example']),
                    ('forceRefresh', True),
                    ('selectedFields', 'selected_fields_example'),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/analysiscategories/{web_id}/security'.format(web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_analysis_category_get_security_entries(client):
    """Test case for analysis_category_get_security_entries

    Retrieve the security entries associated with the analysis category based on the specified criteria. By default, all security entries for this analysis category are returned.
    """
    params = [('nameFilter', 'name_filter_example'),
                    ('selectedFields', 'selected_fields_example'),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/analysiscategories/{web_id}/securityentries'.format(web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_analysis_category_get_security_entry_by_name(client):
    """Test case for analysis_category_get_security_entry_by_name

    Retrieve the security entry associated with the analysis category with the specified name.
    """
    params = [('selectedFields', 'selected_fields_example'),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/analysiscategories/{web_id}/securityentries/{name}'.format(name='name_example', web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_analysis_category_update(client):
    """Test case for analysis_category_update

    Update an analysis category by replacing items in its definition.
    """
    category = {"Path":"\\\\MyAssetServer\\Database\\CategoriesAnalysis[CategoryName]","Description":"Relative energy use per ton of process feed.","WebException":{"Errors":["An error has occurred."],"StatusCode":500},"WebId":"I1XCDqD5loBNH0erqeqJodtALAoko2-UoOVEibhTWQCk1MDw","Links":{"SecurityEntries":"SecurityEntries","Database":"Database","Self":"Self","Security":"Security"},"Id":"f9364aa2-0e4a-4854-9b85-35900a4d4c0f","Name":"CategoryName"}
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/piwebapi/analysiscategories/{web_id}'.format(web_id='web_id_example'),
        headers=headers,
        json=category,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_analysis_category_update_security_entry(client):
    """Test case for analysis_category_update_security_entry

    Update a security entry owned by the analysis category.
    """
    security_entry = {"WebException":{"Errors":["An error has occurred."],"StatusCode":500},"AllowRights":["Read","ReadData"],"DenyRights":["Write","Execute","Admin"],"Links":{"SecurableObject":"SecurableObject","SecurityIdentity":"SecurityIdentity","Self":"Self"},"SecurityIdentityName":"domain\\user1","Name":"domain\\user1"}
    params = [('applyToChildren', True)]
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/piwebapi/analysiscategories/{web_id}/securityentries/{name}'.format(name='name_example', web_id='web_id_example'),
        headers=headers,
        json=security_entry,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

