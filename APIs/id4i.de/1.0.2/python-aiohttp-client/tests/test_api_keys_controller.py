# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.add_api_key_privilege_request import AddApiKeyPrivilegeRequest
from openapi_server.models.api_error import ApiError
from openapi_server.models.api_key_change_request import ApiKeyChangeRequest
from openapi_server.models.api_key_creation_request import ApiKeyCreationRequest
from openapi_server.models.api_key_presentation import ApiKeyPresentation
from openapi_server.models.list_of_id4ns import ListOfId4ns
from openapi_server.models.paginated_response_of_api_key_presentation import PaginatedResponseOfApiKeyPresentation
from openapi_server.models.paginated_response_of_api_key_privilege import PaginatedResponseOfApiKeyPrivilege
from openapi_server.models.paginated_response_of_api_key_privilege_info import PaginatedResponseOfApiKeyPrivilegeInfo
from openapi_server.models.paginated_response_of_id4n_presentation import PaginatedResponseOfId4nPresentation
from openapi_server.models.remove_api_key_privilege_request import RemoveApiKeyPrivilegeRequest


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_add_api_key_privilege(client):
    """Test case for add_api_key_privilege

    Add privilege
    """
    body = {"privilege":"privilege"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/apikeys/{key}/privileges'.format(key='key_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_add_api_key_privilege_for_id4ns(client):
    """Test case for add_api_key_privilege_for_id4ns

    Add ID4ns of a privilege
    """
    body = {"id4ns":["id4ns","id4ns"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/apikeys/{key}/privileges/{privilege}/id4ns'.format(key='key_example', privilege='privilege_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_create_new_api_key(client):
    """Test case for create_new_api_key

    Create API key
    """
    body = {"organizationId":"de.acme","label":"label","secret":"secret"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/apikeys',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_api_key(client):
    """Test case for delete_api_key

    Delete API key
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/apikeys/{key}'.format(key='key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_api_key(client):
    """Test case for get_api_key

    Show API key
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/apikeys/{key}'.format(key='key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_all_api_key_privileges(client):
    """Test case for list_all_api_key_privileges

    List all privileges
    """
    params = [('id4nConcerning', True),
                    ('offset', 56),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/apikeys/privileges',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_all_api_keys_of_organization(client):
    """Test case for list_all_api_keys_of_organization

    Find API key by organization
    """
    params = [('organizationId', 'organization_id_example'),
                    ('offset', 56),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/apikeys',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_api_key_privileges(client):
    """Test case for list_api_key_privileges

    List privileges
    """
    params = [('offset', 56),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/apikeys/{key}/privileges'.format(key='key_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_id4ns(client):
    """Test case for list_id4ns

    ID4ns of a privilege
    """
    params = [('offset', 56),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/apikeys/{key}/privileges/{privilege}/id4ns'.format(key='key_example', privilege='privilege_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_remove_api_key_privilege(client):
    """Test case for remove_api_key_privilege

    Remove privilege
    """
    body = {"privilege":"privilege"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/apikeys/{key}/privileges'.format(key='key_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_remove_api_key_privilege_for_id4ns(client):
    """Test case for remove_api_key_privilege_for_id4ns

    Remove id4ns of a privilege
    """
    body = {"id4ns":["id4ns","id4ns"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/apikeys/{key}/privileges/{privilege}/id4ns'.format(key='key_example', privilege='privilege_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_update_api_key(client):
    """Test case for update_api_key

    Update API keys
    """
    body = {"newLabel":"newLabel","active":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/apikeys/{key}'.format(key='key_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

