# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.query_response import QueryResponse


pytestmark = pytest.mark.asyncio

async def test_get_concept_hmda(client):
    """Test case for get_concept_hmda

    Get information about a particular concept in this dataset.
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/data/hmda/concept/{concept}'.format(concept='concept_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_dataset_hmda(client):
    """Test case for get_dataset_hmda

    Get metadata for this dataset.
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/data/hmda',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_slice_metadata_hmda(client):
    """Test case for get_slice_metadata_hmda

    Get the metadata for a slice in this dataset.
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/data/hmda/slice/{slice}/metadata'.format(slice='slice_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_query_slice_hmda(client):
    """Test case for query_slice_hmda

    Query a slice in this dataset.
    """
    params = [('$select', 'select_example'),
                    ('$where', 'where_example'),
                    ('$group', 'group_example'),
                    ('$limit', 56),
                    ('$offset', 56),
                    ('$orderBy', 'order_by_example'),
                    ('$callback', 'param_callback_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/data/hmda/slice/{slice}'.format(slice='slice_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

