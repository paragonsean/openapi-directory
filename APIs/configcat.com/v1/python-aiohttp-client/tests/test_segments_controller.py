# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_segment_model import CreateSegmentModel
from openapi_server.models.segment_list_model import SegmentListModel
from openapi_server.models.segment_list_model_haljson import SegmentListModelHaljson
from openapi_server.models.segment_model import SegmentModel
from openapi_server.models.segment_model_haljson import SegmentModelHaljson
from openapi_server.models.update_segment_model import UpdateSegmentModel


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_create_segment(client):
    """Test case for create_segment

    Create Segment
    """
    body = {"comparator":"isOneOf","comparisonValue":"comparisonValue","name":"name","description":"description","comparisonAttribute":"comparisonAttribute"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/v1/products/{product_id}/segments'.format(product_id='product_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_segment(client):
    """Test case for delete_segment

    Delete Segment
    """
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/segments/{segment_id}'.format(segment_id='segment_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_segment(client):
    """Test case for get_segment

    Get Segment
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/segments/{segment_id}'.format(segment_id='segment_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_segments(client):
    """Test case for get_segments

    List Segments
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/products/{product_id}/segments'.format(product_id='product_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_update_segment(client):
    """Test case for update_segment

    Update Segment
    """
    body = {"comparator":"isOneOf","comparisonValue":"comparisonValue","name":"name","description":"description","comparisonAttribute":"comparisonAttribute"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PUT',
        path='/v1/segments/{segment_id}'.format(segment_id='segment_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

