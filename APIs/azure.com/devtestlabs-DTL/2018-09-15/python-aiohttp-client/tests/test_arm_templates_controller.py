# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.arm_template import ArmTemplate
from openapi_server.models.arm_template_list import ArmTemplateList
from openapi_server.models.cloud_error import CloudError


pytestmark = pytest.mark.asyncio

async def test_arm_templates_get(client):
    """Test case for arm_templates_get

    
    """
    params = [('$expand', 'expand_example'),
                    ('api-version', '2018-09-15')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DevTestLab/labs/{lab_name}/artifactsources/{artifact_source_name}/armtemplates/{name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', lab_name='lab_name_example', artifact_source_name='artifact_source_name_example', name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_arm_templates_list(client):
    """Test case for arm_templates_list

    
    """
    params = [('$expand', 'expand_example'),
                    ('$filter', 'filter_example'),
                    ('$top', 56),
                    ('$orderby', 'orderby_example'),
                    ('api-version', '2018-09-15')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DevTestLab/labs/{lab_name}/artifactsources/{artifact_source_name}/armtemplates'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', lab_name='lab_name_example', artifact_source_name='artifact_source_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

