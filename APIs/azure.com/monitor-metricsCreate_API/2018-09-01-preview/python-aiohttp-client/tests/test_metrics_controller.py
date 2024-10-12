# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.azure_metrics_document import AzureMetricsDocument
from openapi_server.models.azure_metrics_result import AzureMetricsResult


pytestmark = pytest.mark.asyncio

async def test_metrics_create(client):
    """Test case for metrics_create

    
    """
    body = {"data":{"baseData":{"metric":"metric","series":[{"dimValues":["dimValues","dimValues"],"min":1.4658129805029452,"max":6.027456183070403,"count":0,"sum":5.962133916683182},{"dimValues":["dimValues","dimValues"],"min":1.4658129805029452,"max":6.027456183070403,"count":0,"sum":5.962133916683182}],"namespace":"namespace","dimNames":["dimNames","dimNames"]}},"time":"time"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'content_type': 'content_type_example',
        'content_length': 56,
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/{resource_provider}/{resource_type_name}/{resource_name}/metrics'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', resource_provider='resource_provider_example', resource_type_name='resource_type_name_example', resource_name='resource_name_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

