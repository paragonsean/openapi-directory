# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.active_directory_config import ActiveDirectoryConfig
from openapi_server.models.active_directory_config_list import ActiveDirectoryConfigList
from openapi_server.models.create_active_directory_config_request import CreateActiveDirectoryConfigRequest
from openapi_server.models.create_o_auth_client_request import CreateOAuthClientRequest
from openapi_server.models.create_open_id_idp_config_request import CreateOpenIdIdpConfigRequest
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.o_auth_client import OAuthClient
from openapi_server.models.open_id_idp_config import OpenIdIdpConfig
from openapi_server.models.radius_config import RadiusConfig
from openapi_server.models.radius_config_create_request import RadiusConfigCreateRequest
from openapi_server.models.radius_config_update_request import RadiusConfigUpdateRequest
from openapi_server.models.reset_password400_response import ResetPassword400Response
from openapi_server.models.test_active_directory_config_request import TestActiveDirectoryConfigRequest
from openapi_server.models.test_active_directory_config_response import TestActiveDirectoryConfigResponse
from openapi_server.models.update_active_directory_config_request import UpdateActiveDirectoryConfigRequest
from openapi_server.models.update_o_auth_client_request import UpdateOAuthClientRequest
from openapi_server.models.update_open_id_idp_config_request import UpdateOpenIdIdpConfigRequest


pytestmark = pytest.mark.asyncio

