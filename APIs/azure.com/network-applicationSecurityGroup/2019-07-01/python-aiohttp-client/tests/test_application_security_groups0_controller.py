# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.application_security_group import ApplicationSecurityGroup
from openapi_server.models.application_security_groups_update_tags_request import ApplicationSecurityGroupsUpdateTagsRequest


pytestmark = pytest.mark.asyncio

async def test_application_security_groups_update_tags(client):
    """Test case for application_security_groups_update_tags

    
    """
    parameters = openapi_server.ApplicationSecurityGroupsUpdateTagsRequest()
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/applicationSecurityGroups/{application_security_group_name}'.format(resource_group_name='resource_group_name_example', application_security_group_name='application_security_group_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

