# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.managed_configuration import ManagedConfiguration
from openapi_server.models.managed_configurations_for_user_list_response import ManagedConfigurationsForUserListResponse


pytestmark = pytest.mark.asyncio

async def test_androidenterprise_managedconfigurationsforuser_delete(client):
    """Test case for androidenterprise_managedconfigurationsforuser_delete

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/androidenterprise/v1/enterprises/{enterprise_id}/users/{user_id}/managedConfigurationsForUser/{managed_configuration_for_user_id}'.format(enterprise_id='enterprise_id_example', user_id='user_id_example', managed_configuration_for_user_id='managed_configuration_for_user_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_androidenterprise_managedconfigurationsforuser_get(client):
    """Test case for androidenterprise_managedconfigurationsforuser_get

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/androidenterprise/v1/enterprises/{enterprise_id}/users/{user_id}/managedConfigurationsForUser/{managed_configuration_for_user_id}'.format(enterprise_id='enterprise_id_example', user_id='user_id_example', managed_configuration_for_user_id='managed_configuration_for_user_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_androidenterprise_managedconfigurationsforuser_list(client):
    """Test case for androidenterprise_managedconfigurationsforuser_list

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/androidenterprise/v1/enterprises/{enterprise_id}/users/{user_id}/managedConfigurationsForUser'.format(enterprise_id='enterprise_id_example', user_id='user_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_androidenterprise_managedconfigurationsforuser_update(client):
    """Test case for androidenterprise_managedconfigurationsforuser_update

    
    """
    body = {"productId":"productId","kind":"kind","managedProperty":[{"valueBundle":{"managedProperty":[null,null]},"valueStringArray":["valueStringArray","valueStringArray"],"valueString":"valueString","valueBundleArray":[{"managedProperty":[null,null]},{"managedProperty":[null,null]}],"valueInteger":1,"key":"key","valueBool":True},{"valueBundle":{"managedProperty":[null,null]},"valueStringArray":["valueStringArray","valueStringArray"],"valueString":"valueString","valueBundleArray":[{"managedProperty":[null,null]},{"managedProperty":[null,null]}],"valueInteger":1,"key":"key","valueBool":True}],"configurationVariables":{"mcmId":"mcmId","variableSet":[{"userValue":"userValue","placeholder":"placeholder"},{"userValue":"userValue","placeholder":"placeholder"}]}}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/androidenterprise/v1/enterprises/{enterprise_id}/users/{user_id}/managedConfigurationsForUser/{managed_configuration_for_user_id}'.format(enterprise_id='enterprise_id_example', user_id='user_id_example', managed_configuration_for_user_id='managed_configuration_for_user_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

