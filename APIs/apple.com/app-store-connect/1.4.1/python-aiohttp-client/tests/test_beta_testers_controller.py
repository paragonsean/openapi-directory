# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.apps_response import AppsResponse
from openapi_server.models.beta_groups_response import BetaGroupsResponse
from openapi_server.models.beta_tester_apps_linkages_request import BetaTesterAppsLinkagesRequest
from openapi_server.models.beta_tester_apps_linkages_response import BetaTesterAppsLinkagesResponse
from openapi_server.models.beta_tester_beta_groups_linkages_request import BetaTesterBetaGroupsLinkagesRequest
from openapi_server.models.beta_tester_beta_groups_linkages_response import BetaTesterBetaGroupsLinkagesResponse
from openapi_server.models.beta_tester_builds_linkages_request import BetaTesterBuildsLinkagesRequest
from openapi_server.models.beta_tester_builds_linkages_response import BetaTesterBuildsLinkagesResponse
from openapi_server.models.beta_tester_create_request import BetaTesterCreateRequest
from openapi_server.models.beta_tester_response import BetaTesterResponse
from openapi_server.models.beta_testers_response import BetaTestersResponse
from openapi_server.models.builds_response import BuildsResponse
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_beta_testers_apps_delete_to_many_relationship(client):
    """Test case for beta_testers_apps_delete_to_many_relationship

    
    """
    body = {"data":[{"id":"id","type":"apps"},{"id":"id","type":"apps"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/betaTesters/{id}/relationships/apps'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_beta_testers_apps_get_to_many_related(client):
    """Test case for beta_testers_apps_get_to_many_related

    
    """
    params = [('fields[apps]', ['fields_apps_example']),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/betaTesters/{id}/apps'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_beta_testers_apps_get_to_many_relationship(client):
    """Test case for beta_testers_apps_get_to_many_relationship

    
    """
    params = [('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/betaTesters/{id}/relationships/apps'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_beta_testers_beta_groups_create_to_many_relationship(client):
    """Test case for beta_testers_beta_groups_create_to_many_relationship

    
    """
    body = {"data":[{"id":"id","type":"betaGroups"},{"id":"id","type":"betaGroups"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/betaTesters/{id}/relationships/betaGroups'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_beta_testers_beta_groups_delete_to_many_relationship(client):
    """Test case for beta_testers_beta_groups_delete_to_many_relationship

    
    """
    body = {"data":[{"id":"id","type":"betaGroups"},{"id":"id","type":"betaGroups"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/betaTesters/{id}/relationships/betaGroups'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_beta_testers_beta_groups_get_to_many_related(client):
    """Test case for beta_testers_beta_groups_get_to_many_related

    
    """
    params = [('fields[betaGroups]', ['fields_beta_groups_example']),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/betaTesters/{id}/betaGroups'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_beta_testers_beta_groups_get_to_many_relationship(client):
    """Test case for beta_testers_beta_groups_get_to_many_relationship

    
    """
    params = [('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/betaTesters/{id}/relationships/betaGroups'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_beta_testers_builds_create_to_many_relationship(client):
    """Test case for beta_testers_builds_create_to_many_relationship

    
    """
    body = {"data":[{"id":"id","type":"builds"},{"id":"id","type":"builds"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/betaTesters/{id}/relationships/builds'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_beta_testers_builds_delete_to_many_relationship(client):
    """Test case for beta_testers_builds_delete_to_many_relationship

    
    """
    body = {"data":[{"id":"id","type":"builds"},{"id":"id","type":"builds"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/betaTesters/{id}/relationships/builds'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_beta_testers_builds_get_to_many_related(client):
    """Test case for beta_testers_builds_get_to_many_related

    
    """
    params = [('fields[builds]', ['fields_builds_example']),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/betaTesters/{id}/builds'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_beta_testers_builds_get_to_many_relationship(client):
    """Test case for beta_testers_builds_get_to_many_relationship

    
    """
    params = [('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/betaTesters/{id}/relationships/builds'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_beta_testers_create_instance(client):
    """Test case for beta_testers_create_instance

    
    """
    body = {"data":{"relationships":{"betaGroups":{"data":[{"id":"id","type":"betaGroups"},{"id":"id","type":"betaGroups"}]},"builds":{"data":[{"id":"id","type":"builds"},{"id":"id","type":"builds"}]}},"attributes":{"firstName":"firstName","lastName":"lastName","email":"email"},"type":"betaTesters"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/betaTesters',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_beta_testers_delete_instance(client):
    """Test case for beta_testers_delete_instance

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/betaTesters/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_beta_testers_get_collection(client):
    """Test case for beta_testers_get_collection

    
    """
    params = [('filter[email]', ['filter_email_example']),
                    ('filter[firstName]', ['filter_first_name_example']),
                    ('filter[inviteType]', ['filter_invite_type_example']),
                    ('filter[lastName]', ['filter_last_name_example']),
                    ('filter[apps]', ['filter_apps_example']),
                    ('filter[betaGroups]', ['filter_beta_groups_example']),
                    ('filter[builds]', ['filter_builds_example']),
                    ('sort', ['sort_example']),
                    ('fields[betaTesters]', ['fields_beta_testers_example']),
                    ('limit', 56),
                    ('include', ['include_example']),
                    ('fields[betaGroups]', ['fields_beta_groups_example']),
                    ('fields[builds]', ['fields_builds_example']),
                    ('fields[apps]', ['fields_apps_example']),
                    ('limit[apps]', 56),
                    ('limit[betaGroups]', 56),
                    ('limit[builds]', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/betaTesters',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_beta_testers_get_instance(client):
    """Test case for beta_testers_get_instance

    
    """
    params = [('fields[betaTesters]', ['fields_beta_testers_example']),
                    ('include', ['include_example']),
                    ('fields[betaGroups]', ['fields_beta_groups_example']),
                    ('fields[builds]', ['fields_builds_example']),
                    ('fields[apps]', ['fields_apps_example']),
                    ('limit[apps]', 56),
                    ('limit[betaGroups]', 56),
                    ('limit[builds]', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/betaTesters/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

