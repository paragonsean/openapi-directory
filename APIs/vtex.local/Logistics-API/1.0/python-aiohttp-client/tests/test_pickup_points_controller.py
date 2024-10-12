# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_update import CreateUpdate
from openapi_server.models.create_update_pickup_point_request import CreateUpdatePickupPointRequest
from openapi_server.models.get_by_id1 import GetById1
from openapi_server.models.list_all_pickup_ppoints200_response_inner import ListAllPickupPpoints200ResponseInner


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/json; charset&#x3D;utf-8 not supported by Connexion")
async def test_create_update_pickup_point(client):
    """Test case for create_update_pickup_point

    Create/Update Pickup Point
    """
    body = {"address":{"city":"Rio de Janeiro","complement":"","country":{"acronym":"BRA","name":"Brazil"},"location":{"latitude":-22.974477767944336,"longitude":-43.18672561645508},"neighborhood":"Copacabana","number":"","postalCode":"22070002","reference":"Grey building","state":"RJ","street":"Avenida Atl├óntica"},"businessHours":[{"closingTime":72000,"dayOfWeek":1,"openingTime":"08:00:00"},{"closingTime":72000,"dayOfWeek":2,"openingTime":"08:00:00"},{"closingTime":72000,"dayOfWeek":3,"openingTime":"08:00:00"},{"closingTime":72000,"dayOfWeek":4,"openingTime":"08:00:00"},{"closingTime":72000,"dayOfWeek":5,"openingTime":"08:00:00"}],"description":"","formatted_address":"undefined","id":"1a227d3","instructions":"Obrigat├│rio apresentar documento de identifica├º├úo","isActive":true,"name":"Loja Copacabana","tagsLabel":["zonasul","rio de janeiro"]}
    headers = { 
        'Accept': 'application/json; charset=utf-8',
        'Content-Type': 'application/json; charset=utf-8',
        'content_type': 'application/json; charset=utf-8',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/logistics/pvt/configuration/pickuppoints/{pickup_point_id}'.format(pickup_point_id='123456789'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete(client):
    """Test case for delete

    Delete Pickup Point
    """
    headers = { 
        'content_type': 'application/json; charset=utf-8',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/logistics/pvt/configuration/pickuppoints/{pickup_point_id}'.format(pickup_point_id='pickup_point_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_by_id(client):
    """Test case for get_by_id

    List Pickup Point By ID
    """
    headers = { 
        'Accept': 'application/json; charset=utf-8',
        'content_type': 'application/json; charset=utf-8',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/logistics/pvt/configuration/pickuppoints/{pickup_point_id}'.format(pickup_point_id='pickup_point_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_getpaged(client):
    """Test case for getpaged

    List paged Pickup Points
    """
    params = [('page', '{{pageNumber}}'),
                    ('pageSize', '{{pageSize}}'),
                    ('keyword', '')]
    headers = { 
        'content_type': 'application/json; charset=utf-8',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/logistics/pvt/configuration/pickuppoints/_search',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_all_pickup_ppoints(client):
    """Test case for list_all_pickup_ppoints

    List all pickup points
    """
    headers = { 
        'Accept': 'application/json; charset=utf-8',
        'content_type': 'application/json; charset=utf-8',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/logistics/pvt/configuration/pickuppoints',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

