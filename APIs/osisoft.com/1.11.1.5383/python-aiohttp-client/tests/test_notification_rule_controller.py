# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.errors import Errors
from openapi_server.models.items_notification_rule import ItemsNotificationRule
from openapi_server.models.items_notification_rule_subscriber import ItemsNotificationRuleSubscriber
from openapi_server.models.items_security_entry import ItemsSecurityEntry
from openapi_server.models.items_security_rights import ItemsSecurityRights
from openapi_server.models.notification_rule import NotificationRule
from openapi_server.models.notification_rule_subscriber import NotificationRuleSubscriber
from openapi_server.models.security_entry import SecurityEntry


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_notification_rule_create_notification_rule_subscriber(client):
    """Test case for notification_rule_create_notification_rule_subscriber

    Create a notification rule subscriber.
    """
    notification_rule_subscriber = {"Path":"\\\\MyAssetServer\\MyDatabase\\NotificationRules[NotificationSubscriptionRuleName]","ConfigString":"ToEmail=mike@testemail.com","NotifyOption":"EventStart","ContactType":"Individual","Description":"Manufacturing Machine MachineName subscription","WebException":{"Errors":["An error has occurred."],"StatusCode":500},"MaximumRetries":3,"Name":"NotificationSubscriptionRuleName","EscalationTimeout":"PT3S","ContactTemplateName":"Plant Manager","WebId":"I1NSLDqD5loBNH0erqeqJodtALA5bYfWno26BGgMQAVXYR0AgPUJJXNlEW1w78rnCXDmcDA","Id":"e9a984d0-f47c-11e7-8454-00155d029708","RetryInterval":"PT3S","PlugInName":"Email","DeliveryFormatName":"DeliveryFormat"}
    params = [('webIdType', 'web_id_type_example')]
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/piwebapi/notificationrules/{web_id}/notificationrulesubscribers'.format(web_id='web_id_example'),
        headers=headers,
        json=notification_rule_subscriber,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_notification_rule_create_security_entry(client):
    """Test case for notification_rule_create_security_entry

    Create a security entry owned by the notification rule.
    """
    security_entry = {"WebException":{"Errors":["An error has occurred."],"StatusCode":500},"AllowRights":["Read","ReadData"],"DenyRights":["Write","Execute","Admin"],"Links":{"SecurableObject":"SecurableObject","SecurityIdentity":"SecurityIdentity","Self":"Self"},"SecurityIdentityName":"domain\\user1","Name":"domain\\user1"}
    params = [('applyToChildren', True),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/piwebapi/notificationrules/{web_id}/securityentries'.format(web_id='web_id_example'),
        headers=headers,
        json=security_entry,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_notification_rule_delete(client):
    """Test case for notification_rule_delete

    Delete a notification rule.
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/piwebapi/notificationrules/{web_id}'.format(web_id='web_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_notification_rule_delete_security_entry(client):
    """Test case for notification_rule_delete_security_entry

    Delete a security entry owned by the notification rule.
    """
    params = [('applyToChildren', True)]
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/piwebapi/notificationrules/{web_id}/securityentries/{name}'.format(name='name_example', web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_notification_rule_get(client):
    """Test case for notification_rule_get

    Retrieve a notification rule.
    """
    params = [('selectedFields', 'selected_fields_example'),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/notificationrules/{web_id}'.format(web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_notification_rule_get_by_path(client):
    """Test case for notification_rule_get_by_path

    Retrieve a notification rule by path.
    """
    params = [('path', 'path_example'),
                    ('selectedFields', 'selected_fields_example'),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/notificationrules',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_notification_rule_get_notification_rule_subscribers(client):
    """Test case for notification_rule_get_notification_rule_subscribers

    Retrieve notification rule subscribers.
    """
    params = [('selectedFields', 'selected_fields_example'),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/notificationrules/{web_id}/notificationrulesubscribers'.format(web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_notification_rule_get_notification_rules_query(client):
    """Test case for notification_rule_get_notification_rules_query

    Retrieve notification rules based on the specified conditions. Returns notification rules using the specified search query string.
    """
    params = [('databaseWebId', 'database_web_id_example'),
                    ('maxCount', 56),
                    ('query', 'query_example'),
                    ('selectedFields', 'selected_fields_example'),
                    ('startIndex', 56),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/notificationrules/search',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_notification_rule_get_security(client):
    """Test case for notification_rule_get_security

    Get the security information of the specified security item associated with the notification rule for a specified user.
    """
    params = [('userIdentity', ['user_identity_example']),
                    ('forceRefresh', True),
                    ('selectedFields', 'selected_fields_example'),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/notificationrules/{web_id}/security'.format(web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_notification_rule_get_security_entries(client):
    """Test case for notification_rule_get_security_entries

    Retrieve the security entries associated with the notification rule based on the specified criteria. By default, all security entries for this notification rule are returned.
    """
    params = [('nameFilter', 'name_filter_example'),
                    ('selectedFields', 'selected_fields_example'),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/notificationrules/{web_id}/securityentries'.format(web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_notification_rule_get_security_entry_by_name(client):
    """Test case for notification_rule_get_security_entry_by_name

    Retrieve the security entry associated with the notification rule with the specified name.
    """
    params = [('selectedFields', 'selected_fields_example'),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/notificationrules/{web_id}/securityentries/{name}'.format(name='name_example', web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_notification_rule_update(client):
    """Test case for notification_rule_update

    Update a notification rule by replacing items in its definition.
    """
    notification_rule = {"Path":"\\\\MyAssetServer\\MyDatabase\\CityName\\EngineeringProcess\\Equipment\\MachineName\\NotificationRules[RuleName]","Status":"Disabled","MultiTriggerEventOption":"HighestSeverity","Description":"Manufacturing Equipment MachineName","WebException":{"Errors":["An error has occurred."],"StatusCode":500},"ResendInterval":"PT5S","Criteria":"Name: EventFrameCriteriaName","Name":"MachineName","CategoryNames":["Equipment Assets"],"AutoCreated":True,"WebId":"I1NRDqD5loBNH0erqeqJodtALA5bYfWno26BGgMQAVXYR0Ag","TemplateName":"MachineName Notification Rule","Id":"e9a984d0-f47c-11e7-8454-00155d029708","NonrepetitionInterval":"PT3S"}
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/piwebapi/notificationrules/{web_id}'.format(web_id='web_id_example'),
        headers=headers,
        json=notification_rule,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_notification_rule_update_security_entry(client):
    """Test case for notification_rule_update_security_entry

    Update a security entry owned by the notification rule.
    """
    security_entry = {"WebException":{"Errors":["An error has occurred."],"StatusCode":500},"AllowRights":["Read","ReadData"],"DenyRights":["Write","Execute","Admin"],"Links":{"SecurableObject":"SecurableObject","SecurityIdentity":"SecurityIdentity","Self":"Self"},"SecurityIdentityName":"domain\\user1","Name":"domain\\user1"}
    params = [('applyToChildren', True)]
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/piwebapi/notificationrules/{web_id}/securityentries/{name}'.format(name='name_example', web_id='web_id_example'),
        headers=headers,
        json=security_entry,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

