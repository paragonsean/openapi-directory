# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.items_notification_rule_subscriber import ItemsNotificationRuleSubscriber
from openapi_server.models.notification_rule_subscriber import NotificationRuleSubscriber


pytestmark = pytest.mark.asyncio

async def test_notification_rule_subscriber_delete(client):
    """Test case for notification_rule_subscriber_delete

    Delete a notification rule subscriber.
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/piwebapi/notificationrulesubscribers/{web_id}'.format(web_id='web_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_notification_rule_subscriber_get(client):
    """Test case for notification_rule_subscriber_get

    Retrieve a notification rule subscriber.
    """
    params = [('selectedFields', 'selected_fields_example'),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/notificationrulesubscribers/{web_id}'.format(web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_notification_rule_subscriber_get_by_path(client):
    """Test case for notification_rule_subscriber_get_by_path

    Retrieve a notification rule subscriber by path.
    """
    params = [('path', 'path_example'),
                    ('selectedFields', 'selected_fields_example'),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/notificationrulesubscribers',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_notification_rule_subscriber_get_notification_rule_subscribers(client):
    """Test case for notification_rule_subscriber_get_notification_rule_subscribers

    Retrieve notification rule subscriber subscribers.
    """
    params = [('selectedFields', 'selected_fields_example'),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/notificationrulesubscribers/{web_id}/notificationrulesubscribers'.format(web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_notification_rule_subscriber_update(client):
    """Test case for notification_rule_subscriber_update

    Update a notification rule subscriber.
    """
    notification_rule_subscriber = {"Path":"\\\\MyAssetServer\\MyDatabase\\NotificationRules[NotificationSubscriptionRuleName]","ConfigString":"ToEmail=mike@testemail.com","NotifyOption":"EventStart","ContactType":"Individual","Description":"Manufacturing Machine MachineName subscription","WebException":{"Errors":["An error has occurred."],"StatusCode":500},"MaximumRetries":3,"Name":"NotificationSubscriptionRuleName","EscalationTimeout":"PT3S","ContactTemplateName":"Plant Manager","WebId":"I1NSLDqD5loBNH0erqeqJodtALA5bYfWno26BGgMQAVXYR0AgPUJJXNlEW1w78rnCXDmcDA","Id":"e9a984d0-f47c-11e7-8454-00155d029708","RetryInterval":"PT3S","PlugInName":"Email","DeliveryFormatName":"DeliveryFormat"}
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/piwebapi/notificationrulesubscribers/{web_id}'.format(web_id='web_id_example'),
        headers=headers,
        json=notification_rule_subscriber,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

