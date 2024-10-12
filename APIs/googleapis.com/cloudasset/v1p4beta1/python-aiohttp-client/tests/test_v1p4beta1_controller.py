# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.analyze_iam_policy_response import AnalyzeIamPolicyResponse
from openapi_server.models.export_iam_policy_analysis_request import ExportIamPolicyAnalysisRequest
from openapi_server.models.operation import Operation


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
                    ('analysisQuery.identitySelector.identity', 'analysis_query_identity_selector_identity_example'),
                    ('analysisQuery.resourceSelector.fullResourceName', 'analysis_query_resource_selector_full_resource_name_example'),
                    ('options.analyzeServiceAccountImpersonation', True),
                    ('options.executionTimeout', 'options_execution_timeout_example'),
                    ('options.expandGroups', True),
                    ('options.expandResources', True),
                    ('options.expandRoles', True),
                    ('options.outputGroupEdges', True),
                    ('options.outputResourceEdges', True)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1p4beta1/{parentanalyze_iam_polic}'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cloudasset_export_iam_policy_analysis(client):
    """Test case for cloudasset_export_iam_policy_analysis

    
    """
    body = {"outputConfig":{"gcsDestination":{"uri":"uri"}},"options":{"expandRoles":True,"outputGroupEdges":True,"expandGroups":True,"expandResources":True,"outputResourceEdges":True,"analyzeServiceAccountImpersonation":True},"analysisQuery":{"parent":"parent","resourceSelector":{"fullResourceName":"fullResourceName"},"accessSelector":{"permissions":["permissions","permissions"],"roles":["roles","roles"]},"identitySelector":{"identity":"identity"}}}
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
        path='/v1p4beta1/{parentexport_iam_policy_analysi}'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

