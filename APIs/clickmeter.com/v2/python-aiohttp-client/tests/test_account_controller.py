# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_core_dto_accounting_domain_whitelist_entry import ApiCoreDtoAccountingDomainWhitelistEntry
from openapi_server.models.api_core_dto_accounting_guest import ApiCoreDtoAccountingGuest
from openapi_server.models.api_core_dto_accounting_ip_blacklist_entry import ApiCoreDtoAccountingIpBlacklistEntry
from openapi_server.models.api_core_dto_accounting_plan import ApiCoreDtoAccountingPlan
from openapi_server.models.api_core_dto_accounting_user import ApiCoreDtoAccountingUser
from openapi_server.models.api_core_requests_permission_patch_request import ApiCoreRequestsPermissionPatchRequest
from openapi_server.models.api_core_responses_count_responce import ApiCoreResponsesCountResponce
from openapi_server.models.api_core_responses_entities_response_api_core_dto_accounting_domain_whitelist_entry import ApiCoreResponsesEntitiesResponseApiCoreDtoAccountingDomainWhitelistEntry
from openapi_server.models.api_core_responses_entities_response_api_core_dto_accounting_ip_blacklist_entry import ApiCoreResponsesEntitiesResponseApiCoreDtoAccountingIpBlacklistEntry
from openapi_server.models.api_core_responses_entities_response_api_core_dto_grants_grant import ApiCoreResponsesEntitiesResponseApiCoreDtoGrantsGrant
from openapi_server.models.api_core_responses_entities_response_api_core_responses_entity_uri_system_int64 import ApiCoreResponsesEntitiesResponseApiCoreResponsesEntityUriSystemInt64
from openapi_server.models.api_core_responses_entity_uri_system_int64 import ApiCoreResponsesEntityUriSystemInt64


pytestmark = pytest.mark.asyncio

async def test_account_delete_domain_whitelist(client):
    """Test case for account_delete_domain_whitelist

    Delete an domain entry
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/account/domainwhitelist/{whitelist_id}'.format(whitelist_id='whitelist_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_account_delete_guest(client):
    """Test case for account_delete_guest

    Delete a guest
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/account/guests/{guest_id}'.format(guest_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_account_delete_ip_blacklist(client):
    """Test case for account_delete_ip_blacklist

    Delete an ip blacklist entry
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/account/ipblacklist/{blacklist_id}'.format(blacklist_id='blacklist_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_account_get(client):
    """Test case for account_get

    Retrieve current account data
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/account',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_account_get_domain_whitelist(client):
    """Test case for account_get_domain_whitelist

    Retrieve list of a domains allowed to redirect in DDU mode
    """
    params = [('offset', 56),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/account/domainwhitelist',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_account_get_guest(client):
    """Test case for account_get_guest

    Retrieve a guest
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/account/guests/{guest_id}'.format(guest_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_account_get_guests(client):
    """Test case for account_get_guests

    Retrieve list of a guest
    """
    params = [('offset', 56),
                    ('limit', 56),
                    ('sortBy', 'sort_by_example'),
                    ('sortDirection', 'sort_direction_example'),
                    ('textSearch', 'text_search_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/account/guests',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_account_get_guests_count(client):
    """Test case for account_get_guests_count

    Retrieve count of guests
    """
    params = [('textSearch', 'text_search_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/account/guests/count',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_account_get_ip_blacklist(client):
    """Test case for account_get_ip_blacklist

    Retrieve list of a ip to exclude from event tracking
    """
    params = [('offset', 56),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/account/ipblacklist',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_account_get_permissions(client):
    """Test case for account_get_permissions

    Retrieve permissions for a guest
    """
    params = [('entityType', 'entity_type_example'),
                    ('offset', 56),
                    ('limit', 56),
                    ('type', 'type_example'),
                    ('entityId', 56)]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/account/guests/{guest_id}/permissions'.format(guest_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_account_get_permissions_count(client):
    """Test case for account_get_permissions_count

    Retrieve count of the permissions for a guest
    """
    params = [('entityType', 'entity_type_example'),
                    ('type', 'type_example'),
                    ('entityId', 56)]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/account/guests/{guest_id}/permissions/count'.format(guest_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_account_get_plan(client):
    """Test case for account_get_plan

    Retrieve current account plan
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/account/plan',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_account_guests_guest_id_type_permissions_patch_post(client):
    """Test case for account_guests_guest_id_type_permissions_patch_post

    Change the permission on a shared object
    """
    body = openapi_server.ApiCoreRequestsPermissionPatchRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/account/guests/{guest_id}/{type}/permissions/patch'.format(guest_id=56, type='type_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_account_patch_permissions(client):
    """Test case for account_patch_permissions

    Change the permission on a shared object
    """
    body = openapi_server.ApiCoreRequestsPermissionPatchRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/account/guests/{guest_id}/{type}/permissions/patch'.format(guest_id=56, type='type_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_account_post(client):
    """Test case for account_post

    Update current account data
    """
    body = openapi_server.ApiCoreDtoAccountingUser()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/account',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_account_post_guest(client):
    """Test case for account_post_guest

    Update a guest
    """
    body = openapi_server.ApiCoreDtoAccountingGuest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/account/guests/{guest_id}'.format(guest_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_account_put_domain_whitelist(client):
    """Test case for account_put_domain_whitelist

    Create an domain entry
    """
    body = openapi_server.ApiCoreDtoAccountingDomainWhitelistEntry()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/account/domainwhitelist',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_account_put_guest(client):
    """Test case for account_put_guest

    Create a guest
    """
    body = openapi_server.ApiCoreDtoAccountingGuest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/account/guests',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_account_put_ip_blacklist(client):
    """Test case for account_put_ip_blacklist

    Create an ip blacklist entry
    """
    body = openapi_server.ApiCoreDtoAccountingIpBlacklistEntry()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/account/ipblacklist',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

