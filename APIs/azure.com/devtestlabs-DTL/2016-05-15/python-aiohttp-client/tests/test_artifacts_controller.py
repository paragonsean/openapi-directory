# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.arm_template_info import ArmTemplateInfo
from openapi_server.models.artifact import Artifact
from openapi_server.models.cloud_error import CloudError
from openapi_server.models.generate_arm_template_request import GenerateArmTemplateRequest
from openapi_server.models.response_with_continuation_artifact import ResponseWithContinuationArtifact


pytestmark = pytest.mark.asyncio

async def test_artifacts_generate_arm_template(client):
    """Test case for artifacts_generate_arm_template

    
    """
    generate_arm_template_request = {"fileUploadOptions":"UploadFilesAndGenerateSasTokens","virtualMachineName":"virtualMachineName","location":"location","parameters":[{"name":"name","value":"value"},{"name":"name","value":"value"}]}
    params = [('api-version', '2016-05-15')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DevTestLab/labs/{lab_name}/artifactsources/{artifact_source_name}/artifacts/{name}/generateArmTemplate'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', lab_name='lab_name_example', artifact_source_name='artifact_source_name_example', name='name_example'),
        headers=headers,
        json=generate_arm_template_request,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_artifacts_get(client):
    """Test case for artifacts_get

    
    """
    params = [('$expand', 'expand_example'),
                    ('api-version', '2016-05-15')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DevTestLab/labs/{lab_name}/artifactsources/{artifact_source_name}/artifacts/{name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', lab_name='lab_name_example', artifact_source_name='artifact_source_name_example', name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_artifacts_list(client):
    """Test case for artifacts_list

    
    """
    params = [('$expand', 'expand_example'),
                    ('$filter', 'filter_example'),
                    ('$top', 56),
                    ('$orderby', 'orderby_example'),
                    ('api-version', '2016-05-15')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DevTestLab/labs/{lab_name}/artifactsources/{artifact_source_name}/artifacts'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', lab_name='lab_name_example', artifact_source_name='artifact_source_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