async def test_create_ad_config(client):
    """Test case for create_ad_config

    Create Active Directory configuration
    """
    body = {"createHomeFolder":False,"userImport":False,"serverAdminPassword":"serverAdminPassword","useLdaps":False,"sslFingerPrint":"sslFingerPrint","adExportGroup":"adExportGroup","ldapUsersDomain":"ldapUsersDomain","serverPort":1,"serverAdminName":"serverAdminName","homeFolderParent":0,"alias":"alias","serverIp":"serverIp","userFilter":"userFilter","sdsImportGroup":6}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v4/system/config/auth/ads',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_o_auth_client(client):
    """Test case for create_o_auth_client

    Create OAuth client
    """
    body = {"grantTypes":["authorization_code","authorization_code"],"clientId":"clientId","clientType":"confidential","clientName":"clientName","refreshTokenValidity":1,"approvalValidity":6,"clientSecret":"clientSecret","redirectUris":["redirectUris","redirectUris"],"accessTokenValidity":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v4/system/config/oauth/clients',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_open_id_idp_config(client):
    """Test case for create_open_id_idp_config

    Create OpenID Connect IDP configuration
    """
    body = {"clientId":"clientId","mappingClaim":"mappingClaim","tokenEndPointUrl":"tokenEndPointUrl","fallbackMappingClaim":"fallbackMappingClaim","userInfoEndPointUrl":"userInfoEndPointUrl","redirectUris":["redirectUris","redirectUris"],"issuer":"issuer","userUpdateEnabled":False,"jwksEndPointUrl":"jwksEndPointUrl","pkceChallengeMethod":"plain","pkceEnabled":False,"userManagementUrl":"userManagementUrl","authorizationEndPointUrl":"authorizationEndPointUrl","userImportGroup":0,"userInfoSource":"user_info_endpoint","name":"name","clientSecret":"clientSecret","scopes":["scopes","scopes"],"flow":"authorization_code","userImportEnabled":False}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v4/system/config/auth/openid/idps',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_radius_config(client):
    """Test case for create_radius_config

    Create RADIUS configuration
    """
    body = {"port":0,"failoverServer":{"failoverIpAddress":"failoverIpAddress","failoverPort":0,"failoverEnabled":True},"ipAddress":"ipAddress","otpPinFirst":True,"sharedSecret":"sharedSecret"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v4/system/config/auth/radius',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remove_ad_config(client):
    """Test case for remove_ad_config

    Remove Active Directory configuration
    """
    headers = { 
        'Accept': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v4/system/config/auth/ads/{ad_id}'.format(ad_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remove_o_auth_client(client):
    """Test case for remove_o_auth_client

    Remove OAuth client
    """
    headers = { 
        'Accept': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v4/system/config/oauth/clients/{client_id}'.format(client_id='client_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remove_open_id_idp_config(client):
    """Test case for remove_open_id_idp_config

    Remove OpenID Connect IDP configuration
    """
    headers = { 
        'Accept': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v4/system/config/auth/openid/idps/{idp_id}'.format(idp_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remove_radius_config(client):
    """Test case for remove_radius_config

    Remove RADIUS configuration
    """
    headers = { 
        'Accept': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v4/system/config/auth/radius',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_request_ad_config(client):
    """Test case for request_ad_config

    Request Active Directory configuration
    """
    headers = { 
        'Accept': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/system/config/auth/ads/{ad_id}'.format(ad_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_request_ad_configs(client):
    """Test case for request_ad_configs

    Request list of Active Directory configurations
    """
    headers = { 
        'Accept': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/system/config/auth/ads',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_request_o_auth_client(client):
    """Test case for request_o_auth_client

    Request OAuth client
    """
    headers = { 
        'Accept': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/system/config/oauth/clients/{client_id}'.format(client_id='client_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_request_o_auth_clients(client):
    """Test case for request_o_auth_clients

    Request list of OAuth clients
    """
    params = [('filter', 'filter_example'),
                    ('sort', 'sort_example')]
    headers = { 
        'Accept': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/system/config/oauth/clients',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_request_open_id_idp_config(client):
    """Test case for request_open_id_idp_config

    Request OpenID Connect IDP configuration
    """
    headers = { 
        'Accept': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/system/config/auth/openid/idps/{idp_id}'.format(idp_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_request_open_id_idp_configs(client):
    """Test case for request_open_id_idp_configs

    Request list of OpenID Connect IDP configurations
    """
    headers = { 
        'Accept': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/system/config/auth/openid/idps',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_request_radius_config(client):
    """Test case for request_radius_config

    Request RADIUS configuration
    """
    headers = { 
        'Accept': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/system/config/auth/radius',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_test_ad_config(client):
    """Test case for test_ad_config

    Test Active Directory configuration
    """
    body = {"serverAdminPassword":"serverAdminPassword","useLdaps":False,"serverIp":"serverIp","sslFingerPrint":"sslFingerPrint","ldapUsersDomain":"ldapUsersDomain","serverPort":0,"serverAdminName":"serverAdminName"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v4/system/config/actions/test/ad',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_test_radius_config(client):
    """Test case for test_radius_config

    Test RADIUS server availability
    """
    headers = { 
        'Accept': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v4/system/config/actions/test/radius',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_ad_config(client):
    """Test case for update_ad_config

    Update Active Directory configuration
    """
    body = {"createHomeFolder":False,"userImport":True,"serverAdminPassword":"serverAdminPassword","useLdaps":True,"sslFingerPrint":"sslFingerPrint","adExportGroup":"adExportGroup","ldapUsersDomain":"ldapUsersDomain","serverPort":1,"serverAdminName":"serverAdminName","homeFolderParent":0,"alias":"alias","serverIp":"serverIp","userFilter":"userFilter","sdsImportGroup":6}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v4/system/config/auth/ads/{ad_id}'.format(ad_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_o_auth_client(client):
    """Test case for update_o_auth_client

    Update OAuth client
    """
    body = {"grantTypes":["authorization_code","authorization_code"],"clientType":"confidential","clientName":"clientName","refreshTokenValidity":1,"isEnabled":True,"approvalValidity":6,"clientSecret":"clientSecret","redirectUris":["redirectUris","redirectUris"],"accessTokenValidity":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v4/system/config/oauth/clients/{client_id}'.format(client_id='client_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_open_id_idp_config(client):
    """Test case for update_open_id_idp_config

    Update OpenID Connect IDP configuration
    """
    body = {"clientId":"clientId","mappingClaim":"mappingClaim","resetFallbackMappingClaim":True,"tokenEndPointUrl":"tokenEndPointUrl","fallbackMappingClaim":"fallbackMappingClaim","userInfoEndPointUrl":"userInfoEndPointUrl","redirectUris":["redirectUris","redirectUris"],"issuer":"issuer","userUpdateEnabled":False,"jwksEndPointUrl":"jwksEndPointUrl","pkceChallengeMethod":"pkceChallengeMethod","pkceEnabled":False,"userManagementUrl":"userManagementUrl","authorizationEndPointUrl":"authorizationEndPointUrl","userImportGroup":0,"userInfoSource":"user_info_endpoint","name":"name","clientSecret":"clientSecret","scopes":["scopes","scopes"],"flow":"authorization_code","userImportEnabled":False}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v4/system/config/auth/openid/idps/{idp_id}'.format(idp_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_radius_config(client):
    """Test case for update_radius_config

    Update RADIUS configuration
    """
    body = {"port":0,"failoverServer":{"failoverIpAddress":"failoverIpAddress","failoverPort":0,"failoverEnabled":True},"ipAddress":"ipAddress","otpPinFirst":True,"sharedSecret":"sharedSecret"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v4/system/config/auth/radius',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

