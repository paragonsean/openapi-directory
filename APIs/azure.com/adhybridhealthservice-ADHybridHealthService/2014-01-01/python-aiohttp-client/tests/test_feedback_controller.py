# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.alert_feedback import AlertFeedback
from openapi_server.models.alert_feedbacks import AlertFeedbacks


pytestmark = pytest.mark.asyncio

async def test_services_add_alert_feedback(client):
    """Test case for services_add_alert_feedback

    
    """
    alert_feedback = {"feedback":"feedback","createdDate":"2000-01-23T04:56:07.000+00:00","level":"level","consentedToShare":True,"comment":"comment","state":"state","shortName":"shortName","serviceMemberId":"serviceMemberId"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/providers/Microsoft.ADHybridHealthService/services/{service_name}/feedbacktype/alerts/feedback'.format(service_name='service_name_example'),
        headers=headers,
        json=alert_feedback,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_services_list_alert_feedback(client):
    """Test case for services_list_alert_feedback

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.ADHybridHealthService/services/{service_name}/feedbacktype/alerts/{short_name}/alertfeedback'.format(service_name='service_name_example', short_name='short_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

