# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.seriestype import Seriestype
from openapi_server.models.seriestyperule import Seriestyperule
from openapi_server.models.seriestyperuleattribute import Seriestyperuleattribute
from openapi_server.models.seriestypeupdatestatus import Seriestypeupdatestatus


pytestmark = pytest.mark.asyncio

async def test_seriestypes_get(client):
    """Test case for seriestypes_get

    
    """
    params = [('startindex', 0),
                    ('count', 20)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/seriestypes',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_seriestypes_id_delete(client):
    """Test case for seriestypes_id_delete

    
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/api/seriestypes/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_seriestypes_id_put(client):
    """Test case for seriestypes_id_put

    
    """
    headers = { 
    }
    response = await client.request(
        method='PUT',
        path='/api/seriestypes/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_seriestypes_post(client):
    """Test case for seriestypes_post

    
    """
    series_type = openapi_server.Seriestype()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/seriestypes',
        headers=headers,
        json=series_type,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_seriestypes_rules_get(client):
    """Test case for seriestypes_rules_get

    
    """
    params = [('seriestypeid', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/seriestypes/rules',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_seriestypes_rules_id_attributes_get(client):
    """Test case for seriestypes_rules_id_attributes_get

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/seriestypes/rules/{id}/attributes'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_seriestypes_rules_id_attributes_post(client):
    """Test case for seriestypes_rules_id_attributes_post

    
    """
    series_type_rule_attribute = openapi_server.Seriestyperuleattribute()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/seriestypes/rules/{id}/attributes'.format(id=56),
        headers=headers,
        json=series_type_rule_attribute,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_seriestypes_rules_id_delete(client):
    """Test case for seriestypes_rules_id_delete

    
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/api/seriestypes/rules/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_seriestypes_rules_post(client):
    """Test case for seriestypes_rules_post

    
    """
    series_type_rule = openapi_server.Seriestyperule()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/seriestypes/rules',
        headers=headers,
        json=series_type_rule,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_seriestypes_rules_rule_id_attributes_attribute_id_delete(client):
    """Test case for seriestypes_rules_rule_id_attributes_attribute_id_delete

    
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/api/seriestypes/rules/{rule_id}/attributes/{attribute_id}'.format(rule_id=56, attribute_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_seriestypes_rules_updatestatus_get(client):
    """Test case for seriestypes_rules_updatestatus_get

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/seriestypes/rules/updatestatus',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

