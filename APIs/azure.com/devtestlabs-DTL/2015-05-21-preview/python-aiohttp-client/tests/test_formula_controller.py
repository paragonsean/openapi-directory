# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.formula import Formula
from openapi_server.models.response_with_continuation_formula import ResponseWithContinuationFormula


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_formula_create_or_update_resource(client):
    """Test case for formula_create_or_update_resource

    
    """
    formula = {"name":"name","location":"location","id":"id","type":"type","properties":{"author":"author","vm":{"labVmId":"labVmId"},"formulaContent":{"name":"name","location":"location","id":"id","type":"type","properties":{"createdByUserId":"createdByUserId","labVirtualNetworkId":"labVirtualNetworkId","notes":"notes","createdByUser":"createdByUser","fqdn":"fqdn","provisioningState":"provisioningState","userName":"userName","labSubnetName":"labSubnetName","artifactDeploymentStatus":{"deploymentStatus":"deploymentStatus","artifactsApplied":0,"totalArtifacts":6},"disallowPublicIpAddress":True,"password":"password","computeId":"computeId","isAuthenticationWithSshKey":True,"size":"size","sshKey":"sshKey","ownerObjectId":"ownerObjectId","osType":"osType","galleryImageReference":{"offer":"offer","osType":"osType","publisher":"publisher","sku":"sku","version":"version"},"artifacts":[{"artifactId":"artifactId","parameters":[{"name":"name","value":"value"},{"name":"name","value":"value"}]},{"artifactId":"artifactId","parameters":[{"name":"name","value":"value"},{"name":"name","value":"value"}]}],"customImageId":"customImageId"},"tags":{"key":"tags"}},"osType":"osType","description":"description","provisioningState":"provisioningState","creationDate":"2000-01-23T04:56:07.000+00:00"},"tags":{"key":"tags"}}
    params = [('api-version', '2015-05-21-preview')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DevTestLab/labs/{lab_name}/formulas/{name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', lab_name='lab_name_example', name='name_example'),
        headers=headers,
        json=formula,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_formula_delete_resource(client):
    """Test case for formula_delete_resource

    
    """
    params = [('api-version', '2015-05-21-preview')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DevTestLab/labs/{lab_name}/formulas/{name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', lab_name='lab_name_example', name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_formula_get_resource(client):
    """Test case for formula_get_resource

    
    """
    params = [('api-version', '2015-05-21-preview')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DevTestLab/labs/{lab_name}/formulas/{name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', lab_name='lab_name_example', name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_formula_list(client):
    """Test case for formula_list

    
    """
    params = [('$filter', 'filter_example'),
                    ('$top', 56),
                    ('$orderBy', 'order_by_example'),
                    ('api-version', '2015-05-21-preview')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DevTestLab/labs/{lab_name}/formulas'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', lab_name='lab_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

