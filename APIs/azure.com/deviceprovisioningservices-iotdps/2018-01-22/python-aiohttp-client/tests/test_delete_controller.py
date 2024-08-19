# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_details import ErrorDetails


pytestmark = pytest.mark.asyncio

async def test_dps_certificate_delete(client):
    """Test case for dps_certificate_delete

    Delete the Provisioning Service Certificate.
    """
    params = [('certificate.name', 'certificate_name_example'),
                    ('certificate.rawBytes', 'certificate_raw_bytes_example'),
                    ('certificate.isVerified', True),
                    ('certificate.purpose', 'certificate_purpose_example'),
                    ('certificate.created', '2013-10-20T19:20:30+01:00'),
                    ('certificate.lastUpdated', '2013-10-20T19:20:30+01:00'),
                    ('certificate.hasPrivateKey', True),
                    ('certificate.nonce', 'certificate_nonce_example'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'if_match': 'if_match_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Devices/provisioningServices/{provisioning_service_name}/certificates/{certificate_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', provisioning_service_name='provisioning_service_name_example', certificate_name='certificate_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_iot_dps_resource_delete(client):
    """Test case for iot_dps_resource_delete

    Delete the Provisioning Service
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Devices/provisioningServices/{provisioning_service_name}'.format(provisioning_service_name='provisioning_service_name_example', subscription_id='subscription_id_example', resource_group_name='resource_group_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

