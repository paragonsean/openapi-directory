# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.algorithm_version_info_list import AlgorithmVersionInfoList
from openapi_server.models.classification_policies_config import ClassificationPoliciesConfig
from openapi_server.models.config_option_list import ConfigOptionList
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.general_settings_info import GeneralSettingsInfo
from openapi_server.models.guest_users_policies_config import GuestUsersPoliciesConfig
from openapi_server.models.infrastructure_properties import InfrastructureProperties
from openapi_server.models.notification_channel_list import NotificationChannelList
from openapi_server.models.password_policies_config import PasswordPoliciesConfig
from openapi_server.models.product_package_response_list import ProductPackageResponseList
from openapi_server.models.s3_tag_list import S3TagList
from openapi_server.models.system_defaults import SystemDefaults


pytestmark = pytest.mark.asyncio

async def test_request_algorithms(client):
    """Test case for request_algorithms

    Request algorithms
    """
    headers = { 
        'Accept': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/config/info/policies/algorithms',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_request_classification_policies_config_info(client):
    """Test case for request_classification_policies_config_info

    Request classification policies
    """
    headers = { 
        'Accept': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/config/info/policies/classifications',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_request_current_product_packages(client):
    """Test case for request_current_product_packages

    Request list of currently enabled product packages
    """
    headers = { 
        'Accept': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/config/info/product_packages/current',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_request_general_settings_info(client):
    """Test case for request_general_settings_info

    Request general settings
    """
    headers = { 
        'Accept': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/config/info/general',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_request_guest_users_policies_config_info(client):
    """Test case for request_guest_users_policies_config_info

    Request guest users policies
    """
    headers = { 
        'Accept': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/config/info/policies/guest_users',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_request_infrastructure_properties_info(client):
    """Test case for request_infrastructure_properties_info

    Request infrastructure properties
    """
    headers = { 
        'Accept': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/config/info/infrastructure',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_request_notification_channels_info(client):
    """Test case for request_notification_channels_info

    Request list of notification channels
    """
    headers = { 
        'Accept': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/config/info/notifications/channels',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_request_password_policies_config_info(client):
    """Test case for request_password_policies_config_info

    Request password policies
    """
    headers = { 
        'Accept': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/config/info/policies/passwords',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_request_product_packages(client):
    """Test case for request_product_packages

    Request list of product packages
    """
    headers = { 
        'Accept': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/config/info/product_packages',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_request_s3_tags_info(client):
    """Test case for request_s3_tags_info

    Request list of configured S3 tags
    """
    headers = { 
        'Accept': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/config/info/s3_tags',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_request_system_defaults_info(client):
    """Test case for request_system_defaults_info

    Request default values
    """
    headers = { 
        'Accept': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/config/info/defaults',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_request_system_settings(client):
    """Test case for request_system_settings

    Request system settings
    """
    headers = { 
        'Accept': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/config/settings',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_system_settings(client):
    """Test case for update_system_settings

    Update system settings
    """
    body = {"items":[{"value":"value","key":"key"},{"value":"value","key":"key"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v4/config/settings',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

