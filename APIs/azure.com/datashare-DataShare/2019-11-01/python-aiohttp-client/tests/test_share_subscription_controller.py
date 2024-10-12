# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.consumer_source_data_set_list import ConsumerSourceDataSetList
from openapi_server.models.data_share_error import DataShareError
from openapi_server.models.operation_response import OperationResponse
from openapi_server.models.share_subscription import ShareSubscription
from openapi_server.models.share_subscription_list import ShareSubscriptionList
from openapi_server.models.share_subscription_synchronization import ShareSubscriptionSynchronization
from openapi_server.models.share_subscription_synchronization_list import ShareSubscriptionSynchronizationList
from openapi_server.models.source_share_synchronization_setting_list import SourceShareSynchronizationSettingList
from openapi_server.models.synchronization_details_list import SynchronizationDetailsList
from openapi_server.models.synchronize import Synchronize


pytestmark = pytest.mark.asyncio

async def test_consumer_source_data_sets_list_by_share_subscription(client):
    """Test case for consumer_source_data_sets_list_by_share_subscription

    Get source dataSets of a shareSubscription.
    """
    params = [('api-version', 'api_version_example'),
                    ('$skipToken', 'skip_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DataShare/accounts/{account_name}/shareSubscriptions/{share_subscription_name}/ConsumerSourceDataSets'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', share_subscription_name='share_subscription_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_share_subscriptions_cancel_synchronization(client):
    """Test case for share_subscriptions_cancel_synchronization

    Request cancellation of a data share snapshot
    """
    share_subscription_synchronization = {"startTime":"2000-01-23T04:56:07.000+00:00","endTime":"2000-01-23T04:56:07.000+00:00","message":"message","durationMs":0,"synchronizationId":"synchronizationId","synchronizationMode":"Incremental","status":"status"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DataShare/accounts/{account_name}/shareSubscriptions/{share_subscription_name}/cancelSynchronization'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', share_subscription_name='share_subscription_name_example'),
        headers=headers,
        json=share_subscription_synchronization,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_share_subscriptions_create(client):
    """Test case for share_subscriptions_create

    Create shareSubscription in an account.
    """
    share_subscription = {"properties":{"shareTerms":"shareTerms","providerTenantName":"providerTenantName","invitationId":"invitationId","provisioningState":"Succeeded","userName":"userName","sourceShareLocation":"sourceShareLocation","createdAt":"2000-01-23T04:56:07.000+00:00","userEmail":"userEmail","shareName":"shareName","shareSubscriptionStatus":"Active","shareDescription":"shareDescription","shareKind":"CopyBased","providerEmail":"providerEmail","providerName":"providerName"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DataShare/accounts/{account_name}/shareSubscriptions/{share_subscription_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', share_subscription_name='share_subscription_name_example'),
        headers=headers,
        json=share_subscription,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_share_subscriptions_delete(client):
    """Test case for share_subscriptions_delete

    Delete shareSubscription in an account.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DataShare/accounts/{account_name}/shareSubscriptions/{share_subscription_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', share_subscription_name='share_subscription_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_share_subscriptions_get(client):
    """Test case for share_subscriptions_get

    Get shareSubscription in an account.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DataShare/accounts/{account_name}/shareSubscriptions/{share_subscription_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', share_subscription_name='share_subscription_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_share_subscriptions_list_by_account(client):
    """Test case for share_subscriptions_list_by_account

    List of available share subscriptions under an account.
    """
    params = [('api-version', 'api_version_example'),
                    ('$skipToken', 'skip_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DataShare/accounts/{account_name}/shareSubscriptions'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_share_subscriptions_list_source_share_synchronization_settings(client):
    """Test case for share_subscriptions_list_source_share_synchronization_settings

    Get source share synchronization settings for a shareSubscription.
    """
    params = [('api-version', 'api_version_example'),
                    ('$skipToken', 'skip_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DataShare/accounts/{account_name}/shareSubscriptions/{share_subscription_name}/listSourceShareSynchronizationSettings'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', share_subscription_name='share_subscription_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_share_subscriptions_list_synchronization_details(client):
    """Test case for share_subscriptions_list_synchronization_details

    List data set level details for a share subscription synchronization
    """
    share_subscription_synchronization = {"startTime":"2000-01-23T04:56:07.000+00:00","endTime":"2000-01-23T04:56:07.000+00:00","message":"message","durationMs":0,"synchronizationId":"synchronizationId","synchronizationMode":"Incremental","status":"status"}
    params = [('api-version', 'api_version_example'),
                    ('$skipToken', 'skip_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DataShare/accounts/{account_name}/shareSubscriptions/{share_subscription_name}/listSynchronizationDetails'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', share_subscription_name='share_subscription_name_example'),
        headers=headers,
        json=share_subscription_synchronization,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_share_subscriptions_list_synchronizations(client):
    """Test case for share_subscriptions_list_synchronizations

    List Synchronizations in a share subscription.
    """
    params = [('api-version', 'api_version_example'),
                    ('$skipToken', 'skip_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DataShare/accounts/{account_name}/shareSubscriptions/{share_subscription_name}/listSynchronizations'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', share_subscription_name='share_subscription_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_share_subscriptions_synchronize(client):
    """Test case for share_subscriptions_synchronize

    Initiate an asynchronous data share job
    """
    synchronize = {"synchronizationMode":"Incremental"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DataShare/accounts/{account_name}/shareSubscriptions/{share_subscription_name}/Synchronize'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', share_subscription_name='share_subscription_name_example'),
        headers=headers,
        json=synchronize,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

