# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.google_cloud_policysimulator_v1_list_org_policy_violations_previews_response import GoogleCloudPolicysimulatorV1ListOrgPolicyViolationsPreviewsResponse
from openapi_server.models.google_cloud_policysimulator_v1_list_org_policy_violations_response import GoogleCloudPolicysimulatorV1ListOrgPolicyViolationsResponse
from openapi_server.models.google_cloud_policysimulator_v1_org_policy_violations_preview import GoogleCloudPolicysimulatorV1OrgPolicyViolationsPreview
from openapi_server.models.google_longrunning_operation import GoogleLongrunningOperation


pytestmark = pytest.mark.asyncio

async def test_policysimulator_organizations_locations_org_policy_violations_previews_create(client):
    """Test case for policysimulator_organizations_locations_org_policy_violations_previews_create

    
    """
    body = {"overlay":{"customConstraints":[{"customConstraintParent":"customConstraintParent","customConstraint":{"actionType":"ACTION_TYPE_UNSPECIFIED","resourceTypes":["resourceTypes","resourceTypes"],"condition":"condition","displayName":"displayName","name":"name","description":"description","updateTime":"updateTime","methodTypes":["METHOD_TYPE_UNSPECIFIED","METHOD_TYPE_UNSPECIFIED"]}},{"customConstraintParent":"customConstraintParent","customConstraint":{"actionType":"ACTION_TYPE_UNSPECIFIED","resourceTypes":["resourceTypes","resourceTypes"],"condition":"condition","displayName":"displayName","name":"name","description":"description","updateTime":"updateTime","methodTypes":["METHOD_TYPE_UNSPECIFIED","METHOD_TYPE_UNSPECIFIED"]}}],"policies":[{"policyParent":"policyParent","policy":{"dryRunSpec":{"inheritFromParent":True,"reset":True,"etag":"etag","rules":[{"condition":{"expression":"expression","description":"description","location":"location","title":"title"},"values":{"allowedValues":["allowedValues","allowedValues"],"deniedValues":["deniedValues","deniedValues"]},"allowAll":True,"enforce":True,"denyAll":True},{"condition":{"expression":"expression","description":"description","location":"location","title":"title"},"values":{"allowedValues":["allowedValues","allowedValues"],"deniedValues":["deniedValues","deniedValues"]},"allowAll":True,"enforce":True,"denyAll":True}],"updateTime":"updateTime"},"name":"name","alternate":{"launch":"launch","spec":{"inheritFromParent":True,"reset":True,"etag":"etag","rules":[{"condition":{"expression":"expression","description":"description","location":"location","title":"title"},"values":{"allowedValues":["allowedValues","allowedValues"],"deniedValues":["deniedValues","deniedValues"]},"allowAll":True,"enforce":True,"denyAll":True},{"condition":{"expression":"expression","description":"description","location":"location","title":"title"},"values":{"allowedValues":["allowedValues","allowedValues"],"deniedValues":["deniedValues","deniedValues"]},"allowAll":True,"enforce":True,"denyAll":True}],"updateTime":"updateTime"}},"etag":"etag","spec":{"inheritFromParent":True,"reset":True,"etag":"etag","rules":[{"condition":{"expression":"expression","description":"description","location":"location","title":"title"},"values":{"allowedValues":["allowedValues","allowedValues"],"deniedValues":["deniedValues","deniedValues"]},"allowAll":True,"enforce":True,"denyAll":True},{"condition":{"expression":"expression","description":"description","location":"location","title":"title"},"values":{"allowedValues":["allowedValues","allowedValues"],"deniedValues":["deniedValues","deniedValues"]},"allowAll":True,"enforce":True,"denyAll":True}],"updateTime":"updateTime"}}},{"policyParent":"policyParent","policy":{"dryRunSpec":{"inheritFromParent":True,"reset":True,"etag":"etag","rules":[{"condition":{"expression":"expression","description":"description","location":"location","title":"title"},"values":{"allowedValues":["allowedValues","allowedValues"],"deniedValues":["deniedValues","deniedValues"]},"allowAll":True,"enforce":True,"denyAll":True},{"condition":{"expression":"expression","description":"description","location":"location","title":"title"},"values":{"allowedValues":["allowedValues","allowedValues"],"deniedValues":["deniedValues","deniedValues"]},"allowAll":True,"enforce":True,"denyAll":True}],"updateTime":"updateTime"},"name":"name","alternate":{"launch":"launch","spec":{"inheritFromParent":True,"reset":True,"etag":"etag","rules":[{"condition":{"expression":"expression","description":"description","location":"location","title":"title"},"values":{"allowedValues":["allowedValues","allowedValues"],"deniedValues":["deniedValues","deniedValues"]},"allowAll":True,"enforce":True,"denyAll":True},{"condition":{"expression":"expression","description":"description","location":"location","title":"title"},"values":{"allowedValues":["allowedValues","allowedValues"],"deniedValues":["deniedValues","deniedValues"]},"allowAll":True,"enforce":True,"denyAll":True}],"updateTime":"updateTime"}},"etag":"etag","spec":{"inheritFromParent":True,"reset":True,"etag":"etag","rules":[{"condition":{"expression":"expression","description":"description","location":"location","title":"title"},"values":{"allowedValues":["allowedValues","allowedValues"],"deniedValues":["deniedValues","deniedValues"]},"allowAll":True,"enforce":True,"denyAll":True},{"condition":{"expression":"expression","description":"description","location":"location","title":"title"},"values":{"allowedValues":["allowedValues","allowedValues"],"deniedValues":["deniedValues","deniedValues"]},"allowAll":True,"enforce":True,"denyAll":True}],"updateTime":"updateTime"}}}]},"createTime":"createTime","resourceCounts":{"noncompliant":1,"scanned":5,"unenforced":5,"compliant":0,"errors":6},"customConstraints":["customConstraints","customConstraints"],"name":"name","state":"PREVIEW_STATE_UNSPECIFIED","violationsCount":2}
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
                    ('orgPolicyViolationsPreviewId', 'org_policy_violations_preview_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{parent}/orgPolicyViolationsPreviews'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_policysimulator_organizations_locations_org_policy_violations_previews_list(client):
    """Test case for policysimulator_organizations_locations_org_policy_violations_previews_list

    
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
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{parent}/orgPolicyViolationsPreviews'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_policysimulator_organizations_locations_org_policy_violations_previews_org_policy_violations_list(client):
    """Test case for policysimulator_organizations_locations_org_policy_violations_previews_org_policy_violations_list

    
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
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{parent}/orgPolicyViolations'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

