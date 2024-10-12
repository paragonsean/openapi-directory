# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.configuration import Configuration
from openapi_server.models.individual_update import IndividualUpdate
from openapi_server.models.interactions import Interactions
from openapi_server.models.new_update import NewUpdate
from openapi_server.models.profile import Profile
from openapi_server.models.profiles_inner import ProfilesInner
from openapi_server.models.schedules import Schedules
from openapi_server.models.shares import Shares
from openapi_server.models.shuffle import Shuffle
from openapi_server.models.success import Success
from openapi_server.models.update import Update
from openapi_server.models.updates_array import UpdatesArray
from openapi_server.models.user import User


pytestmark = pytest.mark.asyncio

async def test_info_configurationmedia_type_extension_get(client):
    """Test case for info_configurationmedia_type_extension_get

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/1/info/configuration{mediaTypeExtension}'.format(media_type_extension='media_type_extension_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_links_sharesmedia_type_extension_get(client):
    """Test case for links_sharesmedia_type_extension_get

    
    """
    params = [('url', 'url_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/1/links/shares{mediaTypeExtension}'.format(media_type_extension='media_type_extension_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_profiles_id_schedules_updatemedia_type_extension_post(client):
    """Test case for profiles_id_schedules_updatemedia_type_extension_post

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/1/profiles/{id}/schedules/update{mediaTypeExtension}'.format(id='id_example', media_type_extension='media_type_extension_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_profiles_id_schedulesmedia_type_extension_get(client):
    """Test case for profiles_id_schedulesmedia_type_extension_get

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/1/profiles/{id}/schedules{mediaTypeExtension}'.format(id='id_example', media_type_extension='media_type_extension_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_profiles_id_updates_pendingmedia_type_extension_get(client):
    """Test case for profiles_id_updates_pendingmedia_type_extension_get

    
    """
    params = [('page', 56),
                    ('count', 56),
                    ('since', '2013-10-20'),
                    ('utc', True)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/1/profiles/{id}/updates/pending{mediaTypeExtension}'.format(id='id_example', media_type_extension='media_type_extension_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_profiles_id_updates_reordermedia_type_extension_post(client):
    """Test case for profiles_id_updates_reordermedia_type_extension_post

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/1/profiles/{id}/updates/reorder{mediaTypeExtension}'.format(id='id_example', media_type_extension='media_type_extension_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_profiles_id_updates_sentmedia_type_extension_get(client):
    """Test case for profiles_id_updates_sentmedia_type_extension_get

    
    """
    params = [('page', 56),
                    ('count', 56),
                    ('since', '2013-10-20'),
                    ('utc', True)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/1/profiles/{id}/updates/sent{mediaTypeExtension}'.format(id='id_example', media_type_extension='media_type_extension_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_profiles_id_updates_shufflemedia_type_extension_post(client):
    """Test case for profiles_id_updates_shufflemedia_type_extension_post

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/1/profiles/{id}/updates/shuffle{mediaTypeExtension}'.format(id='id_example', media_type_extension='media_type_extension_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_profiles_idmedia_type_extension_get(client):
    """Test case for profiles_idmedia_type_extension_get

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/1/profiles/{idmedia_type_extension}'.format(media_type_extension='media_type_extension_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_profilesmedia_type_extension_get(client):
    """Test case for profilesmedia_type_extension_get

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/1/profiles{mediaTypeExtension}'.format(media_type_extension='media_type_extension_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_updates_createmedia_type_extension_post(client):
    """Test case for updates_createmedia_type_extension_post

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/1/updates/create{mediaTypeExtension}'.format(media_type_extension='media_type_extension_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_updates_id_destroymedia_type_extension_post(client):
    """Test case for updates_id_destroymedia_type_extension_post

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/1/updates/{id}/destroy{mediaTypeExtension}'.format(id='id_example', media_type_extension='media_type_extension_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_updates_id_interactionsmedia_type_extension_get(client):
    """Test case for updates_id_interactionsmedia_type_extension_get

    
    """
    params = [('event', 'event_example'),
                    ('page', 56),
                    ('count', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/1/updates/{id}/interactions{mediaTypeExtension}'.format(id='id_example', media_type_extension='media_type_extension_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_updates_id_move_to_topmedia_type_extension_post(client):
    """Test case for updates_id_move_to_topmedia_type_extension_post

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/1/updates/{id}/move_to_top{mediaTypeExtension}'.format(id='id_example', media_type_extension='media_type_extension_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_updates_id_sharemedia_type_extension_post(client):
    """Test case for updates_id_sharemedia_type_extension_post

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/1/updates/{id}/share{mediaTypeExtension}'.format(id='id_example', media_type_extension='media_type_extension_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_updates_id_updatemedia_type_extension_post(client):
    """Test case for updates_id_updatemedia_type_extension_post

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/1/updates/{id}/update{mediaTypeExtension}'.format(id='id_example', media_type_extension='media_type_extension_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_updates_idmedia_type_extension_get(client):
    """Test case for updates_idmedia_type_extension_get

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/1/updates/{idmedia_type_extension}'.format(media_type_extension='media_type_extension_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_usermedia_type_extension_get(client):
    """Test case for usermedia_type_extension_get

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/1/user{mediaTypeExtension}'.format(media_type_extension='media_type_extension_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

