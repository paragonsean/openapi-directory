# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_organism_attribute_search_query_get(client):
    """Test case for organism_attribute_search_query_get

    
    """
    params = [('limit', 56),
                    ('attrName', 'attr_name_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/{organism}/attributeSearch/{query}'.format(organism='organism_example', query='query_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_organism_attribute_set_get(client):
    """Test case for organism_attribute_set_get

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/{organism}/attributeSet'.format(organism='organism_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_organism_attributes_system_code_identifier_get(client):
    """Test case for organism_attributes_system_code_identifier_get

    
    """
    params = [('attrName', 'attr_name_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/{organism}/attributes/{system_code}/{identifier}'.format(organism='organism_example', system_code=En, identifier='ENSG00000122375'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_organism_is_free_search_supported_get(client):
    """Test case for organism_is_free_search_supported_get

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/{organism}/isFreeSearchSupported'.format(organism='organism_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_organism_is_mapping_supported_source_system_code_target_system_code_get(client):
    """Test case for organism_is_mapping_supported_source_system_code_target_system_code_get

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/{organism}/isMappingSupported/{source_system_code}/{target_system_code}'.format(organism='organism_example', source_system_code=L, target_system_code='target_system_code_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_organism_properties_get(client):
    """Test case for organism_properties_get

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/{organism}/properties'.format(organism='organism_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_organism_search_query_get(client):
    """Test case for organism_search_query_get

    
    """
    params = [('limit', 56)]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/{organism}/search/{query}'.format(organism='organism_example', query='1234'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_organism_source_data_sources_get(client):
    """Test case for organism_source_data_sources_get

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/{organism}/sourceDataSources'.format(organism='organism_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_organism_target_data_sources_get(client):
    """Test case for organism_target_data_sources_get

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/{organism}/targetDataSources'.format(organism='organism_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_organism_xref_exists_system_code_identifier_get(client):
    """Test case for organism_xref_exists_system_code_identifier_get

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/{organism}/xrefExists/{system_code}/{identifier}'.format(organism='organism_example', system_code=L, identifier='1234'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/html not supported by Connexion")
async def test_organism_xrefs_batch_post(client):
    """Test case for organism_xrefs_batch_post

    
    """
    body = 'body_example'
    params = [('dataSource', 'data_source_example')]
    headers = { 
        'Content-Type': 'text/html',
    }
    response = await client.request(
        method='POST',
        path='/{organism}/xrefsBatch'.format(organism='organism_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/html not supported by Connexion")
async def test_organism_xrefs_batch_system_code_post(client):
    """Test case for organism_xrefs_batch_system_code_post

    
    """
    body = 'body_example'
    params = [('dataSource', 'data_source_example')]
    headers = { 
        'Content-Type': 'text/html',
    }
    response = await client.request(
        method='POST',
        path='/{organism}/xrefsBatch/{system_code}'.format(organism='organism_example', system_code=L),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_organism_xrefs_system_code_identifier_get(client):
    """Test case for organism_xrefs_system_code_identifier_get

    
    """
    params = [('dataSource', 'data_source_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/{organism}/xrefs/{system_code}/{identifier}'.format(organism='organism_example', system_code=L, identifier='1234'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

