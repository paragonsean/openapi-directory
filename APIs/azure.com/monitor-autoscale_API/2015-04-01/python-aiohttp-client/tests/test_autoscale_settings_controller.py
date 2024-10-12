# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.autoscale_setting_resource import AutoscaleSettingResource
from openapi_server.models.autoscale_setting_resource_collection import AutoscaleSettingResourceCollection
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_autoscale_settings_create_or_update(client):
    """Test case for autoscale_settings_create_or_update

    
    """
    parameters = {"properties":{"targetResourceUri":"targetResourceUri","name":"name","profiles":[{"recurrence":{"schedule":{"hours":[0,0],"minutes":[6,6],"days":["days","days"],"timeZone":"timeZone"},"frequency":"None"},"fixedDate":{"start":"2000-01-23T04:56:07.000+00:00","timeZone":"timeZone","end":"2000-01-23T04:56:07.000+00:00"},"name":"name","rules":[{"scaleAction":{"cooldown":"cooldown","type":"ChangeCount","value":"1","direction":"None"},"metricTrigger":{"metricResourceUri":"metricResourceUri","statistic":"Average","timeGrain":"timeGrain","timeWindow":"timeWindow","metricName":"metricName","timeAggregation":"Average","threshold":1.4658129805029452,"operator":"Equals"}},{"scaleAction":{"cooldown":"cooldown","type":"ChangeCount","value":"1","direction":"None"},"metricTrigger":{"metricResourceUri":"metricResourceUri","statistic":"Average","timeGrain":"timeGrain","timeWindow":"timeWindow","metricName":"metricName","timeAggregation":"Average","threshold":1.4658129805029452,"operator":"Equals"}}],"capacity":{"default":"default","maximum":"maximum","minimum":"minimum"}},{"recurrence":{"schedule":{"hours":[0,0],"minutes":[6,6],"days":["days","days"],"timeZone":"timeZone"},"frequency":"None"},"fixedDate":{"start":"2000-01-23T04:56:07.000+00:00","timeZone":"timeZone","end":"2000-01-23T04:56:07.000+00:00"},"name":"name","rules":[{"scaleAction":{"cooldown":"cooldown","type":"ChangeCount","value":"1","direction":"None"},"metricTrigger":{"metricResourceUri":"metricResourceUri","statistic":"Average","timeGrain":"timeGrain","timeWindow":"timeWindow","metricName":"metricName","timeAggregation":"Average","threshold":1.4658129805029452,"operator":"Equals"}},{"scaleAction":{"cooldown":"cooldown","type":"ChangeCount","value":"1","direction":"None"},"metricTrigger":{"metricResourceUri":"metricResourceUri","statistic":"Average","timeGrain":"timeGrain","timeWindow":"timeWindow","metricName":"metricName","timeAggregation":"Average","threshold":1.4658129805029452,"operator":"Equals"}}],"capacity":{"default":"default","maximum":"maximum","minimum":"minimum"}},{"recurrence":{"schedule":{"hours":[0,0],"minutes":[6,6],"days":["days","days"],"timeZone":"timeZone"},"frequency":"None"},"fixedDate":{"start":"2000-01-23T04:56:07.000+00:00","timeZone":"timeZone","end":"2000-01-23T04:56:07.000+00:00"},"name":"name","rules":[{"scaleAction":{"cooldown":"cooldown","type":"ChangeCount","value":"1","direction":"None"},"metricTrigger":{"metricResourceUri":"metricResourceUri","statistic":"Average","timeGrain":"timeGrain","timeWindow":"timeWindow","metricName":"metricName","timeAggregation":"Average","threshold":1.4658129805029452,"operator":"Equals"}},{"scaleAction":{"cooldown":"cooldown","type":"ChangeCount","value":"1","direction":"None"},"metricTrigger":{"metricResourceUri":"metricResourceUri","statistic":"Average","timeGrain":"timeGrain","timeWindow":"timeWindow","metricName":"metricName","timeAggregation":"Average","threshold":1.4658129805029452,"operator":"Equals"}}],"capacity":{"default":"default","maximum":"maximum","minimum":"minimum"}},{"recurrence":{"schedule":{"hours":[0,0],"minutes":[6,6],"days":["days","days"],"timeZone":"timeZone"},"frequency":"None"},"fixedDate":{"start":"2000-01-23T04:56:07.000+00:00","timeZone":"timeZone","end":"2000-01-23T04:56:07.000+00:00"},"name":"name","rules":[{"scaleAction":{"cooldown":"cooldown","type":"ChangeCount","value":"1","direction":"None"},"metricTrigger":{"metricResourceUri":"metricResourceUri","statistic":"Average","timeGrain":"timeGrain","timeWindow":"timeWindow","metricName":"metricName","timeAggregation":"Average","threshold":1.4658129805029452,"operator":"Equals"}},{"scaleAction":{"cooldown":"cooldown","type":"ChangeCount","value":"1","direction":"None"},"metricTrigger":{"metricResourceUri":"metricResourceUri","statistic":"Average","timeGrain":"timeGrain","timeWindow":"timeWindow","metricName":"metricName","timeAggregation":"Average","threshold":1.4658129805029452,"operator":"Equals"}}],"capacity":{"default":"default","maximum":"maximum","minimum":"minimum"}},{"recurrence":{"schedule":{"hours":[0,0],"minutes":[6,6],"days":["days","days"],"timeZone":"timeZone"},"frequency":"None"},"fixedDate":{"start":"2000-01-23T04:56:07.000+00:00","timeZone":"timeZone","end":"2000-01-23T04:56:07.000+00:00"},"name":"name","rules":[{"scaleAction":{"cooldown":"cooldown","type":"ChangeCount","value":"1","direction":"None"},"metricTrigger":{"metricResourceUri":"metricResourceUri","statistic":"Average","timeGrain":"timeGrain","timeWindow":"timeWindow","metricName":"metricName","timeAggregation":"Average","threshold":1.4658129805029452,"operator":"Equals"}},{"scaleAction":{"cooldown":"cooldown","type":"ChangeCount","value":"1","direction":"None"},"metricTrigger":{"metricResourceUri":"metricResourceUri","statistic":"Average","timeGrain":"timeGrain","timeWindow":"timeWindow","metricName":"metricName","timeAggregation":"Average","threshold":1.4658129805029452,"operator":"Equals"}}],"capacity":{"default":"default","maximum":"maximum","minimum":"minimum"}}],"enabled":True,"notifications":[{"webhooks":[{"serviceUri":"serviceUri","properties":{"key":"properties"}},{"serviceUri":"serviceUri","properties":{"key":"properties"}}],"operation":"Scale","email":{"sendToSubscriptionAdministrator":True,"customEmails":["customEmails","customEmails"],"sendToSubscriptionCoAdministrators":True}},{"webhooks":[{"serviceUri":"serviceUri","properties":{"key":"properties"}},{"serviceUri":"serviceUri","properties":{"key":"properties"}}],"operation":"Scale","email":{"sendToSubscriptionAdministrator":True,"customEmails":["customEmails","customEmails"],"sendToSubscriptionCoAdministrators":True}}]}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/microsoft.insights/autoscalesettings/{autoscale_setting_name}'.format(resource_group_name='resource_group_name_example', autoscale_setting_name='autoscale_setting_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_autoscale_settings_delete(client):
    """Test case for autoscale_settings_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/microsoft.insights/autoscalesettings/{autoscale_setting_name}'.format(resource_group_name='resource_group_name_example', autoscale_setting_name='autoscale_setting_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_autoscale_settings_get(client):
    """Test case for autoscale_settings_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/microsoft.insights/autoscalesettings/{autoscale_setting_name}'.format(resource_group_name='resource_group_name_example', autoscale_setting_name='autoscale_setting_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_autoscale_settings_list_by_resource_group(client):
    """Test case for autoscale_settings_list_by_resource_group

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/microsoft.insights/autoscalesettings'.format(resource_group_name='resource_group_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_autoscale_settings_list_by_subscription(client):
    """Test case for autoscale_settings_list_by_subscription

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/microsoft.insights/autoscalesettings'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

