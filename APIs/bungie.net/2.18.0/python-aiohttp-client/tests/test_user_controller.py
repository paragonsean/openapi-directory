# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_available_locales200_response import GetAvailableLocales200Response
from openapi_server.models.user_get_available_themes200_response import UserGetAvailableThemes200Response
from openapi_server.models.user_get_bungie_net_user_by_id200_response import UserGetBungieNetUserById200Response
from openapi_server.models.user_get_credential_types_for_target_account200_response import UserGetCredentialTypesForTargetAccount200Response
from openapi_server.models.user_get_membership_data_by_id200_response import UserGetMembershipDataById200Response
from openapi_server.models.user_get_membership_from_hard_linked_credential200_response import UserGetMembershipFromHardLinkedCredential200Response
from openapi_server.models.user_search_by_global_name_post200_response import UserSearchByGlobalNamePost200Response


pytestmark = pytest.mark.asyncio

async def test_user_get_available_themes(client):
    """Test case for user_get_available_themes

    
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/Platform/User/GetAvailableThemes/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_user_get_bungie_net_user_by_id(client):
    """Test case for user_get_bungie_net_user_by_id

    
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/Platform/User/GetBungieNetUserById/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_user_get_credential_types_for_target_account(client):
    """Test case for user_get_credential_types_for_target_account

    
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/Platform/User/GetCredentialTypesForTargetAccount/{membership_id}'.format(membership_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_user_get_membership_data_by_id(client):
    """Test case for user_get_membership_data_by_id

    
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/Platform/User/GetMembershipsById/{membership_id}/{membership_type}'.format(membership_id=56, membership_type=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_user_get_membership_data_for_current_user(client):
    """Test case for user_get_membership_data_for_current_user

    
    """
    headers = { 
        'Accept': '*/*',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/Platform/User/GetMembershipsForCurrentUser/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_user_get_membership_from_hard_linked_credential(client):
    """Test case for user_get_membership_from_hard_linked_credential

    
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/Platform/User/GetMembershipFromHardLinkedCredential/{cr_type}/{credential}'.format(credential='credential_example', cr_type=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_user_get_sanitized_platform_display_names(client):
    """Test case for user_get_sanitized_platform_display_names

    
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/Platform/User/GetSanitizedPlatformDisplayNames/{membership_id}'.format(membership_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_user_search_by_global_name_post(client):
    """Test case for user_search_by_global_name_post

    
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='POST',
        path='/Platform/User/Search/GlobalName/{page}'.format(page=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_user_search_by_global_name_prefix(client):
    """Test case for user_search_by_global_name_prefix

    
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/Platform/User/Search/Prefix/{display_name_prefix}/{page}'.format(display_name_prefix='display_name_prefix_example', page=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

