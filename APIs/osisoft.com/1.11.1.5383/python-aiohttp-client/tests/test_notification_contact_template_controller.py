# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.errors import Errors
from openapi_server.models.items_notification_contact_template import ItemsNotificationContactTemplate
from openapi_server.models.items_security_entry import ItemsSecurityEntry
from openapi_server.models.items_security_rights import ItemsSecurityRights
from openapi_server.models.notification_contact_template import NotificationContactTemplate
from openapi_server.models.security_entry import SecurityEntry


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_notification_contact_template_create_security_entry(client):
    """Test case for notification_contact_template_create_security_entry

    Create a security entry owned by the notification contact template.
    """
    security_entry = {"WebException":{"Errors":["An error has occurred."],"StatusCode":500},"AllowRights":["Read","ReadData"],"DenyRights":["Write","Execute","Admin"],"Links":{"SecurableObject":"SecurableObject","SecurityIdentity":"SecurityIdentity","Self":"Self"},"SecurityIdentityName":"domain\\user1","Name":"domain\\user1"}
    params = [('applyToChildren', True),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/piwebapi/notificationcontacttemplates/{web_id}/securityentries'.format(web_id='web_id_example'),
        headers=headers,
        json=security_entry,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_notification_contact_template_delete(client):
    """Test case for notification_contact_template_delete

    Delete a notification contact template.
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/piwebapi/notificationcontacttemplates/{web_id}'.format(web_id='web_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_notification_contact_template_delete_security_entry(client):
    """Test case for notification_contact_template_delete_security_entry

    Delete a security entry owned by the notification contact template.
    """
    params = [('applyToChildren', True)]
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/piwebapi/notificationcontacttemplates/{web_id}/securityentries/{name}'.format(name='name_example', web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_notification_contact_template_get(client):
    """Test case for notification_contact_template_get

    Retrieve a notification contact template.
    """
    params = [('selectedFields', 'selected_fields_example'),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/notificationcontacttemplates/{web_id}'.format(web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_notification_contact_template_get_by_path(client):
    """Test case for notification_contact_template_get_by_path

    Retrieve a notification contact template by path.
    """
    params = [('path', 'path_example'),
                    ('selectedFields', 'selected_fields_example'),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/notificationcontacttemplates',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_notification_contact_template_get_notification_contact_templates(client):
    """Test case for notification_contact_template_get_notification_contact_templates

    Retrieve notification contact template's child templates.
    """
    params = [('selectedFields', 'selected_fields_example'),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/notificationcontacttemplates/{web_id}/notificationcontacttemplates'.format(web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_notification_contact_template_get_notification_contact_templates_query(client):
    """Test case for notification_contact_template_get_notification_contact_templates_query

    Retrieve notification contact templates based on the specified conditions. Returns notification contact templates using the specified search query string.
    """
    params = [('assetServerWebId', 'asset_server_web_id_example'),
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
        path='/piwebapi/notificationcontacttemplates/search',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_notification_contact_template_get_security(client):
    """Test case for notification_contact_template_get_security

    Get the security information of the specified security item associated with the notification contact template for a specified user.
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
        path='/piwebapi/notificationcontacttemplates/{web_id}/security'.format(web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_notification_contact_template_get_security_entries(client):
    """Test case for notification_contact_template_get_security_entries

    Retrieve the security entries associated with the notification contact template based on the specified criteria. By default, all security entries for this notification contact template are returned.
    """
    params = [('nameFilter', 'name_filter_example'),
                    ('selectedFields', 'selected_fields_example'),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/notificationcontacttemplates/{web_id}/securityentries'.format(web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_notification_contact_template_get_security_entry_by_name(client):
    """Test case for notification_contact_template_get_security_entry_by_name

    Retrieve the security entry associated with the notification contact template with the specified name.
    """
    params = [('selectedFields', 'selected_fields_example'),
                    ('webIdType', 'web_id_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/notificationcontacttemplates/{web_id}/securityentries/{name}'.format(name='name_example', web_id='web_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_notification_contact_template_update(client):
    """Test case for notification_contact_template_update

    Update a notification contact template by replacing items in its definition.
    """
    notification_contact_template = {"Path":"\\\\MyAssetServer\\NotificationContactTemplates[Plant Manager]","ConfigString":"","NotifyWhenInstanceEnded":True,"ContactType":"Individual","Description":"","WebException":{"Errors":["An error has occurred."],"StatusCode":500},"MaximumRetries":5,"Name":"Plant Manager","HasChildren":False,"EscalationTimeout":"PT3S","WebId":"I1NCEDqD5loBNH0erqeqJodtALAYIKyyz2F5BGAxQAVXYRDBAGyPedZG1sUmxOOclp3Flwg","MinimumAcknowledgements":2,"Links":{"SecurityEntries":"SecurityEntries","NotificationPlugIn":"NotificationPlugIn","NotificationContactTemplates":"NotificationContactTemplates","Self":"Self","Security":"Security","AssetServer":"AssetServer"},"Available":True,"Id":"cbb28260-853d-11e4-80c5-00155d844304","RetryInterval":"PT5S","PlugInName":""}
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/piwebapi/notificationcontacttemplates/{web_id}'.format(web_id='web_id_example'),
        headers=headers,
        json=notification_contact_template,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_notification_contact_template_update_security_entry(client):
    """Test case for notification_contact_template_update_security_entry

    Update a security entry owned by the notification contact template.
    """
    security_entry = {"WebException":{"Errors":["An error has occurred."],"StatusCode":500},"AllowRights":["Read","ReadData"],"DenyRights":["Write","Execute","Admin"],"Links":{"SecurableObject":"SecurableObject","SecurityIdentity":"SecurityIdentity","Self":"Self"},"SecurityIdentityName":"domain\\user1","Name":"domain\\user1"}
    params = [('applyToChildren', True)]
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/piwebapi/notificationcontacttemplates/{web_id}/securityentries/{name}'.format(name='name_example', web_id='web_id_example'),
        headers=headers,
        json=security_entry,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

