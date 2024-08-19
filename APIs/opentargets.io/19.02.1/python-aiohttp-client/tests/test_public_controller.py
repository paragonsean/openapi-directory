# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_get_association_by_id(client):
    """Test case for get_association_by_id

    Get association by id
    """
    params = [('id', 'id_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v3/platform/public/association',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_association_filter(client):
    """Test case for get_association_filter

    Filter available associations
    """
    params = [('target', 'target_example'),
                    ('disease', 'disease_example'),
                    ('therapeutic_area', 'therapeutic_area_example'),
                    ('datasource', 'datasource_example'),
                    ('datatype', 'datatype_example'),
                    ('pathway', 'pathway_example'),
                    ('target_class', 'target_class_example'),
                    ('uniprotkw', 'uniprotkw_example'),
                    ('direct', True),
                    ('datastructure', 'datastructure_example'),
                    ('fields', 'fields_example'),
                    ('facets', False),
                    ('scorevalue_min', 0),
                    ('scorevalue_max', 3.4),
                    ('scorevalue_types', 'scorevalue_types_example'),
                    ('size', 3.4),
                    ('from', 3.4),
                    ('format', 'format_example'),
                    ('sort', 'sort_example'),
                    ('search', 'search_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v3/platform/public/association/filter',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_data_metrics(client):
    """Test case for get_data_metrics

    Get metrics about the current data release
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v3/platform/public/utils/metrics',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_data_stats(client):
    """Test case for get_data_stats

    Get statistics about the current data release
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v3/platform/public/utils/stats',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_evidence_by_id(client):
    """Test case for get_evidence_by_id

    Get evidence by ID
    """
    params = [('id', 'id_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v3/platform/public/evidence',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_evidence_filter(client):
    """Test case for get_evidence_filter

    Filter available evidence
    """
    params = [('target', 'target_example'),
                    ('disease', 'disease_example'),
                    ('data source', 'data_source_example'),
                    ('datatype', 'datatype_example'),
                    ('pathway', 'pathway_example'),
                    ('uniprotkw', 'uniprotkw_example'),
                    ('datastructure', 'datastructure_example'),
                    ('fields', 'fields_example'),
                    ('scorevalue_min', 0),
                    ('scorevalue_max', 3.4),
                    ('sort', 'sort_example'),
                    ('size', 3.4),
                    ('from', 3.4),
                    ('format', 'format_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v3/platform/public/evidence/filter',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_ping(client):
    """Test case for get_ping

    Ping service
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v3/platform/public/utils/ping',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_search(client):
    """Test case for get_search

    Search for a disease or a target
    """
    params = [('q', 'q_example'),
                    ('size', 'size_example'),
                    ('from', '_from_example'),
                    ('filter', 'filter_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v3/platform/public/search',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_therapeutic_areas(client):
    """Test case for get_therapeutic_areas

    Get the list of therapeutic areas about the current data release
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v3/platform/public/utils/therapeuticareas',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_version(client):
    """Test case for get_version

    Get API version
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v3/platform/public/utils/version',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_association_filter(client):
    """Test case for post_association_filter

    Batch query available associations
    """
    body = 'body_example'
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v3/platform/public/association/filter',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_evidence_by_id(client):
    """Test case for post_evidence_by_id

    Get evidence for a list of IDs
    """
    body = 'body_example'
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v3/platform/public/evidence',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_evidence_filter(client):
    """Test case for post_evidence_filter

    Batch filter available evidence
    """
    body = 'body_example'
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v3/platform/public/evidence/filter',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

