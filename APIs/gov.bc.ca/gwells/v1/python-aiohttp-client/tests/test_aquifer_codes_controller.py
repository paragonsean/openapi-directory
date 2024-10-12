# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.aquifer_codes_demand_list200_response import AquiferCodesDemandList200Response
from openapi_server.models.aquifer_codes_materials_list200_response import AquiferCodesMaterialsList200Response
from openapi_server.models.aquifer_codes_productivity_list200_response import AquiferCodesProductivityList200Response
from openapi_server.models.aquifer_codes_quality_concerns_list200_response import AquiferCodesQualityConcernsList200Response
from openapi_server.models.aquifer_codes_subtypes_list200_response import AquiferCodesSubtypesList200Response
from openapi_server.models.aquifer_codes_vulnerability_list200_response import AquiferCodesVulnerabilityList200Response
from openapi_server.models.aquifer_codes_water_use_list200_response import AquiferCodesWaterUseList200Response


pytestmark = pytest.mark.asyncio

async def test_aquifer_codes_demand_list(client):
    """Test case for aquifer_codes_demand_list

    
    """
    params = [('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/gwells/api/v1/aquifer-codes/demand/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aquifer_codes_materials_list(client):
    """Test case for aquifer_codes_materials_list

    
    """
    params = [('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/gwells/api/v1/aquifer-codes/materials/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aquifer_codes_productivity_list(client):
    """Test case for aquifer_codes_productivity_list

    
    """
    params = [('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/gwells/api/v1/aquifer-codes/productivity/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aquifer_codes_quality_concerns_list(client):
    """Test case for aquifer_codes_quality_concerns_list

    
    """
    params = [('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/gwells/api/v1/aquifer-codes/quality-concerns/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aquifer_codes_subtypes_list(client):
    """Test case for aquifer_codes_subtypes_list

    
    """
    params = [('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/gwells/api/v1/aquifer-codes/subtypes/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aquifer_codes_vulnerability_list(client):
    """Test case for aquifer_codes_vulnerability_list

    
    """
    params = [('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/gwells/api/v1/aquifer-codes/vulnerability/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aquifer_codes_water_use_list(client):
    """Test case for aquifer_codes_water_use_list

    
    """
    params = [('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/gwells/api/v1/aquifer-codes/water-use/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

