# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.accounts_list400_response import AccountsList400Response
from openapi_server.models.accounts_list401_response import AccountsList401Response
from openapi_server.models.accounts_list403_response import AccountsList403Response
from openapi_server.models.accounts_read404_response import AccountsRead404Response
from openapi_server.models.product_offering import ProductOffering
from openapi_server.models.product_offering_partial import ProductOfferingPartial


pytestmark = pytest.mark.asyncio

async def test_product_offerings_list(client):
    """Test case for product_offerings_list

    
    """
    params = [('id', ['id1,id2,id3']),
                    ('type', 'type_example'),
                    ('name', 'name_example'),
                    ('handover_metro_area', 'handover_metro_area_example'),
                    ('handover_metro_area_network', 'handover_metro_area_network_example'),
                    ('service_metro_area', 'service_metro_area_example'),
                    ('service_metro_area_network', 'service_metro_area_network_example'),
                    ('service_provider', 'service_provider_example'),
                    ('downgrade_allowed', 'downgrade_allowed_example'),
                    ('upgrade_allowed', 'upgrade_allowed_example'),
                    ('bandwidth', 56),
                    ('physical_port_speed', 56),
                    ('service_provider_region', 'service_provider_region_example'),
                    ('service_provider_pop', 'service_provider_pop_example'),
                    ('delivery_method', 'delivery_method_example'),
                    ('cloud_key', 'cloud_key_example'),
                    ('fields', 'handover_metro_area,service_provider')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/product-offerings',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_product_offerings_read(client):
    """Test case for product_offerings_read

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/product-offerings/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

