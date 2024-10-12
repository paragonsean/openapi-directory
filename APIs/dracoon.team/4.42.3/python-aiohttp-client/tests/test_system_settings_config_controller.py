# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.auth_config import AuthConfig
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.eventlog_config import EventlogConfig
from openapi_server.models.general_settings import GeneralSettings
from openapi_server.models.infrastructure_properties import InfrastructureProperties
from openapi_server.models.syslog_config import SyslogConfig
from openapi_server.models.system_defaults import SystemDefaults
from openapi_server.models.update_eventlog_config import UpdateEventlogConfig
from openapi_server.models.update_general_settings import UpdateGeneralSettings
from openapi_server.models.update_syslog_config import UpdateSyslogConfig
from openapi_server.models.update_system_defaults import UpdateSystemDefaults


pytestmark = pytest.mark.asyncio

async def test_request_auth_config(client):
    """Test case for request_auth_config

    Request authentication settings
    """
    headers = { 
        'Accept': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/system/config/settings/auth',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_request_eventlog_config(client):
    """Test case for request_eventlog_config

    Request eventlog settings
    """
    headers = { 
        'Accept': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/system/config/settings/eventlog',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_request_general_settings(client):
    """Test case for request_general_settings

    Request general settings
    """
    headers = { 
        'Accept': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/system/config/settings/general',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_request_infrastructure_properties(client):
    """Test case for request_infrastructure_properties

    Request infrastructure properties
    """
    headers = { 
        'Accept': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/system/config/settings/infrastructure',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_request_syslog_config(client):
    """Test case for request_syslog_config

    Request syslog settings
    """
    headers = { 
        'Accept': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/system/config/settings/syslog',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_request_system_defaults(client):
    """Test case for request_system_defaults

    Request system defaults
    """
    headers = { 
        'Accept': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/system/config/settings/defaults',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_auth_config(client):
    """Test case for update_auth_config

    Update authentication settings
    """
    body = {"authMethods":[{"isEnabled":True,"name":"name","priority":0},{"isEnabled":True,"name":"name","priority":0}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v4/system/config/settings/auth',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_eventlog_config(client):
    """Test case for update_eventlog_config

    Update eventlog settings
    """
    body = {"logIpEnabled":True,"enabled":True,"retentionPeriod":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v4/system/config/settings/eventlog',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_general_settings(client):
    """Test case for update_general_settings

    Update general settings
    """
    body = {"sharePasswordSmsEnabled":True,"hideLoginInputFields":True,"authTokenRestrictions":{"overwriteEnabled":True,"refreshTokenValidity":6,"accessTokenValidity":0},"emailNotificationButtonEnabled":True,"weakPasswordEnabled":True,"eulaEnabled":True,"cryptoEnabled":True,"s3TagsEnabled":True,"mediaServerEnabled":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v4/system/config/settings/general',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_syslog_config(client):
    """Test case for update_syslog_config

    Update syslog settings
    """
    body = {"logIpEnabled":True,"protocol":"TCP","port":0,"host":"host","enabled":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v4/system/config/settings/syslog',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_system_defaults(client):
    """Test case for update_system_defaults

    Update system defaults
    """
    body = {"nonmemberViewerDefault":True,"uploadShareDefaultExpirationPeriod":1,"languageDefault":"languageDefault","downloadShareDefaultExpirationPeriod":0,"fileDefaultExpirationPeriod":6}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v4/system/config/settings/defaults',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

