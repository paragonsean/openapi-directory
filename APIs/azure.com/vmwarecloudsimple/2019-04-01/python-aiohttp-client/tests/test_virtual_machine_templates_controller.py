# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.csrp_error import CSRPError
from openapi_server.models.virtual_machine_template import VirtualMachineTemplate
from openapi_server.models.virtual_machine_template_list_response import VirtualMachineTemplateListResponse


pytestmark = pytest.mark.asyncio

async def test_virtual_machine_templates_get(client):
    """Test case for virtual_machine_templates_get

    Implements virtual machine template GET method
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.VMwareCloudSimple/locations/{region_id}/privateClouds/{pc_name}/virtualMachineTemplates/{virtual_machine_template_name}'.format(subscription_id='subscription_id_example', region_id='region_id_example', pc_name='pc_name_example', virtual_machine_template_name='virtual_machine_template_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtual_machine_templates_list(client):
    """Test case for virtual_machine_templates_list

    Implements list of available VM templates
    """
    params = [('api-version', 'api_version_example'),
                    ('resourcePoolName', 'resource_pool_name_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.VMwareCloudSimple/locations/{region_id}/privateClouds/{pc_name}/virtualMachineTemplates'.format(subscription_id='subscription_id_example', pc_name='pc_name_example', region_id='region_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

