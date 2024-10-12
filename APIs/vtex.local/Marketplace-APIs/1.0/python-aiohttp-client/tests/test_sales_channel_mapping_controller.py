# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.upsert_mapping_request import UpsertMappingRequest


pytestmark = pytest.mark.asyncio

async def test_retrieve_mapping(client):
    """Test case for retrieve_mapping

    Get Sales Channel Mapping Data
    """
    params = [('accountName', 'apiexamples'),
                    ('environment', 'vtexcommercestable'),
                    ('an', 'apiexamples')]
    headers = { 
        'Accept': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/seller-register/pvt/sellers/{seller_id}/sales-channel/mapping'.format(seller_id='seller123'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_upsert_mapping(client):
    """Test case for upsert_mapping

    Upsert Sales Channel Mapping
    """
    body = {"marketplaceSalesChannel":1,"sellerChannel":"GCB"}
    params = [('accountName', 'apiexamples'),
                    ('environment', 'vtexcommercestable'),
                    ('an', 'apiexamples')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/seller-register/pvt/sellers/{seller_id}/sales-channel/mapping'.format(seller_id='seller123'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

