# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.applied_inventories_parameters_service_plan import AppliedInventoriesParametersServicePlan
from openapi_server.models.error_not_found import ErrorNotFound
from openapi_server.models.order_parameters_service_offering import OrderParametersServiceOffering
from openapi_server.models.order_service_offering200_response import OrderServiceOffering200Response
from openapi_server.models.service_instances_collection import ServiceInstancesCollection
from openapi_server.models.service_offering import ServiceOffering
from openapi_server.models.service_offering_nodes_collection import ServiceOfferingNodesCollection
from openapi_server.models.service_offerings_collection import ServiceOfferingsCollection
from openapi_server.models.service_plans_collection import ServicePlansCollection
from openapi_server.models.tag import Tag


pytestmark = pytest.mark.asyncio

async def test_applied_inventories_tags_for_service_offering(client):
    """Test case for applied_inventories_tags_for_service_offering

    Invokes computing of ServiceInventories tags for given ServiceOffering
    """
    body = {"service_parameters":"{}"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='//api/catalog-inventory/v1.0/service_offerings/{id}/applied_inventories_tags'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_service_offering_service_instances(client):
    """Test case for list_service_offering_service_instances

    List ServiceInstances for ServiceOffering
    """
    params = [('limit', 100),
                    ('offset', 0),
                    ('filter', None),
                    ('sort_by', None)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='//api/catalog-inventory/v1.0/service_offerings/{id}/service_instances'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_service_offering_service_offering_nodes(client):
    """Test case for list_service_offering_service_offering_nodes

    List ServiceOfferingNodes for ServiceOffering
    """
    params = [('limit', 100),
                    ('offset', 0),
                    ('filter', None),
                    ('sort_by', None)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='//api/catalog-inventory/v1.0/service_offerings/{id}/service_offering_nodes'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_service_offering_service_plans(client):
    """Test case for list_service_offering_service_plans

    List ServicePlans for ServiceOffering
    """
    params = [('limit', 100),
                    ('offset', 0),
                    ('filter', None),
                    ('sort_by', None)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='//api/catalog-inventory/v1.0/service_offerings/{id}/service_plans'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_service_offerings(client):
    """Test case for list_service_offerings

    List ServiceOfferings
    """
    params = [('limit', 100),
                    ('offset', 0),
                    ('filter', None),
                    ('sort_by', None)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='//api/catalog-inventory/v1.0/service_offerings',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_order_service_offering(client):
    """Test case for order_service_offering

    Order an existing ServiceOffering
    """
    body = {"service_parameters":"{}","service_plan_id":"service_plan_id","provider_control_parameters":"{}"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='//api/catalog-inventory/v1.0/service_offerings/{id}/order'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_show_service_offering(client):
    """Test case for show_service_offering

    Show an existing ServiceOffering
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='//api/catalog-inventory/v1.0/service_offerings/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

