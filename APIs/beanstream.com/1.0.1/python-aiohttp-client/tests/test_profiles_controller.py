# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.beanstream_exception import BeanstreamException
from openapi_server.models.create_profile_body import CreateProfileBody
from openapi_server.models.payment_profile import PaymentProfile
from openapi_server.models.profile_card import ProfileCard
from openapi_server.models.profile_get_cards import ProfileGetCards
from openapi_server.models.profile_response import ProfileResponse
from openapi_server.models.update_profile_body import UpdateProfileBody


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_profiles_post(client):
    """Test case for profiles_post

    Create Profile
    """
    create_profile_body = openapi_server.CreateProfileBody()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/profiles',
        headers=headers,
        json=create_profile_body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_profiles_profile_id_cards_card_id_delete(client):
    """Test case for profiles_profile_id_cards_card_id_delete

    Delete card
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/profiles/{profile_id}/cards/{card_id}'.format(profile_id='profile_id_example', card_id=3.4),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_profiles_profile_id_cards_card_id_put(client):
    """Test case for profiles_profile_id_cards_card_id_put

    Update card
    """
    card = openapi_server.ProfileCard()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/profiles/{profile_id}/cards/{card_id}'.format(profile_id='profile_id_example', card_id=3.4),
        headers=headers,
        json=card,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_profiles_profile_id_cards_get(client):
    """Test case for profiles_profile_id_cards_get

    Get cards
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/profiles/{profile_id}/cards'.format(profile_id='profile_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_profiles_profile_id_cards_post(client):
    """Test case for profiles_profile_id_cards_post

    Add card
    """
    card = openapi_server.ProfileCard()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/profiles/{profile_id}/cards'.format(profile_id='profile_id_example'),
        headers=headers,
        json=card,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_profiles_profile_id_delete(client):
    """Test case for profiles_profile_id_delete

    Delete profile
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/profiles/{profile_id}'.format(profile_id='profile_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_profiles_profile_id_get(client):
    """Test case for profiles_profile_id_get

    Get profile
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/profiles/{profile_id}'.format(profile_id='profile_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_profiles_profile_id_put(client):
    """Test case for profiles_profile_id_put

    Update Profile
    """
    update_profile_body = openapi_server.UpdateProfileBody()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/profiles/{profile_id}'.format(profile_id='profile_id_example'),
        headers=headers,
        json=update_profile_body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

