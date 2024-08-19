# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_get_association_filter_0(client):
    """Test case for get_association_filter_0

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

async def test_get_evidence_filter_0(client):
    """Test case for get_evidence_filter_0

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

async def test_post_association_filter_0(client):
    """Test case for post_association_filter_0

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

async def test_post_evidence_filter_0(client):
    """Test case for post_evidence_filter_0

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

