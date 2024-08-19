# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_error import ApiError
from openapi_server.models.image_template import ImageTemplate
from openapi_server.models.image_template_list_result import ImageTemplateListResult
from openapi_server.models.image_template_update_parameters import ImageTemplateUpdateParameters
from openapi_server.models.run_output import RunOutput
from openapi_server.models.run_output_collection import RunOutputCollection


pytestmark = pytest.mark.asyncio

async def test_virtual_machine_image_templates_create_or_update(client):
    """Test case for virtual_machine_image_templates_create_or_update

    
    """
    parameters = {"properties":{"provisioningError":{"provisioningErrorCode":"BadSourceType","message":"message"},"lastRunStatus":{"runSubState":"Queued","startTime":"2000-01-23T04:56:07.000+00:00","endTime":"2000-01-23T04:56:07.000+00:00","message":"message","runState":"Running"},"distribute":[{"artifactTags":{"key":"artifactTags"},"runOutputName":"runOutputName","type":"type"},{"artifactTags":{"key":"artifactTags"},"runOutputName":"runOutputName","type":"type"}],"provisioningState":"Creating","source":{"type":"type"},"customize":[{"name":"name","type":"type"},{"name":"name","type":"type"}]}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.VirtualMachineImages/imageTemplates/{image_template_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', image_template_name='image_template_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtual_machine_image_templates_delete(client):
    """Test case for virtual_machine_image_templates_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.VirtualMachineImages/imageTemplates/{image_template_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', image_template_name='image_template_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtual_machine_image_templates_get(client):
    """Test case for virtual_machine_image_templates_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.VirtualMachineImages/imageTemplates/{image_template_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', image_template_name='image_template_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtual_machine_image_templates_get_run_output(client):
    """Test case for virtual_machine_image_templates_get_run_output

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.VirtualMachineImages/imageTemplates/{image_template_name}/runOutputs/{run_output_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', image_template_name='image_template_name_example', run_output_name='run_output_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtual_machine_image_templates_list(client):
    """Test case for virtual_machine_image_templates_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.VirtualMachineImages/imageTemplates'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtual_machine_image_templates_list_by_resource_group(client):
    """Test case for virtual_machine_image_templates_list_by_resource_group

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.VirtualMachineImages/imageTemplates'.format(resource_group_name='resource_group_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtual_machine_image_templates_list_run_outputs(client):
    """Test case for virtual_machine_image_templates_list_run_outputs

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.VirtualMachineImages/imageTemplates/{image_template_name}/runOutputs'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', image_template_name='image_template_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtual_machine_image_templates_run(client):
    """Test case for virtual_machine_image_templates_run

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.VirtualMachineImages/imageTemplates/{image_template_name}/run'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', image_template_name='image_template_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtual_machine_image_templates_update(client):
    """Test case for virtual_machine_image_templates_update

    
    """
    parameters = {"tags":{"key":"tags"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.VirtualMachineImages/imageTemplates/{image_template_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', image_template_name='image_template_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

