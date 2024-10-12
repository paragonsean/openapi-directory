# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.photo_model_results import PhotoModelResults
from openapi_server.models.property_room_model_results import PropertyRoomModelResults
from openapi_server.models.sales_feature_model_results import SalesFeatureModelResults
from openapi_server.models.sales_feature_type_model import SalesFeatureTypeModel
from openapi_server.models.sales_feature_type_model_results import SalesFeatureTypeModelResults
from openapi_server.models.sales_instruction_model import SalesInstructionModel
from openapi_server.models.sales_instruction_model_results import SalesInstructionModelResults


pytestmark = pytest.mark.asyncio

async def test_sales_controller_get_advertised_sales(client):
    """Test case for sales_controller_get_advertised_sales

    Search all sales properties available given a range of search criteria
    """
    params = [('branchID', 'branch_id_example'),
                    ('offset', 56),
                    ('count', 56),
                    ('onlyDevelopement', True),
                    ('onlyInvestements', True),
                    ('minimumPrice', 3.4),
                    ('maximumPrice', 3.4),
                    ('minimumBeds', 56),
                    ('minimumBathrooms', 56),
                    ('minimumEnsuites', 56),
                    ('minimumToilets', 56),
                    ('minimumReception', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/tier1/{short_name}/sales/advertisedsales'.format(short_name='short_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sales_controller_get_eer(client):
    """Test case for sales_controller_get_eer

    Downloads the energy efficiency report (EER) graph for a sales instruction
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/tier1/{short_name}/sales/reports/eer/{sales_instruction_id}'.format(short_name='short_name_example', sales_instruction_id='sales_instruction_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sales_controller_get_eir(client):
    """Test case for sales_controller_get_eir

    Downloads the energy efficiency report (EIR) graph for a sales instruction
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/tier1/{short_name}/sales/reports/eir/{sales_instruction_id}'.format(short_name='short_name_example', sales_instruction_id='sales_instruction_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sales_controller_get_sales_instructions_features(client):
    """Test case for sales_controller_get_sales_instructions_features

    A collection of all features linked to a sales instruction
    """
    params = [('offset', 56),
                    ('count', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/tier1/{short_name}/sales/salesinstructions/{sales_instruction_id}/features'.format(short_name='short_name_example', sales_instruction_id='sales_instruction_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sales_controller_get_sales_instructions_floor_plans(client):
    """Test case for sales_controller_get_sales_instructions_floor_plans

    A collection of floor plans linked to an instruction
    """
    params = [('offset', 56),
                    ('count', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/tier1/{short_name}/sales/salesinstructions/{sales_instruction_id}/floorplans'.format(short_name='short_name_example', sales_instruction_id='sales_instruction_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sales_controller_get_sales_instructions_photos(client):
    """Test case for sales_controller_get_sales_instructions_photos

    A collection of photos linked to an instruction
    """
    params = [('offset', 56),
                    ('count', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/tier1/{short_name}/sales/salesinstructions/{sales_instruction_id}/photos'.format(short_name='short_name_example', sales_instruction_id='sales_instruction_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sales_controller_get_sales_instructions_rooms(client):
    """Test case for sales_controller_get_sales_instructions_rooms

    A collection of rooms linked to an instruction
    """
    params = [('offset', 56),
                    ('count', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/tier1/{short_name}/sales/salesinstructions/{sales_instruction_id}/rooms'.format(short_name='short_name_example', sales_instruction_id='sales_instruction_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v2_tier1_short_name_sales_salesfeaturetypes_get(client):
    """Test case for v2_tier1_short_name_sales_salesfeaturetypes_get

    A collection of all sales feature types linked to a company
    """
    params = [('offset', 56),
                    ('count', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/tier1/{short_name}/sales/salesfeaturetypes'.format(short_name='short_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v2_tier1_short_name_sales_salesfeaturetypes_sales_feature_type_idget(client):
    """Test case for v2_tier1_short_name_sales_salesfeaturetypes_sales_feature_type_idget

    Get a specific sales feature type given its unique Object ID (OID)
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/tier1/{short_name}/sales/salesfeaturetypes/{sales_feature_type_id}'.format(short_name='short_name_example', sales_feature_type_id='sales_feature_type_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v2_tier1_short_name_sales_salesinstructions_get(client):
    """Test case for v2_tier1_short_name_sales_salesinstructions_get

    A collection of all sales instructions linked to a company
    """
    params = [('offset', 56),
                    ('count', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/tier1/{short_name}/sales/salesinstructions'.format(short_name='short_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v2_tier1_short_name_sales_salesinstructions_sales_instruction_idget(client):
    """Test case for v2_tier1_short_name_sales_salesinstructions_sales_instruction_idget

    Get a specific sales instruction given its unique Object ID (OID)
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/tier1/{short_name}/sales/salesinstructions/{sales_instruction_id}'.format(short_name='short_name_example', sales_instruction_id='sales_instruction_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

