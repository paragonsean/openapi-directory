# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.errors import Errors
from openapi_server.models.items_notification_rule_subscriber import ItemsNotificationRuleSubscriber
from openapi_server.models.items_notification_rule_template import ItemsNotificationRuleTemplate
from openapi_server.models.items_security_entry import ItemsSecurityEntry
from openapi_server.models.items_security_rights import ItemsSecurityRights
from openapi_server.models.notification_rule_subscriber import NotificationRuleSubscriber
from openapi_server.models.notification_rule_template import NotificationRuleTemplate
from openapi_server.models.security_entry import SecurityEntry


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_notification_rule_template_create_notification_rule_template_subscriber(client):
    """Test case for notification_rule_template_create_notification_rule_template_subscriber

    Create a notification rule subscriber.
    """
    notification_rule_subscriber = {"Path":"\\\\MyAssetServer\\MyDatabase\\NotificationRules[NotificationSubscriptionRuleName]","ConfigString":"ToEmail=mike@testemail.com","NotifyOption":"EventStart","ContactType":"Individual","Description":"Manufacturing Machine MachineName subscription","WebException":{"Errors":["An error has occurred."],"StatusCode":500},"MaximumRetries":3,"Name":"NotificationSubscriptionRuleName","EscalationTimeout":"PT3S","ContactTemplateName":"Plant Manager","WebId":"I1NSLDqD5loBNH0erqeqJodtALA5bYfWno26BGgMQAVXYR0AgPUJJXNlEW1w78rnCXDmcDA","Id":"e9a984d0-f47c-11e7-8454-00155d029708","RetryInterval":"PT3S","PlugInName":"Email","DeliveryFormatName":"DeliveryFormat"}
    params = [('webIdType', 'web_id_type_example')]
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/piwebapi/notificationruletemplates/{web_id}/notificationrulesubscribers'.format(web_id='web_id_example'),
        headers=headers,
        json=notification_rule_subscriber,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_notification_rule_template_create_security_entry(client):
    """Test case for notification_rule_template_create_security_entry

    Create a security entry owned by the notification rule template.
    """
    security_entry = {"WebException":{"Errors":["An error has occurred."],"StatusCode":500},"AllowRights":["Read","ReadData"],"DenyRights":["Write","Execute","Admin"],"Links":{"SecurableObject":"SecurableObject","SecurityIdentity":"SecurityIdentity","Self":"Self"},"SecurityIdentityName":"domain\\user1","Name":"domain\\user1"}
    params = [('applyToChildren', True),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/piwebapi/notificationruletemplates/{web_id}/securityentries'.format(web_id='web_id_example'),
        headers=headers,
        json=security_entry,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_notification_rule_template_delete(client):
    """Test case for notification_rule_template_delete

    Delete a notification rule template.
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/piwebapi/notificationruletemplates/{web_id}'.format(web_id='web_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_notification_rule_template_delete_security_entry(client):
    """Test case for notification_rule_template_delete_security_entry

    Delete a security entry owned by the notification rule template.
    """
    params = [('applyToChildren', True)]
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/piwebapi/notificationruletemplates/{web_id}/securityentries/{name}'.format(name='name_example', web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_notification_rule_template_get(client):
    """Test case for notification_rule_template_get

    Get the specified notification rule template.
    """
    params = [('selectedFields', 'selected_fields_example'),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/notificationruletemplates/{web_id}'.format(web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_notification_rule_template_get_by_path(client):
    """Test case for notification_rule_template_get_by_path

    Retrieve a notification rule template by path.
    """
    params = [('path', 'path_example'),
                    ('selectedFields', 'selected_fields_example'),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/notificationruletemplates',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_notification_rule_template_get_notification_rule_template_subscribers(client):
    """Test case for notification_rule_template_get_notification_rule_template_subscribers

    Retrieve notification rule template subscribers.
    """
    params = [('selectedFields', 'selected_fields_example'),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/notificationruletemplates/{web_id}/notificationrulesubscribers'.format(web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_notification_rule_template_get_notification_rule_templates_query(client):
    """Test case for notification_rule_template_get_notification_rule_templates_query

    Retrieve Notification rule templates based on the specified conditions. Returns Notification rule templates using the specified search query string.
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
        path='/piwebapi/notificationruletemplates/search',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_notification_rule_template_get_security(client):
    """Test case for notification_rule_template_get_security

    Get the security information of the specified security item associated with the notification rule template for a specified user.
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
        path='/piwebapi/notificationruletemplates/{web_id}/security'.format(web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_notification_rule_template_get_security_entries(client):
    """Test case for notification_rule_template_get_security_entries

    Retrieve the security entries associated with the notification rule template based on the specified criteria. By default, all security entries for this notification rule template are returned.
    """
    params = [('nameFilter', 'name_filter_example'),
                    ('selectedFields', 'selected_fields_example'),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/notificationruletemplates/{web_id}/securityentries'.format(web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_notification_rule_template_get_security_entry_by_name(client):
    """Test case for notification_rule_template_get_security_entry_by_name

    Retrieve the security entry associated with the notification rule template with the specified name.
    """
    params = [('selectedFields', 'selected_fields_example'),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/notificationruletemplates/{web_id}/securityentries/{name}'.format(name='name_example', web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_notification_rule_template_update(client):
    """Test case for notification_rule_template_update

    Update a notification rule template by replacing items in its definition.
    """
    notification_rule_template = {"Path":"\\\\MyAssetServer\\MyDatabase\\CityName\\ElementTemplates[Template3]\\NotificationRuleTemplates[Notification Rule Template]","Status":"Functioning","MultiTriggerEventOption":"HighestSeverity","Description":"Description entered by the user","WebException":{"Errors":["An error has occurred."],"StatusCode":500},"ResendInterval":"PT5S","Criteria":"Name: EventFrameCriteriaName","Name":"MachineName","CategoryNames":["MachineNameAlerts"],"WebId":"I1NTDqD5loBNH0erqeqJodtALAtdcX5JH_5xGEKAAVXTSaAg","TemplateName":"MachineName Notification Rule Template","Id":"e9a984d0-f47c-11e7-8454-00155d029708","NonrepetitionInterval":"PT3S"}
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/piwebapi/notificationruletemplates/{web_id}'.format(web_id='web_id_example'),
        headers=headers,
        json=notification_rule_template,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_notification_rule_template_update_security_entry(client):
    """Test case for notification_rule_template_update_security_entry

    Update a security entry owned by the notification rule template.
    """
    security_entry = {"WebException":{"Errors":["An error has occurred."],"StatusCode":500},"AllowRights":["Read","ReadData"],"DenyRights":["Write","Execute","Admin"],"Links":{"SecurableObject":"SecurableObject","SecurityIdentity":"SecurityIdentity","Self":"Self"},"SecurityIdentityName":"domain\\user1","Name":"domain\\user1"}
    params = [('applyToChildren', True)]
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/piwebapi/notificationruletemplates/{web_id}/securityentries/{name}'.format(name='name_example', web_id='web_id_example'),
        headers=headers,
        json=security_entry,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

