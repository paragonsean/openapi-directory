# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.automotive_parts_compatibility_policy_response import AutomotivePartsCompatibilityPolicyResponse
from openapi_server.models.extended_producer_responsibility_policy_response import ExtendedProducerResponsibilityPolicyResponse
from openapi_server.models.hazardous_material_details_response import HazardousMaterialDetailsResponse
from openapi_server.models.item_condition_policy_response import ItemConditionPolicyResponse
from openapi_server.models.listing_structure_policy_response import ListingStructurePolicyResponse
from openapi_server.models.negotiated_price_policy_response import NegotiatedPricePolicyResponse
from openapi_server.models.return_policy_response import ReturnPolicyResponse


pytestmark = pytest.mark.asyncio

async def test_get_automotive_parts_compatibility_policies(client):
    """Test case for get_automotive_parts_compatibility_policies

    
    """
    params = [('filter', 'filter_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/sell/metadata/v1/marketplace/{marketplace_id}/get_automotive_parts_compatibility_policies'.format(marketplace_id='marketplace_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_extended_producer_responsibility_policies(client):
    """Test case for get_extended_producer_responsibility_policies

    
    """
    params = [('filter', 'filter_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/sell/metadata/v1/marketplace/{marketplace_id}/get_extended_producer_responsibility_policies'.format(marketplace_id='marketplace_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_hazardous_materials_labels(client):
    """Test case for get_hazardous_materials_labels

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/sell/metadata/v1/marketplace/{marketplace_id}/get_hazardous_materials_labels'.format(marketplace_id='marketplace_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_item_condition_policies(client):
    """Test case for get_item_condition_policies

    
    """
    params = [('filter', 'filter_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/sell/metadata/v1/marketplace/{marketplace_id}/get_item_condition_policies'.format(marketplace_id='marketplace_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_listing_structure_policies(client):
    """Test case for get_listing_structure_policies

    
    """
    params = [('filter', 'filter_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/sell/metadata/v1/marketplace/{marketplace_id}/get_listing_structure_policies'.format(marketplace_id='marketplace_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_negotiated_price_policies(client):
    """Test case for get_negotiated_price_policies

    
    """
    params = [('filter', 'filter_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/sell/metadata/v1/marketplace/{marketplace_id}/get_negotiated_price_policies'.format(marketplace_id='marketplace_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_return_policies(client):
    """Test case for get_return_policies

    
    """
    params = [('filter', 'filter_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/sell/metadata/v1/marketplace/{marketplace_id}/get_return_policies'.format(marketplace_id='marketplace_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

