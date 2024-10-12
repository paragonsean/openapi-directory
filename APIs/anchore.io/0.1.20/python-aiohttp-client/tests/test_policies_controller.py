# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_error_response import ApiErrorResponse
from openapi_server.models.policy_bundle import PolicyBundle
from openapi_server.models.policy_bundle_record import PolicyBundleRecord


pytestmark = pytest.mark.asyncio

async def test_add_policy(client):
    """Test case for add_policy

    Add a new policy
    """
    body = {"blacklisted_images":[{"image":{"type":"tag","value":"value"},"registry":"registry","name":"name","id":"id","repository":"repository"},{"image":{"type":"tag","value":"value"},"registry":"registry","name":"name","id":"id","repository":"repository"}],"mappings":[{"image":{"type":"tag","value":"value"},"registry":"registry","whitelist_ids":["whitelist_ids","whitelist_ids"],"policy_id":"policy_id","name":"name","id":"id","policy_ids":["policy_ids","policy_ids"],"repository":"repository"},{"image":{"type":"tag","value":"value"},"registry":"registry","whitelist_ids":["whitelist_ids","whitelist_ids"],"policy_id":"policy_id","name":"name","id":"id","policy_ids":["policy_ids","policy_ids"],"repository":"repository"}],"whitelists":[{"name":"name","comment":"comment","id":"id","items":[{"expires_on":"2000-01-23T04:56:07.000+00:00","trigger_id":"trigger_id","gate":"gate","id":"id"},{"expires_on":"2000-01-23T04:56:07.000+00:00","trigger_id":"trigger_id","gate":"gate","id":"id"}],"version":"version"},{"name":"name","comment":"comment","id":"id","items":[{"expires_on":"2000-01-23T04:56:07.000+00:00","trigger_id":"trigger_id","gate":"gate","id":"id"},{"expires_on":"2000-01-23T04:56:07.000+00:00","trigger_id":"trigger_id","gate":"gate","id":"id"}],"version":"version"}],"name":"name","policies":[{"name":"name","comment":"comment","rules":[{"action":"GO","gate":"gate","id":"id","trigger":"trigger","params":[{"name":"name","value":"value"},{"name":"name","value":"value"}]},{"action":"GO","gate":"gate","id":"id","trigger":"trigger","params":[{"name":"name","value":"value"},{"name":"name","value":"value"}]}],"id":"id","version":"version"},{"name":"name","comment":"comment","rules":[{"action":"GO","gate":"gate","id":"id","trigger":"trigger","params":[{"name":"name","value":"value"},{"name":"name","value":"value"}]},{"action":"GO","gate":"gate","id":"id","trigger":"trigger","params":[{"name":"name","value":"value"},{"name":"name","value":"value"}]}],"id":"id","version":"version"}],"whitelisted_images":[{"image":{"type":"tag","value":"value"},"registry":"registry","name":"name","id":"id","repository":"repository"},{"image":{"type":"tag","value":"value"},"registry":"registry","name":"name","id":"id","repository":"repository"}],"comment":"comment","id":"id","version":"version"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_anchore_account': 'x_anchore_account_example',
    }
    response = await client.request(
        method='POST',
        path='/policies',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_policy(client):
    """Test case for delete_policy

    Delete policy
    """
    headers = { 
        'Accept': 'application/json',
        'x_anchore_account': 'x_anchore_account_example',
    }
    response = await client.request(
        method='DELETE',
        path='/policies/{policy_id}'.format(policy_id='policy_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_policy(client):
    """Test case for get_policy

    Get specific policy
    """
    params = [('detail', True)]
    headers = { 
        'Accept': 'application/json',
        'x_anchore_account': 'x_anchore_account_example',
    }
    response = await client.request(
        method='GET',
        path='/policies/{policy_id}'.format(policy_id='policy_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_policies(client):
    """Test case for list_policies

    List policies
    """
    params = [('detail', True)]
    headers = { 
        'Accept': 'application/json',
        'x_anchore_account': 'x_anchore_account_example',
    }
    response = await client.request(
        method='GET',
        path='/policies',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_policy(client):
    """Test case for update_policy

    Update policy
    """
    body = {"policybundle":{"blacklisted_images":[{"image":{"type":"tag","value":"value"},"registry":"registry","name":"name","id":"id","repository":"repository"},{"image":{"type":"tag","value":"value"},"registry":"registry","name":"name","id":"id","repository":"repository"}],"mappings":[{"image":{"type":"tag","value":"value"},"registry":"registry","whitelist_ids":["whitelist_ids","whitelist_ids"],"policy_id":"policy_id","name":"name","id":"id","policy_ids":["policy_ids","policy_ids"],"repository":"repository"},{"image":{"type":"tag","value":"value"},"registry":"registry","whitelist_ids":["whitelist_ids","whitelist_ids"],"policy_id":"policy_id","name":"name","id":"id","policy_ids":["policy_ids","policy_ids"],"repository":"repository"}],"whitelists":[{"name":"name","comment":"comment","id":"id","items":[{"expires_on":"2000-01-23T04:56:07.000+00:00","trigger_id":"trigger_id","gate":"gate","id":"id"},{"expires_on":"2000-01-23T04:56:07.000+00:00","trigger_id":"trigger_id","gate":"gate","id":"id"}],"version":"version"},{"name":"name","comment":"comment","id":"id","items":[{"expires_on":"2000-01-23T04:56:07.000+00:00","trigger_id":"trigger_id","gate":"gate","id":"id"},{"expires_on":"2000-01-23T04:56:07.000+00:00","trigger_id":"trigger_id","gate":"gate","id":"id"}],"version":"version"}],"name":"name","policies":[{"name":"name","comment":"comment","rules":[{"action":"GO","gate":"gate","id":"id","trigger":"trigger","params":[{"name":"name","value":"value"},{"name":"name","value":"value"}]},{"action":"GO","gate":"gate","id":"id","trigger":"trigger","params":[{"name":"name","value":"value"},{"name":"name","value":"value"}]}],"id":"id","version":"version"},{"name":"name","comment":"comment","rules":[{"action":"GO","gate":"gate","id":"id","trigger":"trigger","params":[{"name":"name","value":"value"},{"name":"name","value":"value"}]},{"action":"GO","gate":"gate","id":"id","trigger":"trigger","params":[{"name":"name","value":"value"},{"name":"name","value":"value"}]}],"id":"id","version":"version"}],"whitelisted_images":[{"image":{"type":"tag","value":"value"},"registry":"registry","name":"name","id":"id","repository":"repository"},{"image":{"type":"tag","value":"value"},"registry":"registry","name":"name","id":"id","repository":"repository"}],"comment":"comment","id":"id","version":"version"},"policy_source":"policy_source","last_updated":"2000-01-23T04:56:07.000+00:00","policyId":"policyId","active":True,"created_at":"2000-01-23T04:56:07.000+00:00","userId":"userId"}
    params = [('active', True)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_anchore_account': 'x_anchore_account_example',
    }
    response = await client.request(
        method='PUT',
        path='/policies/{policy_id}'.format(policy_id='policy_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

