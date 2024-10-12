# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api2_controllers_web_apime_controller_preference_options import API2ControllersWebAPIMeControllerPreferenceOptions
from openapi_server.models.api2_models_big_oven_user import API2ModelsBigOvenUser
from openapi_server.models.api2_models_personal import API2ModelsPersonal
from openapi_server.models.api2_models_preference import API2ModelsPreference
from openapi_server.models.api2_models_profile import API2ModelsProfile


pytestmark = pytest.mark.asyncio

async def test_me_get_options(client):
    """Test case for me_get_options

    Gets the options.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/me/preferences/options',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_me_index(client):
    """Test case for me_index

    Indexes this instance.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/me',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_me_profile_put(client):
    """Test case for me_profile_put

    Puts me.
    """
    body = openapi_server.API2ModelsProfile()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/me/profile',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_me_put_me(client):
    """Test case for me_put_me

    Puts me.
    """
    body = openapi_server.API2ModelsBigOvenUser()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/me',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_me_put_me_personal(client):
    """Test case for me_put_me_personal

    Puts me personal.
    """
    body = openapi_server.API2ModelsPersonal()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/me/personal',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_me_put_me_preferences(client):
    """Test case for me_put_me_preferences

    Puts me preferences.
    """
    body = openapi_server.API2ModelsPreference()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/me/preferences',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_me_skinny(client):
    """Test case for me_skinny

    Skinnies this instance.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/me/skinny',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

