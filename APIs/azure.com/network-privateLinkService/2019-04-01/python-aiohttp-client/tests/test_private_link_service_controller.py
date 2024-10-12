# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.private_link_service import PrivateLinkService
from openapi_server.models.private_link_services_list_by_subscription_default_response import PrivateLinkServicesListBySubscriptionDefaultResponse


pytestmark = pytest.mark.asyncio

async def test_private_link_services_create_or_update(client):
    """Test case for private_link_services_create_or_update

    
    """
    parameters = {"etag":"etag","properties":{"ipConfigurations":[{"name":"name","etag":"etag","type":"type","properties":{"subnet":{"name":"name","etag":"etag","properties":"{}"},"privateIPAllocationMethod":"Static","privateIPAddress":"privateIPAddress","privateIPAddressVersion":"IPv4","provisioningState":"Succeeded","primary":True}},{"name":"name","etag":"etag","type":"type","properties":{"subnet":{"name":"name","etag":"etag","properties":"{}"},"privateIPAllocationMethod":"Static","privateIPAddress":"privateIPAddress","privateIPAddressVersion":"IPv4","provisioningState":"Succeeded","primary":True}}],"networkInterfaces":[{"etag":"etag","properties":"{}"},{"etag":"etag","properties":"{}"}],"privateEndpointConnections":[{"name":"name","etag":"etag","type":"type","properties":{"privateLinkServiceConnectionState":{"actionsRequired":"actionsRequired","description":"description","status":"status"},"privateEndpoint":{"etag":"etag","properties":"{}"},"provisioningState":"Succeeded"}},{"name":"name","etag":"etag","type":"type","properties":{"privateLinkServiceConnectionState":{"actionsRequired":"actionsRequired","description":"description","status":"status"},"privateEndpoint":{"etag":"etag","properties":"{}"},"provisioningState":"Succeeded"}}],"visibility":"{}","alias":"alias","loadBalancerFrontendIpConfigurations":[{"name":"name","etag":"etag","zones":["zones","zones"],"properties":"{}"},{"name":"name","etag":"etag","zones":["zones","zones"],"properties":"{}"}],"autoApproval":"{}","provisioningState":"Succeeded","fqdns":["fqdns","fqdns"]}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/privateLinkServices/{service_name}'.format(resource_group_name='resource_group_name_example', service_name='service_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

