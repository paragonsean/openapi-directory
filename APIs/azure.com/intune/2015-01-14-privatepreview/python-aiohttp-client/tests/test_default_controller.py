# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.android_mam_policy import AndroidMAMPolicy
from openapi_server.models.android_mam_policy_collection import AndroidMAMPolicyCollection
from openapi_server.models.application_collection import ApplicationCollection
from openapi_server.models.device import Device
from openapi_server.models.device_collection import DeviceCollection
from openapi_server.models.error import Error
from openapi_server.models.flagged_enrolled_app_collection import FlaggedEnrolledAppCollection
from openapi_server.models.flagged_user import FlaggedUser
from openapi_server.models.flagged_user_collection import FlaggedUserCollection
from openapi_server.models.groups_collection import GroupsCollection
from openapi_server.models.iosmam_policy import IOSMAMPolicy
from openapi_server.models.iosmam_policy_collection import IOSMAMPolicyCollection
from openapi_server.models.location import Location
from openapi_server.models.location_collection import LocationCollection
from openapi_server.models.mam_policy_app_id_or_group_id_payload import MAMPolicyAppIdOrGroupIdPayload
from openapi_server.models.operation_result_collection import OperationResultCollection
from openapi_server.models.statuses_default import StatusesDefault
from openapi_server.models.wipe_device_operation_result import WipeDeviceOperationResult


pytestmark = pytest.mark.asyncio

