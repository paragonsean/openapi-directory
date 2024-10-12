# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.attestor import Attestor
from openapi_server.models.evaluate_gke_policy_request import EvaluateGkePolicyRequest
from openapi_server.models.evaluate_gke_policy_response import EvaluateGkePolicyResponse
from openapi_server.models.iam_policy import IamPolicy
from openapi_server.models.list_attestors_response import ListAttestorsResponse
from openapi_server.models.list_platform_policies_response import ListPlatformPoliciesResponse
from openapi_server.models.platform_policy import PlatformPolicy
from openapi_server.models.set_iam_policy_request import SetIamPolicyRequest
from openapi_server.models.test_iam_permissions_request import TestIamPermissionsRequest
from openapi_server.models.test_iam_permissions_response import TestIamPermissionsResponse
from openapi_server.models.validate_attestation_occurrence_request import ValidateAttestationOccurrenceRequest
from openapi_server.models.validate_attestation_occurrence_response import ValidateAttestationOccurrenceResponse


pytestmark = pytest.mark.asyncio

async def test_binaryauthorization_projects_attestors_create(client):
    """Test case for binaryauthorization_projects_attestors_create

    
    """
    body = {"name":"name","description":"description","etag":"etag","updateTime":"updateTime","userOwnedGrafeasNote":{"delegationServiceAccountEmail":"delegationServiceAccountEmail","noteReference":"noteReference","publicKeys":[{"pkixPublicKey":{"publicKeyPem":"publicKeyPem","keyId":"keyId","signatureAlgorithm":"SIGNATURE_ALGORITHM_UNSPECIFIED"},"asciiArmoredPgpPublicKey":"asciiArmoredPgpPublicKey","comment":"comment","id":"id"},{"pkixPublicKey":{"publicKeyPem":"publicKeyPem","keyId":"keyId","signatureAlgorithm":"SIGNATURE_ALGORITHM_UNSPECIFIED"},"asciiArmoredPgpPublicKey":"asciiArmoredPgpPublicKey","comment":"comment","id":"id"}]}}
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
                    ('attestorId', 'attestor_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{parent}/attestors'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_binaryauthorization_projects_attestors_list(client):
    """Test case for binaryauthorization_projects_attestors_list

    
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
        path='/v1/{parent}/attestors'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_binaryauthorization_projects_attestors_validate_attestation_occurrence(client):
    """Test case for binaryauthorization_projects_attestors_validate_attestation_occurrence

    
    """
    body = {"attestation":{"serializedPayload":"serializedPayload","jwts":[{"compactJwt":"compactJwt"},{"compactJwt":"compactJwt"}],"signatures":[{"signature":"signature","publicKeyId":"publicKeyId"},{"signature":"signature","publicKeyId":"publicKeyId"}]},"occurrenceNote":"occurrenceNote","occurrenceResourceUri":"occurrenceResourceUri"}
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
        path='/v1/{attestorvalidate_attestation_occurrenc}'.format(attestor='attestor_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_binaryauthorization_projects_platforms_gke_policies_evaluate(client):
    """Test case for binaryauthorization_projects_platforms_gke_policies_evaluate

    
    """
    body = {"resource":{"key":""}}
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
        path='/v1/{nameevaluat}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_binaryauthorization_projects_platforms_policies_create(client):
    """Test case for binaryauthorization_projects_platforms_policies_create

    
    """
    body = {"name":"name","description":"description","updateTime":"updateTime","gkePolicy":{"imageAllowlist":{"allowPattern":["allowPattern","allowPattern"]},"checkSets":[{"checks":[{"alwaysDeny":True,"slsaCheck":{"rules":[{"configBasedBuildRequired":True,"trustedSourceRepoPatterns":["trustedSourceRepoPatterns","trustedSourceRepoPatterns"],"attestationSource":{"containerAnalysisAttestationProjects":["containerAnalysisAttestationProjects","containerAnalysisAttestationProjects"]},"trustedBuilder":"BUILDER_UNSPECIFIED"},{"configBasedBuildRequired":True,"trustedSourceRepoPatterns":["trustedSourceRepoPatterns","trustedSourceRepoPatterns"],"attestationSource":{"containerAnalysisAttestationProjects":["containerAnalysisAttestationProjects","containerAnalysisAttestationProjects"]},"trustedBuilder":"BUILDER_UNSPECIFIED"}]},"sigstoreSignatureCheck":{"sigstoreAuthorities":[{"displayName":"displayName","publicKeySet":{"publicKeys":[{"publicKeyPem":"publicKeyPem"},{"publicKeyPem":"publicKeyPem"}]}},{"displayName":"displayName","publicKeySet":{"publicKeys":[{"publicKeyPem":"publicKeyPem"},{"publicKeyPem":"publicKeyPem"}]}}]},"imageFreshnessCheck":{"maxUploadAgeDays":0},"vulnerabilityCheck":{"blockedCves":["blockedCves","blockedCves"],"maximumUnfixableSeverity":"MAXIMUM_ALLOWED_SEVERITY_UNSPECIFIED","allowedCves":["allowedCves","allowedCves"],"containerAnalysisVulnerabilityProjects":["containerAnalysisVulnerabilityProjects","containerAnalysisVulnerabilityProjects"],"maximumFixableSeverity":"MAXIMUM_ALLOWED_SEVERITY_UNSPECIFIED"},"imageAllowlist":{"allowPattern":["allowPattern","allowPattern"]},"displayName":"displayName","simpleSigningAttestationCheck":{"containerAnalysisAttestationProjects":["containerAnalysisAttestationProjects","containerAnalysisAttestationProjects"],"attestationAuthenticators":[{"pkixPublicKeySet":{"pkixPublicKeys":[{"publicKeyPem":"publicKeyPem","keyId":"keyId","signatureAlgorithm":"SIGNATURE_ALGORITHM_UNSPECIFIED"},{"publicKeyPem":"publicKeyPem","keyId":"keyId","signatureAlgorithm":"SIGNATURE_ALGORITHM_UNSPECIFIED"}]},"displayName":"displayName"},{"pkixPublicKeySet":{"pkixPublicKeys":[{"publicKeyPem":"publicKeyPem","keyId":"keyId","signatureAlgorithm":"SIGNATURE_ALGORITHM_UNSPECIFIED"},{"publicKeyPem":"publicKeyPem","keyId":"keyId","signatureAlgorithm":"SIGNATURE_ALGORITHM_UNSPECIFIED"}]},"displayName":"displayName"}]},"trustedDirectoryCheck":{"trustedDirPatterns":["trustedDirPatterns","trustedDirPatterns"]}},{"alwaysDeny":True,"slsaCheck":{"rules":[{"configBasedBuildRequired":True,"trustedSourceRepoPatterns":["trustedSourceRepoPatterns","trustedSourceRepoPatterns"],"attestationSource":{"containerAnalysisAttestationProjects":["containerAnalysisAttestationProjects","containerAnalysisAttestationProjects"]},"trustedBuilder":"BUILDER_UNSPECIFIED"},{"configBasedBuildRequired":True,"trustedSourceRepoPatterns":["trustedSourceRepoPatterns","trustedSourceRepoPatterns"],"attestationSource":{"containerAnalysisAttestationProjects":["containerAnalysisAttestationProjects","containerAnalysisAttestationProjects"]},"trustedBuilder":"BUILDER_UNSPECIFIED"}]},"sigstoreSignatureCheck":{"sigstoreAuthorities":[{"displayName":"displayName","publicKeySet":{"publicKeys":[{"publicKeyPem":"publicKeyPem"},{"publicKeyPem":"publicKeyPem"}]}},{"displayName":"displayName","publicKeySet":{"publicKeys":[{"publicKeyPem":"publicKeyPem"},{"publicKeyPem":"publicKeyPem"}]}}]},"imageFreshnessCheck":{"maxUploadAgeDays":0},"vulnerabilityCheck":{"blockedCves":["blockedCves","blockedCves"],"maximumUnfixableSeverity":"MAXIMUM_ALLOWED_SEVERITY_UNSPECIFIED","allowedCves":["allowedCves","allowedCves"],"containerAnalysisVulnerabilityProjects":["containerAnalysisVulnerabilityProjects","containerAnalysisVulnerabilityProjects"],"maximumFixableSeverity":"MAXIMUM_ALLOWED_SEVERITY_UNSPECIFIED"},"imageAllowlist":{"allowPattern":["allowPattern","allowPattern"]},"displayName":"displayName","simpleSigningAttestationCheck":{"containerAnalysisAttestationProjects":["containerAnalysisAttestationProjects","containerAnalysisAttestationProjects"],"attestationAuthenticators":[{"pkixPublicKeySet":{"pkixPublicKeys":[{"publicKeyPem":"publicKeyPem","keyId":"keyId","signatureAlgorithm":"SIGNATURE_ALGORITHM_UNSPECIFIED"},{"publicKeyPem":"publicKeyPem","keyId":"keyId","signatureAlgorithm":"SIGNATURE_ALGORITHM_UNSPECIFIED"}]},"displayName":"displayName"},{"pkixPublicKeySet":{"pkixPublicKeys":[{"publicKeyPem":"publicKeyPem","keyId":"keyId","signatureAlgorithm":"SIGNATURE_ALGORITHM_UNSPECIFIED"},{"publicKeyPem":"publicKeyPem","keyId":"keyId","signatureAlgorithm":"SIGNATURE_ALGORITHM_UNSPECIFIED"}]},"displayName":"displayName"}]},"trustedDirectoryCheck":{"trustedDirPatterns":["trustedDirPatterns","trustedDirPatterns"]}}],"imageAllowlist":{"allowPattern":["allowPattern","allowPattern"]},"displayName":"displayName","scope":{"kubernetesNamespace":"kubernetesNamespace","kubernetesServiceAccount":"kubernetesServiceAccount"}},{"checks":[{"alwaysDeny":True,"slsaCheck":{"rules":[{"configBasedBuildRequired":True,"trustedSourceRepoPatterns":["trustedSourceRepoPatterns","trustedSourceRepoPatterns"],"attestationSource":{"containerAnalysisAttestationProjects":["containerAnalysisAttestationProjects","containerAnalysisAttestationProjects"]},"trustedBuilder":"BUILDER_UNSPECIFIED"},{"configBasedBuildRequired":True,"trustedSourceRepoPatterns":["trustedSourceRepoPatterns","trustedSourceRepoPatterns"],"attestationSource":{"containerAnalysisAttestationProjects":["containerAnalysisAttestationProjects","containerAnalysisAttestationProjects"]},"trustedBuilder":"BUILDER_UNSPECIFIED"}]},"sigstoreSignatureCheck":{"sigstoreAuthorities":[{"displayName":"displayName","publicKeySet":{"publicKeys":[{"publicKeyPem":"publicKeyPem"},{"publicKeyPem":"publicKeyPem"}]}},{"displayName":"displayName","publicKeySet":{"publicKeys":[{"publicKeyPem":"publicKeyPem"},{"publicKeyPem":"publicKeyPem"}]}}]},"imageFreshnessCheck":{"maxUploadAgeDays":0},"vulnerabilityCheck":{"blockedCves":["blockedCves","blockedCves"],"maximumUnfixableSeverity":"MAXIMUM_ALLOWED_SEVERITY_UNSPECIFIED","allowedCves":["allowedCves","allowedCves"],"containerAnalysisVulnerabilityProjects":["containerAnalysisVulnerabilityProjects","containerAnalysisVulnerabilityProjects"],"maximumFixableSeverity":"MAXIMUM_ALLOWED_SEVERITY_UNSPECIFIED"},"imageAllowlist":{"allowPattern":["allowPattern","allowPattern"]},"displayName":"displayName","simpleSigningAttestationCheck":{"containerAnalysisAttestationProjects":["containerAnalysisAttestationProjects","containerAnalysisAttestationProjects"],"attestationAuthenticators":[{"pkixPublicKeySet":{"pkixPublicKeys":[{"publicKeyPem":"publicKeyPem","keyId":"keyId","signatureAlgorithm":"SIGNATURE_ALGORITHM_UNSPECIFIED"},{"publicKeyPem":"publicKeyPem","keyId":"keyId","signatureAlgorithm":"SIGNATURE_ALGORITHM_UNSPECIFIED"}]},"displayName":"displayName"},{"pkixPublicKeySet":{"pkixPublicKeys":[{"publicKeyPem":"publicKeyPem","keyId":"keyId","signatureAlgorithm":"SIGNATURE_ALGORITHM_UNSPECIFIED"},{"publicKeyPem":"publicKeyPem","keyId":"keyId","signatureAlgorithm":"SIGNATURE_ALGORITHM_UNSPECIFIED"}]},"displayName":"displayName"}]},"trustedDirectoryCheck":{"trustedDirPatterns":["trustedDirPatterns","trustedDirPatterns"]}},{"alwaysDeny":True,"slsaCheck":{"rules":[{"configBasedBuildRequired":True,"trustedSourceRepoPatterns":["trustedSourceRepoPatterns","trustedSourceRepoPatterns"],"attestationSource":{"containerAnalysisAttestationProjects":["containerAnalysisAttestationProjects","containerAnalysisAttestationProjects"]},"trustedBuilder":"BUILDER_UNSPECIFIED"},{"configBasedBuildRequired":True,"trustedSourceRepoPatterns":["trustedSourceRepoPatterns","trustedSourceRepoPatterns"],"attestationSource":{"containerAnalysisAttestationProjects":["containerAnalysisAttestationProjects","containerAnalysisAttestationProjects"]},"trustedBuilder":"BUILDER_UNSPECIFIED"}]},"sigstoreSignatureCheck":{"sigstoreAuthorities":[{"displayName":"displayName","publicKeySet":{"publicKeys":[{"publicKeyPem":"publicKeyPem"},{"publicKeyPem":"publicKeyPem"}]}},{"displayName":"displayName","publicKeySet":{"publicKeys":[{"publicKeyPem":"publicKeyPem"},{"publicKeyPem":"publicKeyPem"}]}}]},"imageFreshnessCheck":{"maxUploadAgeDays":0},"vulnerabilityCheck":{"blockedCves":["blockedCves","blockedCves"],"maximumUnfixableSeverity":"MAXIMUM_ALLOWED_SEVERITY_UNSPECIFIED","allowedCves":["allowedCves","allowedCves"],"containerAnalysisVulnerabilityProjects":["containerAnalysisVulnerabilityProjects","containerAnalysisVulnerabilityProjects"],"maximumFixableSeverity":"MAXIMUM_ALLOWED_SEVERITY_UNSPECIFIED"},"imageAllowlist":{"allowPattern":["allowPattern","allowPattern"]},"displayName":"displayName","simpleSigningAttestationCheck":{"containerAnalysisAttestationProjects":["containerAnalysisAttestationProjects","containerAnalysisAttestationProjects"],"attestationAuthenticators":[{"pkixPublicKeySet":{"pkixPublicKeys":[{"publicKeyPem":"publicKeyPem","keyId":"keyId","signatureAlgorithm":"SIGNATURE_ALGORITHM_UNSPECIFIED"},{"publicKeyPem":"publicKeyPem","keyId":"keyId","signatureAlgorithm":"SIGNATURE_ALGORITHM_UNSPECIFIED"}]},"displayName":"displayName"},{"pkixPublicKeySet":{"pkixPublicKeys":[{"publicKeyPem":"publicKeyPem","keyId":"keyId","signatureAlgorithm":"SIGNATURE_ALGORITHM_UNSPECIFIED"},{"publicKeyPem":"publicKeyPem","keyId":"keyId","signatureAlgorithm":"SIGNATURE_ALGORITHM_UNSPECIFIED"}]},"displayName":"displayName"}]},"trustedDirectoryCheck":{"trustedDirPatterns":["trustedDirPatterns","trustedDirPatterns"]}}],"imageAllowlist":{"allowPattern":["allowPattern","allowPattern"]},"displayName":"displayName","scope":{"kubernetesNamespace":"kubernetesNamespace","kubernetesServiceAccount":"kubernetesServiceAccount"}}]}}
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
                    ('policyId', 'policy_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{parent}/policies'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_binaryauthorization_projects_platforms_policies_delete(client):
    """Test case for binaryauthorization_projects_platforms_policies_delete

    
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
        path='/v1/{name}'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_binaryauthorization_projects_platforms_policies_list(client):
    """Test case for binaryauthorization_projects_platforms_policies_list

    
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
        path='/v1/{parent}/policies'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_binaryauthorization_projects_platforms_policies_replace_platform_policy(client):
    """Test case for binaryauthorization_projects_platforms_policies_replace_platform_policy

    
    """
    body = {"name":"name","description":"description","updateTime":"updateTime","gkePolicy":{"imageAllowlist":{"allowPattern":["allowPattern","allowPattern"]},"checkSets":[{"checks":[{"alwaysDeny":True,"slsaCheck":{"rules":[{"configBasedBuildRequired":True,"trustedSourceRepoPatterns":["trustedSourceRepoPatterns","trustedSourceRepoPatterns"],"attestationSource":{"containerAnalysisAttestationProjects":["containerAnalysisAttestationProjects","containerAnalysisAttestationProjects"]},"trustedBuilder":"BUILDER_UNSPECIFIED"},{"configBasedBuildRequired":True,"trustedSourceRepoPatterns":["trustedSourceRepoPatterns","trustedSourceRepoPatterns"],"attestationSource":{"containerAnalysisAttestationProjects":["containerAnalysisAttestationProjects","containerAnalysisAttestationProjects"]},"trustedBuilder":"BUILDER_UNSPECIFIED"}]},"sigstoreSignatureCheck":{"sigstoreAuthorities":[{"displayName":"displayName","publicKeySet":{"publicKeys":[{"publicKeyPem":"publicKeyPem"},{"publicKeyPem":"publicKeyPem"}]}},{"displayName":"displayName","publicKeySet":{"publicKeys":[{"publicKeyPem":"publicKeyPem"},{"publicKeyPem":"publicKeyPem"}]}}]},"imageFreshnessCheck":{"maxUploadAgeDays":0},"vulnerabilityCheck":{"blockedCves":["blockedCves","blockedCves"],"maximumUnfixableSeverity":"MAXIMUM_ALLOWED_SEVERITY_UNSPECIFIED","allowedCves":["allowedCves","allowedCves"],"containerAnalysisVulnerabilityProjects":["containerAnalysisVulnerabilityProjects","containerAnalysisVulnerabilityProjects"],"maximumFixableSeverity":"MAXIMUM_ALLOWED_SEVERITY_UNSPECIFIED"},"imageAllowlist":{"allowPattern":["allowPattern","allowPattern"]},"displayName":"displayName","simpleSigningAttestationCheck":{"containerAnalysisAttestationProjects":["containerAnalysisAttestationProjects","containerAnalysisAttestationProjects"],"attestationAuthenticators":[{"pkixPublicKeySet":{"pkixPublicKeys":[{"publicKeyPem":"publicKeyPem","keyId":"keyId","signatureAlgorithm":"SIGNATURE_ALGORITHM_UNSPECIFIED"},{"publicKeyPem":"publicKeyPem","keyId":"keyId","signatureAlgorithm":"SIGNATURE_ALGORITHM_UNSPECIFIED"}]},"displayName":"displayName"},{"pkixPublicKeySet":{"pkixPublicKeys":[{"publicKeyPem":"publicKeyPem","keyId":"keyId","signatureAlgorithm":"SIGNATURE_ALGORITHM_UNSPECIFIED"},{"publicKeyPem":"publicKeyPem","keyId":"keyId","signatureAlgorithm":"SIGNATURE_ALGORITHM_UNSPECIFIED"}]},"displayName":"displayName"}]},"trustedDirectoryCheck":{"trustedDirPatterns":["trustedDirPatterns","trustedDirPatterns"]}},{"alwaysDeny":True,"slsaCheck":{"rules":[{"configBasedBuildRequired":True,"trustedSourceRepoPatterns":["trustedSourceRepoPatterns","trustedSourceRepoPatterns"],"attestationSource":{"containerAnalysisAttestationProjects":["containerAnalysisAttestationProjects","containerAnalysisAttestationProjects"]},"trustedBuilder":"BUILDER_UNSPECIFIED"},{"configBasedBuildRequired":True,"trustedSourceRepoPatterns":["trustedSourceRepoPatterns","trustedSourceRepoPatterns"],"attestationSource":{"containerAnalysisAttestationProjects":["containerAnalysisAttestationProjects","containerAnalysisAttestationProjects"]},"trustedBuilder":"BUILDER_UNSPECIFIED"}]},"sigstoreSignatureCheck":{"sigstoreAuthorities":[{"displayName":"displayName","publicKeySet":{"publicKeys":[{"publicKeyPem":"publicKeyPem"},{"publicKeyPem":"publicKeyPem"}]}},{"displayName":"displayName","publicKeySet":{"publicKeys":[{"publicKeyPem":"publicKeyPem"},{"publicKeyPem":"publicKeyPem"}]}}]},"imageFreshnessCheck":{"maxUploadAgeDays":0},"vulnerabilityCheck":{"blockedCves":["blockedCves","blockedCves"],"maximumUnfixableSeverity":"MAXIMUM_ALLOWED_SEVERITY_UNSPECIFIED","allowedCves":["allowedCves","allowedCves"],"containerAnalysisVulnerabilityProjects":["containerAnalysisVulnerabilityProjects","containerAnalysisVulnerabilityProjects"],"maximumFixableSeverity":"MAXIMUM_ALLOWED_SEVERITY_UNSPECIFIED"},"imageAllowlist":{"allowPattern":["allowPattern","allowPattern"]},"displayName":"displayName","simpleSigningAttestationCheck":{"containerAnalysisAttestationProjects":["containerAnalysisAttestationProjects","containerAnalysisAttestationProjects"],"attestationAuthenticators":[{"pkixPublicKeySet":{"pkixPublicKeys":[{"publicKeyPem":"publicKeyPem","keyId":"keyId","signatureAlgorithm":"SIGNATURE_ALGORITHM_UNSPECIFIED"},{"publicKeyPem":"publicKeyPem","keyId":"keyId","signatureAlgorithm":"SIGNATURE_ALGORITHM_UNSPECIFIED"}]},"displayName":"displayName"},{"pkixPublicKeySet":{"pkixPublicKeys":[{"publicKeyPem":"publicKeyPem","keyId":"keyId","signatureAlgorithm":"SIGNATURE_ALGORITHM_UNSPECIFIED"},{"publicKeyPem":"publicKeyPem","keyId":"keyId","signatureAlgorithm":"SIGNATURE_ALGORITHM_UNSPECIFIED"}]},"displayName":"displayName"}]},"trustedDirectoryCheck":{"trustedDirPatterns":["trustedDirPatterns","trustedDirPatterns"]}}],"imageAllowlist":{"allowPattern":["allowPattern","allowPattern"]},"displayName":"displayName","scope":{"kubernetesNamespace":"kubernetesNamespace","kubernetesServiceAccount":"kubernetesServiceAccount"}},{"checks":[{"alwaysDeny":True,"slsaCheck":{"rules":[{"configBasedBuildRequired":True,"trustedSourceRepoPatterns":["trustedSourceRepoPatterns","trustedSourceRepoPatterns"],"attestationSource":{"containerAnalysisAttestationProjects":["containerAnalysisAttestationProjects","containerAnalysisAttestationProjects"]},"trustedBuilder":"BUILDER_UNSPECIFIED"},{"configBasedBuildRequired":True,"trustedSourceRepoPatterns":["trustedSourceRepoPatterns","trustedSourceRepoPatterns"],"attestationSource":{"containerAnalysisAttestationProjects":["containerAnalysisAttestationProjects","containerAnalysisAttestationProjects"]},"trustedBuilder":"BUILDER_UNSPECIFIED"}]},"sigstoreSignatureCheck":{"sigstoreAuthorities":[{"displayName":"displayName","publicKeySet":{"publicKeys":[{"publicKeyPem":"publicKeyPem"},{"publicKeyPem":"publicKeyPem"}]}},{"displayName":"displayName","publicKeySet":{"publicKeys":[{"publicKeyPem":"publicKeyPem"},{"publicKeyPem":"publicKeyPem"}]}}]},"imageFreshnessCheck":{"maxUploadAgeDays":0},"vulnerabilityCheck":{"blockedCves":["blockedCves","blockedCves"],"maximumUnfixableSeverity":"MAXIMUM_ALLOWED_SEVERITY_UNSPECIFIED","allowedCves":["allowedCves","allowedCves"],"containerAnalysisVulnerabilityProjects":["containerAnalysisVulnerabilityProjects","containerAnalysisVulnerabilityProjects"],"maximumFixableSeverity":"MAXIMUM_ALLOWED_SEVERITY_UNSPECIFIED"},"imageAllowlist":{"allowPattern":["allowPattern","allowPattern"]},"displayName":"displayName","simpleSigningAttestationCheck":{"containerAnalysisAttestationProjects":["containerAnalysisAttestationProjects","containerAnalysisAttestationProjects"],"attestationAuthenticators":[{"pkixPublicKeySet":{"pkixPublicKeys":[{"publicKeyPem":"publicKeyPem","keyId":"keyId","signatureAlgorithm":"SIGNATURE_ALGORITHM_UNSPECIFIED"},{"publicKeyPem":"publicKeyPem","keyId":"keyId","signatureAlgorithm":"SIGNATURE_ALGORITHM_UNSPECIFIED"}]},"displayName":"displayName"},{"pkixPublicKeySet":{"pkixPublicKeys":[{"publicKeyPem":"publicKeyPem","keyId":"keyId","signatureAlgorithm":"SIGNATURE_ALGORITHM_UNSPECIFIED"},{"publicKeyPem":"publicKeyPem","keyId":"keyId","signatureAlgorithm":"SIGNATURE_ALGORITHM_UNSPECIFIED"}]},"displayName":"displayName"}]},"trustedDirectoryCheck":{"trustedDirPatterns":["trustedDirPatterns","trustedDirPatterns"]}},{"alwaysDeny":True,"slsaCheck":{"rules":[{"configBasedBuildRequired":True,"trustedSourceRepoPatterns":["trustedSourceRepoPatterns","trustedSourceRepoPatterns"],"attestationSource":{"containerAnalysisAttestationProjects":["containerAnalysisAttestationProjects","containerAnalysisAttestationProjects"]},"trustedBuilder":"BUILDER_UNSPECIFIED"},{"configBasedBuildRequired":True,"trustedSourceRepoPatterns":["trustedSourceRepoPatterns","trustedSourceRepoPatterns"],"attestationSource":{"containerAnalysisAttestationProjects":["containerAnalysisAttestationProjects","containerAnalysisAttestationProjects"]},"trustedBuilder":"BUILDER_UNSPECIFIED"}]},"sigstoreSignatureCheck":{"sigstoreAuthorities":[{"displayName":"displayName","publicKeySet":{"publicKeys":[{"publicKeyPem":"publicKeyPem"},{"publicKeyPem":"publicKeyPem"}]}},{"displayName":"displayName","publicKeySet":{"publicKeys":[{"publicKeyPem":"publicKeyPem"},{"publicKeyPem":"publicKeyPem"}]}}]},"imageFreshnessCheck":{"maxUploadAgeDays":0},"vulnerabilityCheck":{"blockedCves":["blockedCves","blockedCves"],"maximumUnfixableSeverity":"MAXIMUM_ALLOWED_SEVERITY_UNSPECIFIED","allowedCves":["allowedCves","allowedCves"],"containerAnalysisVulnerabilityProjects":["containerAnalysisVulnerabilityProjects","containerAnalysisVulnerabilityProjects"],"maximumFixableSeverity":"MAXIMUM_ALLOWED_SEVERITY_UNSPECIFIED"},"imageAllowlist":{"allowPattern":["allowPattern","allowPattern"]},"displayName":"displayName","simpleSigningAttestationCheck":{"containerAnalysisAttestationProjects":["containerAnalysisAttestationProjects","containerAnalysisAttestationProjects"],"attestationAuthenticators":[{"pkixPublicKeySet":{"pkixPublicKeys":[{"publicKeyPem":"publicKeyPem","keyId":"keyId","signatureAlgorithm":"SIGNATURE_ALGORITHM_UNSPECIFIED"},{"publicKeyPem":"publicKeyPem","keyId":"keyId","signatureAlgorithm":"SIGNATURE_ALGORITHM_UNSPECIFIED"}]},"displayName":"displayName"},{"pkixPublicKeySet":{"pkixPublicKeys":[{"publicKeyPem":"publicKeyPem","keyId":"keyId","signatureAlgorithm":"SIGNATURE_ALGORITHM_UNSPECIFIED"},{"publicKeyPem":"publicKeyPem","keyId":"keyId","signatureAlgorithm":"SIGNATURE_ALGORITHM_UNSPECIFIED"}]},"displayName":"displayName"}]},"trustedDirectoryCheck":{"trustedDirPatterns":["trustedDirPatterns","trustedDirPatterns"]}}],"imageAllowlist":{"allowPattern":["allowPattern","allowPattern"]},"displayName":"displayName","scope":{"kubernetesNamespace":"kubernetesNamespace","kubernetesServiceAccount":"kubernetesServiceAccount"}}]}}
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
        method='PUT',
        path='/v1/{name}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_binaryauthorization_projects_policy_get_iam_policy(client):
    """Test case for binaryauthorization_projects_policy_get_iam_policy

    
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

async def test_binaryauthorization_projects_policy_set_iam_policy(client):
    """Test case for binaryauthorization_projects_policy_set_iam_policy

    
    """
    body = {"policy":{"bindings":[{"condition":{"expression":"expression","description":"description","location":"location","title":"title"},"role":"role","members":["members","members"]},{"condition":{"expression":"expression","description":"description","location":"location","title":"title"},"role":"role","members":["members","members"]}],"etag":"etag","version":0}}
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

async def test_binaryauthorization_projects_policy_test_iam_permissions(client):
    """Test case for binaryauthorization_projects_policy_test_iam_permissions

    
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

