# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.generate_config_report_request import GenerateConfigReportRequest
from openapi_server.models.generate_config_report_response import GenerateConfigReportResponse
from openapi_server.models.get_iam_policy_request import GetIamPolicyRequest
from openapi_server.models.list_service_configs_response import ListServiceConfigsResponse
from openapi_server.models.list_service_rollouts_response import ListServiceRolloutsResponse
from openapi_server.models.list_services_response import ListServicesResponse
from openapi_server.models.managed_service import ManagedService
from openapi_server.models.operation import Operation
from openapi_server.models.policy import Policy
from openapi_server.models.rollout import Rollout
from openapi_server.models.service import Service
from openapi_server.models.set_iam_policy_request import SetIamPolicyRequest
from openapi_server.models.submit_config_source_request import SubmitConfigSourceRequest
from openapi_server.models.test_iam_permissions_request import TestIamPermissionsRequest
from openapi_server.models.test_iam_permissions_response import TestIamPermissionsResponse


pytestmark = pytest.mark.asyncio

async def test_servicemanagement_services_configs_create(client):
    """Test case for servicemanagement_services_configs_create

    
    """
    body = {"usage":{"requirements":["requirements","requirements"],"producerNotificationChannel":"producerNotificationChannel","rules":[{"skipServiceControl":True,"allowUnregisteredCalls":True,"selector":"selector"},{"skipServiceControl":True,"allowUnregisteredCalls":True,"selector":"selector"}]},"producerProjectId":"producerProjectId","customError":{"types":["types","types"],"rules":[{"isErrorType":True,"selector":"selector"},{"isErrorType":True,"selector":"selector"}]},"title":"title","billing":{"consumerDestinations":[{"metrics":["metrics","metrics"],"monitoredResource":"monitoredResource"},{"metrics":["metrics","metrics"],"monitoredResource":"monitoredResource"}]},"enums":[{"enumvalue":[{"number":5,"name":"name","options":[{"name":"name","value":{"key":""}},{"name":"name","value":{"key":""}}]},{"number":5,"name":"name","options":[{"name":"name","value":{"key":""}},{"name":"name","value":{"key":""}}]}],"name":"name","options":[{"name":"name","value":{"key":""}},{"name":"name","value":{"key":""}}],"edition":"edition","syntax":"SYNTAX_PROTO2","sourceContext":{"fileName":"fileName"}},{"enumvalue":[{"number":5,"name":"name","options":[{"name":"name","value":{"key":""}},{"name":"name","value":{"key":""}}]},{"number":5,"name":"name","options":[{"name":"name","value":{"key":""}},{"name":"name","value":{"key":""}}]}],"name":"name","options":[{"name":"name","value":{"key":""}},{"name":"name","value":{"key":""}}],"edition":"edition","syntax":"SYNTAX_PROTO2","sourceContext":{"fileName":"fileName"}}],"sourceInfo":{"sourceFiles":[{"key":""},{"key":""}]},"quota":{"metricRules":[{"metricCosts":{"key":"metricCosts"},"selector":"selector"},{"metricCosts":{"key":"metricCosts"},"selector":"selector"}],"limits":[{"duration":"duration","freeTier":"freeTier","unit":"unit","maxLimit":"maxLimit","metric":"metric","displayName":"displayName","defaultLimit":"defaultLimit","values":{"key":"values"},"name":"name","description":"description"},{"duration":"duration","freeTier":"freeTier","unit":"unit","maxLimit":"maxLimit","metric":"metric","displayName":"displayName","defaultLimit":"defaultLimit","values":{"key":"values"},"name":"name","description":"description"}]},"context":{"rules":[{"requested":["requested","requested"],"allowedResponseExtensions":["allowedResponseExtensions","allowedResponseExtensions"],"provided":["provided","provided"],"selector":"selector","allowedRequestExtensions":["allowedRequestExtensions","allowedRequestExtensions"]},{"requested":["requested","requested"],"allowedResponseExtensions":["allowedResponseExtensions","allowedResponseExtensions"],"provided":["provided","provided"],"selector":"selector","allowedRequestExtensions":["allowedRequestExtensions","allowedRequestExtensions"]}]},"backend":{"rules":[{"disableAuth":True,"jwtAudience":"jwtAudience","operationDeadline":1.4658129805029452,"protocol":"protocol","address":"address","overridesByRequestProtocol":{},"pathTranslation":"PATH_TRANSLATION_UNSPECIFIED","selector":"selector","deadline":0.8008281904610115,"minDeadline":6.027456183070403},{"disableAuth":True,"jwtAudience":"jwtAudience","operationDeadline":1.4658129805029452,"protocol":"protocol","address":"address","overridesByRequestProtocol":{},"pathTranslation":"PATH_TRANSLATION_UNSPECIFIED","selector":"selector","deadline":0.8008281904610115,"minDeadline":6.027456183070403}]},"id":"id","logs":[{"displayName":"displayName","name":"name","description":"description","labels":[{"valueType":"STRING","description":"description","key":"key"},{"valueType":"STRING","description":"description","key":"key"}]},{"displayName":"displayName","name":"name","description":"description","labels":[{"valueType":"STRING","description":"description","key":"key"},{"valueType":"STRING","description":"description","key":"key"}]}],"publishing":{"librarySettings":[{"pythonSettings":{"common":{"referenceDocsUri":"referenceDocsUri","destinations":["CLIENT_LIBRARY_DESTINATION_UNSPECIFIED","CLIENT_LIBRARY_DESTINATION_UNSPECIFIED"]}},"cppSettings":{"common":{"referenceDocsUri":"referenceDocsUri","destinations":["CLIENT_LIBRARY_DESTINATION_UNSPECIFIED","CLIENT_LIBRARY_DESTINATION_UNSPECIFIED"]}},"dotnetSettings":{"handwrittenSignatures":["handwrittenSignatures","handwrittenSignatures"],"renamedServices":{"key":"renamedServices"},"common":{"referenceDocsUri":"referenceDocsUri","destinations":["CLIENT_LIBRARY_DESTINATION_UNSPECIFIED","CLIENT_LIBRARY_DESTINATION_UNSPECIFIED"]},"renamedResources":{"key":"renamedResources"},"forcedNamespaceAliases":["forcedNamespaceAliases","forcedNamespaceAliases"],"ignoredResources":["ignoredResources","ignoredResources"]},"rubySettings":{"common":{"referenceDocsUri":"referenceDocsUri","destinations":["CLIENT_LIBRARY_DESTINATION_UNSPECIFIED","CLIENT_LIBRARY_DESTINATION_UNSPECIFIED"]}},"phpSettings":{"common":{"referenceDocsUri":"referenceDocsUri","destinations":["CLIENT_LIBRARY_DESTINATION_UNSPECIFIED","CLIENT_LIBRARY_DESTINATION_UNSPECIFIED"]}},"launchStage":"LAUNCH_STAGE_UNSPECIFIED","restNumericEnums":True,"version":"version","goSettings":{"common":{"referenceDocsUri":"referenceDocsUri","destinations":["CLIENT_LIBRARY_DESTINATION_UNSPECIFIED","CLIENT_LIBRARY_DESTINATION_UNSPECIFIED"]}},"javaSettings":{"common":{"referenceDocsUri":"referenceDocsUri","destinations":["CLIENT_LIBRARY_DESTINATION_UNSPECIFIED","CLIENT_LIBRARY_DESTINATION_UNSPECIFIED"]},"serviceClassNames":{"key":"serviceClassNames"},"libraryPackage":"libraryPackage"},"nodeSettings":{"common":{"referenceDocsUri":"referenceDocsUri","destinations":["CLIENT_LIBRARY_DESTINATION_UNSPECIFIED","CLIENT_LIBRARY_DESTINATION_UNSPECIFIED"]}}},{"pythonSettings":{"common":{"referenceDocsUri":"referenceDocsUri","destinations":["CLIENT_LIBRARY_DESTINATION_UNSPECIFIED","CLIENT_LIBRARY_DESTINATION_UNSPECIFIED"]}},"cppSettings":{"common":{"referenceDocsUri":"referenceDocsUri","destinations":["CLIENT_LIBRARY_DESTINATION_UNSPECIFIED","CLIENT_LIBRARY_DESTINATION_UNSPECIFIED"]}},"dotnetSettings":{"handwrittenSignatures":["handwrittenSignatures","handwrittenSignatures"],"renamedServices":{"key":"renamedServices"},"common":{"referenceDocsUri":"referenceDocsUri","destinations":["CLIENT_LIBRARY_DESTINATION_UNSPECIFIED","CLIENT_LIBRARY_DESTINATION_UNSPECIFIED"]},"renamedResources":{"key":"renamedResources"},"forcedNamespaceAliases":["forcedNamespaceAliases","forcedNamespaceAliases"],"ignoredResources":["ignoredResources","ignoredResources"]},"rubySettings":{"common":{"referenceDocsUri":"referenceDocsUri","destinations":["CLIENT_LIBRARY_DESTINATION_UNSPECIFIED","CLIENT_LIBRARY_DESTINATION_UNSPECIFIED"]}},"phpSettings":{"common":{"referenceDocsUri":"referenceDocsUri","destinations":["CLIENT_LIBRARY_DESTINATION_UNSPECIFIED","CLIENT_LIBRARY_DESTINATION_UNSPECIFIED"]}},"launchStage":"LAUNCH_STAGE_UNSPECIFIED","restNumericEnums":True,"version":"version","goSettings":{"common":{"referenceDocsUri":"referenceDocsUri","destinations":["CLIENT_LIBRARY_DESTINATION_UNSPECIFIED","CLIENT_LIBRARY_DESTINATION_UNSPECIFIED"]}},"javaSettings":{"common":{"referenceDocsUri":"referenceDocsUri","destinations":["CLIENT_LIBRARY_DESTINATION_UNSPECIFIED","CLIENT_LIBRARY_DESTINATION_UNSPECIFIED"]},"serviceClassNames":{"key":"serviceClassNames"},"libraryPackage":"libraryPackage"},"nodeSettings":{"common":{"referenceDocsUri":"referenceDocsUri","destinations":["CLIENT_LIBRARY_DESTINATION_UNSPECIFIED","CLIENT_LIBRARY_DESTINATION_UNSPECIFIED"]}}}],"githubLabel":"githubLabel","docTagPrefix":"docTagPrefix","apiShortName":"apiShortName","codeownerGithubTeams":["codeownerGithubTeams","codeownerGithubTeams"],"documentationUri":"documentationUri","organization":"CLIENT_LIBRARY_ORGANIZATION_UNSPECIFIED","restReferenceDocumentationUri":"restReferenceDocumentationUri","methodSettings":[{"autoPopulatedFields":["autoPopulatedFields","autoPopulatedFields"],"longRunning":{"initialPollDelay":"initialPollDelay","pollDelayMultiplier":2.302136,"maxPollDelay":"maxPollDelay","totalPollTimeout":"totalPollTimeout"},"selector":"selector"},{"autoPopulatedFields":["autoPopulatedFields","autoPopulatedFields"],"longRunning":{"initialPollDelay":"initialPollDelay","pollDelayMultiplier":2.302136,"maxPollDelay":"maxPollDelay","totalPollTimeout":"totalPollTimeout"},"selector":"selector"}],"protoReferenceDocumentationUri":"protoReferenceDocumentationUri","newIssueUri":"newIssueUri"},"authentication":{"rules":[{"requirements":[{"providerId":"providerId","audiences":"audiences"},{"providerId":"providerId","audiences":"audiences"}],"allowWithoutCredential":True,"selector":"selector","oauth":{"canonicalScopes":"canonicalScopes"}},{"requirements":[{"providerId":"providerId","audiences":"audiences"},{"providerId":"providerId","audiences":"audiences"}],"allowWithoutCredential":True,"selector":"selector","oauth":{"canonicalScopes":"canonicalScopes"}}],"providers":[{"authorizationUrl":"authorizationUrl","audiences":"audiences","jwksUri":"jwksUri","id":"id","jwtLocations":[{"cookie":"cookie","valuePrefix":"valuePrefix","query":"query","header":"header"},{"cookie":"cookie","valuePrefix":"valuePrefix","query":"query","header":"header"}],"issuer":"issuer"},{"authorizationUrl":"authorizationUrl","audiences":"audiences","jwksUri":"jwksUri","id":"id","jwtLocations":[{"cookie":"cookie","valuePrefix":"valuePrefix","query":"query","header":"header"},{"cookie":"cookie","valuePrefix":"valuePrefix","query":"query","header":"header"}],"issuer":"issuer"}]},"endpoints":[{"allowCors":True,"aliases":["aliases","aliases"],"name":"name","target":"target"},{"allowCors":True,"aliases":["aliases","aliases"],"name":"name","target":"target"}],"types":[{"oneofs":["oneofs","oneofs"],"name":"name","options":[{"name":"name","value":{"key":""}},{"name":"name","value":{"key":""}}],"edition":"edition","syntax":"SYNTAX_PROTO2","fields":[{"number":7,"typeUrl":"typeUrl","jsonName":"jsonName","oneofIndex":9,"defaultValue":"defaultValue","kind":"TYPE_UNKNOWN","name":"name","options":[{"name":"name","value":{"key":""}},{"name":"name","value":{"key":""}}],"packed":True,"cardinality":"CARDINALITY_UNKNOWN"},{"number":7,"typeUrl":"typeUrl","jsonName":"jsonName","oneofIndex":9,"defaultValue":"defaultValue","kind":"TYPE_UNKNOWN","name":"name","options":[{"name":"name","value":{"key":""}},{"name":"name","value":{"key":""}}],"packed":True,"cardinality":"CARDINALITY_UNKNOWN"}],"sourceContext":{"fileName":"fileName"}},{"oneofs":["oneofs","oneofs"],"name":"name","options":[{"name":"name","value":{"key":""}},{"name":"name","value":{"key":""}}],"edition":"edition","syntax":"SYNTAX_PROTO2","fields":[{"number":7,"typeUrl":"typeUrl","jsonName":"jsonName","oneofIndex":9,"defaultValue":"defaultValue","kind":"TYPE_UNKNOWN","name":"name","options":[{"name":"name","value":{"key":""}},{"name":"name","value":{"key":""}}],"packed":True,"cardinality":"CARDINALITY_UNKNOWN"},{"number":7,"typeUrl":"typeUrl","jsonName":"jsonName","oneofIndex":9,"defaultValue":"defaultValue","kind":"TYPE_UNKNOWN","name":"name","options":[{"name":"name","value":{"key":""}},{"name":"name","value":{"key":""}}],"packed":True,"cardinality":"CARDINALITY_UNKNOWN"}],"sourceContext":{"fileName":"fileName"}}],"configVersion":5,"systemParameters":{"rules":[{"selector":"selector","parameters":[{"httpHeader":"httpHeader","name":"name","urlQueryParameter":"urlQueryParameter"},{"httpHeader":"httpHeader","name":"name","urlQueryParameter":"urlQueryParameter"}]},{"selector":"selector","parameters":[{"httpHeader":"httpHeader","name":"name","urlQueryParameter":"urlQueryParameter"},{"httpHeader":"httpHeader","name":"name","urlQueryParameter":"urlQueryParameter"}]}]},"documentation":{"summary":"summary","overview":"overview","pages":[{"subpages":[null,null],"name":"name","content":"content"},{"subpages":[null,null],"name":"name","content":"content"}],"documentationRootUrl":"documentationRootUrl","serviceRootUrl":"serviceRootUrl","rules":[{"deprecationDescription":"deprecationDescription","description":"description","disableReplacementWords":"disableReplacementWords","selector":"selector"},{"deprecationDescription":"deprecationDescription","description":"description","disableReplacementWords":"disableReplacementWords","selector":"selector"}],"sectionOverrides":[{"subpages":[null,null],"name":"name","content":"content"},{"subpages":[null,null],"name":"name","content":"content"}]},"monitoredResources":[{"displayName":"displayName","name":"name","description":"description","launchStage":"LAUNCH_STAGE_UNSPECIFIED","type":"type","labels":[{"valueType":"STRING","description":"description","key":"key"},{"valueType":"STRING","description":"description","key":"key"}]},{"displayName":"displayName","name":"name","description":"description","launchStage":"LAUNCH_STAGE_UNSPECIFIED","type":"type","labels":[{"valueType":"STRING","description":"description","key":"key"},{"valueType":"STRING","description":"description","key":"key"}]}],"control":{"environment":"environment","methodPolicies":[{"requestPolicies":[{"selector":"selector","resourcePermission":"resourcePermission","resourceType":"resourceType"},{"selector":"selector","resourcePermission":"resourcePermission","resourceType":"resourceType"}],"selector":"selector"},{"requestPolicies":[{"selector":"selector","resourcePermission":"resourcePermission","resourceType":"resourceType"},{"selector":"selector","resourcePermission":"resourcePermission","resourceType":"resourceType"}],"selector":"selector"}]},"monitoring":{"producerDestinations":[{"metrics":["metrics","metrics"],"monitoredResource":"monitoredResource"},{"metrics":["metrics","metrics"],"monitoredResource":"monitoredResource"}],"consumerDestinations":[{"metrics":["metrics","metrics"],"monitoredResource":"monitoredResource"},{"metrics":["metrics","metrics"],"monitoredResource":"monitoredResource"}]},"systemTypes":[{"oneofs":["oneofs","oneofs"],"name":"name","options":[{"name":"name","value":{"key":""}},{"name":"name","value":{"key":""}}],"edition":"edition","syntax":"SYNTAX_PROTO2","fields":[{"number":7,"typeUrl":"typeUrl","jsonName":"jsonName","oneofIndex":9,"defaultValue":"defaultValue","kind":"TYPE_UNKNOWN","name":"name","options":[{"name":"name","value":{"key":""}},{"name":"name","value":{"key":""}}],"packed":True,"cardinality":"CARDINALITY_UNKNOWN"},{"number":7,"typeUrl":"typeUrl","jsonName":"jsonName","oneofIndex":9,"defaultValue":"defaultValue","kind":"TYPE_UNKNOWN","name":"name","options":[{"name":"name","value":{"key":""}},{"name":"name","value":{"key":""}}],"packed":True,"cardinality":"CARDINALITY_UNKNOWN"}],"sourceContext":{"fileName":"fileName"}},{"oneofs":["oneofs","oneofs"],"name":"name","options":[{"name":"name","value":{"key":""}},{"name":"name","value":{"key":""}}],"edition":"edition","syntax":"SYNTAX_PROTO2","fields":[{"number":7,"typeUrl":"typeUrl","jsonName":"jsonName","oneofIndex":9,"defaultValue":"defaultValue","kind":"TYPE_UNKNOWN","name":"name","options":[{"name":"name","value":{"key":""}},{"name":"name","value":{"key":""}}],"packed":True,"cardinality":"CARDINALITY_UNKNOWN"},{"number":7,"typeUrl":"typeUrl","jsonName":"jsonName","oneofIndex":9,"defaultValue":"defaultValue","kind":"TYPE_UNKNOWN","name":"name","options":[{"name":"name","value":{"key":""}},{"name":"name","value":{"key":""}}],"packed":True,"cardinality":"CARDINALITY_UNKNOWN"}],"sourceContext":{"fileName":"fileName"}}],"apis":[{"mixins":[{"root":"root","name":"name"},{"root":"root","name":"name"}],"methods":[{"requestTypeUrl":"requestTypeUrl","responseTypeUrl":"responseTypeUrl","responseStreaming":True,"name":"name","options":[{"name":"name","value":{"key":""}},{"name":"name","value":{"key":""}}],"syntax":"SYNTAX_PROTO2","requestStreaming":True},{"requestTypeUrl":"requestTypeUrl","responseTypeUrl":"responseTypeUrl","responseStreaming":True,"name":"name","options":[{"name":"name","value":{"key":""}},{"name":"name","value":{"key":""}}],"syntax":"SYNTAX_PROTO2","requestStreaming":True}],"name":"name","options":[{"name":"name","value":{"key":""}},{"name":"name","value":{"key":""}}],"syntax":"SYNTAX_PROTO2","version":"version","sourceContext":{"fileName":"fileName"}},{"mixins":[{"root":"root","name":"name"},{"root":"root","name":"name"}],"methods":[{"requestTypeUrl":"requestTypeUrl","responseTypeUrl":"responseTypeUrl","responseStreaming":True,"name":"name","options":[{"name":"name","value":{"key":""}},{"name":"name","value":{"key":""}}],"syntax":"SYNTAX_PROTO2","requestStreaming":True},{"requestTypeUrl":"requestTypeUrl","responseTypeUrl":"responseTypeUrl","responseStreaming":True,"name":"name","options":[{"name":"name","value":{"key":""}},{"name":"name","value":{"key":""}}],"syntax":"SYNTAX_PROTO2","requestStreaming":True}],"name":"name","options":[{"name":"name","value":{"key":""}},{"name":"name","value":{"key":""}}],"syntax":"SYNTAX_PROTO2","version":"version","sourceContext":{"fileName":"fileName"}}],"name":"name","http":{"fullyDecodeReservedExpansion":True,"rules":[{"patch":"patch","responseBody":"responseBody","post":"post","custom":{"path":"path","kind":"kind"},"get":"get","selector":"selector","additionalBindings":[null,null],"body":"body","delete":"delete","put":"put"},{"patch":"patch","responseBody":"responseBody","post":"post","custom":{"path":"path","kind":"kind"},"get":"get","selector":"selector","additionalBindings":[null,null],"body":"body","delete":"delete","put":"put"}]},"logging":{"producerDestinations":[{"logs":["logs","logs"],"monitoredResource":"monitoredResource"},{"logs":["logs","logs"],"monitoredResource":"monitoredResource"}],"consumerDestinations":[{"logs":["logs","logs"],"monitoredResource":"monitoredResource"},{"logs":["logs","logs"],"monitoredResource":"monitoredResource"}]},"metrics":[{"monitoredResourceTypes":["monitoredResourceTypes","monitoredResourceTypes"],"metadata":{"ingestDelay":"ingestDelay","launchStage":"LAUNCH_STAGE_UNSPECIFIED","samplePeriod":"samplePeriod"},"unit":"unit","metricKind":"METRIC_KIND_UNSPECIFIED","displayName":"displayName","valueType":"VALUE_TYPE_UNSPECIFIED","name":"name","description":"description","launchStage":"LAUNCH_STAGE_UNSPECIFIED","type":"type","labels":[{"valueType":"STRING","description":"description","key":"key"},{"valueType":"STRING","description":"description","key":"key"}]},{"monitoredResourceTypes":["monitoredResourceTypes","monitoredResourceTypes"],"metadata":{"ingestDelay":"ingestDelay","launchStage":"LAUNCH_STAGE_UNSPECIFIED","samplePeriod":"samplePeriod"},"unit":"unit","metricKind":"METRIC_KIND_UNSPECIFIED","displayName":"displayName","valueType":"VALUE_TYPE_UNSPECIFIED","name":"name","description":"description","launchStage":"LAUNCH_STAGE_UNSPECIFIED","type":"type","labels":[{"valueType":"STRING","description":"description","key":"key"},{"valueType":"STRING","description":"description","key":"key"}]}]}
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
        path='/v1/services/{service_name}/configs'.format(service_name='service_name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_servicemanagement_services_configs_get(client):
    """Test case for servicemanagement_services_configs_get

    
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
                    ('view', 'view_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/services/{service_name}/configs/{config_id}'.format(service_name='service_name_example', config_id='config_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_servicemanagement_services_configs_list(client):
    """Test case for servicemanagement_services_configs_list

    
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
        path='/v1/services/{service_name}/configs'.format(service_name='service_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_servicemanagement_services_configs_submit(client):
    """Test case for servicemanagement_services_configs_submit

    
    """
    body = {"validateOnly":True,"configSource":{"files":[{"filePath":"filePath","fileContents":"fileContents","fileType":"FILE_TYPE_UNSPECIFIED"},{"filePath":"filePath","fileContents":"fileContents","fileType":"FILE_TYPE_UNSPECIFIED"}],"id":"id"}}
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
        path='/v1/services/{service_name}/configs:submit'.format(service_name='service_name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_servicemanagement_services_consumers_get_iam_policy(client):
    """Test case for servicemanagement_services_consumers_get_iam_policy

    
    """
    body = {"options":{"requestedPolicyVersion":0}}
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
        path='/v1/{resourceget_iam_polic}'.format(resource='resource_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_servicemanagement_services_consumers_set_iam_policy(client):
    """Test case for servicemanagement_services_consumers_set_iam_policy

    
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

async def test_servicemanagement_services_consumers_test_iam_permissions(client):
    """Test case for servicemanagement_services_consumers_test_iam_permissions

    
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


pytestmark = pytest.mark.asyncio

async def test_servicemanagement_services_create(client):
    """Test case for servicemanagement_services_create

    
    """
    body = {"producerProjectId":"producerProjectId","serviceName":"serviceName"}
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
        path='/v1/services',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_servicemanagement_services_delete(client):
    """Test case for servicemanagement_services_delete

    
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
        method='DELETE',
        path='/v1/services/{service_name}'.format(service_name='service_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_servicemanagement_services_generate_config_report(client):
    """Test case for servicemanagement_services_generate_config_report

    
    """
    body = {"oldConfig":{"key":""},"newConfig":{"key":""}}
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
        path='/v1/services:generateConfigReport',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_servicemanagement_services_get(client):
    """Test case for servicemanagement_services_get

    
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
        path='/v1/services/{service_name}'.format(service_name='service_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_servicemanagement_services_get_config(client):
    """Test case for servicemanagement_services_get_config

    
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
                    ('configId', 'config_id_example'),
                    ('view', 'view_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/services/{service_name}/config'.format(service_name='service_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_servicemanagement_services_list(client):
    """Test case for servicemanagement_services_list

    
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
                    ('consumerId', 'consumer_id_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example'),
                    ('producerProjectId', 'producer_project_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/services',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_servicemanagement_services_rollouts_create(client):
    """Test case for servicemanagement_services_rollouts_create

    
    """
    body = {"createTime":"createTime","createdBy":"createdBy","deleteServiceStrategy":"{}","rolloutId":"rolloutId","trafficPercentStrategy":{"percentages":{"key":0.8008281904610115}},"serviceName":"serviceName","status":"ROLLOUT_STATUS_UNSPECIFIED"}
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
        path='/v1/services/{service_name}/rollouts'.format(service_name='service_name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_servicemanagement_services_rollouts_get(client):
    """Test case for servicemanagement_services_rollouts_get

    
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
        path='/v1/services/{service_name}/rollouts/{rollout_id}'.format(service_name='service_name_example', rollout_id='rollout_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_servicemanagement_services_rollouts_list(client):
    """Test case for servicemanagement_services_rollouts_list

    
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
        path='/v1/services/{service_name}/rollouts'.format(service_name='service_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_servicemanagement_services_undelete(client):
    """Test case for servicemanagement_services_undelete

    
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
        method='POST',
        path='/v1/services/{service_nameundelet}'.format(service_name='service_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