async def test_android_add_app_for_mam_policy(client):
    """Test case for android_add_app_for_mam_policy

    
    """
    parameters = {"properties":{"url":"url"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/providers/Microsoft.Intune/locations/{host_name}/androidPolicies/{policy_name}/apps/{app_name}'.format(host_name='host_name_example', policy_name='policy_name_example', app_name='app_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_android_add_group_for_mam_policy(client):
    """Test case for android_add_group_for_mam_policy

    
    """
    parameters = {"properties":{"url":"url"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/providers/Microsoft.Intune/locations/{host_name}/androidPolicies/{policy_name}/groups/{group_id}'.format(host_name='host_name_example', policy_name='policy_name_example', group_id='group_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_android_create_or_update_mam_policy(client):
    """Test case for android_create_or_update_mam_policy

    
    """
    parameters = {"properties":{"screenCapture":"allow","fileEncryption":"required"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/providers/Microsoft.Intune/locations/{host_name}/androidPolicies/{policy_name}'.format(host_name='host_name_example', policy_name='policy_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_android_delete_app_for_mam_policy(client):
    """Test case for android_delete_app_for_mam_policy

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/providers/Microsoft.Intune/locations/{host_name}/androidPolicies/{policy_name}/apps/{app_name}'.format(host_name='host_name_example', policy_name='policy_name_example', app_name='app_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_android_delete_group_for_mam_policy(client):
    """Test case for android_delete_group_for_mam_policy

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/providers/Microsoft.Intune/locations/{host_name}/androidPolicies/{policy_name}/groups/{group_id}'.format(host_name='host_name_example', policy_name='policy_name_example', group_id='group_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_android_delete_mam_policy(client):
    """Test case for android_delete_mam_policy

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/providers/Microsoft.Intune/locations/{host_name}/androidPolicies/{policy_name}'.format(host_name='host_name_example', policy_name='policy_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_android_get_app_for_mam_policy(client):
    """Test case for android_get_app_for_mam_policy

    
    """
    params = [('api-version', 'api_version_example'),
                    ('$filter', 'filter_example'),
                    ('$top', 56),
                    ('$select', 'select_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.Intune/locations/{host_name}/AndroidPolicies/{policy_name}/apps'.format(host_name='host_name_example', policy_name='policy_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_android_get_groups_for_mam_policy(client):
    """Test case for android_get_groups_for_mam_policy

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.Intune/locations/{host_name}/androidPolicies/{policy_name}/groups'.format(host_name='host_name_example', policy_name='policy_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_android_get_mam_policies(client):
    """Test case for android_get_mam_policies

    
    """
    params = [('api-version', 'api_version_example'),
                    ('$filter', 'filter_example'),
                    ('$top', 56),
                    ('$select', 'select_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.Intune/locations/{host_name}/androidPolicies'.format(host_name='host_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_android_get_mam_policy_by_name(client):
    """Test case for android_get_mam_policy_by_name

    
    """
    params = [('api-version', 'api_version_example'),
                    ('$select', 'select_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.Intune/locations/{host_name}/androidPolicies/{policy_name}'.format(host_name='host_name_example', policy_name='policy_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_android_patch_mam_policy(client):
    """Test case for android_patch_mam_policy

    
    """
    parameters = {"properties":{"screenCapture":"allow","fileEncryption":"required"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/providers/Microsoft.Intune/locations/{host_name}/androidPolicies/{policy_name}'.format(host_name='host_name_example', policy_name='policy_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_apps(client):
    """Test case for get_apps

    
    """
    params = [('api-version', 'api_version_example'),
                    ('$filter', 'filter_example'),
                    ('$top', 56),
                    ('$select', 'select_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.Intune/locations/{host_name}/apps'.format(host_name='host_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_location_by_host_name(client):
    """Test case for get_location_by_host_name

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.Intune/locations/hostName',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_locations(client):
    """Test case for get_locations

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.Intune/locations',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_mam_flagged_user_by_name(client):
    """Test case for get_mam_flagged_user_by_name

    
    """
    params = [('api-version', 'api_version_example'),
                    ('$select', 'select_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.Intune/locations/{host_name}/flaggedUsers/{user_name}'.format(host_name='host_name_example', user_name='user_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_mam_flagged_users(client):
    """Test case for get_mam_flagged_users

    
    """
    params = [('api-version', 'api_version_example'),
                    ('$filter', 'filter_example'),
                    ('$top', 56),
                    ('$select', 'select_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.Intune/locations/{host_name}/flaggedUsers'.format(host_name='host_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_mam_statuses(client):
    """Test case for get_mam_statuses

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.Intune/locations/{host_name}/statuses/default'.format(host_name='host_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_mam_user_device_by_device_name(client):
    """Test case for get_mam_user_device_by_device_name

    
    """
    params = [('api-version', 'api_version_example'),
                    ('$select', 'select_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.Intune/locations/{host_name}/users/{user_name}/devices/{device_name}'.format(host_name='host_name_example', user_name='user_name_example', device_name='device_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_mam_user_devices(client):
    """Test case for get_mam_user_devices

    
    """
    params = [('api-version', 'api_version_example'),
                    ('$filter', 'filter_example'),
                    ('$top', 56),
                    ('$select', 'select_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.Intune/locations/{host_name}/users/{user_name}/devices'.format(host_name='host_name_example', user_name='user_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_mam_user_flagged_enrolled_apps(client):
    """Test case for get_mam_user_flagged_enrolled_apps

    
    """
    params = [('api-version', 'api_version_example'),
                    ('$filter', 'filter_example'),
                    ('$top', 56),
                    ('$select', 'select_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.Intune/locations/{host_name}/flaggedUsers/{user_name}/flaggedEnrolledApps'.format(host_name='host_name_example', user_name='user_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_operation_results(client):
    """Test case for get_operation_results

    
    """
    params = [('api-version', 'api_version_example'),
                    ('$filter', 'filter_example'),
                    ('$top', 56),
                    ('$select', 'select_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.Intune/locations/{host_name}/operationResults'.format(host_name='host_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ios_add_app_for_mam_policy(client):
    """Test case for ios_add_app_for_mam_policy

    
    """
    parameters = {"properties":{"url":"url"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/providers/Microsoft.Intune/locations/{host_name}/iosPolicies/{policy_name}/apps/{app_name}'.format(host_name='host_name_example', policy_name='policy_name_example', app_name='app_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ios_add_group_for_mam_policy(client):
    """Test case for ios_add_group_for_mam_policy

    
    """
    parameters = {"properties":{"url":"url"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/providers/Microsoft.Intune/locations/{host_name}/iosPolicies/{policy_name}/groups/{group_id}'.format(host_name='host_name_example', policy_name='policy_name_example', group_id='group_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ios_create_or_update_mam_policy(client):
    """Test case for ios_create_or_update_mam_policy

    
    """
    parameters = openapi_server.IOSMAMPolicy()
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/providers/Microsoft.Intune/locations/{host_name}/iosPolicies/{policy_name}'.format(host_name='host_name_example', policy_name='policy_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ios_delete_app_for_mam_policy(client):
    """Test case for ios_delete_app_for_mam_policy

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/providers/Microsoft.Intune/locations/{host_name}/iosPolicies/{policy_name}/apps/{app_name}'.format(host_name='host_name_example', policy_name='policy_name_example', app_name='app_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ios_delete_group_for_mam_policy(client):
    """Test case for ios_delete_group_for_mam_policy

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/providers/Microsoft.Intune/locations/{host_name}/iosPolicies/{policy_name}/groups/{group_id}'.format(host_name='host_name_example', policy_name='policy_name_example', group_id='group_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ios_delete_mam_policy(client):
    """Test case for ios_delete_mam_policy

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/providers/Microsoft.Intune/locations/{host_name}/iosPolicies/{policy_name}'.format(host_name='host_name_example', policy_name='policy_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ios_get_app_for_mam_policy(client):
    """Test case for ios_get_app_for_mam_policy

    
    """
    params = [('api-version', 'api_version_example'),
                    ('$filter', 'filter_example'),
                    ('$top', 56),
                    ('$select', 'select_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.Intune/locations/{host_name}/iosPolicies/{policy_name}/apps'.format(host_name='host_name_example', policy_name='policy_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ios_get_groups_for_mam_policy(client):
    """Test case for ios_get_groups_for_mam_policy

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.Intune/locations/{host_name}/iosPolicies/{policy_name}/groups'.format(host_name='host_name_example', policy_name='policy_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ios_get_mam_policies(client):
    """Test case for ios_get_mam_policies

    
    """
    params = [('api-version', 'api_version_example'),
                    ('$filter', 'filter_example'),
                    ('$top', 56),
                    ('$select', 'select_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.Intune/locations/{host_name}/iosPolicies'.format(host_name='host_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ios_get_mam_policy_by_name(client):
    """Test case for ios_get_mam_policy_by_name

    
    """
    params = [('api-version', 'api_version_example'),
                    ('$select', 'select_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.Intune/locations/{host_name}/iosPolicies/{policy_name}'.format(host_name='host_name_example', policy_name='policy_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ios_patch_mam_policy(client):
    """Test case for ios_patch_mam_policy

    
    """
    parameters = openapi_server.IOSMAMPolicy()
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/providers/Microsoft.Intune/locations/{host_name}/iosPolicies/{policy_name}'.format(host_name='host_name_example', policy_name='policy_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_wipe_mam_user_device(client):
    """Test case for wipe_mam_user_device

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/providers/Microsoft.Intune/locations/{host_name}/users/{user_name}/devices/{device_name}/wipe'.format(host_name='host_name_example', user_name='user_name_example', device_name='device_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

