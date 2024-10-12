# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.list_content_keys_response import ListContentKeysResponse
from openapi_server.models.list_paths_response import ListPathsResponse
from openapi_server.models.streaming_locator import StreamingLocator
from openapi_server.models.streaming_locator_collection import StreamingLocatorCollection
from openapi_server.models.streaming_locators_list_default_response import StreamingLocatorsListDefaultResponse
from openapi_server.models.streaming_policy import StreamingPolicy
from openapi_server.models.streaming_policy_collection import StreamingPolicyCollection


pytestmark = pytest.mark.asyncio

async def test_streaming_locators_create(client):
    """Test case for streaming_locators_create

    Create a Streaming Locator
    """
    parameters = {"properties":{"defaultContentKeyPolicyName":"defaultContentKeyPolicyName","contentKeys":[{"id":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","label":"label","value":"value"},{"id":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","label":"label","value":"value"}],"created":"2000-01-23T04:56:07.000+00:00","streamingPolicyName":"streamingPolicyName","assetName":"assetName","startTime":"2000-01-23T04:56:07.000+00:00","endTime":"2000-01-23T04:56:07.000+00:00","streamingLocatorId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Media/mediaServices/{account_name}/streamingLocators/{streaming_locator_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', streaming_locator_name='streaming_locator_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_streaming_locators_delete(client):
    """Test case for streaming_locators_delete

    Delete a Streaming Locator
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Media/mediaServices/{account_name}/streamingLocators/{streaming_locator_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', streaming_locator_name='streaming_locator_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_streaming_locators_get(client):
    """Test case for streaming_locators_get

    Get a Streaming Locator
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Media/mediaServices/{account_name}/streamingLocators/{streaming_locator_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', streaming_locator_name='streaming_locator_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_streaming_locators_list(client):
    """Test case for streaming_locators_list

    List Streaming Locators
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
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Media/mediaServices/{account_name}/streamingLocators'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_streaming_locators_list_content_keys(client):
    """Test case for streaming_locators_list_content_keys

    List Content Keys
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Media/mediaServices/{account_name}/streamingLocators/{streaming_locator_name}/listContentKeys'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', streaming_locator_name='streaming_locator_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_streaming_locators_list_paths(client):
    """Test case for streaming_locators_list_paths

    List Paths
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Media/mediaServices/{account_name}/streamingLocators/{streaming_locator_name}/listPaths'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', streaming_locator_name='streaming_locator_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_streaming_policies_create(client):
    """Test case for streaming_policies_create

    Create a Streaming Policy
    """
    parameters = {"properties":{"defaultContentKeyPolicyName":"defaultContentKeyPolicyName","noEncryption":{"enabledProtocols":{"download":True,"smoothStreaming":True,"dash":True,"hls":True}},"created":"2000-01-23T04:56:07.000+00:00","envelopeEncryption":{"enabledProtocols":{"download":True,"smoothStreaming":True,"dash":True,"hls":True},"contentKeys":{"keyToTrackMappings":[{"policyName":"policyName","label":"label","tracks":[{"trackSelections":[{"property":"Unknown","operation":"Unknown","value":"value"},{"property":"Unknown","operation":"Unknown","value":"value"}]},{"trackSelections":[{"property":"Unknown","operation":"Unknown","value":"value"},{"property":"Unknown","operation":"Unknown","value":"value"}]}]},{"policyName":"policyName","label":"label","tracks":[{"trackSelections":[{"property":"Unknown","operation":"Unknown","value":"value"},{"property":"Unknown","operation":"Unknown","value":"value"}]},{"trackSelections":[{"property":"Unknown","operation":"Unknown","value":"value"},{"property":"Unknown","operation":"Unknown","value":"value"}]}]}],"defaultKey":{"policyName":"policyName","label":"label"}},"clearTracks":[{"trackSelections":[{"property":"Unknown","operation":"Unknown","value":"value"},{"property":"Unknown","operation":"Unknown","value":"value"}]},{"trackSelections":[{"property":"Unknown","operation":"Unknown","value":"value"},{"property":"Unknown","operation":"Unknown","value":"value"}]}],"customLicenseAcquisitionUrlTemplate":"customLicenseAcquisitionUrlTemplate"},"commonEncryptionCenc":{"enabledProtocols":{"download":True,"smoothStreaming":True,"dash":True,"hls":True},"contentKeys":{"keyToTrackMappings":[{"policyName":"policyName","label":"label","tracks":[{"trackSelections":[{"property":"Unknown","operation":"Unknown","value":"value"},{"property":"Unknown","operation":"Unknown","value":"value"}]},{"trackSelections":[{"property":"Unknown","operation":"Unknown","value":"value"},{"property":"Unknown","operation":"Unknown","value":"value"}]}]},{"policyName":"policyName","label":"label","tracks":[{"trackSelections":[{"property":"Unknown","operation":"Unknown","value":"value"},{"property":"Unknown","operation":"Unknown","value":"value"}]},{"trackSelections":[{"property":"Unknown","operation":"Unknown","value":"value"},{"property":"Unknown","operation":"Unknown","value":"value"}]}]}],"defaultKey":{"policyName":"policyName","label":"label"}},"clearTracks":[{"trackSelections":[{"property":"Unknown","operation":"Unknown","value":"value"},{"property":"Unknown","operation":"Unknown","value":"value"}]},{"trackSelections":[{"property":"Unknown","operation":"Unknown","value":"value"},{"property":"Unknown","operation":"Unknown","value":"value"}]}],"drm":{"playReady":{"playReadyCustomAttributes":"playReadyCustomAttributes","customLicenseAcquisitionUrlTemplate":"customLicenseAcquisitionUrlTemplate"},"widevine":{"customLicenseAcquisitionUrlTemplate":"customLicenseAcquisitionUrlTemplate"}}},"commonEncryptionCbcs":{"enabledProtocols":{"download":True,"smoothStreaming":True,"dash":True,"hls":True},"contentKeys":{"keyToTrackMappings":[{"policyName":"policyName","label":"label","tracks":[{"trackSelections":[{"property":"Unknown","operation":"Unknown","value":"value"},{"property":"Unknown","operation":"Unknown","value":"value"}]},{"trackSelections":[{"property":"Unknown","operation":"Unknown","value":"value"},{"property":"Unknown","operation":"Unknown","value":"value"}]}]},{"policyName":"policyName","label":"label","tracks":[{"trackSelections":[{"property":"Unknown","operation":"Unknown","value":"value"},{"property":"Unknown","operation":"Unknown","value":"value"}]},{"trackSelections":[{"property":"Unknown","operation":"Unknown","value":"value"},{"property":"Unknown","operation":"Unknown","value":"value"}]}]}],"defaultKey":{"policyName":"policyName","label":"label"}},"clearTracks":[{"trackSelections":[{"property":"Unknown","operation":"Unknown","value":"value"},{"property":"Unknown","operation":"Unknown","value":"value"}]},{"trackSelections":[{"property":"Unknown","operation":"Unknown","value":"value"},{"property":"Unknown","operation":"Unknown","value":"value"}]}],"drm":{"fairPlay":{"allowPersistentLicense":True,"customLicenseAcquisitionUrlTemplate":"customLicenseAcquisitionUrlTemplate"},"playReady":{"playReadyCustomAttributes":"playReadyCustomAttributes","customLicenseAcquisitionUrlTemplate":"customLicenseAcquisitionUrlTemplate"},"widevine":{"customLicenseAcquisitionUrlTemplate":"customLicenseAcquisitionUrlTemplate"}}}}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Media/mediaServices/{account_name}/streamingPolicies/{streaming_policy_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', streaming_policy_name='streaming_policy_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_streaming_policies_delete(client):
    """Test case for streaming_policies_delete

    Delete a Streaming Policy
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Media/mediaServices/{account_name}/streamingPolicies/{streaming_policy_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', streaming_policy_name='streaming_policy_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_streaming_policies_get(client):
    """Test case for streaming_policies_get

    Get a Streaming Policy
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Media/mediaServices/{account_name}/streamingPolicies/{streaming_policy_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', streaming_policy_name='streaming_policy_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_streaming_policies_list(client):
    """Test case for streaming_policies_list

    List Streaming Policies
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
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Media/mediaServices/{account_name}/streamingPolicies'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

