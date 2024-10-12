# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.google_cloud_apigee_v1_provision_organization_request import GoogleCloudApigeeV1ProvisionOrganizationRequest
from openapi_server.models.google_longrunning_operation import GoogleLongrunningOperation


pytestmark = pytest.mark.asyncio

async def test_apigee_projects_provision_organization(client):
    """Test case for apigee_projects_provision_organization

    
    """
    body = {"disableVpcPeering":True,"authorizedNetwork":"authorizedNetwork","runtimeLocation":"runtimeLocation","analyticsRegion":"analyticsRegion"}
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
        path='/v1/{projectprovision_organizatio}'.format(project='project_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

