# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.feature import Feature
from openapi_server.models.fleet import Fleet
from openapi_server.models.generate_connect_manifest_response import GenerateConnectManifestResponse
from openapi_server.models.list_features_response import ListFeaturesResponse
from openapi_server.models.list_fleets_response import ListFleetsResponse
from openapi_server.models.list_locations_response import ListLocationsResponse
from openapi_server.models.list_membership_bindings_response import ListMembershipBindingsResponse
from openapi_server.models.list_memberships_response import ListMembershipsResponse
from openapi_server.models.list_operations_response import ListOperationsResponse
from openapi_server.models.list_scope_namespaces_response import ListScopeNamespacesResponse
from openapi_server.models.list_scope_rbac_role_bindings_response import ListScopeRBACRoleBindingsResponse
from openapi_server.models.list_scopes_response import ListScopesResponse
from openapi_server.models.membership import Membership
from openapi_server.models.membership_binding import MembershipBinding
from openapi_server.models.namespace import Namespace
from openapi_server.models.operation import Operation
from openapi_server.models.policy import Policy
from openapi_server.models.rbac_role_binding import RBACRoleBinding
from openapi_server.models.scope import Scope
from openapi_server.models.set_iam_policy_request import SetIamPolicyRequest
from openapi_server.models.test_iam_permissions_request import TestIamPermissionsRequest
from openapi_server.models.test_iam_permissions_response import TestIamPermissionsResponse


pytestmark = pytest.mark.asyncio

