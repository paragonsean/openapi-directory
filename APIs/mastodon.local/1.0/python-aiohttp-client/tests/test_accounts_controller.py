# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.account import Account
from openapi_server.models.api_v1_accounts_id_follow_post_request import ApiV1AccountsIdFollowPostRequest
from openapi_server.models.api_v1_accounts_id_mute_post_request import ApiV1AccountsIdMutePostRequest
from openapi_server.models.api_v1_accounts_id_note_post_request import ApiV1AccountsIdNotePostRequest
from openapi_server.models.api_v1_accounts_post_request import ApiV1AccountsPostRequest
from openapi_server.models.api_v1_accounts_update_credentials_patch_request import ApiV1AccountsUpdateCredentialsPatchRequest
from openapi_server.models.error import Error
from openapi_server.models.featured_tag import FeaturedTag
from openapi_server.models.identity_proof import IdentityProof
from openapi_server.models.relationship import Relationship
from openapi_server.models.status import Status


pytestmark = pytest.mark.asyncio

async def test_api_v1_accounts_id_block_post(client):
    """Test case for api_v1_accounts_id_block_post

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/accounts/{id}/block'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v1_accounts_id_featured_tags_get(client):
    """Test case for api_v1_accounts_id_featured_tags_get

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/accounts/{id}/featured_tags'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/form-data not supported by Connexion")
async def test_api_v1_accounts_id_follow_post(client):
    """Test case for api_v1_accounts_id_follow_post

    
    """
    body = openapi_server.ApiV1AccountsIdFollowPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/form-data',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/accounts/{id}/follow'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v1_accounts_id_followers_get(client):
    """Test case for api_v1_accounts_id_followers_get

    
    """
    params = [('max_id', 'max_id_example'),
                    ('since_id', 'since_id_example'),
                    ('limit', 40)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/accounts/{id}/followers'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v1_accounts_id_following_get(client):
    """Test case for api_v1_accounts_id_following_get

    
    """
    params = [('max_id', 'max_id_example'),
                    ('since_id', 'since_id_example'),
                    ('limit', 40)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/accounts/{id}/following'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v1_accounts_id_get(client):
    """Test case for api_v1_accounts_id_get

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/accounts/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v1_accounts_id_identity_proofs_get(client):
    """Test case for api_v1_accounts_id_identity_proofs_get

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/accounts/{id}/identity_proofs'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v1_accounts_id_lists_get(client):
    """Test case for api_v1_accounts_id_lists_get

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/accounts/{id}/lists'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/form-data not supported by Connexion")
async def test_api_v1_accounts_id_mute_post(client):
    """Test case for api_v1_accounts_id_mute_post

    
    """
    body = openapi_server.ApiV1AccountsIdMutePostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/form-data',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/accounts/{id}/mute'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/form-data not supported by Connexion")
async def test_api_v1_accounts_id_note_post(client):
    """Test case for api_v1_accounts_id_note_post

    
    """
    body = openapi_server.ApiV1AccountsIdNotePostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/form-data',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/accounts/{id}/note'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v1_accounts_id_pin_post(client):
    """Test case for api_v1_accounts_id_pin_post

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/accounts/{id}/pin'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v1_accounts_id_statuses_get(client):
    """Test case for api_v1_accounts_id_statuses_get

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/accounts/{id}/statuses'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v1_accounts_id_unblock_post(client):
    """Test case for api_v1_accounts_id_unblock_post

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/accounts/{id}/unblock'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v1_accounts_id_unfollow_post(client):
    """Test case for api_v1_accounts_id_unfollow_post

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/accounts/{id}/unfollow'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v1_accounts_id_unmute_post(client):
    """Test case for api_v1_accounts_id_unmute_post

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/accounts/{id}/unmute'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v1_accounts_id_unpin_post(client):
    """Test case for api_v1_accounts_id_unpin_post

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/accounts/{id}/unpin'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/form-data not supported by Connexion")
async def test_api_v1_accounts_post_0(client):
    """Test case for api_v1_accounts_post_0

    
    """
    body = openapi_server.ApiV1AccountsPostRequest()
    headers = { 
        'Content-Type': 'application/form-data',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/accounts',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v1_accounts_relationships_get(client):
    """Test case for api_v1_accounts_relationships_get

    
    """
    params = [('id', ['id_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/accounts/relationships',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v1_accounts_search_get(client):
    """Test case for api_v1_accounts_search_get

    
    """
    params = [('q', 'q_example'),
                    ('limit', 40),
                    ('resolve', 'resolve_example'),
                    ('following', True)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/accounts/search',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/form-data not supported by Connexion")
async def test_api_v1_accounts_update_credentials_patch(client):
    """Test case for api_v1_accounts_update_credentials_patch

    
    """
    body = openapi_server.ApiV1AccountsUpdateCredentialsPatchRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/form-data',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v1/accounts/update_credentials',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v1_accounts_verify_credentials_get(client):
    """Test case for api_v1_accounts_verify_credentials_get

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/accounts/verify_credentials',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

