# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.check_access_response import CheckAccessResponse
from openapi_server.models.list_item_names_for_unmapped_identity_response import ListItemNamesForUnmappedIdentityResponse
from openapi_server.models.list_unmapped_identities_response import ListUnmappedIdentitiesResponse
from openapi_server.models.principal import Principal
from openapi_server.models.search_items_by_view_url_request import SearchItemsByViewUrlRequest
from openapi_server.models.search_items_by_view_url_response import SearchItemsByViewUrlResponse


pytestmark = pytest.mark.asyncio

async def test_cloudsearch_debug_datasources_items_check_access(client):
    """Test case for cloudsearch_debug_datasources_items_check_access

    
    """
    body = {"groupResourceName":"groupResourceName","userResourceName":"userResourceName","gsuitePrincipal":{"gsuiteGroupEmail":"gsuiteGroupEmail","gsuiteDomain":True,"gsuiteUserEmail":"gsuiteUserEmail"}}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('debugOptions.enableDebugging', True)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/debug/{namecheck_acces}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cloudsearch_debug_datasources_items_search_by_view_url(client):
    """Test case for cloudsearch_debug_datasources_items_search_by_view_url

    
    """
    body = {"debugOptions":{"enableDebugging":True},"viewUrl":"viewUrl","pageToken":"pageToken"}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/debug/{name}/items:searchByViewUrl'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cloudsearch_debug_identitysources_items_list_forunmappedidentity(client):
    """Test case for cloudsearch_debug_identitysources_items_list_forunmappedidentity

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('debugOptions.enableDebugging', True),
                    ('groupResourceName', 'group_resource_name_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example'),
                    ('userResourceName', 'user_resource_name_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/debug/{parent}/items:forunmappedidentity'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cloudsearch_debug_identitysources_unmappedids_list(client):
    """Test case for cloudsearch_debug_identitysources_unmappedids_list

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('debugOptions.enableDebugging', True),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example'),
                    ('resolutionStatusCode', 'resolution_status_code_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/debug/{parent}/unmappedids'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

