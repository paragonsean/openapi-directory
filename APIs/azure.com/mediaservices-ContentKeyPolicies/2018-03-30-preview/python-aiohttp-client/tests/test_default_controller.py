# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.content_key_policies_list_default_response import ContentKeyPoliciesListDefaultResponse
from openapi_server.models.content_key_policy import ContentKeyPolicy
from openapi_server.models.content_key_policy_collection import ContentKeyPolicyCollection
from openapi_server.models.content_key_policy_properties import ContentKeyPolicyProperties


pytestmark = pytest.mark.asyncio

async def test_content_key_policies_create_or_update(client):
    """Test case for content_key_policies_create_or_update

    Create or update an Content Key Policy
    """
    parameters = {"properties":{"policyId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","created":"2000-01-23T04:56:07.000+00:00","options":[{"configuration":{"@odata.type":"@odata.type"},"name":"name","policyOptionId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","restriction":{"@odata.type":"@odata.type"}},{"configuration":{"@odata.type":"@odata.type"},"name":"name","policyOptionId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","restriction":{"@odata.type":"@odata.type"}}],"description":"description","lastModified":"2000-01-23T04:56:07.000+00:00"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Media/mediaServices/{account_name}/contentKeyPolicies/{content_key_policy_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', content_key_policy_name='content_key_policy_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_content_key_policies_delete(client):
    """Test case for content_key_policies_delete

    Delete a Content Key Policy
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Media/mediaServices/{account_name}/contentKeyPolicies/{content_key_policy_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', content_key_policy_name='content_key_policy_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_content_key_policies_get(client):
    """Test case for content_key_policies_get

    Get a Content Key Policy
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Media/mediaServices/{account_name}/contentKeyPolicies/{content_key_policy_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', content_key_policy_name='content_key_policy_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_content_key_policies_get_policy_properties_with_secrets(client):
    """Test case for content_key_policies_get_policy_properties_with_secrets

    Get a Content Key Policy with secrets
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Media/mediaServices/{account_name}/contentKeyPolicies/{content_key_policy_name}/getPolicyPropertiesWithSecrets'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', content_key_policy_name='content_key_policy_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_content_key_policies_list(client):
    """Test case for content_key_policies_list

    List Content Key Policies
    """
    params = [('api-version', 'api_version_example'),
                    ('$filter', 'filter_example'),
                    ('$top', 56),
                    ('$orderby', 'orderby_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Media/mediaServices/{account_name}/contentKeyPolicies'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_content_key_policies_update(client):
    """Test case for content_key_policies_update

    Update a Content Key Policy
    """
    parameters = {"properties":{"policyId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","created":"2000-01-23T04:56:07.000+00:00","options":[{"configuration":{"@odata.type":"@odata.type"},"name":"name","policyOptionId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","restriction":{"@odata.type":"@odata.type"}},{"configuration":{"@odata.type":"@odata.type"},"name":"name","policyOptionId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","restriction":{"@odata.type":"@odata.type"}}],"description":"description","lastModified":"2000-01-23T04:56:07.000+00:00"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Media/mediaServices/{account_name}/contentKeyPolicies/{content_key_policy_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', content_key_policy_name='content_key_policy_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

