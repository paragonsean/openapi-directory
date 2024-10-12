# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.data_share_error import DataShareError
from openapi_server.models.operation_response import OperationResponse
from openapi_server.models.trigger import Trigger
from openapi_server.models.trigger_list import TriggerList


pytestmark = pytest.mark.asyncio

async def test_triggers_create(client):
    """Test case for triggers_create

    This method creates a trigger for a share subscription
    """
    trigger = {"kind":"ScheduleBased"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DataShare/accounts/{account_name}/shareSubscriptions/{share_subscription_name}/triggers/{trigger_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', share_subscription_name='share_subscription_name_example', trigger_name='trigger_name_example'),
        headers=headers,
        json=trigger,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_triggers_delete(client):
    """Test case for triggers_delete

    Delete Trigger in a shareSubscription.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DataShare/accounts/{account_name}/shareSubscriptions/{share_subscription_name}/triggers/{trigger_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', share_subscription_name='share_subscription_name_example', trigger_name='trigger_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_triggers_get(client):
    """Test case for triggers_get

    Get Trigger in a shareSubscription.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DataShare/accounts/{account_name}/shareSubscriptions/{share_subscription_name}/triggers/{trigger_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', share_subscription_name='share_subscription_name_example', trigger_name='trigger_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_triggers_list_by_share_subscription(client):
    """Test case for triggers_list_by_share_subscription

    List Triggers in a share subscription.
    """
    params = [('api-version', 'api_version_example'),
                    ('$skipToken', 'skip_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DataShare/accounts/{account_name}/shareSubscriptions/{share_subscription_name}/triggers'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', share_subscription_name='share_subscription_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

