# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.certificate_body_description import CertificateBodyDescription
from openapi_server.models.certificate_response import CertificateResponse
from openapi_server.models.error_details import ErrorDetails
from openapi_server.models.provisioning_service_description import ProvisioningServiceDescription


pytestmark = pytest.mark.asyncio

async def test_dps_certificate_create_or_update(client):
    """Test case for dps_certificate_create_or_update

    Upload the certificate to the provisioning service.
    """
    certificate_description = {"certificate":"certificate"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'if_match': 'if_match_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Devices/provisioningServices/{provisioning_service_name}/certificates/{certificate_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', provisioning_service_name='provisioning_service_name_example', certificate_name='certificate_name_example'),
        headers=headers,
        json=certificate_description,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_iot_dps_resource_create_or_update(client):
    """Test case for iot_dps_resource_create_or_update

    Create or update the metadata of the provisioning service.
    """
    iot_dps_description = {"etag":"etag","sku":{"tier":"tier","name":"S1","capacity":6},"properties":{"iotHubs":[{"connectionString":"connectionString","applyAllocationPolicy":True,"allocationWeight":0,"name":"name","location":"location"},{"connectionString":"connectionString","applyAllocationPolicy":True,"allocationWeight":0,"name":"name","location":"location"}],"serviceOperationsHostName":"serviceOperationsHostName","deviceProvisioningHostName":"deviceProvisioningHostName","idScope":"idScope","provisioningState":"provisioningState","state":"Activating","authorizationPolicies":[{"secondaryKey":"secondaryKey","rights":"ServiceConfig","keyName":"keyName","primaryKey":"primaryKey"},{"secondaryKey":"secondaryKey","rights":"ServiceConfig","keyName":"keyName","primaryKey":"primaryKey"}],"allocationPolicy":"Hashed"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Devices/provisioningServices/{provisioning_service_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', provisioning_service_name='provisioning_service_name_example'),
        headers=headers,
        json=iot_dps_description,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

