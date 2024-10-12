# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_active_sessions(client):
    """Test case for active_sessions

    &nbsp; <i class=\"fa fa-lg fa-unlock-alt\"></i>
    """
    headers = { 
        'Accept': 'application/json',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/user/active/sessions',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_panic_terminate(client):
    """Test case for panic_terminate

    &nbsp; <i class=\"fa fa-lg fa-unlock-alt\"></i>
    """
    blazemeter_routing_v4_user_model5 = None
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v4/user/active/terminate',
        headers=headers,
        json=blazemeter_routing_v4_user_model5,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_register(client):
    """Test case for register

    Registration&nbsp; <i class=\"fa fa-lg fa-unlock-alt\"></i>
    """
    blazemeter_routing_v4_user_model4 = None
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v4/user/register',
        headers=headers,
        json=blazemeter_routing_v4_user_model4,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_register_retrieve(client):
    """Test case for register_retrieve

    Registration&nbsp; <i class=\"fa fa-lg fa-unlock-alt\"></i>
    """
    params = [('email', 'email_example'),
                    ('password', 'password_example'),
                    ('firstName', 'first_name_example'),
                    ('lastName', 'last_name_example')]
    headers = { 
        'Accept': 'application/json',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/user/register',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retrieve_collections(client):
    """Test case for retrieve_collections

    List organization multi-tests&nbsp; <i class=\"fa fa-lg fa-unlock-alt\"></i>
    """
    params = [('skip', 'skip_example'),
                    ('limit', 'limit_example')]
    headers = { 
        'Accept': 'application/json',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/user/collections',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retrieve_invites(client):
    """Test case for retrieve_invites

    &nbsp; <i class=\"fa fa-lg fa-unlock-alt\"></i>
    """
    headers = { 
        'Accept': 'application/json',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/user/invites',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retrieve_locations(client):
    """Test case for retrieve_locations

    Get user available locations&nbsp; <i class=\"fa fa-lg fa-unlock-alt\"></i>
    """
    headers = { 
        'Accept': 'application/json',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/user/locations',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retrieve_masters(client):
    """Test case for retrieve_masters

    List user private masters&nbsp; <i class=\"fa fa-lg fa-unlock-alt\"></i>
    """
    params = [('skip', 56),
                    ('limit', 1000)]
    headers = { 
        'Accept': 'application/json',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/user/masters',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retrieve_projects(client):
    """Test case for retrieve_projects

    Get user projects&nbsp; <i class=\"fa fa-lg fa-unlock-alt\"></i>
    """
    headers = { 
        'Accept': 'application/json',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/user/projects',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retrieve_tests(client):
    """Test case for retrieve_tests

    List user private tests&nbsp; <i class=\"fa fa-lg fa-unlock-alt\"></i>
    """
    params = [('skip', 'skip_example'),
                    ('limit', 'limit_example')]
    headers = { 
        'Accept': 'application/json',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/user/tests',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_top(client):
    """Test case for top

    &nbsp; <i class=\"fa fa-lg fa-unlock-alt\"></i>
    """
    headers = { 
        'Accept': 'application/json',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/user/top',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_user_password_patch(client):
    """Test case for user_password_patch

    Update user name&nbsp; <i class=\"fa fa-lg fa-unlock-alt\"></i>
    """
    blazemeter_routing_v4_user_model1 = None
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v4/user/password',
        headers=headers,
        json=blazemeter_routing_v4_user_model1,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_user_password_post(client):
    """Test case for user_password_post

    Update user name&nbsp; <i class=\"fa fa-lg fa-unlock-alt\"></i>
    """
    blazemeter_routing_v4_user_model3 = None
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v4/user/password',
        headers=headers,
        json=blazemeter_routing_v4_user_model3,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_user_password_put(client):
    """Test case for user_password_put

    Update user name&nbsp; <i class=\"fa fa-lg fa-unlock-alt\"></i>
    """
    blazemeter_routing_v4_user_model2 = None
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v4/user/password',
        headers=headers,
        json=blazemeter_routing_v4_user_model2,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

