# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.analyze_iam_policy_longrunning_request import AnalyzeIamPolicyLongrunningRequest
from openapi_server.models.analyze_iam_policy_response import AnalyzeIamPolicyResponse
from openapi_server.models.analyze_move_response import AnalyzeMoveResponse
from openapi_server.models.analyze_org_policies_response import AnalyzeOrgPoliciesResponse
from openapi_server.models.analyze_org_policy_governed_assets_response import AnalyzeOrgPolicyGovernedAssetsResponse
from openapi_server.models.analyze_org_policy_governed_containers_response import AnalyzeOrgPolicyGovernedContainersResponse
from openapi_server.models.batch_get_assets_history_response import BatchGetAssetsHistoryResponse
from openapi_server.models.export_assets_request import ExportAssetsRequest
from openapi_server.models.operation import Operation
from openapi_server.models.query_assets_request import QueryAssetsRequest
from openapi_server.models.query_assets_response import QueryAssetsResponse
from openapi_server.models.search_all_iam_policies_response import SearchAllIamPoliciesResponse
from openapi_server.models.search_all_resources_response import SearchAllResourcesResponse


pytestmark = pytest.mark.asyncio

async def test_cloudasset_analyze_iam_policy(client):
    """Test case for cloudasset_analyze_iam_policy

    
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
                    ('analysisQuery.accessSelector.permissions', ['analysis_query_access_selector_permissions_example']),
                    ('analysisQuery.accessSelector.roles', ['analysis_query_access_selector_roles_example']),
                    ('analysisQuery.conditionContext.accessTime', 'analysis_query_condition_context_access_time_example'),
                    ('analysisQuery.identitySelector.identity', 'analysis_query_identity_selector_identity_example'),
                    ('analysisQuery.options.analyzeServiceAccountImpersonation', True),
                    ('analysisQuery.options.expandGroups', True),
                    ('analysisQuery.options.expandResources', True),
                    ('analysisQuery.options.expandRoles', True),
                    ('analysisQuery.options.outputGroupEdges', True),
                    ('analysisQuery.options.outputResourceEdges', True),
                    ('analysisQuery.resourceSelector.fullResourceName', 'analysis_query_resource_selector_full_resource_name_example'),
                    ('executionTimeout', 'execution_timeout_example'),
                    ('savedAnalysisQuery', 'saved_analysis_query_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{scopeanalyze_iam_polic}'.format(scope='scope_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cloudasset_analyze_iam_policy_longrunning(client):
    """Test case for cloudasset_analyze_iam_policy_longrunning

    
    """
    body = {"outputConfig":{"gcsDestination":{"uri":"uri"},"bigqueryDestination":{"partitionKey":"PARTITION_KEY_UNSPECIFIED","tablePrefix":"tablePrefix","writeDisposition":"writeDisposition","dataset":"dataset"}},"analysisQuery":{"conditionContext":{"accessTime":"accessTime"},"scope":"scope","options":{"expandRoles":True,"outputGroupEdges":True,"expandGroups":True,"expandResources":True,"outputResourceEdges":True,"analyzeServiceAccountImpersonation":True},"resourceSelector":{"fullResourceName":"fullResourceName"},"accessSelector":{"permissions":["permissions","permissions"],"roles":["roles","roles"]},"identitySelector":{"identity":"identity"}},"savedAnalysisQuery":"savedAnalysisQuery"}
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
        path='/v1/{scopeanalyze_iam_policy_longrunnin}'.format(scope='scope_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cloudasset_analyze_move(client):
    """Test case for cloudasset_analyze_move

    
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
                    ('destinationParent', 'destination_parent_example'),
                    ('view', 'view_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{resourceanalyze_mov}'.format(resource='resource_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cloudasset_analyze_org_policies(client):
    """Test case for cloudasset_analyze_org_policies

    
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
                    ('constraint', 'constraint_example'),
                    ('filter', 'filter_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{scopeanalyze_org_policie}'.format(scope='scope_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cloudasset_analyze_org_policy_governed_assets(client):
    """Test case for cloudasset_analyze_org_policy_governed_assets

    
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
                    ('constraint', 'constraint_example'),
                    ('filter', 'filter_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{scopeanalyze_org_policy_governed_asset}'.format(scope='scope_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cloudasset_analyze_org_policy_governed_containers(client):
    """Test case for cloudasset_analyze_org_policy_governed_containers

    
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
                    ('constraint', 'constraint_example'),
                    ('filter', 'filter_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{scopeanalyze_org_policy_governed_container}'.format(scope='scope_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cloudasset_batch_get_assets_history(client):
    """Test case for cloudasset_batch_get_assets_history

    
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
                    ('assetNames', ['asset_names_example']),
                    ('contentType', 'content_type_example'),
                    ('readTimeWindow.endTime', 'read_time_window_end_time_example'),
                    ('readTimeWindow.startTime', 'read_time_window_start_time_example'),
                    ('relationshipTypes', ['relationship_types_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{parentbatch_get_assets_histor}'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cloudasset_export_assets(client):
    """Test case for cloudasset_export_assets

    
    """
    body = {"assetTypes":["assetTypes","assetTypes"],"outputConfig":{"gcsDestination":{"uriPrefix":"uriPrefix","uri":"uri"},"bigqueryDestination":{"separateTablesPerAssetType":True,"force":True,"dataset":"dataset","partitionSpec":{"partitionKey":"PARTITION_KEY_UNSPECIFIED"},"table":"table"}},"readTime":"readTime","relationshipTypes":["relationshipTypes","relationshipTypes"],"contentType":"CONTENT_TYPE_UNSPECIFIED"}
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
        path='/v1/{parentexport_asset}'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cloudasset_query_assets(client):
    """Test case for cloudasset_query_assets

    
    """
    body = {"outputConfig":{"bigqueryDestination":{"writeDisposition":"writeDisposition","dataset":"dataset","table":"table"}},"readTimeWindow":{"startTime":"startTime","endTime":"endTime"},"statement":"statement","pageSize":0,"readTime":"readTime","pageToken":"pageToken","jobReference":"jobReference","timeout":"timeout"}
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
        path='/v1/{parentquery_asset}'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cloudasset_search_all_iam_policies(client):
    """Test case for cloudasset_search_all_iam_policies

    
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
                    ('assetTypes', ['asset_types_example']),
                    ('orderBy', 'order_by_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example'),
                    ('query', 'query_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{scopesearch_all_iam_policie}'.format(scope='scope_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cloudasset_search_all_resources(client):
    """Test case for cloudasset_search_all_resources

    
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
                    ('assetTypes', ['asset_types_example']),
                    ('orderBy', 'order_by_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example'),
                    ('query', 'query_example'),
                    ('readMask', 'read_mask_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{scopesearch_all_resource}'.format(scope='scope_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

