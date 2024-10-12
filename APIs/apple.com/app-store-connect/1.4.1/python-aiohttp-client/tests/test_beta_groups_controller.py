# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.app_response import AppResponse
from openapi_server.models.beta_group_beta_testers_linkages_request import BetaGroupBetaTestersLinkagesRequest
from openapi_server.models.beta_group_beta_testers_linkages_response import BetaGroupBetaTestersLinkagesResponse
from openapi_server.models.beta_group_builds_linkages_request import BetaGroupBuildsLinkagesRequest
from openapi_server.models.beta_group_builds_linkages_response import BetaGroupBuildsLinkagesResponse
from openapi_server.models.beta_group_create_request import BetaGroupCreateRequest
from openapi_server.models.beta_group_response import BetaGroupResponse
from openapi_server.models.beta_group_update_request import BetaGroupUpdateRequest
from openapi_server.models.beta_groups_response import BetaGroupsResponse
from openapi_server.models.beta_testers_response import BetaTestersResponse
from openapi_server.models.builds_response import BuildsResponse
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_beta_groups_app_get_to_one_related(client):
    """Test case for beta_groups_app_get_to_one_related

    
    """
    params = [('fields[apps]', ['fields_apps_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/betaGroups/{id}/app'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_beta_groups_beta_testers_create_to_many_relationship(client):
    """Test case for beta_groups_beta_testers_create_to_many_relationship

    
    """
    body = {"data":[{"id":"id","type":"betaTesters"},{"id":"id","type":"betaTesters"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/betaGroups/{id}/relationships/betaTesters'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_beta_groups_beta_testers_delete_to_many_relationship(client):
    """Test case for beta_groups_beta_testers_delete_to_many_relationship

    
    """
    body = {"data":[{"id":"id","type":"betaTesters"},{"id":"id","type":"betaTesters"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/betaGroups/{id}/relationships/betaTesters'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_beta_groups_beta_testers_get_to_many_related(client):
    """Test case for beta_groups_beta_testers_get_to_many_related

    
    """
    params = [('fields[betaTesters]', ['fields_beta_testers_example']),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/betaGroups/{id}/betaTesters'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_beta_groups_beta_testers_get_to_many_relationship(client):
    """Test case for beta_groups_beta_testers_get_to_many_relationship

    
    """
    params = [('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/betaGroups/{id}/relationships/betaTesters'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_beta_groups_builds_create_to_many_relationship(client):
    """Test case for beta_groups_builds_create_to_many_relationship

    
    """
    body = {"data":[{"id":"id","type":"builds"},{"id":"id","type":"builds"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/betaGroups/{id}/relationships/builds'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_beta_groups_builds_delete_to_many_relationship(client):
    """Test case for beta_groups_builds_delete_to_many_relationship

    
    """
    body = {"data":[{"id":"id","type":"builds"},{"id":"id","type":"builds"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/betaGroups/{id}/relationships/builds'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_beta_groups_builds_get_to_many_related(client):
    """Test case for beta_groups_builds_get_to_many_related

    
    """
    params = [('fields[builds]', ['fields_builds_example']),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/betaGroups/{id}/builds'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_beta_groups_builds_get_to_many_relationship(client):
    """Test case for beta_groups_builds_get_to_many_relationship

    
    """
    params = [('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/betaGroups/{id}/relationships/builds'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_beta_groups_create_instance(client):
    """Test case for beta_groups_create_instance

    
    """
    body = {"data":{"relationships":{"app":{"data":{"id":"id","type":"apps"}},"builds":{"data":[{"id":"id","type":"builds"},{"id":"id","type":"builds"}]},"betaTesters":{"data":[{"id":"id","type":"betaTesters"},{"id":"id","type":"betaTesters"}]}},"attributes":{"publicLinkLimit":0,"publicLinkEnabled":True,"name":"name","feedbackEnabled":True,"publicLinkLimitEnabled":True},"type":"betaGroups"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/betaGroups',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_beta_groups_delete_instance(client):
    """Test case for beta_groups_delete_instance

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/betaGroups/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_beta_groups_get_collection(client):
    """Test case for beta_groups_get_collection

    
    """
    params = [('filter[isInternalGroup]', ['filter_is_internal_group_example']),
                    ('filter[name]', ['filter_name_example']),
                    ('filter[publicLink]', ['filter_public_link_example']),
                    ('filter[publicLinkEnabled]', ['filter_public_link_enabled_example']),
                    ('filter[publicLinkLimitEnabled]', ['filter_public_link_limit_enabled_example']),
                    ('filter[app]', ['filter_app_example']),
                    ('filter[builds]', ['filter_builds_example']),
                    ('filter[id]', ['filter_id_example']),
                    ('sort', ['sort_example']),
                    ('fields[betaGroups]', ['fields_beta_groups_example']),
                    ('limit', 56),
                    ('include', ['include_example']),
                    ('fields[builds]', ['fields_builds_example']),
                    ('fields[betaTesters]', ['fields_beta_testers_example']),
                    ('fields[apps]', ['fields_apps_example']),
                    ('limit[betaTesters]', 56),
                    ('limit[builds]', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/betaGroups',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_beta_groups_get_instance(client):
    """Test case for beta_groups_get_instance

    
    """
    params = [('fields[betaGroups]', ['fields_beta_groups_example']),
                    ('include', ['include_example']),
                    ('fields[builds]', ['fields_builds_example']),
                    ('fields[betaTesters]', ['fields_beta_testers_example']),
                    ('fields[apps]', ['fields_apps_example']),
                    ('limit[betaTesters]', 56),
                    ('limit[builds]', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/betaGroups/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_beta_groups_update_instance(client):
    """Test case for beta_groups_update_instance

    
    """
    body = {"data":{"attributes":{"publicLinkLimit":0,"publicLinkEnabled":True,"name":"name","feedbackEnabled":True,"publicLinkLimitEnabled":True},"id":"id","type":"betaGroups"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v1/betaGroups/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

