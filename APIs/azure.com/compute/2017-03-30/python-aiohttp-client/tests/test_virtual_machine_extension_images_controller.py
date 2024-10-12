# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.virtual_machine_extension_image import VirtualMachineExtensionImage


pytestmark = pytest.mark.asyncio

async def test_virtual_machine_extension_images_get(client):
    """Test case for virtual_machine_extension_images_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Compute/locations/{location}/publishers/{publisher_name}/artifacttypes/vmextension/types/{type}/versions/{version}'.format(location='location_example', publisher_name='publisher_name_example', type='type_example', version='version_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtual_machine_extension_images_list_types(client):
    """Test case for virtual_machine_extension_images_list_types

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Compute/locations/{location}/publishers/{publisher_name}/artifacttypes/vmextension/types'.format(location='location_example', publisher_name='publisher_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtual_machine_extension_images_list_versions(client):
    """Test case for virtual_machine_extension_images_list_versions

    
    """
    params = [('$filter', 'filter_example'),
                    ('$top', 56),
                    ('$orderby', 'orderby_example'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Compute/locations/{location}/publishers/{publisher_name}/artifacttypes/vmextension/types/{type}/versions'.format(location='location_example', publisher_name='publisher_name_example', type='type_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

