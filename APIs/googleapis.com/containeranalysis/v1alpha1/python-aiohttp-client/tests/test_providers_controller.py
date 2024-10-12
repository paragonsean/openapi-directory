# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_iam_policy_request import GetIamPolicyRequest
from openapi_server.models.list_note_occurrences_response import ListNoteOccurrencesResponse
from openapi_server.models.list_notes_response import ListNotesResponse
from openapi_server.models.note import Note
from openapi_server.models.policy import Policy
from openapi_server.models.set_iam_policy_request import SetIamPolicyRequest
from openapi_server.models.test_iam_permissions_request import TestIamPermissionsRequest
from openapi_server.models.test_iam_permissions_response import TestIamPermissionsResponse


pytestmark = pytest.mark.asyncio

async def test_containeranalysis_providers_notes_create(client):
    """Test case for containeranalysis_providers_notes_create

    
    """
    body = {"longDescription":"longDescription","package":{"license":{"comments":"comments","expression":"expression"},"digest":[{"digestBytes":"digestBytes","algo":"algo"},{"digestBytes":"digestBytes","algo":"algo"}],"name":"name","description":"description","distribution":[{"latestVersion":{"inclusive":True,"kind":"NORMAL","name":"name","epoch":6,"revision":"revision"},"description":"description","cpeUri":"cpeUri","maintainer":"maintainer","url":"url","architecture":"ARCHITECTURE_UNSPECIFIED"},{"latestVersion":{"inclusive":True,"kind":"NORMAL","name":"name","epoch":6,"revision":"revision"},"description":"description","cpeUri":"cpeUri","maintainer":"maintainer","url":"url","architecture":"ARCHITECTURE_UNSPECIFIED"}],"cpeUri":"cpeUri","packageType":"packageType","version":{"inclusive":True,"kind":"NORMAL","name":"name","epoch":6,"revision":"revision"},"maintainer":"maintainer","url":"url","architecture":"ARCHITECTURE_UNSPECIFIED"},"upgrade":{"package":"package","version":{"inclusive":True,"kind":"NORMAL","name":"name","epoch":6,"revision":"revision"},"distributions":[{"severity":"severity","cve":["cve","cve"],"classification":"classification","cpeUri":"cpeUri"},{"severity":"severity","cve":["cve","cve"],"classification":"classification","cpeUri":"cpeUri"}]},"kind":"KIND_UNSPECIFIED","sbomReference":{"format":"format","version":"version"},"vulnerabilityAssessment":{"longDescription":"longDescription","assessment":{"longDescription":"longDescription","cve":"cve","vulnerabilityId":"vulnerabilityId","relatedUris":[{"label":"label","uri":"uri"},{"label":"label","uri":"uri"}],"remediations":[{"remediationType":"REMEDIATION_TYPE_UNSPECIFIED","remediationUri":{"label":"label","uri":"uri"},"details":"details"},{"remediationType":"REMEDIATION_TYPE_UNSPECIFIED","remediationUri":{"label":"label","uri":"uri"},"details":"details"}],"impacts":["impacts","impacts"],"justification":{"justificationType":"JUSTIFICATION_TYPE_UNSPECIFIED","details":"details"},"shortDescription":"shortDescription","state":"STATE_UNSPECIFIED"},"product":{"identifierHelper":{"field":"IDENTIFIER_HELPER_FIELD_UNSPECIFIED","genericUri":"genericUri"},"name":"name","id":"id"},"publisher":{"issuingAuthority":"issuingAuthority","name":"name","publisherNamespace":"publisherNamespace"},"shortDescription":"shortDescription","languageCode":"languageCode","title":"title"},"attestationAuthority":{"hint":{"humanReadableName":"humanReadableName"}},"baseImage":{"resourceUrl":"resourceUrl","fingerprint":{"v1Name":"v1Name","v2Blob":["v2Blob","v2Blob"],"v2Name":"v2Name"}},"dsseAttestation":{"hint":{"humanReadableName":"humanReadableName"}},"updateTime":"updateTime","shortDescription":"shortDescription","spdxRelationship":{"type":"RELATIONSHIP_TYPE_UNSPECIFIED"},"spdxFile":{"checksum":["checksum","checksum"],"title":"title","fileType":"FILE_TYPE_UNSPECIFIED"},"deployable":{"resourceUri":["resourceUri","resourceUri"]},"createTime":"createTime","buildType":{"signature":{"signature":"signature","keyId":"keyId","publicKey":"publicKey","keyType":"KEY_TYPE_UNSPECIFIED"},"builderVersion":"builderVersion"},"compliance":{"remediation":"remediation","cisBenchmark":{"severity":"SEVERITY_UNSPECIFIED","profileLevel":0},"scanInstructions":"scanInstructions","description":"description","title":"title","rationale":"rationale","version":[{"benchmarkDocument":"benchmarkDocument","cpeUri":"cpeUri","version":"version"},{"benchmarkDocument":"benchmarkDocument","cpeUri":"cpeUri","version":"version"}]},"discovery":{"analysisKind":"KIND_UNSPECIFIED"},"expirationTime":"expirationTime","spdxPackage":{"copyright":"copyright","filesLicenseInfo":["filesLicenseInfo","filesLicenseInfo"],"analyzed":True,"externalRefs":[{"comment":"comment","category":"CATEGORY_UNSPECIFIED","type":"type","locator":"locator"},{"comment":"comment","category":"CATEGORY_UNSPECIFIED","type":"type","locator":"locator"}],"downloadLocation":"downloadLocation","originator":"originator","title":"title","homePage":"homePage","packageType":"packageType","version":"version","verificationCode":"verificationCode","detailedDescription":"detailedDescription","supplier":"supplier","attribution":"attribution","checksum":"checksum","licenseDeclared":{"comments":"comments","expression":"expression"},"summaryDescription":"summaryDescription"},"name":"name","sbom":{"dataLicence":"dataLicence","spdxVersion":"spdxVersion"},"relatedUrl":[{"label":"label","url":"url"},{"label":"label","url":"url"}],"vulnerabilityType":{"cwe":["cwe","cwe"],"severity":"SEVERITY_UNSPECIFIED","cvssScore":1.4658129,"cvssVersion":"CVSS_VERSION_UNSPECIFIED","details":[{"minAffectedVersion":{"inclusive":True,"kind":"NORMAL","name":"name","epoch":6,"revision":"revision"},"package":"package","maxAffectedVersion":{"inclusive":True,"kind":"NORMAL","name":"name","epoch":6,"revision":"revision"},"vendor":"vendor","description":"description","isObsolete":True,"source":"source","cpeUri":"cpeUri","fixedLocation":{"package":"package","fileLocation":[{"filePath":"filePath"},{"filePath":"filePath"}],"cpeUri":"cpeUri","version":{"inclusive":True,"kind":"NORMAL","name":"name","epoch":6,"revision":"revision"}},"packageType":"packageType","severityName":"severityName"},{"minAffectedVersion":{"inclusive":True,"kind":"NORMAL","name":"name","epoch":6,"revision":"revision"},"package":"package","maxAffectedVersion":{"inclusive":True,"kind":"NORMAL","name":"name","epoch":6,"revision":"revision"},"vendor":"vendor","description":"description","isObsolete":True,"source":"source","cpeUri":"cpeUri","fixedLocation":{"package":"package","fileLocation":[{"filePath":"filePath"},{"filePath":"filePath"}],"cpeUri":"cpeUri","version":{"inclusive":True,"kind":"NORMAL","name":"name","epoch":6,"revision":"revision"}},"packageType":"packageType","severityName":"severityName"}],"cvssV2":{"exploitabilityScore":5.637377,"confidentialityImpact":"IMPACT_UNSPECIFIED","attackComplexity":"ATTACK_COMPLEXITY_UNSPECIFIED","scope":"SCOPE_UNSPECIFIED","attackVector":"ATTACK_VECTOR_UNSPECIFIED","availabilityImpact":"IMPACT_UNSPECIFIED","integrityImpact":"IMPACT_UNSPECIFIED","baseScore":5.962134,"privilegesRequired":"PRIVILEGES_REQUIRED_UNSPECIFIED","impactScore":2.302136,"userInteraction":"USER_INTERACTION_UNSPECIFIED","authentication":"AUTHENTICATION_UNSPECIFIED"}}}
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
                    ('noteId', 'note_id_example'),
                    ('parent', 'parent_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1alpha1/{name}/notes'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_containeranalysis_providers_notes_delete(client):
    """Test case for containeranalysis_providers_notes_delete

    
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
        path='/v1alpha1/{name}'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_containeranalysis_providers_notes_get(client):
    """Test case for containeranalysis_providers_notes_get

    
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
        path='/v1alpha1/{name}'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_containeranalysis_providers_notes_get_iam_policy(client):
    """Test case for containeranalysis_providers_notes_get_iam_policy

    
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
        path='/v1alpha1/{resourceget_iam_polic}'.format(resource='resource_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_containeranalysis_providers_notes_list(client):
    """Test case for containeranalysis_providers_notes_list

    
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
                    ('pageToken', 'page_token_example'),
                    ('parent', 'parent_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1alpha1/{name}/notes'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_containeranalysis_providers_notes_occurrences_list(client):
    """Test case for containeranalysis_providers_notes_occurrences_list

    
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
        path='/v1alpha1/{name}/occurrences'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_containeranalysis_providers_notes_patch(client):
    """Test case for containeranalysis_providers_notes_patch

    
    """
    body = {"longDescription":"longDescription","package":{"license":{"comments":"comments","expression":"expression"},"digest":[{"digestBytes":"digestBytes","algo":"algo"},{"digestBytes":"digestBytes","algo":"algo"}],"name":"name","description":"description","distribution":[{"latestVersion":{"inclusive":True,"kind":"NORMAL","name":"name","epoch":6,"revision":"revision"},"description":"description","cpeUri":"cpeUri","maintainer":"maintainer","url":"url","architecture":"ARCHITECTURE_UNSPECIFIED"},{"latestVersion":{"inclusive":True,"kind":"NORMAL","name":"name","epoch":6,"revision":"revision"},"description":"description","cpeUri":"cpeUri","maintainer":"maintainer","url":"url","architecture":"ARCHITECTURE_UNSPECIFIED"}],"cpeUri":"cpeUri","packageType":"packageType","version":{"inclusive":True,"kind":"NORMAL","name":"name","epoch":6,"revision":"revision"},"maintainer":"maintainer","url":"url","architecture":"ARCHITECTURE_UNSPECIFIED"},"upgrade":{"package":"package","version":{"inclusive":True,"kind":"NORMAL","name":"name","epoch":6,"revision":"revision"},"distributions":[{"severity":"severity","cve":["cve","cve"],"classification":"classification","cpeUri":"cpeUri"},{"severity":"severity","cve":["cve","cve"],"classification":"classification","cpeUri":"cpeUri"}]},"kind":"KIND_UNSPECIFIED","sbomReference":{"format":"format","version":"version"},"vulnerabilityAssessment":{"longDescription":"longDescription","assessment":{"longDescription":"longDescription","cve":"cve","vulnerabilityId":"vulnerabilityId","relatedUris":[{"label":"label","uri":"uri"},{"label":"label","uri":"uri"}],"remediations":[{"remediationType":"REMEDIATION_TYPE_UNSPECIFIED","remediationUri":{"label":"label","uri":"uri"},"details":"details"},{"remediationType":"REMEDIATION_TYPE_UNSPECIFIED","remediationUri":{"label":"label","uri":"uri"},"details":"details"}],"impacts":["impacts","impacts"],"justification":{"justificationType":"JUSTIFICATION_TYPE_UNSPECIFIED","details":"details"},"shortDescription":"shortDescription","state":"STATE_UNSPECIFIED"},"product":{"identifierHelper":{"field":"IDENTIFIER_HELPER_FIELD_UNSPECIFIED","genericUri":"genericUri"},"name":"name","id":"id"},"publisher":{"issuingAuthority":"issuingAuthority","name":"name","publisherNamespace":"publisherNamespace"},"shortDescription":"shortDescription","languageCode":"languageCode","title":"title"},"attestationAuthority":{"hint":{"humanReadableName":"humanReadableName"}},"baseImage":{"resourceUrl":"resourceUrl","fingerprint":{"v1Name":"v1Name","v2Blob":["v2Blob","v2Blob"],"v2Name":"v2Name"}},"dsseAttestation":{"hint":{"humanReadableName":"humanReadableName"}},"updateTime":"updateTime","shortDescription":"shortDescription","spdxRelationship":{"type":"RELATIONSHIP_TYPE_UNSPECIFIED"},"spdxFile":{"checksum":["checksum","checksum"],"title":"title","fileType":"FILE_TYPE_UNSPECIFIED"},"deployable":{"resourceUri":["resourceUri","resourceUri"]},"createTime":"createTime","buildType":{"signature":{"signature":"signature","keyId":"keyId","publicKey":"publicKey","keyType":"KEY_TYPE_UNSPECIFIED"},"builderVersion":"builderVersion"},"compliance":{"remediation":"remediation","cisBenchmark":{"severity":"SEVERITY_UNSPECIFIED","profileLevel":0},"scanInstructions":"scanInstructions","description":"description","title":"title","rationale":"rationale","version":[{"benchmarkDocument":"benchmarkDocument","cpeUri":"cpeUri","version":"version"},{"benchmarkDocument":"benchmarkDocument","cpeUri":"cpeUri","version":"version"}]},"discovery":{"analysisKind":"KIND_UNSPECIFIED"},"expirationTime":"expirationTime","spdxPackage":{"copyright":"copyright","filesLicenseInfo":["filesLicenseInfo","filesLicenseInfo"],"analyzed":True,"externalRefs":[{"comment":"comment","category":"CATEGORY_UNSPECIFIED","type":"type","locator":"locator"},{"comment":"comment","category":"CATEGORY_UNSPECIFIED","type":"type","locator":"locator"}],"downloadLocation":"downloadLocation","originator":"originator","title":"title","homePage":"homePage","packageType":"packageType","version":"version","verificationCode":"verificationCode","detailedDescription":"detailedDescription","supplier":"supplier","attribution":"attribution","checksum":"checksum","licenseDeclared":{"comments":"comments","expression":"expression"},"summaryDescription":"summaryDescription"},"name":"name","sbom":{"dataLicence":"dataLicence","spdxVersion":"spdxVersion"},"relatedUrl":[{"label":"label","url":"url"},{"label":"label","url":"url"}],"vulnerabilityType":{"cwe":["cwe","cwe"],"severity":"SEVERITY_UNSPECIFIED","cvssScore":1.4658129,"cvssVersion":"CVSS_VERSION_UNSPECIFIED","details":[{"minAffectedVersion":{"inclusive":True,"kind":"NORMAL","name":"name","epoch":6,"revision":"revision"},"package":"package","maxAffectedVersion":{"inclusive":True,"kind":"NORMAL","name":"name","epoch":6,"revision":"revision"},"vendor":"vendor","description":"description","isObsolete":True,"source":"source","cpeUri":"cpeUri","fixedLocation":{"package":"package","fileLocation":[{"filePath":"filePath"},{"filePath":"filePath"}],"cpeUri":"cpeUri","version":{"inclusive":True,"kind":"NORMAL","name":"name","epoch":6,"revision":"revision"}},"packageType":"packageType","severityName":"severityName"},{"minAffectedVersion":{"inclusive":True,"kind":"NORMAL","name":"name","epoch":6,"revision":"revision"},"package":"package","maxAffectedVersion":{"inclusive":True,"kind":"NORMAL","name":"name","epoch":6,"revision":"revision"},"vendor":"vendor","description":"description","isObsolete":True,"source":"source","cpeUri":"cpeUri","fixedLocation":{"package":"package","fileLocation":[{"filePath":"filePath"},{"filePath":"filePath"}],"cpeUri":"cpeUri","version":{"inclusive":True,"kind":"NORMAL","name":"name","epoch":6,"revision":"revision"}},"packageType":"packageType","severityName":"severityName"}],"cvssV2":{"exploitabilityScore":5.637377,"confidentialityImpact":"IMPACT_UNSPECIFIED","attackComplexity":"ATTACK_COMPLEXITY_UNSPECIFIED","scope":"SCOPE_UNSPECIFIED","attackVector":"ATTACK_VECTOR_UNSPECIFIED","availabilityImpact":"IMPACT_UNSPECIFIED","integrityImpact":"IMPACT_UNSPECIFIED","baseScore":5.962134,"privilegesRequired":"PRIVILEGES_REQUIRED_UNSPECIFIED","impactScore":2.302136,"userInteraction":"USER_INTERACTION_UNSPECIFIED","authentication":"AUTHENTICATION_UNSPECIFIED"}}}
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
        path='/v1alpha1/{name}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_containeranalysis_providers_notes_set_iam_policy(client):
    """Test case for containeranalysis_providers_notes_set_iam_policy

    
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
        path='/v1alpha1/{resourceset_iam_polic}'.format(resource='resource_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_containeranalysis_providers_notes_test_iam_permissions(client):
    """Test case for containeranalysis_providers_notes_test_iam_permissions

    
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
        path='/v1alpha1/{resourcetest_iam_permission}'.format(resource='resource_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

