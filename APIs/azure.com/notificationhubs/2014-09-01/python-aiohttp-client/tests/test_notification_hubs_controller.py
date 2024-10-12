# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.check_availability_parameters import CheckAvailabilityParameters
from openapi_server.models.check_availability_resource import CheckAvailabilityResource
from openapi_server.models.notification_hub_create_or_update_parameters import NotificationHubCreateOrUpdateParameters
from openapi_server.models.notification_hub_list_result import NotificationHubListResult
from openapi_server.models.notification_hub_resource import NotificationHubResource
from openapi_server.models.resource_list_keys import ResourceListKeys
from openapi_server.models.shared_access_authorization_rule_create_or_update_parameters import SharedAccessAuthorizationRuleCreateOrUpdateParameters
from openapi_server.models.shared_access_authorization_rule_list_result import SharedAccessAuthorizationRuleListResult
from openapi_server.models.shared_access_authorization_rule_resource import SharedAccessAuthorizationRuleResource


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_notification_hubs_check_availability(client):
    """Test case for notification_hubs_check_availability

    
    """
    parameters = {"isAvailiable":True,"name":"name","location":"location","tags":{"key":"tags"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.NotificationHubs/namespaces/{namespace_name}/checkNotificationHubAvailability'.format(resource_group_name='resource_group_name_example', namespace_name='namespace_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_notification_hubs_create_or_update(client):
    """Test case for notification_hubs_create_or_update

    
    """
    parameters = {"location":"location","properties":{"baiduCredential":{"properties":{"baiduApiKey":"baiduApiKey","baiduSecretKey":"baiduSecretKey","baiduEndPoint":"baiduEndPoint"}},"mpnsCredential":{"properties":{"mpnsCertificate":"mpnsCertificate","thumbprint":"thumbprint","certificateKey":"certificateKey"}},"apnsCredential":{"properties":{"endpoint":"endpoint","thumbprint":"thumbprint","certificateKey":"certificateKey","apnsCertificate":"apnsCertificate"}},"authorizationRules":[{"claimType":"claimType","modifiedTime":"2000-01-23T04:56:07.000+00:00","secondaryKey":"secondaryKey","rights":["Manage","Manage"],"keyName":"keyName","createdTime":"2000-01-23T04:56:07.000+00:00","claimValue":"claimValue","primaryKey":"primaryKey","revision":0},{"claimType":"claimType","modifiedTime":"2000-01-23T04:56:07.000+00:00","secondaryKey":"secondaryKey","rights":["Manage","Manage"],"keyName":"keyName","createdTime":"2000-01-23T04:56:07.000+00:00","claimValue":"claimValue","primaryKey":"primaryKey","revision":0}],"gcmCredential":{"properties":{"googleApiKey":"googleApiKey","gcmEndpoint":"gcmEndpoint"}},"name":"name","registrationTtl":"registrationTtl","wnsCredential":{"properties":{"secretKey":"secretKey","packageSid":"packageSid","windowsLiveEndpoint":"windowsLiveEndpoint"}},"admCredential":{"properties":{"clientId":"clientId","authTokenUrl":"authTokenUrl","clientSecret":"clientSecret"}}},"tags":{"key":"tags"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.NotificationHubs/namespaces/{namespace_name}/notificationHubs/{notification_hub_name}'.format(resource_group_name='resource_group_name_example', namespace_name='namespace_name_example', notification_hub_name='notification_hub_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_notification_hubs_create_or_update_authorization_rule(client):
    """Test case for notification_hubs_create_or_update_authorization_rule

    
    """
    parameters = {"name":"name","location":"location","properties":{"claimType":"claimType","modifiedTime":"2000-01-23T04:56:07.000+00:00","secondaryKey":"secondaryKey","rights":["Manage","Manage"],"keyName":"keyName","createdTime":"2000-01-23T04:56:07.000+00:00","claimValue":"claimValue","primaryKey":"primaryKey","revision":0}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.NotificationHubs/namespaces/{namespace_name}/notificationHubs/{notification_hub_name}/AuthorizationRules/{authorization_rule_name}'.format(resource_group_name='resource_group_name_example', namespace_name='namespace_name_example', notification_hub_name='notification_hub_name_example', authorization_rule_name='authorization_rule_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_notification_hubs_delete(client):
    """Test case for notification_hubs_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.NotificationHubs/namespaces/{namespace_name}/notificationHubs/{notification_hub_name}'.format(resource_group_name='resource_group_name_example', namespace_name='namespace_name_example', notification_hub_name='notification_hub_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_notification_hubs_delete_authorization_rule(client):
    """Test case for notification_hubs_delete_authorization_rule

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.NotificationHubs/namespaces/{namespace_name}/notificationHubs/{notification_hub_name}/AuthorizationRules/{authorization_rule_name}'.format(resource_group_name='resource_group_name_example', namespace_name='namespace_name_example', notification_hub_name='notification_hub_name_example', authorization_rule_name='authorization_rule_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_notification_hubs_get(client):
    """Test case for notification_hubs_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.NotificationHubs/namespaces/{namespace_name}/notificationHubs/{notification_hub_name}'.format(resource_group_name='resource_group_name_example', namespace_name='namespace_name_example', notification_hub_name='notification_hub_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_notification_hubs_get_authorization_rule(client):
    """Test case for notification_hubs_get_authorization_rule

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.NotificationHubs/namespaces/{namespace_name}/notificationHubs/{notification_hub_name}/AuthorizationRules/{authorization_rule_name}'.format(resource_group_name='resource_group_name_example', namespace_name='namespace_name_example', notification_hub_name='notification_hub_name_example', authorization_rule_name='authorization_rule_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_notification_hubs_get_pns_credentials(client):
    """Test case for notification_hubs_get_pns_credentials

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.NotificationHubs/namespaces/{namespace_name}/notificationHubs/{notification_hub_name}/pnsCredentials'.format(resource_group_name='resource_group_name_example', namespace_name='namespace_name_example', notification_hub_name='notification_hub_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_notification_hubs_list(client):
    """Test case for notification_hubs_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.NotificationHubs/namespaces/{namespace_name}/notificationHubs'.format(resource_group_name='resource_group_name_example', namespace_name='namespace_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_notification_hubs_list_authorization_rules(client):
    """Test case for notification_hubs_list_authorization_rules

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.NotificationHubs/namespaces/{namespace_name}/notificationHubs/{notification_hub_name}/AuthorizationRules'.format(resource_group_name='resource_group_name_example', namespace_name='namespace_name_example', notification_hub_name='notification_hub_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_notification_hubs_list_keys(client):
    """Test case for notification_hubs_list_keys

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.NotificationHubs/namespaces/{namespace_name}/notificationHubs/{notification_hub_name}/AuthorizationRules/{authorization_rule_name}/listKeys'.format(resource_group_name='resource_group_name_example', namespace_name='namespace_name_example', notification_hub_name='notification_hub_name_example', authorization_rule_name='authorization_rule_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

