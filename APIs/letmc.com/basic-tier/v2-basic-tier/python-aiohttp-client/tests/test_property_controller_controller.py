# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.photo_model_results import PhotoModelResults
from openapi_server.models.property_facility_model_results import PropertyFacilityModelResults
from openapi_server.models.property_model import PropertyModel
from openapi_server.models.property_model_results import PropertyModelResults
from openapi_server.models.property_room_model_results import PropertyRoomModelResults
from openapi_server.models.tenancy_model_results import TenancyModelResults


pytestmark = pytest.mark.asyncio

async def test_property_controller_get_properties_facilities(client):
    """Test case for property_controller_get_properties_facilities

    A collection of facilities linked to a block, property or room
    """
    params = [('offset', 56),
                    ('count', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/tier2/{short_name}/property/properties/{property_id}/facilities'.format(short_name='short_name_example', property_id='property_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_property_controller_get_properties_photos(client):
    """Test case for property_controller_get_properties_photos

    A collection showing all the photos linked to a specific block, property or room
    """
    params = [('offset', 56),
                    ('count', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/tier2/{short_name}/property/properties/{property_id}/photos'.format(short_name='short_name_example', property_id='property_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_property_controller_get_properties_rooms(client):
    """Test case for property_controller_get_properties_rooms

    A collection of the rooms that belong to this property or block
    """
    params = [('offset', 56),
                    ('count', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/tier2/{short_name}/property/properties/{property_id}/rooms'.format(short_name='short_name_example', property_id='property_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_property_controller_get_properties_tenancies(client):
    """Test case for property_controller_get_properties_tenancies

    A collection of all tenancies associated with this block, property or room
    """
    params = [('offset', 56),
                    ('count', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/tier2/{short_name}/property/properties/{property_id}/tenancies'.format(short_name='short_name_example', property_id='property_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_property_controller_get_property_eer_download(client):
    """Test case for property_controller_get_property_eer_download

    Downloads the energy efficiency report (EER) graph for a property
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/tier2/{short_name}/property/structures/{property_structure_id}/reports/eer'.format(short_name='short_name_example', property_structure_id='property_structure_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_property_controller_get_property_eir_download(client):
    """Test case for property_controller_get_property_eir_download

    Downloads the environmental impact report (EIR) graph for a property
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/tier2/{short_name}/property/structures/{property_structure_id}/reports/eir'.format(short_name='short_name_example', property_structure_id='property_structure_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v2_tier2_short_name_property_properties_get(client):
    """Test case for v2_tier2_short_name_property_properties_get

    A collection of all properties within a company
    """
    params = [('offset', 56),
                    ('count', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/tier2/{short_name}/property/properties'.format(short_name='short_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v2_tier2_short_name_property_properties_property_idget(client):
    """Test case for v2_tier2_short_name_property_properties_property_idget

    Get a specific property given its unique Object ID (OID)
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/tier2/{short_name}/property/properties/{property_id}'.format(short_name='short_name_example', property_id='property_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

