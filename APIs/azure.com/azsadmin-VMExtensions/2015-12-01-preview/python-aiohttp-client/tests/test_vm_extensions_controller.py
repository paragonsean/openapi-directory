# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.vm_extension import VMExtension
from openapi_server.models.vm_extension_parameters import VMExtensionParameters


pytestmark = pytest.mark.asyncio

async def test_v_m_extensions_create(client):
    """Test case for v_m_extensions_create

    Create a Virtual Machine Extension Image.
    """
    extension = {"properties":{"sourceBlob":{"uri":"uri"},"isSystemExtension":True,"vmScaleSetEnabled":True,"vmOsType":"Unknown","provisioningState":"Creating","computeRole":"computeRole","supportMultipleExtensions":True}}
    params = [('api-version', '2015-12-01-preview')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Compute.Admin/locations/{location}/artifactTypes/VMExtension/publishers/{publisher}/types/{type}/versions/{version}'.format(subscription_id='subscription_id_example', location='location_example', publisher='publisher_example', type='type_example', version='version_example'),
        headers=headers,
        json=extension,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v_m_extensions_delete(client):
    """Test case for v_m_extensions_delete

    Deletes a Virtual Machine Extension Image.
    """
    params = [('api-version', '2015-12-01-preview')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Compute.Admin/locations/{location}/artifactTypes/VMExtension/publishers/{publisher}/types/{type}/versions/{version}'.format(subscription_id='subscription_id_example', location='location_example', publisher='publisher_example', type='type_example', version='version_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v_m_extensions_get(client):
    """Test case for v_m_extensions_get

    Returns requested Virtual Machine Extension Image.
    """
    params = [('api-version', '2015-12-01-preview')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Compute.Admin/locations/{location}/artifactTypes/VMExtension/publishers/{publisher}/types/{type}/versions/{version}'.format(subscription_id='subscription_id_example', location='location_example', publisher='publisher_example', type='type_example', version='version_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v_m_extensions_list(client):
    """Test case for v_m_extensions_list

    Returns a list of all Virtual Machine Extension Images.
    """
    params = [('api-version', '2015-12-01-preview')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Compute.Admin/locations/{location}/artifactTypes/VMExtension'.format(subscription_id='subscription_id_example', location='location_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

