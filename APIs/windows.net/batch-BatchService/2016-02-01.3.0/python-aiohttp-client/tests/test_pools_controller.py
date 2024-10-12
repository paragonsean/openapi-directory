# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.auto_scale_run import AutoScaleRun
from openapi_server.models.batch_error import BatchError
from openapi_server.models.cloud_pool import CloudPool
from openapi_server.models.cloud_pool_list_result import CloudPoolListResult
from openapi_server.models.pool_add_parameter import PoolAddParameter
from openapi_server.models.pool_enable_auto_scale_parameter import PoolEnableAutoScaleParameter
from openapi_server.models.pool_evaluate_auto_scale_parameter import PoolEvaluateAutoScaleParameter
from openapi_server.models.pool_list_pool_usage_metrics_result import PoolListPoolUsageMetricsResult
from openapi_server.models.pool_patch_parameter import PoolPatchParameter
from openapi_server.models.pool_resize_parameter import PoolResizeParameter
from openapi_server.models.pool_statistics import PoolStatistics
from openapi_server.models.pool_update_properties_parameter import PoolUpdatePropertiesParameter
from openapi_server.models.pool_upgrade_os_parameter import PoolUpgradeOSParameter


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/json; odata&#x3D;minimalmetadata not supported by Connexion")
async def test_pool_add(client):
    """Test case for pool_add

    
    """
    body = openapi_server.PoolAddParameter()
    params = [('timeout', 30),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json; odata=minimalmetadata',
        'client_request_id': 'client_request_id_example',
        'return_client_request_id': True,
        'ocp_date': 'ocp_date_example',
    }
    response = await client.request(
        method='POST',
        path='/pools',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_pool_delete(client):
    """Test case for pool_delete

    
    """
    params = [('timeout', 30),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'client_request_id': 'client_request_id_example',
        'return_client_request_id': True,
        'ocp_date': 'ocp_date_example',
        'if_match': 'if_match_example',
        'if_none_match': 'if_none_match_example',
        'if_modified_since': 'if_modified_since_example',
        'if_unmodified_since': 'if_unmodified_since_example',
    }
    response = await client.request(
        method='DELETE',
        path='/pools/{pool_id}'.format(pool_id='pool_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_pool_disable_auto_scale(client):
    """Test case for pool_disable_auto_scale

    
    """
    params = [('timeout', 30),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'client_request_id': 'client_request_id_example',
        'return_client_request_id': True,
        'ocp_date': 'ocp_date_example',
    }
    response = await client.request(
        method='POST',
        path='/pools/{pool_id}/disableautoscale'.format(pool_id='pool_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/json; odata&#x3D;minimalmetadata not supported by Connexion")
async def test_pool_enable_auto_scale(client):
    """Test case for pool_enable_auto_scale

    
    """
    body = openapi_server.PoolEnableAutoScaleParameter()
    params = [('timeout', 30),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json; odata=minimalmetadata',
        'client_request_id': 'client_request_id_example',
        'return_client_request_id': True,
        'ocp_date': 'ocp_date_example',
        'if_match': 'if_match_example',
        'if_none_match': 'if_none_match_example',
        'if_modified_since': 'if_modified_since_example',
        'if_unmodified_since': 'if_unmodified_since_example',
    }
    response = await client.request(
        method='POST',
        path='/pools/{pool_id}/enableautoscale'.format(pool_id='pool_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/json; odata&#x3D;minimalmetadata not supported by Connexion")
async def test_pool_evaluate_auto_scale(client):
    """Test case for pool_evaluate_auto_scale

    
    """
    body = openapi_server.PoolEvaluateAutoScaleParameter()
    params = [('timeout', 30),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json; odata=minimalmetadata',
        'client_request_id': 'client_request_id_example',
        'return_client_request_id': True,
        'ocp_date': 'ocp_date_example',
    }
    response = await client.request(
        method='POST',
        path='/pools/{pool_id}/evaluateautoscale'.format(pool_id='pool_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_pool_exists(client):
    """Test case for pool_exists

    
    """
    params = [('timeout', 30),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'client_request_id': 'client_request_id_example',
        'return_client_request_id': True,
        'ocp_date': 'ocp_date_example',
        'if_match': 'if_match_example',
        'if_none_match': 'if_none_match_example',
        'if_modified_since': 'if_modified_since_example',
        'if_unmodified_since': 'if_unmodified_since_example',
    }
    response = await client.request(
        method='HEAD',
        path='/pools/{pool_id}'.format(pool_id='pool_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_pool_get(client):
    """Test case for pool_get

    
    """
    params = [('$select', 'select_example'),
                    ('$expand', 'expand_example'),
                    ('timeout', 30),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'client_request_id': 'client_request_id_example',
        'return_client_request_id': True,
        'ocp_date': 'ocp_date_example',
        'if_match': 'if_match_example',
        'if_none_match': 'if_none_match_example',
        'if_modified_since': 'if_modified_since_example',
        'if_unmodified_since': 'if_unmodified_since_example',
    }
    response = await client.request(
        method='GET',
        path='/pools/{pool_id}'.format(pool_id='pool_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_pool_get_all_pools_lifetime_statistics(client):
    """Test case for pool_get_all_pools_lifetime_statistics

    
    """
    params = [('timeout', 30),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'client_request_id': 'client_request_id_example',
        'return_client_request_id': True,
        'ocp_date': 'ocp_date_example',
    }
    response = await client.request(
        method='GET',
        path='/lifetimepoolstats',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_pool_list(client):
    """Test case for pool_list

    
    """
    params = [('$filter', 'filter_example'),
                    ('$select', 'select_example'),
                    ('$expand', 'expand_example'),
                    ('maxresults', 56),
                    ('timeout', 30),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'client_request_id': 'client_request_id_example',
        'return_client_request_id': True,
        'ocp_date': 'ocp_date_example',
    }
    response = await client.request(
        method='GET',
        path='/pools',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_pool_list_pool_usage_metrics(client):
    """Test case for pool_list_pool_usage_metrics

    
    """
    params = [('starttime', '2013-10-20T19:20:30+01:00'),
                    ('endtime', '2013-10-20T19:20:30+01:00'),
                    ('$filter', 'filter_example'),
                    ('maxresults', 56),
                    ('timeout', 30),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'client_request_id': 'client_request_id_example',
        'return_client_request_id': True,
        'ocp_date': 'ocp_date_example',
    }
    response = await client.request(
        method='GET',
        path='/poolusagemetrics',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/json; odata&#x3D;minimalmetadata not supported by Connexion")
async def test_pool_patch(client):
    """Test case for pool_patch

    
    """
    body = openapi_server.PoolPatchParameter()
    params = [('timeout', 30),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json; odata=minimalmetadata',
        'client_request_id': 'client_request_id_example',
        'return_client_request_id': True,
        'ocp_date': 'ocp_date_example',
        'if_match': 'if_match_example',
        'if_none_match': 'if_none_match_example',
        'if_modified_since': 'if_modified_since_example',
        'if_unmodified_since': 'if_unmodified_since_example',
    }
    response = await client.request(
        method='PATCH',
        path='/pools/{pool_id}'.format(pool_id='pool_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/json; odata&#x3D;minimalmetadata not supported by Connexion")
async def test_pool_resize(client):
    """Test case for pool_resize

    
    """
    body = openapi_server.PoolResizeParameter()
    params = [('timeout', 30),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json; odata=minimalmetadata',
        'client_request_id': 'client_request_id_example',
        'return_client_request_id': True,
        'ocp_date': 'ocp_date_example',
        'if_match': 'if_match_example',
        'if_none_match': 'if_none_match_example',
        'if_modified_since': 'if_modified_since_example',
        'if_unmodified_since': 'if_unmodified_since_example',
    }
    response = await client.request(
        method='POST',
        path='/pools/{pool_id}/resize'.format(pool_id='pool_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_pool_stop_resize(client):
    """Test case for pool_stop_resize

    
    """
    params = [('timeout', 30),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'client_request_id': 'client_request_id_example',
        'return_client_request_id': True,
        'ocp_date': 'ocp_date_example',
        'if_match': 'if_match_example',
        'if_none_match': 'if_none_match_example',
        'if_modified_since': 'if_modified_since_example',
        'if_unmodified_since': 'if_unmodified_since_example',
    }
    response = await client.request(
        method='POST',
        path='/pools/{pool_id}/stopresize'.format(pool_id='pool_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/json; odata&#x3D;minimalmetadata not supported by Connexion")
async def test_pool_update_properties(client):
    """Test case for pool_update_properties

    
    """
    body = openapi_server.PoolUpdatePropertiesParameter()
    params = [('timeout', 30),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json; odata=minimalmetadata',
        'client_request_id': 'client_request_id_example',
        'return_client_request_id': True,
        'ocp_date': 'ocp_date_example',
    }
    response = await client.request(
        method='POST',
        path='/pools/{pool_id}/updateproperties'.format(pool_id='pool_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/json; odata&#x3D;minimalmetadata not supported by Connexion")
async def test_pool_upgrade_os(client):
    """Test case for pool_upgrade_os

    
    """
    body = openapi_server.PoolUpgradeOSParameter()
    params = [('timeout', 30),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json; odata=minimalmetadata',
        'client_request_id': 'client_request_id_example',
        'return_client_request_id': True,
        'ocp_date': 'ocp_date_example',
        'if_match': 'if_match_example',
        'if_none_match': 'if_none_match_example',
        'if_modified_since': 'if_modified_since_example',
        'if_unmodified_since': 'if_unmodified_since_example',
    }
    response = await client.request(
        method='POST',
        path='/pools/{pool_id}/upgradeos'.format(pool_id='pool_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