async def test_gkehub_projects_locations_features_create(client):
    """Test case for gkehub_projects_locations_features_create

    
    """
    body = {"updateTime":"updateTime","scopeStates":{"key":{"state":{"code":"CODE_UNSPECIFIED","description":"description","updateTime":"updateTime"}}},"spec":{"fleetobservability":{"loggingConfig":{"fleetScopeLogsConfig":{"mode":"MODE_UNSPECIFIED"},"defaultConfig":{"mode":"MODE_UNSPECIFIED"}}},"dataplanev2":{"enableEncryption":True},"multiclusteringress":{"configMembership":"configMembership"},"clusterupgrade":{"upstreamFleets":["upstreamFleets","upstreamFleets"],"postConditions":{"soaking":"soaking"},"gkeUpgradeOverrides":[{"postConditions":{"soaking":"soaking"},"upgrade":{"name":"name","version":"version"}},{"postConditions":{"soaking":"soaking"},"upgrade":{"name":"name","version":"version"}}]},"appdevexperience":"{}"},"labels":{"key":"labels"},"membershipSpecs":{"key":{"fleetobservability":"{}","configmanagement":{"policyController":{"logDeniesEnabled":True,"mutationEnabled":True,"auditIntervalSeconds":"auditIntervalSeconds","templateLibraryInstalled":True,"updateTime":"updateTime","exemptableNamespaces":["exemptableNamespaces","exemptableNamespaces"],"monitoring":{"backends":["MONITORING_BACKEND_UNSPECIFIED","MONITORING_BACKEND_UNSPECIFIED"]},"referentialRulesEnabled":True,"enabled":True},"cluster":"cluster","configSync":{"git":{"syncRepo":"syncRepo","secretType":"secretType","syncWaitSecs":"syncWaitSecs","httpsProxy":"httpsProxy","policyDir":"policyDir","syncBranch":"syncBranch","syncRev":"syncRev","gcpServiceAccountEmail":"gcpServiceAccountEmail"},"oci":{"syncRepo":"syncRepo","secretType":"secretType","syncWaitSecs":"syncWaitSecs","policyDir":"policyDir","gcpServiceAccountEmail":"gcpServiceAccountEmail"},"metricsGcpServiceAccountEmail":"metricsGcpServiceAccountEmail","allowVerticalScale":True,"sourceFormat":"sourceFormat","enabled":True,"preventDrift":True},"management":"MANAGEMENT_UNSPECIFIED","hierarchyController":{"enablePodTreeLabels":True,"enabled":True,"enableHierarchicalResourceQuota":True},"version":"version"},"policycontroller":{"policyControllerHubConfig":{"logDeniesEnabled":True,"installSpec":"INSTALL_SPEC_UNSPECIFIED","mutationEnabled":True,"auditIntervalSeconds":"auditIntervalSeconds","constraintViolationLimit":"constraintViolationLimit","exemptableNamespaces":["exemptableNamespaces","exemptableNamespaces"],"monitoring":{"backends":["MONITORING_BACKEND_UNSPECIFIED","MONITORING_BACKEND_UNSPECIFIED"]},"deploymentConfigs":{"key":{"containerResources":{"requests":{"memory":"memory","cpu":"cpu"},"limits":{"memory":"memory","cpu":"cpu"}},"podTolerations":[{"effect":"effect","value":"value","key":"key","operator":"operator"},{"effect":"effect","value":"value","key":"key","operator":"operator"}],"replicaCount":"replicaCount","podAffinity":"AFFINITY_UNSPECIFIED","podAntiAffinity":True}},"referentialRulesEnabled":True,"policyContent":{"templateLibrary":{"installation":"INSTALLATION_UNSPECIFIED"},"bundles":{"key":{"exemptedNamespaces":["exemptedNamespaces","exemptedNamespaces"]}}}},"version":"version"},"origin":{"type":"TYPE_UNSPECIFIED"},"identityservice":{"authMethods":[{"proxy":"proxy","googleConfig":{"disable":True},"oidcConfig":{"deployCloudConsoleProxy":True,"clientId":"clientId","issuerUri":"issuerUri","extraParams":"extraParams","enableAccessToken":True,"groupsClaim":"groupsClaim","groupPrefix":"groupPrefix","kubectlRedirectUri":"kubectlRedirectUri","userPrefix":"userPrefix","certificateAuthorityData":"certificateAuthorityData","clientSecret":"clientSecret","scopes":"scopes","encryptedClientSecret":"encryptedClientSecret","userClaim":"userClaim"},"name":"name","azureadConfig":{"clientId":"clientId","kubectlRedirectUri":"kubectlRedirectUri","clientSecret":"clientSecret","tenant":"tenant","encryptedClientSecret":"encryptedClientSecret"}},{"proxy":"proxy","googleConfig":{"disable":True},"oidcConfig":{"deployCloudConsoleProxy":True,"clientId":"clientId","issuerUri":"issuerUri","extraParams":"extraParams","enableAccessToken":True,"groupsClaim":"groupsClaim","groupPrefix":"groupPrefix","kubectlRedirectUri":"kubectlRedirectUri","userPrefix":"userPrefix","certificateAuthorityData":"certificateAuthorityData","clientSecret":"clientSecret","scopes":"scopes","encryptedClientSecret":"encryptedClientSecret","userClaim":"userClaim"},"name":"name","azureadConfig":{"clientId":"clientId","kubectlRedirectUri":"kubectlRedirectUri","clientSecret":"clientSecret","tenant":"tenant","encryptedClientSecret":"encryptedClientSecret"}}]},"mesh":{"controlPlane":"CONTROL_PLANE_MANAGEMENT_UNSPECIFIED","management":"MANAGEMENT_UNSPECIFIED"}}},"scopeSpecs":{"key":{}},"createTime":"createTime","deleteTime":"deleteTime","fleetDefaultMemberConfig":{"configmanagement":{"policyController":{"logDeniesEnabled":True,"mutationEnabled":True,"auditIntervalSeconds":"auditIntervalSeconds","templateLibraryInstalled":True,"updateTime":"updateTime","exemptableNamespaces":["exemptableNamespaces","exemptableNamespaces"],"monitoring":{"backends":["MONITORING_BACKEND_UNSPECIFIED","MONITORING_BACKEND_UNSPECIFIED"]},"referentialRulesEnabled":True,"enabled":True},"cluster":"cluster","configSync":{"git":{"syncRepo":"syncRepo","secretType":"secretType","syncWaitSecs":"syncWaitSecs","httpsProxy":"httpsProxy","policyDir":"policyDir","syncBranch":"syncBranch","syncRev":"syncRev","gcpServiceAccountEmail":"gcpServiceAccountEmail"},"oci":{"syncRepo":"syncRepo","secretType":"secretType","syncWaitSecs":"syncWaitSecs","policyDir":"policyDir","gcpServiceAccountEmail":"gcpServiceAccountEmail"},"metricsGcpServiceAccountEmail":"metricsGcpServiceAccountEmail","allowVerticalScale":True,"sourceFormat":"sourceFormat","enabled":True,"preventDrift":True},"management":"MANAGEMENT_UNSPECIFIED","hierarchyController":{"enablePodTreeLabels":True,"enabled":True,"enableHierarchicalResourceQuota":True},"version":"version"},"policycontroller":{"policyControllerHubConfig":{"logDeniesEnabled":True,"installSpec":"INSTALL_SPEC_UNSPECIFIED","mutationEnabled":True,"auditIntervalSeconds":"auditIntervalSeconds","constraintViolationLimit":"constraintViolationLimit","exemptableNamespaces":["exemptableNamespaces","exemptableNamespaces"],"monitoring":{"backends":["MONITORING_BACKEND_UNSPECIFIED","MONITORING_BACKEND_UNSPECIFIED"]},"deploymentConfigs":{"key":{"containerResources":{"requests":{"memory":"memory","cpu":"cpu"},"limits":{"memory":"memory","cpu":"cpu"}},"podTolerations":[{"effect":"effect","value":"value","key":"key","operator":"operator"},{"effect":"effect","value":"value","key":"key","operator":"operator"}],"replicaCount":"replicaCount","podAffinity":"AFFINITY_UNSPECIFIED","podAntiAffinity":True}},"referentialRulesEnabled":True,"policyContent":{"templateLibrary":{"installation":"INSTALLATION_UNSPECIFIED"},"bundles":{"key":{"exemptedNamespaces":["exemptedNamespaces","exemptedNamespaces"]}}}},"version":"version"},"identityservice":{"authMethods":[{"proxy":"proxy","googleConfig":{"disable":True},"oidcConfig":{"deployCloudConsoleProxy":True,"clientId":"clientId","issuerUri":"issuerUri","extraParams":"extraParams","enableAccessToken":True,"groupsClaim":"groupsClaim","groupPrefix":"groupPrefix","kubectlRedirectUri":"kubectlRedirectUri","userPrefix":"userPrefix","certificateAuthorityData":"certificateAuthorityData","clientSecret":"clientSecret","scopes":"scopes","encryptedClientSecret":"encryptedClientSecret","userClaim":"userClaim"},"name":"name","azureadConfig":{"clientId":"clientId","kubectlRedirectUri":"kubectlRedirectUri","clientSecret":"clientSecret","tenant":"tenant","encryptedClientSecret":"encryptedClientSecret"}},{"proxy":"proxy","googleConfig":{"disable":True},"oidcConfig":{"deployCloudConsoleProxy":True,"clientId":"clientId","issuerUri":"issuerUri","extraParams":"extraParams","enableAccessToken":True,"groupsClaim":"groupsClaim","groupPrefix":"groupPrefix","kubectlRedirectUri":"kubectlRedirectUri","userPrefix":"userPrefix","certificateAuthorityData":"certificateAuthorityData","clientSecret":"clientSecret","scopes":"scopes","encryptedClientSecret":"encryptedClientSecret","userClaim":"userClaim"},"name":"name","azureadConfig":{"clientId":"clientId","kubectlRedirectUri":"kubectlRedirectUri","clientSecret":"clientSecret","tenant":"tenant","encryptedClientSecret":"encryptedClientSecret"}}]},"mesh":{"controlPlane":"CONTROL_PLANE_MANAGEMENT_UNSPECIFIED","management":"MANAGEMENT_UNSPECIFIED"}},"name":"name","resourceState":{"state":"STATE_UNSPECIFIED"},"state":{"fleetobservability":{"logging":{"defaultLog":{"code":"CODE_UNSPECIFIED","errors":[{"code":"code","description":"description"},{"code":"code","description":"description"}]},"scopeLog":{"code":"CODE_UNSPECIFIED","errors":[{"code":"code","description":"description"},{"code":"code","description":"description"}]}},"monitoring":{"state":{"code":"CODE_UNSPECIFIED","errors":[{"code":"code","description":"description"},{"code":"code","description":"description"}]}}},"state":{"code":"CODE_UNSPECIFIED","description":"description","updateTime":"updateTime"},"clusterupgrade":{"ignored":{"key":{"reason":"reason","ignoredTime":"ignoredTime"}},"downstreamFleets":["downstreamFleets","downstreamFleets"],"gkeState":{"upgradeState":[{"upgrade":{"name":"name","version":"version"},"stats":{"key":"stats"},"status":{"reason":"reason","code":"CODE_UNSPECIFIED","updateTime":"updateTime"}},{"upgrade":{"name":"name","version":"version"},"stats":{"key":"stats"},"status":{"reason":"reason","code":"CODE_UNSPECIFIED","updateTime":"updateTime"}}],"conditions":[{"reason":"reason","updateTime":"updateTime","type":"type","status":"status"},{"reason":"reason","updateTime":"updateTime","type":"type","status":"status"}]}},"appdevexperience":{"networkingInstallSucceeded":{"code":"CODE_UNSPECIFIED","description":"description"}}},"membershipStates":{"key":{"fleetobservability":"{}","configmanagement":{"hierarchyControllerState":{"state":{"extension":"DEPLOYMENT_STATE_UNSPECIFIED","hnc":"DEPLOYMENT_STATE_UNSPECIFIED"},"version":{"extension":"extension","hnc":"hnc"}},"membershipSpec":{"policyController":{"logDeniesEnabled":True,"mutationEnabled":True,"auditIntervalSeconds":"auditIntervalSeconds","templateLibraryInstalled":True,"updateTime":"updateTime","exemptableNamespaces":["exemptableNamespaces","exemptableNamespaces"],"monitoring":{"backends":["MONITORING_BACKEND_UNSPECIFIED","MONITORING_BACKEND_UNSPECIFIED"]},"referentialRulesEnabled":True,"enabled":True},"cluster":"cluster","configSync":{"git":{"syncRepo":"syncRepo","secretType":"secretType","syncWaitSecs":"syncWaitSecs","httpsProxy":"httpsProxy","policyDir":"policyDir","syncBranch":"syncBranch","syncRev":"syncRev","gcpServiceAccountEmail":"gcpServiceAccountEmail"},"oci":{"syncRepo":"syncRepo","secretType":"secretType","syncWaitSecs":"syncWaitSecs","policyDir":"policyDir","gcpServiceAccountEmail":"gcpServiceAccountEmail"},"metricsGcpServiceAccountEmail":"metricsGcpServiceAccountEmail","allowVerticalScale":True,"sourceFormat":"sourceFormat","enabled":True,"preventDrift":True},"management":"MANAGEMENT_UNSPECIFIED","hierarchyController":{"enablePodTreeLabels":True,"enabled":True,"enableHierarchicalResourceQuota":True},"version":"version"},"configSyncState":{"deploymentState":{"importer":"DEPLOYMENT_STATE_UNSPECIFIED","syncer":"DEPLOYMENT_STATE_UNSPECIFIED","rootReconciler":"DEPLOYMENT_STATE_UNSPECIFIED","admissionWebhook":"DEPLOYMENT_STATE_UNSPECIFIED","gitSync":"DEPLOYMENT_STATE_UNSPECIFIED","monitor":"DEPLOYMENT_STATE_UNSPECIFIED","reconcilerManager":"DEPLOYMENT_STATE_UNSPECIFIED"},"syncState":{"code":"SYNC_CODE_UNSPECIFIED","lastSync":"lastSync","lastSyncTime":"lastSyncTime","syncToken":"syncToken","importToken":"importToken","sourceToken":"sourceToken","errors":[{"code":"code","errorMessage":"errorMessage","errorResources":[{"resourceNamespace":"resourceNamespace","resourceName":"resourceName","resourceGvk":{"kind":"kind","version":"version","group":"group"},"sourcePath":"sourcePath"},{"resourceNamespace":"resourceNamespace","resourceName":"resourceName","resourceGvk":{"kind":"kind","version":"version","group":"group"},"sourcePath":"sourcePath"}]},{"code":"code","errorMessage":"errorMessage","errorResources":[{"resourceNamespace":"resourceNamespace","resourceName":"resourceName","resourceGvk":{"kind":"kind","version":"version","group":"group"},"sourcePath":"sourcePath"},{"resourceNamespace":"resourceNamespace","resourceName":"resourceName","resourceGvk":{"kind":"kind","version":"version","group":"group"},"sourcePath":"sourcePath"}]}]},"state":"STATE_UNSPECIFIED","version":{"importer":"importer","syncer":"syncer","rootReconciler":"rootReconciler","admissionWebhook":"admissionWebhook","gitSync":"gitSync","monitor":"monitor","reconcilerManager":"reconcilerManager"},"errors":[{"errorMessage":"errorMessage"},{"errorMessage":"errorMessage"}],"reposyncCrd":"CRD_STATE_UNSPECIFIED","rootsyncCrd":"CRD_STATE_UNSPECIFIED"},"policyControllerState":{"deploymentState":{"gatekeeperMutation":"DEPLOYMENT_STATE_UNSPECIFIED","gatekeeperAudit":"DEPLOYMENT_STATE_UNSPECIFIED","gatekeeperControllerManagerState":"DEPLOYMENT_STATE_UNSPECIFIED"},"migration":{"stage":"STAGE_UNSPECIFIED","copyTime":"copyTime"},"version":{"version":"version"}},"clusterName":"clusterName","operatorState":{"deploymentState":"DEPLOYMENT_STATE_UNSPECIFIED","version":"version","errors":[{"errorMessage":"errorMessage"},{"errorMessage":"errorMessage"}]}},"policycontroller":{"policyContentState":{"referentialSyncConfigState":{"details":"details","state":"LIFECYCLE_STATE_UNSPECIFIED"},"templateLibraryState":{"details":"details","state":"LIFECYCLE_STATE_UNSPECIFIED"},"bundleStates":{"key":{"details":"details","state":"LIFECYCLE_STATE_UNSPECIFIED"}}},"componentStates":{"key":{"details":"details","state":"LIFECYCLE_STATE_UNSPECIFIED"}},"state":"LIFECYCLE_STATE_UNSPECIFIED"},"servicemesh":{"dataPlaneManagement":{"details":[{"code":"code","details":"details"},{"code":"code","details":"details"}],"state":"LIFECYCLE_STATE_UNSPECIFIED"},"controlPlaneManagement":{"details":[{"code":"code","details":"details"},{"code":"code","details":"details"}],"state":"LIFECYCLE_STATE_UNSPECIFIED"}},"identityservice":{"failureReason":"failureReason","installedVersion":"installedVersion","memberConfig":{"authMethods":[{"proxy":"proxy","googleConfig":{"disable":True},"oidcConfig":{"deployCloudConsoleProxy":True,"clientId":"clientId","issuerUri":"issuerUri","extraParams":"extraParams","enableAccessToken":True,"groupsClaim":"groupsClaim","groupPrefix":"groupPrefix","kubectlRedirectUri":"kubectlRedirectUri","userPrefix":"userPrefix","certificateAuthorityData":"certificateAuthorityData","clientSecret":"clientSecret","scopes":"scopes","encryptedClientSecret":"encryptedClientSecret","userClaim":"userClaim"},"name":"name","azureadConfig":{"clientId":"clientId","kubectlRedirectUri":"kubectlRedirectUri","clientSecret":"clientSecret","tenant":"tenant","encryptedClientSecret":"encryptedClientSecret"}},{"proxy":"proxy","googleConfig":{"disable":True},"oidcConfig":{"deployCloudConsoleProxy":True,"clientId":"clientId","issuerUri":"issuerUri","extraParams":"extraParams","enableAccessToken":True,"groupsClaim":"groupsClaim","groupPrefix":"groupPrefix","kubectlRedirectUri":"kubectlRedirectUri","userPrefix":"userPrefix","certificateAuthorityData":"certificateAuthorityData","clientSecret":"clientSecret","scopes":"scopes","encryptedClientSecret":"encryptedClientSecret","userClaim":"userClaim"},"name":"name","azureadConfig":{"clientId":"clientId","kubectlRedirectUri":"kubectlRedirectUri","clientSecret":"clientSecret","tenant":"tenant","encryptedClientSecret":"encryptedClientSecret"}}]},"state":"DEPLOYMENT_STATE_UNSPECIFIED"},"state":{"code":"CODE_UNSPECIFIED","description":"description","updateTime":"updateTime"},"clusterupgrade":{"ignored":{"reason":"reason","ignoredTime":"ignoredTime"},"upgrades":[{"upgrade":{"name":"name","version":"version"},"status":{"reason":"reason","code":"CODE_UNSPECIFIED","updateTime":"updateTime"}},{"upgrade":{"name":"name","version":"version"},"status":{"reason":"reason","code":"CODE_UNSPECIFIED","updateTime":"updateTime"}}]},"appdevexperience":{"networkingInstallSucceeded":{"code":"CODE_UNSPECIFIED","description":"description"}}}}}
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
                    ('featureId', 'feature_id_example'),
                    ('requestId', 'request_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{parent}/features'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_gkehub_projects_locations_features_list(client):
    """Test case for gkehub_projects_locations_features_list

    
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
                    ('filter', 'filter_example'),
                    ('orderBy', 'order_by_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{parent}/features'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_gkehub_projects_locations_fleets_create(client):
    """Test case for gkehub_projects_locations_fleets_create

    
    """
    body = {"defaultClusterConfig":{"securityPostureConfig":{"mode":"MODE_UNSPECIFIED","vulnerabilityMode":"VULNERABILITY_MODE_UNSPECIFIED"},"binaryAuthorizationConfig":{"policyBindings":[{"name":"name"},{"name":"name"}],"evaluationMode":"EVALUATION_MODE_UNSPECIFIED"}},"uid":"uid","createTime":"createTime","deleteTime":"deleteTime","displayName":"displayName","name":"name","updateTime":"updateTime","state":{"code":"CODE_UNSPECIFIED"},"labels":{"key":"labels"}}
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
        path='/v1/{parent}/fleets'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_gkehub_projects_locations_fleets_list(client):
    """Test case for gkehub_projects_locations_fleets_list

    
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
        path='/v1/{parent}/fleets'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_gkehub_projects_locations_list(client):
    """Test case for gkehub_projects_locations_list

    
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
        path='/v1/{name}/locations'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_gkehub_projects_locations_memberships_bindings_create(client):
    """Test case for gkehub_projects_locations_memberships_bindings_create

    
    """
    body = {"uid":"uid","createTime":"createTime","deleteTime":"deleteTime","scope":"scope","name":"name","updateTime":"updateTime","state":{"code":"CODE_UNSPECIFIED"},"labels":{"key":"labels"}}
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
                    ('membershipBindingId', 'membership_binding_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{parent}/bindings'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_gkehub_projects_locations_memberships_bindings_list(client):
    """Test case for gkehub_projects_locations_memberships_bindings_list

    
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
        path='/v1/{parent}/bindings'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_gkehub_projects_locations_memberships_create(client):
    """Test case for gkehub_projects_locations_memberships_create

    
    """
    body = {"description":"description","externalId":"externalId","updateTime":"updateTime","labels":{"key":"labels"},"endpoint":{"edgeCluster":{"resourceLink":"resourceLink"},"multiCloudCluster":{"clusterMissing":True,"resourceLink":"resourceLink"},"onPremCluster":{"clusterMissing":True,"clusterType":"CLUSTERTYPE_UNSPECIFIED","adminCluster":True,"resourceLink":"resourceLink"},"gkeCluster":{"clusterMissing":True,"resourceLink":"resourceLink"},"applianceCluster":{"resourceLink":"resourceLink"},"googleManaged":True,"kubernetesResource":{"membershipResources":[{"clusterScoped":True,"manifest":"manifest"},{"clusterScoped":True,"manifest":"manifest"}],"membershipCrManifest":"membershipCrManifest","connectResources":[{"clusterScoped":True,"manifest":"manifest"},{"clusterScoped":True,"manifest":"manifest"}],"resourceOptions":{"v1beta1Crd":True,"connectVersion":"connectVersion","k8sVersion":"k8sVersion"}},"kubernetesMetadata":{"memoryMb":0,"nodeProviderId":"nodeProviderId","vcpuCount":1,"nodeCount":6,"updateTime":"updateTime","kubernetesApiServerVersion":"kubernetesApiServerVersion"}},"monitoringConfig":{"kubernetesMetricsPrefix":"kubernetesMetricsPrefix","cluster":"cluster","clusterHash":"clusterHash","location":"location","projectId":"projectId"},"createTime":"createTime","deleteTime":"deleteTime","lastConnectionTime":"lastConnectionTime","authority":{"oidcJwks":"oidcJwks","workloadIdentityPool":"workloadIdentityPool","identityProvider":"identityProvider","issuer":"issuer"},"name":"name","state":{"code":"CODE_UNSPECIFIED"},"uniqueId":"uniqueId"}
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
                    ('membershipId', 'membership_id_example'),
                    ('requestId', 'request_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{parent}/memberships'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_gkehub_projects_locations_memberships_generate_connect_manifest(client):
    """Test case for gkehub_projects_locations_memberships_generate_connect_manifest

    
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
                    ('imagePullSecretContent', 'image_pull_secret_content_example'),
                    ('isUpgrade', True),
                    ('namespace', 'namespace_example'),
                    ('proxy', 'proxy_example'),
                    ('registry', 'registry_example'),
                    ('version', 'version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{namegenerate_connect_manifes}'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_gkehub_projects_locations_memberships_list(client):
    """Test case for gkehub_projects_locations_memberships_list

    
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
                    ('filter', 'filter_example'),
                    ('orderBy', 'order_by_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{parent}/memberships'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_gkehub_projects_locations_operations_cancel(client):
    """Test case for gkehub_projects_locations_operations_cancel

    
    """
    body = None
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
        path='/v1/{namecance}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_gkehub_projects_locations_operations_list(client):
    """Test case for gkehub_projects_locations_operations_list

    
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
        path='/v1/{name}/operations'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_gkehub_projects_locations_scopes_create(client):
    """Test case for gkehub_projects_locations_scopes_create

    
    """
    body = {"namespaceLabels":{"key":"namespaceLabels"},"uid":"uid","createTime":"createTime","deleteTime":"deleteTime","name":"name","updateTime":"updateTime","state":{"code":"CODE_UNSPECIFIED"},"labels":{"key":"labels"}}
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
                    ('scopeId', 'scope_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{parent}/scopes'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_gkehub_projects_locations_scopes_get_iam_policy(client):
    """Test case for gkehub_projects_locations_scopes_get_iam_policy

    
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
                    ('options.requestedPolicyVersion', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{resourceget_iam_polic}'.format(resource='resource_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_gkehub_projects_locations_scopes_list(client):
    """Test case for gkehub_projects_locations_scopes_list

    
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
        path='/v1/{parent}/scopes'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_gkehub_projects_locations_scopes_namespaces_create(client):
    """Test case for gkehub_projects_locations_scopes_namespaces_create

    
    """
    body = {"namespaceLabels":{"key":"namespaceLabels"},"uid":"uid","createTime":"createTime","deleteTime":"deleteTime","scope":"scope","name":"name","updateTime":"updateTime","state":{"code":"CODE_UNSPECIFIED"},"labels":{"key":"labels"}}
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
                    ('scopeNamespaceId', 'scope_namespace_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{parent}/namespaces'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_gkehub_projects_locations_scopes_namespaces_list(client):
    """Test case for gkehub_projects_locations_scopes_namespaces_list

    
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
        path='/v1/{parent}/namespaces'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_gkehub_projects_locations_scopes_rbacrolebindings_create(client):
    """Test case for gkehub_projects_locations_scopes_rbacrolebindings_create

    
    """
    body = {"uid":"uid","role":{"predefinedRole":"UNKNOWN"},"createTime":"createTime","deleteTime":"deleteTime","name":"name","updateTime":"updateTime","state":{"code":"CODE_UNSPECIFIED"},"user":"user","group":"group","labels":{"key":"labels"}}
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
                    ('rbacrolebindingId', 'rbacrolebinding_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{parent}/rbacrolebindings'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_gkehub_projects_locations_scopes_rbacrolebindings_delete(client):
    """Test case for gkehub_projects_locations_scopes_rbacrolebindings_delete

    
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
                    ('force', True),
                    ('requestId', 'request_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/{name}'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_gkehub_projects_locations_scopes_rbacrolebindings_get(client):
    """Test case for gkehub_projects_locations_scopes_rbacrolebindings_get

    
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
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{name}'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_gkehub_projects_locations_scopes_rbacrolebindings_list(client):
    """Test case for gkehub_projects_locations_scopes_rbacrolebindings_list

    
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
        path='/v1/{parent}/rbacrolebindings'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_gkehub_projects_locations_scopes_rbacrolebindings_patch(client):
    """Test case for gkehub_projects_locations_scopes_rbacrolebindings_patch

    
    """
    body = {"uid":"uid","role":{"predefinedRole":"UNKNOWN"},"createTime":"createTime","deleteTime":"deleteTime","name":"name","updateTime":"updateTime","state":{"code":"CODE_UNSPECIFIED"},"user":"user","group":"group","labels":{"key":"labels"}}
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
                    ('updateMask', 'update_mask_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v1/{name}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_gkehub_projects_locations_scopes_set_iam_policy(client):
    """Test case for gkehub_projects_locations_scopes_set_iam_policy

    
    """
    body = {"updateMask":"updateMask","policy":{"bindings":[{"condition":{"expression":"expression","description":"description","location":"location","title":"title"},"role":"role","members":["members","members"]},{"condition":{"expression":"expression","description":"description","location":"location","title":"title"},"role":"role","members":["members","members"]}],"etag":"etag","version":0,"auditConfigs":[{"auditLogConfigs":[{"logType":"LOG_TYPE_UNSPECIFIED","exemptedMembers":["exemptedMembers","exemptedMembers"]},{"logType":"LOG_TYPE_UNSPECIFIED","exemptedMembers":["exemptedMembers","exemptedMembers"]}],"service":"service"},{"auditLogConfigs":[{"logType":"LOG_TYPE_UNSPECIFIED","exemptedMembers":["exemptedMembers","exemptedMembers"]},{"logType":"LOG_TYPE_UNSPECIFIED","exemptedMembers":["exemptedMembers","exemptedMembers"]}],"service":"service"}]}}
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
        path='/v1/{resourceset_iam_polic}'.format(resource='resource_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_gkehub_projects_locations_scopes_test_iam_permissions(client):
    """Test case for gkehub_projects_locations_scopes_test_iam_permissions

    
    """
    body = {"permissions":["permissions","permissions"]}
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
        path='/v1/{resourcetest_iam_permission}'.format(resource='resource_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

