# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.batch_create_notes_request import BatchCreateNotesRequest
from openapi_server.models.batch_create_notes_response import BatchCreateNotesResponse
from openapi_server.models.batch_create_occurrences_request import BatchCreateOccurrencesRequest
from openapi_server.models.batch_create_occurrences_response import BatchCreateOccurrencesResponse
from openapi_server.models.export_sbom_response import ExportSBOMResponse
from openapi_server.models.get_iam_policy_request import GetIamPolicyRequest
from openapi_server.models.list_note_occurrences_response import ListNoteOccurrencesResponse
from openapi_server.models.list_notes_response import ListNotesResponse
from openapi_server.models.list_occurrences_response import ListOccurrencesResponse
from openapi_server.models.note import Note
from openapi_server.models.occurrence import Occurrence
from openapi_server.models.packages_summary_response import PackagesSummaryResponse
from openapi_server.models.policy import Policy
from openapi_server.models.set_iam_policy_request import SetIamPolicyRequest
from openapi_server.models.test_iam_permissions_request import TestIamPermissionsRequest
from openapi_server.models.test_iam_permissions_response import TestIamPermissionsResponse
from openapi_server.models.vulnerability_occurrences_summary import VulnerabilityOccurrencesSummary


pytestmark = pytest.mark.asyncio

async def test_containeranalysis_projects_notes_batch_create(client):
    """Test case for containeranalysis_projects_notes_batch_create

    
    """
    body = {"notes":{"key":{"longDescription":"longDescription","package":{"license":{"comments":"comments","expression":"expression"},"digest":[{"digestBytes":"digestBytes","algo":"algo"},{"digestBytes":"digestBytes","algo":"algo"}],"name":"name","description":"description","distribution":[{"latestVersion":{"inclusive":True,"kind":"VERSION_KIND_UNSPECIFIED","name":"name","epoch":1,"revision":"revision"},"description":"description","cpeUri":"cpeUri","maintainer":"maintainer","url":"url","architecture":"ARCHITECTURE_UNSPECIFIED"},{"latestVersion":{"inclusive":True,"kind":"VERSION_KIND_UNSPECIFIED","name":"name","epoch":1,"revision":"revision"},"description":"description","cpeUri":"cpeUri","maintainer":"maintainer","url":"url","architecture":"ARCHITECTURE_UNSPECIFIED"}],"cpeUri":"cpeUri","packageType":"packageType","version":{"inclusive":True,"kind":"VERSION_KIND_UNSPECIFIED","name":"name","epoch":1,"revision":"revision"},"maintainer":"maintainer","url":"url","architecture":"ARCHITECTURE_UNSPECIFIED"},"kind":"NOTE_KIND_UNSPECIFIED","sbomReference":{"format":"format","version":"version"},"vulnerabilityAssessment":{"longDescription":"longDescription","assessment":{"longDescription":"longDescription","cve":"cve","vulnerabilityId":"vulnerabilityId","relatedUris":[{"label":"label","url":"url"},{"label":"label","url":"url"}],"remediations":[{"remediationType":"REMEDIATION_TYPE_UNSPECIFIED","remediationUri":{"label":"label","url":"url"},"details":"details"},{"remediationType":"REMEDIATION_TYPE_UNSPECIFIED","remediationUri":{"label":"label","url":"url"},"details":"details"}],"impacts":["impacts","impacts"],"justification":{"justificationType":"JUSTIFICATION_TYPE_UNSPECIFIED","details":"details"},"shortDescription":"shortDescription","state":"STATE_UNSPECIFIED"},"product":{"genericUri":"genericUri","name":"name","id":"id"},"publisher":{"issuingAuthority":"issuingAuthority","name":"name","publisherNamespace":"publisherNamespace"},"shortDescription":"shortDescription","languageCode":"languageCode","title":"title"},"attestationAuthority":{"hint":{"humanReadableName":"humanReadableName"}},"baseImage":{"resourceUrl":"resourceUrl","fingerprint":{"v1Name":"v1Name","v2Blob":["v2Blob","v2Blob"],"v2Name":"v2Name"}},"intoto":{"expectedMaterials":[{"artifactRule":["artifactRule","artifactRule"]},{"artifactRule":["artifactRule","artifactRule"]}],"signingKeys":[{"publicKeyValue":"publicKeyValue","keyId":"keyId","keyType":"keyType","keyScheme":"keyScheme"},{"publicKeyValue":"publicKeyValue","keyId":"keyId","keyType":"keyType","keyScheme":"keyScheme"}],"expectedProducts":[{"artifactRule":["artifactRule","artifactRule"]},{"artifactRule":["artifactRule","artifactRule"]}],"stepName":"stepName","threshold":"threshold","expectedCommand":["expectedCommand","expectedCommand"]},"updateTime":"updateTime","shortDescription":"shortDescription","spdxRelationship":{"type":"RELATIONSHIP_TYPE_UNSPECIFIED"},"vulnerability":{"cwe":["cwe","cwe"],"severity":"SEVERITY_UNSPECIFIED","cvssScore":0.8008282,"cvssV3":{"exploitabilityScore":1.4658129,"confidentialityImpact":"IMPACT_UNSPECIFIED","attackComplexity":"ATTACK_COMPLEXITY_UNSPECIFIED","scope":"SCOPE_UNSPECIFIED","attackVector":"ATTACK_VECTOR_UNSPECIFIED","availabilityImpact":"IMPACT_UNSPECIFIED","integrityImpact":"IMPACT_UNSPECIFIED","baseScore":6.0274563,"privilegesRequired":"PRIVILEGES_REQUIRED_UNSPECIFIED","impactScore":5.962134,"userInteraction":"USER_INTERACTION_UNSPECIFIED"},"cvssVersion":"CVSS_VERSION_UNSPECIFIED","details":[{"minAffectedVersion":{"inclusive":True,"kind":"VERSION_KIND_UNSPECIFIED","name":"name","epoch":1,"revision":"revision"},"package":"package","maxAffectedVersion":{"inclusive":True,"kind":"VERSION_KIND_UNSPECIFIED","name":"name","epoch":1,"revision":"revision"},"vendor":"vendor","description":"description","sourceUpdateTime":"sourceUpdateTime","isObsolete":True,"source":"source","cpeUri":"cpeUri","fixedLocation":{"package":"package","cpeUri":"cpeUri","version":{"inclusive":True,"kind":"VERSION_KIND_UNSPECIFIED","name":"name","epoch":1,"revision":"revision"}},"packageType":"packageType","severityName":"severityName"},{"minAffectedVersion":{"inclusive":True,"kind":"VERSION_KIND_UNSPECIFIED","name":"name","epoch":1,"revision":"revision"},"package":"package","maxAffectedVersion":{"inclusive":True,"kind":"VERSION_KIND_UNSPECIFIED","name":"name","epoch":1,"revision":"revision"},"vendor":"vendor","description":"description","sourceUpdateTime":"sourceUpdateTime","isObsolete":True,"source":"source","cpeUri":"cpeUri","fixedLocation":{"package":"package","cpeUri":"cpeUri","version":{"inclusive":True,"kind":"VERSION_KIND_UNSPECIFIED","name":"name","epoch":1,"revision":"revision"}},"packageType":"packageType","severityName":"severityName"}],"sourceUpdateTime":"sourceUpdateTime","cvssV2":{"exploitabilityScore":2.302136,"confidentialityImpact":"IMPACT_UNSPECIFIED","attackComplexity":"ATTACK_COMPLEXITY_UNSPECIFIED","scope":"SCOPE_UNSPECIFIED","attackVector":"ATTACK_VECTOR_UNSPECIFIED","availabilityImpact":"IMPACT_UNSPECIFIED","integrityImpact":"IMPACT_UNSPECIFIED","baseScore":5.637377,"privilegesRequired":"PRIVILEGES_REQUIRED_UNSPECIFIED","impactScore":7.0614014,"userInteraction":"USER_INTERACTION_UNSPECIFIED","authentication":"AUTHENTICATION_UNSPECIFIED"},"windowsDetails":[{"name":"name","description":"description","fixingKbs":[{"name":"name","url":"url"},{"name":"name","url":"url"}],"cpeUri":"cpeUri"},{"name":"name","description":"description","fixingKbs":[{"name":"name","url":"url"},{"name":"name","url":"url"}],"cpeUri":"cpeUri"}]},"relatedNoteNames":["relatedNoteNames","relatedNoteNames"],"spdxFile":{"checksum":["checksum","checksum"],"title":"title","fileType":"FILE_TYPE_UNSPECIFIED"},"deployable":{"resourceUri":["resourceUri","resourceUri"]},"build":{"signature":{"signature":"signature","keyId":"keyId","publicKey":"publicKey","keyType":"KEY_TYPE_UNSPECIFIED"},"builderVersion":"builderVersion"},"createTime":"createTime","discovery":{"analysisKind":"NOTE_KIND_UNSPECIFIED"},"expirationTime":"expirationTime","spdxPackage":{"copyright":"copyright","filesLicenseInfo":["filesLicenseInfo","filesLicenseInfo"],"analyzed":True,"externalRefs":[{"comment":"comment","category":"CATEGORY_UNSPECIFIED","type":"type","locator":"locator"},{"comment":"comment","category":"CATEGORY_UNSPECIFIED","type":"type","locator":"locator"}],"downloadLocation":"downloadLocation","originator":"originator","title":"title","homePage":"homePage","packageType":"packageType","version":"version","verificationCode":"verificationCode","detailedDescription":"detailedDescription","supplier":"supplier","attribution":"attribution","checksum":"checksum","licenseDeclared":{"comments":"comments","expression":"expression"},"summaryDescription":"summaryDescription"},"name":"name","sbom":{"dataLicence":"dataLicence","spdxVersion":"spdxVersion"},"relatedUrl":[{"label":"label","url":"url"},{"label":"label","url":"url"}]}}}
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
        path='/v1beta1/{parent}/notes:batchCreate'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_containeranalysis_projects_notes_create(client):
    """Test case for containeranalysis_projects_notes_create

    
    """
    body = {"longDescription":"longDescription","package":{"license":{"comments":"comments","expression":"expression"},"digest":[{"digestBytes":"digestBytes","algo":"algo"},{"digestBytes":"digestBytes","algo":"algo"}],"name":"name","description":"description","distribution":[{"latestVersion":{"inclusive":True,"kind":"VERSION_KIND_UNSPECIFIED","name":"name","epoch":1,"revision":"revision"},"description":"description","cpeUri":"cpeUri","maintainer":"maintainer","url":"url","architecture":"ARCHITECTURE_UNSPECIFIED"},{"latestVersion":{"inclusive":True,"kind":"VERSION_KIND_UNSPECIFIED","name":"name","epoch":1,"revision":"revision"},"description":"description","cpeUri":"cpeUri","maintainer":"maintainer","url":"url","architecture":"ARCHITECTURE_UNSPECIFIED"}],"cpeUri":"cpeUri","packageType":"packageType","version":{"inclusive":True,"kind":"VERSION_KIND_UNSPECIFIED","name":"name","epoch":1,"revision":"revision"},"maintainer":"maintainer","url":"url","architecture":"ARCHITECTURE_UNSPECIFIED"},"kind":"NOTE_KIND_UNSPECIFIED","sbomReference":{"format":"format","version":"version"},"vulnerabilityAssessment":{"longDescription":"longDescription","assessment":{"longDescription":"longDescription","cve":"cve","vulnerabilityId":"vulnerabilityId","relatedUris":[{"label":"label","url":"url"},{"label":"label","url":"url"}],"remediations":[{"remediationType":"REMEDIATION_TYPE_UNSPECIFIED","remediationUri":{"label":"label","url":"url"},"details":"details"},{"remediationType":"REMEDIATION_TYPE_UNSPECIFIED","remediationUri":{"label":"label","url":"url"},"details":"details"}],"impacts":["impacts","impacts"],"justification":{"justificationType":"JUSTIFICATION_TYPE_UNSPECIFIED","details":"details"},"shortDescription":"shortDescription","state":"STATE_UNSPECIFIED"},"product":{"genericUri":"genericUri","name":"name","id":"id"},"publisher":{"issuingAuthority":"issuingAuthority","name":"name","publisherNamespace":"publisherNamespace"},"shortDescription":"shortDescription","languageCode":"languageCode","title":"title"},"attestationAuthority":{"hint":{"humanReadableName":"humanReadableName"}},"baseImage":{"resourceUrl":"resourceUrl","fingerprint":{"v1Name":"v1Name","v2Blob":["v2Blob","v2Blob"],"v2Name":"v2Name"}},"intoto":{"expectedMaterials":[{"artifactRule":["artifactRule","artifactRule"]},{"artifactRule":["artifactRule","artifactRule"]}],"signingKeys":[{"publicKeyValue":"publicKeyValue","keyId":"keyId","keyType":"keyType","keyScheme":"keyScheme"},{"publicKeyValue":"publicKeyValue","keyId":"keyId","keyType":"keyType","keyScheme":"keyScheme"}],"expectedProducts":[{"artifactRule":["artifactRule","artifactRule"]},{"artifactRule":["artifactRule","artifactRule"]}],"stepName":"stepName","threshold":"threshold","expectedCommand":["expectedCommand","expectedCommand"]},"updateTime":"updateTime","shortDescription":"shortDescription","spdxRelationship":{"type":"RELATIONSHIP_TYPE_UNSPECIFIED"},"vulnerability":{"cwe":["cwe","cwe"],"severity":"SEVERITY_UNSPECIFIED","cvssScore":0.8008282,"cvssV3":{"exploitabilityScore":1.4658129,"confidentialityImpact":"IMPACT_UNSPECIFIED","attackComplexity":"ATTACK_COMPLEXITY_UNSPECIFIED","scope":"SCOPE_UNSPECIFIED","attackVector":"ATTACK_VECTOR_UNSPECIFIED","availabilityImpact":"IMPACT_UNSPECIFIED","integrityImpact":"IMPACT_UNSPECIFIED","baseScore":6.0274563,"privilegesRequired":"PRIVILEGES_REQUIRED_UNSPECIFIED","impactScore":5.962134,"userInteraction":"USER_INTERACTION_UNSPECIFIED"},"cvssVersion":"CVSS_VERSION_UNSPECIFIED","details":[{"minAffectedVersion":{"inclusive":True,"kind":"VERSION_KIND_UNSPECIFIED","name":"name","epoch":1,"revision":"revision"},"package":"package","maxAffectedVersion":{"inclusive":True,"kind":"VERSION_KIND_UNSPECIFIED","name":"name","epoch":1,"revision":"revision"},"vendor":"vendor","description":"description","sourceUpdateTime":"sourceUpdateTime","isObsolete":True,"source":"source","cpeUri":"cpeUri","fixedLocation":{"package":"package","cpeUri":"cpeUri","version":{"inclusive":True,"kind":"VERSION_KIND_UNSPECIFIED","name":"name","epoch":1,"revision":"revision"}},"packageType":"packageType","severityName":"severityName"},{"minAffectedVersion":{"inclusive":True,"kind":"VERSION_KIND_UNSPECIFIED","name":"name","epoch":1,"revision":"revision"},"package":"package","maxAffectedVersion":{"inclusive":True,"kind":"VERSION_KIND_UNSPECIFIED","name":"name","epoch":1,"revision":"revision"},"vendor":"vendor","description":"description","sourceUpdateTime":"sourceUpdateTime","isObsolete":True,"source":"source","cpeUri":"cpeUri","fixedLocation":{"package":"package","cpeUri":"cpeUri","version":{"inclusive":True,"kind":"VERSION_KIND_UNSPECIFIED","name":"name","epoch":1,"revision":"revision"}},"packageType":"packageType","severityName":"severityName"}],"sourceUpdateTime":"sourceUpdateTime","cvssV2":{"exploitabilityScore":2.302136,"confidentialityImpact":"IMPACT_UNSPECIFIED","attackComplexity":"ATTACK_COMPLEXITY_UNSPECIFIED","scope":"SCOPE_UNSPECIFIED","attackVector":"ATTACK_VECTOR_UNSPECIFIED","availabilityImpact":"IMPACT_UNSPECIFIED","integrityImpact":"IMPACT_UNSPECIFIED","baseScore":5.637377,"privilegesRequired":"PRIVILEGES_REQUIRED_UNSPECIFIED","impactScore":7.0614014,"userInteraction":"USER_INTERACTION_UNSPECIFIED","authentication":"AUTHENTICATION_UNSPECIFIED"},"windowsDetails":[{"name":"name","description":"description","fixingKbs":[{"name":"name","url":"url"},{"name":"name","url":"url"}],"cpeUri":"cpeUri"},{"name":"name","description":"description","fixingKbs":[{"name":"name","url":"url"},{"name":"name","url":"url"}],"cpeUri":"cpeUri"}]},"relatedNoteNames":["relatedNoteNames","relatedNoteNames"],"spdxFile":{"checksum":["checksum","checksum"],"title":"title","fileType":"FILE_TYPE_UNSPECIFIED"},"deployable":{"resourceUri":["resourceUri","resourceUri"]},"build":{"signature":{"signature":"signature","keyId":"keyId","publicKey":"publicKey","keyType":"KEY_TYPE_UNSPECIFIED"},"builderVersion":"builderVersion"},"createTime":"createTime","discovery":{"analysisKind":"NOTE_KIND_UNSPECIFIED"},"expirationTime":"expirationTime","spdxPackage":{"copyright":"copyright","filesLicenseInfo":["filesLicenseInfo","filesLicenseInfo"],"analyzed":True,"externalRefs":[{"comment":"comment","category":"CATEGORY_UNSPECIFIED","type":"type","locator":"locator"},{"comment":"comment","category":"CATEGORY_UNSPECIFIED","type":"type","locator":"locator"}],"downloadLocation":"downloadLocation","originator":"originator","title":"title","homePage":"homePage","packageType":"packageType","version":"version","verificationCode":"verificationCode","detailedDescription":"detailedDescription","supplier":"supplier","attribution":"attribution","checksum":"checksum","licenseDeclared":{"comments":"comments","expression":"expression"},"summaryDescription":"summaryDescription"},"name":"name","sbom":{"dataLicence":"dataLicence","spdxVersion":"spdxVersion"},"relatedUrl":[{"label":"label","url":"url"},{"label":"label","url":"url"}]}
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
                    ('noteId', 'note_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta1/{parent}/notes'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_containeranalysis_projects_notes_list(client):
    """Test case for containeranalysis_projects_notes_list

    
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
        path='/v1beta1/{parent}/notes'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_containeranalysis_projects_notes_occurrences_list(client):
    """Test case for containeranalysis_projects_notes_occurrences_list

    
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
        path='/v1beta1/{name}/occurrences'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_containeranalysis_projects_occurrences_batch_create(client):
    """Test case for containeranalysis_projects_occurrences_batch_create

    
    """
    body = {"occurrences":[{"discovered":{"discovered":{"lastScanTime":"lastScanTime","sbomStatus":{"sbomState":"SBOM_STATE_UNSPECIFIED","error":"error"},"analysisCompleted":{"analysisType":["analysisType","analysisType"]},"analysisError":[{"code":6,"details":[{"key":""},{"key":""}],"message":"message"},{"code":6,"details":[{"key":""},{"key":""}],"message":"message"}],"analysisStatusError":{"code":6,"details":[{"key":""},{"key":""}],"message":"message"},"continuousAnalysis":"CONTINUOUS_ANALYSIS_UNSPECIFIED","lastAnalysisTime":"lastAnalysisTime","analysisStatus":"ANALYSIS_STATUS_UNSPECIFIED"}},"attestation":{"attestation":{"genericSignedAttestation":{"serializedPayload":"serializedPayload","contentType":"CONTENT_TYPE_UNSPECIFIED","signatures":[{"signature":"signature","publicKeyId":"publicKeyId"},{"signature":"signature","publicKeyId":"publicKeyId"}]},"pgpSignedAttestation":{"pgpKeyId":"pgpKeyId","signature":"signature","contentType":"CONTENT_TYPE_UNSPECIFIED"}}},"resource":{"name":"name","uri":"uri","contentHash":{"type":"HASH_TYPE_UNSPECIFIED","value":"value"}},"kind":"NOTE_KIND_UNSPECIFIED","noteName":"noteName","sbomReference":{"payloadType":"payloadType","payload":{"predicate":{"referrerId":"referrerId","digest":{"key":"digest"},"location":"location","mimeType":"mimeType"},"predicateType":"predicateType","subject":[{"digest":{"key":"digest"},"name":"name"},{"digest":{"key":"digest"},"name":"name"}],"_type":"_type"},"signatures":[{"sig":"sig","keyid":"keyid"},{"sig":"sig","keyid":"keyid"}]},"intoto":{"signed":{"environment":{"customValues":{"key":"customValues"}},"materials":[{"hashes":{"sha256":"sha256"},"resourceUri":"resourceUri"},{"hashes":{"sha256":"sha256"},"resourceUri":"resourceUri"}],"byproducts":{"customValues":{"key":"customValues"}},"command":["command","command"],"products":[{"hashes":{"sha256":"sha256"},"resourceUri":"resourceUri"},{"hashes":{"sha256":"sha256"},"resourceUri":"resourceUri"}]},"signatures":[{"sig":"sig","keyid":"keyid"},{"sig":"sig","keyid":"keyid"}]},"updateTime":"updateTime","spdxRelationship":{"comment":"comment","source":"source","type":"RELATIONSHIP_TYPE_UNSPECIFIED","target":"target"},"vulnerability":{"longDescription":"longDescription","severity":"SEVERITY_UNSPECIFIED","cvssV2":{"exploitabilityScore":2.302136,"confidentialityImpact":"IMPACT_UNSPECIFIED","attackComplexity":"ATTACK_COMPLEXITY_UNSPECIFIED","scope":"SCOPE_UNSPECIFIED","attackVector":"ATTACK_VECTOR_UNSPECIFIED","availabilityImpact":"IMPACT_UNSPECIFIED","integrityImpact":"IMPACT_UNSPECIFIED","baseScore":5.637377,"privilegesRequired":"PRIVILEGES_REQUIRED_UNSPECIFIED","impactScore":7.0614014,"userInteraction":"USER_INTERACTION_UNSPECIFIED","authentication":"AUTHENTICATION_UNSPECIFIED"},"shortDescription":"shortDescription","type":"type","cvssScore":5.962134,"cvssV3":{"exploitabilityScore":2.302136,"confidentialityImpact":"IMPACT_UNSPECIFIED","attackComplexity":"ATTACK_COMPLEXITY_UNSPECIFIED","scope":"SCOPE_UNSPECIFIED","attackVector":"ATTACK_VECTOR_UNSPECIFIED","availabilityImpact":"IMPACT_UNSPECIFIED","integrityImpact":"IMPACT_UNSPECIFIED","baseScore":5.637377,"privilegesRequired":"PRIVILEGES_REQUIRED_UNSPECIFIED","impactScore":7.0614014,"userInteraction":"USER_INTERACTION_UNSPECIFIED","authentication":"AUTHENTICATION_UNSPECIFIED"},"cvssVersion":"CVSS_VERSION_UNSPECIFIED","relatedUrls":[{"label":"label","url":"url"},{"label":"label","url":"url"}],"packageIssue":[{"affectedLocation":{"package":"package","cpeUri":"cpeUri","version":{"inclusive":True,"kind":"VERSION_KIND_UNSPECIFIED","name":"name","epoch":1,"revision":"revision"}},"effectiveSeverity":"SEVERITY_UNSPECIFIED","fixedLocation":{"package":"package","cpeUri":"cpeUri","version":{"inclusive":True,"kind":"VERSION_KIND_UNSPECIFIED","name":"name","epoch":1,"revision":"revision"}},"packageType":"packageType","severityName":"severityName"},{"affectedLocation":{"package":"package","cpeUri":"cpeUri","version":{"inclusive":True,"kind":"VERSION_KIND_UNSPECIFIED","name":"name","epoch":1,"revision":"revision"}},"effectiveSeverity":"SEVERITY_UNSPECIFIED","fixedLocation":{"package":"package","cpeUri":"cpeUri","version":{"inclusive":True,"kind":"VERSION_KIND_UNSPECIFIED","name":"name","epoch":1,"revision":"revision"}},"packageType":"packageType","severityName":"severityName"}],"extraDetails":"extraDetails","effectiveSeverity":"SEVERITY_UNSPECIFIED","vexAssessment":{"cve":"cve","vulnerabilityId":"vulnerabilityId","relatedUris":[{"label":"label","url":"url"},{"label":"label","url":"url"}],"noteName":"noteName","remediations":[{"remediationType":"REMEDIATION_TYPE_UNSPECIFIED","remediationUri":{"label":"label","url":"url"},"details":"details"},{"remediationType":"REMEDIATION_TYPE_UNSPECIFIED","remediationUri":{"label":"label","url":"url"},"details":"details"}],"impacts":["impacts","impacts"],"justification":{"justificationType":"JUSTIFICATION_TYPE_UNSPECIFIED","details":"details"},"state":"STATE_UNSPECIFIED"}},"spdxFile":{"copyright":"copyright","filesLicenseInfo":["filesLicenseInfo","filesLicenseInfo"],"licenseConcluded":{"comments":"comments","expression":"expression"},"comment":"comment","contributors":["contributors","contributors"],"id":"id","attributions":["attributions","attributions"],"notice":"notice"},"remediation":"remediation","envelope":{"payloadType":"payloadType","payload":"payload","signatures":[{"sig":"sig","keyid":"keyid"},{"sig":"sig","keyid":"keyid"}]},"build":{"provenance":{"creator":"creator","triggerId":"triggerId","buildOptions":{"key":"buildOptions"},"sourceProvenance":{"additionalContexts":[{"git":{"revisionId":"revisionId","url":"url"},"gerrit":{"aliasContext":{"kind":"KIND_UNSPECIFIED","name":"name"},"revisionId":"revisionId","hostUri":"hostUri","gerritProject":"gerritProject"},"cloudRepo":{"aliasContext":{"kind":"KIND_UNSPECIFIED","name":"name"},"revisionId":"revisionId","repoId":{"uid":"uid","projectRepoId":{"repoName":"repoName","projectId":"projectId"}}},"labels":{"key":"labels"}},{"git":{"revisionId":"revisionId","url":"url"},"gerrit":{"aliasContext":{"kind":"KIND_UNSPECIFIED","name":"name"},"revisionId":"revisionId","hostUri":"hostUri","gerritProject":"gerritProject"},"cloudRepo":{"aliasContext":{"kind":"KIND_UNSPECIFIED","name":"name"},"revisionId":"revisionId","repoId":{"uid":"uid","projectRepoId":{"repoName":"repoName","projectId":"projectId"}}},"labels":{"key":"labels"}}],"artifactStorageSourceUri":"artifactStorageSourceUri","context":{"git":{"revisionId":"revisionId","url":"url"},"gerrit":{"aliasContext":{"kind":"KIND_UNSPECIFIED","name":"name"},"revisionId":"revisionId","hostUri":"hostUri","gerritProject":"gerritProject"},"cloudRepo":{"aliasContext":{"kind":"KIND_UNSPECIFIED","name":"name"},"revisionId":"revisionId","repoId":{"uid":"uid","projectRepoId":{"repoName":"repoName","projectId":"projectId"}}},"labels":{"key":"labels"}},"fileHashes":{"key":{"fileHash":[{"type":"HASH_TYPE_UNSPECIFIED","value":"value"},{"type":"HASH_TYPE_UNSPECIFIED","value":"value"}]}}},"createTime":"createTime","logsUri":"logsUri","builderVersion":"builderVersion","builtArtifacts":[{"names":["names","names"],"checksum":"checksum","id":"id"},{"names":["names","names"],"checksum":"checksum","id":"id"}],"startTime":"startTime","endTime":"endTime","id":"id","projectId":"projectId","commands":[{"args":["args","args"],"name":"name","id":"id","dir":"dir","env":["env","env"],"waitFor":["waitFor","waitFor"]},{"args":["args","args"],"name":"name","id":"id","dir":"dir","env":["env","env"],"waitFor":["waitFor","waitFor"]}]},"provenanceBytes":"provenanceBytes","inTotoSlsaProvenanceV1":{"predicate":{"runDetails":{"metadata":{"finishedOn":"finishedOn","invocationId":"invocationId","startedOn":"startedOn"},"builder":{"builderDependencies":[{"digest":{"key":"digest"},"name":"name","annotations":{"key":""},"downloadLocation":"downloadLocation","mediaType":"mediaType","uri":"uri","content":"content"},{"digest":{"key":"digest"},"name":"name","annotations":{"key":""},"downloadLocation":"downloadLocation","mediaType":"mediaType","uri":"uri","content":"content"}],"id":"id","version":{"key":"version"}},"byproducts":[{"digest":{"key":"digest"},"name":"name","annotations":{"key":""},"downloadLocation":"downloadLocation","mediaType":"mediaType","uri":"uri","content":"content"},{"digest":{"key":"digest"},"name":"name","annotations":{"key":""},"downloadLocation":"downloadLocation","mediaType":"mediaType","uri":"uri","content":"content"}]},"buildDefinition":{"buildType":"buildType","internalParameters":{"key":""},"resolvedDependencies":[{"digest":{"key":"digest"},"name":"name","annotations":{"key":""},"downloadLocation":"downloadLocation","mediaType":"mediaType","uri":"uri","content":"content"},{"digest":{"key":"digest"},"name":"name","annotations":{"key":""},"downloadLocation":"downloadLocation","mediaType":"mediaType","uri":"uri","content":"content"}],"externalParameters":{"key":""}}},"predicateType":"predicateType","subject":[{"digest":{"key":"digest"},"name":"name"},{"digest":{"key":"digest"},"name":"name"}],"_type":"_type"}},"createTime":"createTime","spdxPackage":{"sourceInfo":"sourceInfo","filename":"filename","licenseConcluded":{"comments":"comments","expression":"expression"},"comment":"comment","id":"id","title":"title","homePage":"homePage","packageType":"packageType","summaryDescription":"summaryDescription","version":"version"},"installation":{"installation":{"license":{"comments":"comments","expression":"expression"},"name":"name","location":[{"path":"path","cpeUri":"cpeUri","version":{"inclusive":True,"kind":"VERSION_KIND_UNSPECIFIED","name":"name","epoch":1,"revision":"revision"}},{"path":"path","cpeUri":"cpeUri","version":{"inclusive":True,"kind":"VERSION_KIND_UNSPECIFIED","name":"name","epoch":1,"revision":"revision"}}],"cpeUri":"cpeUri","packageType":"packageType","version":{"inclusive":True,"kind":"VERSION_KIND_UNSPECIFIED","name":"name","epoch":1,"revision":"revision"},"architecture":"ARCHITECTURE_UNSPECIFIED"}},"name":"name","sbom":{"creatorComment":"creatorComment","documentComment":"documentComment","licenseListVersion":"licenseListVersion","createTime":"createTime","creators":["creators","creators"],"namespace":"namespace","externalDocumentRefs":["externalDocumentRefs","externalDocumentRefs"],"id":"id","title":"title"},"deployment":{"deployment":{"address":"address","undeployTime":"undeployTime","userEmail":"userEmail","deployTime":"deployTime","resourceUri":["resourceUri","resourceUri"],"config":"config","platform":"PLATFORM_UNSPECIFIED"}},"derivedImage":{"derivedImage":{"distance":0,"fingerprint":{"v1Name":"v1Name","v2Blob":["v2Blob","v2Blob"],"v2Name":"v2Name"},"baseResourceUrl":"baseResourceUrl","layerInfo":[{"arguments":"arguments","directive":"DIRECTIVE_UNSPECIFIED"},{"arguments":"arguments","directive":"DIRECTIVE_UNSPECIFIED"}]}}},{"discovered":{"discovered":{"lastScanTime":"lastScanTime","sbomStatus":{"sbomState":"SBOM_STATE_UNSPECIFIED","error":"error"},"analysisCompleted":{"analysisType":["analysisType","analysisType"]},"analysisError":[{"code":6,"details":[{"key":""},{"key":""}],"message":"message"},{"code":6,"details":[{"key":""},{"key":""}],"message":"message"}],"analysisStatusError":{"code":6,"details":[{"key":""},{"key":""}],"message":"message"},"continuousAnalysis":"CONTINUOUS_ANALYSIS_UNSPECIFIED","lastAnalysisTime":"lastAnalysisTime","analysisStatus":"ANALYSIS_STATUS_UNSPECIFIED"}},"attestation":{"attestation":{"genericSignedAttestation":{"serializedPayload":"serializedPayload","contentType":"CONTENT_TYPE_UNSPECIFIED","signatures":[{"signature":"signature","publicKeyId":"publicKeyId"},{"signature":"signature","publicKeyId":"publicKeyId"}]},"pgpSignedAttestation":{"pgpKeyId":"pgpKeyId","signature":"signature","contentType":"CONTENT_TYPE_UNSPECIFIED"}}},"resource":{"name":"name","uri":"uri","contentHash":{"type":"HASH_TYPE_UNSPECIFIED","value":"value"}},"kind":"NOTE_KIND_UNSPECIFIED","noteName":"noteName","sbomReference":{"payloadType":"payloadType","payload":{"predicate":{"referrerId":"referrerId","digest":{"key":"digest"},"location":"location","mimeType":"mimeType"},"predicateType":"predicateType","subject":[{"digest":{"key":"digest"},"name":"name"},{"digest":{"key":"digest"},"name":"name"}],"_type":"_type"},"signatures":[{"sig":"sig","keyid":"keyid"},{"sig":"sig","keyid":"keyid"}]},"intoto":{"signed":{"environment":{"customValues":{"key":"customValues"}},"materials":[{"hashes":{"sha256":"sha256"},"resourceUri":"resourceUri"},{"hashes":{"sha256":"sha256"},"resourceUri":"resourceUri"}],"byproducts":{"customValues":{"key":"customValues"}},"command":["command","command"],"products":[{"hashes":{"sha256":"sha256"},"resourceUri":"resourceUri"},{"hashes":{"sha256":"sha256"},"resourceUri":"resourceUri"}]},"signatures":[{"sig":"sig","keyid":"keyid"},{"sig":"sig","keyid":"keyid"}]},"updateTime":"updateTime","spdxRelationship":{"comment":"comment","source":"source","type":"RELATIONSHIP_TYPE_UNSPECIFIED","target":"target"},"vulnerability":{"longDescription":"longDescription","severity":"SEVERITY_UNSPECIFIED","cvssV2":{"exploitabilityScore":2.302136,"confidentialityImpact":"IMPACT_UNSPECIFIED","attackComplexity":"ATTACK_COMPLEXITY_UNSPECIFIED","scope":"SCOPE_UNSPECIFIED","attackVector":"ATTACK_VECTOR_UNSPECIFIED","availabilityImpact":"IMPACT_UNSPECIFIED","integrityImpact":"IMPACT_UNSPECIFIED","baseScore":5.637377,"privilegesRequired":"PRIVILEGES_REQUIRED_UNSPECIFIED","impactScore":7.0614014,"userInteraction":"USER_INTERACTION_UNSPECIFIED","authentication":"AUTHENTICATION_UNSPECIFIED"},"shortDescription":"shortDescription","type":"type","cvssScore":5.962134,"cvssV3":{"exploitabilityScore":2.302136,"confidentialityImpact":"IMPACT_UNSPECIFIED","attackComplexity":"ATTACK_COMPLEXITY_UNSPECIFIED","scope":"SCOPE_UNSPECIFIED","attackVector":"ATTACK_VECTOR_UNSPECIFIED","availabilityImpact":"IMPACT_UNSPECIFIED","integrityImpact":"IMPACT_UNSPECIFIED","baseScore":5.637377,"privilegesRequired":"PRIVILEGES_REQUIRED_UNSPECIFIED","impactScore":7.0614014,"userInteraction":"USER_INTERACTION_UNSPECIFIED","authentication":"AUTHENTICATION_UNSPECIFIED"},"cvssVersion":"CVSS_VERSION_UNSPECIFIED","relatedUrls":[{"label":"label","url":"url"},{"label":"label","url":"url"}],"packageIssue":[{"affectedLocation":{"package":"package","cpeUri":"cpeUri","version":{"inclusive":True,"kind":"VERSION_KIND_UNSPECIFIED","name":"name","epoch":1,"revision":"revision"}},"effectiveSeverity":"SEVERITY_UNSPECIFIED","fixedLocation":{"package":"package","cpeUri":"cpeUri","version":{"inclusive":True,"kind":"VERSION_KIND_UNSPECIFIED","name":"name","epoch":1,"revision":"revision"}},"packageType":"packageType","severityName":"severityName"},{"affectedLocation":{"package":"package","cpeUri":"cpeUri","version":{"inclusive":True,"kind":"VERSION_KIND_UNSPECIFIED","name":"name","epoch":1,"revision":"revision"}},"effectiveSeverity":"SEVERITY_UNSPECIFIED","fixedLocation":{"package":"package","cpeUri":"cpeUri","version":{"inclusive":True,"kind":"VERSION_KIND_UNSPECIFIED","name":"name","epoch":1,"revision":"revision"}},"packageType":"packageType","severityName":"severityName"}],"extraDetails":"extraDetails","effectiveSeverity":"SEVERITY_UNSPECIFIED","vexAssessment":{"cve":"cve","vulnerabilityId":"vulnerabilityId","relatedUris":[{"label":"label","url":"url"},{"label":"label","url":"url"}],"noteName":"noteName","remediations":[{"remediationType":"REMEDIATION_TYPE_UNSPECIFIED","remediationUri":{"label":"label","url":"url"},"details":"details"},{"remediationType":"REMEDIATION_TYPE_UNSPECIFIED","remediationUri":{"label":"label","url":"url"},"details":"details"}],"impacts":["impacts","impacts"],"justification":{"justificationType":"JUSTIFICATION_TYPE_UNSPECIFIED","details":"details"},"state":"STATE_UNSPECIFIED"}},"spdxFile":{"copyright":"copyright","filesLicenseInfo":["filesLicenseInfo","filesLicenseInfo"],"licenseConcluded":{"comments":"comments","expression":"expression"},"comment":"comment","contributors":["contributors","contributors"],"id":"id","attributions":["attributions","attributions"],"notice":"notice"},"remediation":"remediation","envelope":{"payloadType":"payloadType","payload":"payload","signatures":[{"sig":"sig","keyid":"keyid"},{"sig":"sig","keyid":"keyid"}]},"build":{"provenance":{"creator":"creator","triggerId":"triggerId","buildOptions":{"key":"buildOptions"},"sourceProvenance":{"additionalContexts":[{"git":{"revisionId":"revisionId","url":"url"},"gerrit":{"aliasContext":{"kind":"KIND_UNSPECIFIED","name":"name"},"revisionId":"revisionId","hostUri":"hostUri","gerritProject":"gerritProject"},"cloudRepo":{"aliasContext":{"kind":"KIND_UNSPECIFIED","name":"name"},"revisionId":"revisionId","repoId":{"uid":"uid","projectRepoId":{"repoName":"repoName","projectId":"projectId"}}},"labels":{"key":"labels"}},{"git":{"revisionId":"revisionId","url":"url"},"gerrit":{"aliasContext":{"kind":"KIND_UNSPECIFIED","name":"name"},"revisionId":"revisionId","hostUri":"hostUri","gerritProject":"gerritProject"},"cloudRepo":{"aliasContext":{"kind":"KIND_UNSPECIFIED","name":"name"},"revisionId":"revisionId","repoId":{"uid":"uid","projectRepoId":{"repoName":"repoName","projectId":"projectId"}}},"labels":{"key":"labels"}}],"artifactStorageSourceUri":"artifactStorageSourceUri","context":{"git":{"revisionId":"revisionId","url":"url"},"gerrit":{"aliasContext":{"kind":"KIND_UNSPECIFIED","name":"name"},"revisionId":"revisionId","hostUri":"hostUri","gerritProject":"gerritProject"},"cloudRepo":{"aliasContext":{"kind":"KIND_UNSPECIFIED","name":"name"},"revisionId":"revisionId","repoId":{"uid":"uid","projectRepoId":{"repoName":"repoName","projectId":"projectId"}}},"labels":{"key":"labels"}},"fileHashes":{"key":{"fileHash":[{"type":"HASH_TYPE_UNSPECIFIED","value":"value"},{"type":"HASH_TYPE_UNSPECIFIED","value":"value"}]}}},"createTime":"createTime","logsUri":"logsUri","builderVersion":"builderVersion","builtArtifacts":[{"names":["names","names"],"checksum":"checksum","id":"id"},{"names":["names","names"],"checksum":"checksum","id":"id"}],"startTime":"startTime","endTime":"endTime","id":"id","projectId":"projectId","commands":[{"args":["args","args"],"name":"name","id":"id","dir":"dir","env":["env","env"],"waitFor":["waitFor","waitFor"]},{"args":["args","args"],"name":"name","id":"id","dir":"dir","env":["env","env"],"waitFor":["waitFor","waitFor"]}]},"provenanceBytes":"provenanceBytes","inTotoSlsaProvenanceV1":{"predicate":{"runDetails":{"metadata":{"finishedOn":"finishedOn","invocationId":"invocationId","startedOn":"startedOn"},"builder":{"builderDependencies":[{"digest":{"key":"digest"},"name":"name","annotations":{"key":""},"downloadLocation":"downloadLocation","mediaType":"mediaType","uri":"uri","content":"content"},{"digest":{"key":"digest"},"name":"name","annotations":{"key":""},"downloadLocation":"downloadLocation","mediaType":"mediaType","uri":"uri","content":"content"}],"id":"id","version":{"key":"version"}},"byproducts":[{"digest":{"key":"digest"},"name":"name","annotations":{"key":""},"downloadLocation":"downloadLocation","mediaType":"mediaType","uri":"uri","content":"content"},{"digest":{"key":"digest"},"name":"name","annotations":{"key":""},"downloadLocation":"downloadLocation","mediaType":"mediaType","uri":"uri","content":"content"}]},"buildDefinition":{"buildType":"buildType","internalParameters":{"key":""},"resolvedDependencies":[{"digest":{"key":"digest"},"name":"name","annotations":{"key":""},"downloadLocation":"downloadLocation","mediaType":"mediaType","uri":"uri","content":"content"},{"digest":{"key":"digest"},"name":"name","annotations":{"key":""},"downloadLocation":"downloadLocation","mediaType":"mediaType","uri":"uri","content":"content"}],"externalParameters":{"key":""}}},"predicateType":"predicateType","subject":[{"digest":{"key":"digest"},"name":"name"},{"digest":{"key":"digest"},"name":"name"}],"_type":"_type"}},"createTime":"createTime","spdxPackage":{"sourceInfo":"sourceInfo","filename":"filename","licenseConcluded":{"comments":"comments","expression":"expression"},"comment":"comment","id":"id","title":"title","homePage":"homePage","packageType":"packageType","summaryDescription":"summaryDescription","version":"version"},"installation":{"installation":{"license":{"comments":"comments","expression":"expression"},"name":"name","location":[{"path":"path","cpeUri":"cpeUri","version":{"inclusive":True,"kind":"VERSION_KIND_UNSPECIFIED","name":"name","epoch":1,"revision":"revision"}},{"path":"path","cpeUri":"cpeUri","version":{"inclusive":True,"kind":"VERSION_KIND_UNSPECIFIED","name":"name","epoch":1,"revision":"revision"}}],"cpeUri":"cpeUri","packageType":"packageType","version":{"inclusive":True,"kind":"VERSION_KIND_UNSPECIFIED","name":"name","epoch":1,"revision":"revision"},"architecture":"ARCHITECTURE_UNSPECIFIED"}},"name":"name","sbom":{"creatorComment":"creatorComment","documentComment":"documentComment","licenseListVersion":"licenseListVersion","createTime":"createTime","creators":["creators","creators"],"namespace":"namespace","externalDocumentRefs":["externalDocumentRefs","externalDocumentRefs"],"id":"id","title":"title"},"deployment":{"deployment":{"address":"address","undeployTime":"undeployTime","userEmail":"userEmail","deployTime":"deployTime","resourceUri":["resourceUri","resourceUri"],"config":"config","platform":"PLATFORM_UNSPECIFIED"}},"derivedImage":{"derivedImage":{"distance":0,"fingerprint":{"v1Name":"v1Name","v2Blob":["v2Blob","v2Blob"],"v2Name":"v2Name"},"baseResourceUrl":"baseResourceUrl","layerInfo":[{"arguments":"arguments","directive":"DIRECTIVE_UNSPECIFIED"},{"arguments":"arguments","directive":"DIRECTIVE_UNSPECIFIED"}]}}}]}
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
        path='/v1beta1/{parent}/occurrences:batchCreate'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_containeranalysis_projects_occurrences_create(client):
    """Test case for containeranalysis_projects_occurrences_create

    
    """
    body = {"discovered":{"discovered":{"lastScanTime":"lastScanTime","sbomStatus":{"sbomState":"SBOM_STATE_UNSPECIFIED","error":"error"},"analysisCompleted":{"analysisType":["analysisType","analysisType"]},"analysisError":[{"code":6,"details":[{"key":""},{"key":""}],"message":"message"},{"code":6,"details":[{"key":""},{"key":""}],"message":"message"}],"analysisStatusError":{"code":6,"details":[{"key":""},{"key":""}],"message":"message"},"continuousAnalysis":"CONTINUOUS_ANALYSIS_UNSPECIFIED","lastAnalysisTime":"lastAnalysisTime","analysisStatus":"ANALYSIS_STATUS_UNSPECIFIED"}},"attestation":{"attestation":{"genericSignedAttestation":{"serializedPayload":"serializedPayload","contentType":"CONTENT_TYPE_UNSPECIFIED","signatures":[{"signature":"signature","publicKeyId":"publicKeyId"},{"signature":"signature","publicKeyId":"publicKeyId"}]},"pgpSignedAttestation":{"pgpKeyId":"pgpKeyId","signature":"signature","contentType":"CONTENT_TYPE_UNSPECIFIED"}}},"resource":{"name":"name","uri":"uri","contentHash":{"type":"HASH_TYPE_UNSPECIFIED","value":"value"}},"kind":"NOTE_KIND_UNSPECIFIED","noteName":"noteName","sbomReference":{"payloadType":"payloadType","payload":{"predicate":{"referrerId":"referrerId","digest":{"key":"digest"},"location":"location","mimeType":"mimeType"},"predicateType":"predicateType","subject":[{"digest":{"key":"digest"},"name":"name"},{"digest":{"key":"digest"},"name":"name"}],"_type":"_type"},"signatures":[{"sig":"sig","keyid":"keyid"},{"sig":"sig","keyid":"keyid"}]},"intoto":{"signed":{"environment":{"customValues":{"key":"customValues"}},"materials":[{"hashes":{"sha256":"sha256"},"resourceUri":"resourceUri"},{"hashes":{"sha256":"sha256"},"resourceUri":"resourceUri"}],"byproducts":{"customValues":{"key":"customValues"}},"command":["command","command"],"products":[{"hashes":{"sha256":"sha256"},"resourceUri":"resourceUri"},{"hashes":{"sha256":"sha256"},"resourceUri":"resourceUri"}]},"signatures":[{"sig":"sig","keyid":"keyid"},{"sig":"sig","keyid":"keyid"}]},"updateTime":"updateTime","spdxRelationship":{"comment":"comment","source":"source","type":"RELATIONSHIP_TYPE_UNSPECIFIED","target":"target"},"vulnerability":{"longDescription":"longDescription","severity":"SEVERITY_UNSPECIFIED","cvssV2":{"exploitabilityScore":2.302136,"confidentialityImpact":"IMPACT_UNSPECIFIED","attackComplexity":"ATTACK_COMPLEXITY_UNSPECIFIED","scope":"SCOPE_UNSPECIFIED","attackVector":"ATTACK_VECTOR_UNSPECIFIED","availabilityImpact":"IMPACT_UNSPECIFIED","integrityImpact":"IMPACT_UNSPECIFIED","baseScore":5.637377,"privilegesRequired":"PRIVILEGES_REQUIRED_UNSPECIFIED","impactScore":7.0614014,"userInteraction":"USER_INTERACTION_UNSPECIFIED","authentication":"AUTHENTICATION_UNSPECIFIED"},"shortDescription":"shortDescription","type":"type","cvssScore":5.962134,"cvssV3":{"exploitabilityScore":2.302136,"confidentialityImpact":"IMPACT_UNSPECIFIED","attackComplexity":"ATTACK_COMPLEXITY_UNSPECIFIED","scope":"SCOPE_UNSPECIFIED","attackVector":"ATTACK_VECTOR_UNSPECIFIED","availabilityImpact":"IMPACT_UNSPECIFIED","integrityImpact":"IMPACT_UNSPECIFIED","baseScore":5.637377,"privilegesRequired":"PRIVILEGES_REQUIRED_UNSPECIFIED","impactScore":7.0614014,"userInteraction":"USER_INTERACTION_UNSPECIFIED","authentication":"AUTHENTICATION_UNSPECIFIED"},"cvssVersion":"CVSS_VERSION_UNSPECIFIED","relatedUrls":[{"label":"label","url":"url"},{"label":"label","url":"url"}],"packageIssue":[{"affectedLocation":{"package":"package","cpeUri":"cpeUri","version":{"inclusive":True,"kind":"VERSION_KIND_UNSPECIFIED","name":"name","epoch":1,"revision":"revision"}},"effectiveSeverity":"SEVERITY_UNSPECIFIED","fixedLocation":{"package":"package","cpeUri":"cpeUri","version":{"inclusive":True,"kind":"VERSION_KIND_UNSPECIFIED","name":"name","epoch":1,"revision":"revision"}},"packageType":"packageType","severityName":"severityName"},{"affectedLocation":{"package":"package","cpeUri":"cpeUri","version":{"inclusive":True,"kind":"VERSION_KIND_UNSPECIFIED","name":"name","epoch":1,"revision":"revision"}},"effectiveSeverity":"SEVERITY_UNSPECIFIED","fixedLocation":{"package":"package","cpeUri":"cpeUri","version":{"inclusive":True,"kind":"VERSION_KIND_UNSPECIFIED","name":"name","epoch":1,"revision":"revision"}},"packageType":"packageType","severityName":"severityName"}],"extraDetails":"extraDetails","effectiveSeverity":"SEVERITY_UNSPECIFIED","vexAssessment":{"cve":"cve","vulnerabilityId":"vulnerabilityId","relatedUris":[{"label":"label","url":"url"},{"label":"label","url":"url"}],"noteName":"noteName","remediations":[{"remediationType":"REMEDIATION_TYPE_UNSPECIFIED","remediationUri":{"label":"label","url":"url"},"details":"details"},{"remediationType":"REMEDIATION_TYPE_UNSPECIFIED","remediationUri":{"label":"label","url":"url"},"details":"details"}],"impacts":["impacts","impacts"],"justification":{"justificationType":"JUSTIFICATION_TYPE_UNSPECIFIED","details":"details"},"state":"STATE_UNSPECIFIED"}},"spdxFile":{"copyright":"copyright","filesLicenseInfo":["filesLicenseInfo","filesLicenseInfo"],"licenseConcluded":{"comments":"comments","expression":"expression"},"comment":"comment","contributors":["contributors","contributors"],"id":"id","attributions":["attributions","attributions"],"notice":"notice"},"remediation":"remediation","envelope":{"payloadType":"payloadType","payload":"payload","signatures":[{"sig":"sig","keyid":"keyid"},{"sig":"sig","keyid":"keyid"}]},"build":{"provenance":{"creator":"creator","triggerId":"triggerId","buildOptions":{"key":"buildOptions"},"sourceProvenance":{"additionalContexts":[{"git":{"revisionId":"revisionId","url":"url"},"gerrit":{"aliasContext":{"kind":"KIND_UNSPECIFIED","name":"name"},"revisionId":"revisionId","hostUri":"hostUri","gerritProject":"gerritProject"},"cloudRepo":{"aliasContext":{"kind":"KIND_UNSPECIFIED","name":"name"},"revisionId":"revisionId","repoId":{"uid":"uid","projectRepoId":{"repoName":"repoName","projectId":"projectId"}}},"labels":{"key":"labels"}},{"git":{"revisionId":"revisionId","url":"url"},"gerrit":{"aliasContext":{"kind":"KIND_UNSPECIFIED","name":"name"},"revisionId":"revisionId","hostUri":"hostUri","gerritProject":"gerritProject"},"cloudRepo":{"aliasContext":{"kind":"KIND_UNSPECIFIED","name":"name"},"revisionId":"revisionId","repoId":{"uid":"uid","projectRepoId":{"repoName":"repoName","projectId":"projectId"}}},"labels":{"key":"labels"}}],"artifactStorageSourceUri":"artifactStorageSourceUri","context":{"git":{"revisionId":"revisionId","url":"url"},"gerrit":{"aliasContext":{"kind":"KIND_UNSPECIFIED","name":"name"},"revisionId":"revisionId","hostUri":"hostUri","gerritProject":"gerritProject"},"cloudRepo":{"aliasContext":{"kind":"KIND_UNSPECIFIED","name":"name"},"revisionId":"revisionId","repoId":{"uid":"uid","projectRepoId":{"repoName":"repoName","projectId":"projectId"}}},"labels":{"key":"labels"}},"fileHashes":{"key":{"fileHash":[{"type":"HASH_TYPE_UNSPECIFIED","value":"value"},{"type":"HASH_TYPE_UNSPECIFIED","value":"value"}]}}},"createTime":"createTime","logsUri":"logsUri","builderVersion":"builderVersion","builtArtifacts":[{"names":["names","names"],"checksum":"checksum","id":"id"},{"names":["names","names"],"checksum":"checksum","id":"id"}],"startTime":"startTime","endTime":"endTime","id":"id","projectId":"projectId","commands":[{"args":["args","args"],"name":"name","id":"id","dir":"dir","env":["env","env"],"waitFor":["waitFor","waitFor"]},{"args":["args","args"],"name":"name","id":"id","dir":"dir","env":["env","env"],"waitFor":["waitFor","waitFor"]}]},"provenanceBytes":"provenanceBytes","inTotoSlsaProvenanceV1":{"predicate":{"runDetails":{"metadata":{"finishedOn":"finishedOn","invocationId":"invocationId","startedOn":"startedOn"},"builder":{"builderDependencies":[{"digest":{"key":"digest"},"name":"name","annotations":{"key":""},"downloadLocation":"downloadLocation","mediaType":"mediaType","uri":"uri","content":"content"},{"digest":{"key":"digest"},"name":"name","annotations":{"key":""},"downloadLocation":"downloadLocation","mediaType":"mediaType","uri":"uri","content":"content"}],"id":"id","version":{"key":"version"}},"byproducts":[{"digest":{"key":"digest"},"name":"name","annotations":{"key":""},"downloadLocation":"downloadLocation","mediaType":"mediaType","uri":"uri","content":"content"},{"digest":{"key":"digest"},"name":"name","annotations":{"key":""},"downloadLocation":"downloadLocation","mediaType":"mediaType","uri":"uri","content":"content"}]},"buildDefinition":{"buildType":"buildType","internalParameters":{"key":""},"resolvedDependencies":[{"digest":{"key":"digest"},"name":"name","annotations":{"key":""},"downloadLocation":"downloadLocation","mediaType":"mediaType","uri":"uri","content":"content"},{"digest":{"key":"digest"},"name":"name","annotations":{"key":""},"downloadLocation":"downloadLocation","mediaType":"mediaType","uri":"uri","content":"content"}],"externalParameters":{"key":""}}},"predicateType":"predicateType","subject":[{"digest":{"key":"digest"},"name":"name"},{"digest":{"key":"digest"},"name":"name"}],"_type":"_type"}},"createTime":"createTime","spdxPackage":{"sourceInfo":"sourceInfo","filename":"filename","licenseConcluded":{"comments":"comments","expression":"expression"},"comment":"comment","id":"id","title":"title","homePage":"homePage","packageType":"packageType","summaryDescription":"summaryDescription","version":"version"},"installation":{"installation":{"license":{"comments":"comments","expression":"expression"},"name":"name","location":[{"path":"path","cpeUri":"cpeUri","version":{"inclusive":True,"kind":"VERSION_KIND_UNSPECIFIED","name":"name","epoch":1,"revision":"revision"}},{"path":"path","cpeUri":"cpeUri","version":{"inclusive":True,"kind":"VERSION_KIND_UNSPECIFIED","name":"name","epoch":1,"revision":"revision"}}],"cpeUri":"cpeUri","packageType":"packageType","version":{"inclusive":True,"kind":"VERSION_KIND_UNSPECIFIED","name":"name","epoch":1,"revision":"revision"},"architecture":"ARCHITECTURE_UNSPECIFIED"}},"name":"name","sbom":{"creatorComment":"creatorComment","documentComment":"documentComment","licenseListVersion":"licenseListVersion","createTime":"createTime","creators":["creators","creators"],"namespace":"namespace","externalDocumentRefs":["externalDocumentRefs","externalDocumentRefs"],"id":"id","title":"title"},"deployment":{"deployment":{"address":"address","undeployTime":"undeployTime","userEmail":"userEmail","deployTime":"deployTime","resourceUri":["resourceUri","resourceUri"],"config":"config","platform":"PLATFORM_UNSPECIFIED"}},"derivedImage":{"derivedImage":{"distance":0,"fingerprint":{"v1Name":"v1Name","v2Blob":["v2Blob","v2Blob"],"v2Name":"v2Name"},"baseResourceUrl":"baseResourceUrl","layerInfo":[{"arguments":"arguments","directive":"DIRECTIVE_UNSPECIFIED"},{"arguments":"arguments","directive":"DIRECTIVE_UNSPECIFIED"}]}}}
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
        path='/v1beta1/{parent}/occurrences'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_containeranalysis_projects_occurrences_delete(client):
    """Test case for containeranalysis_projects_occurrences_delete

    
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
        path='/v1beta1/{name}'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_containeranalysis_projects_occurrences_get(client):
    """Test case for containeranalysis_projects_occurrences_get

    
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
        path='/v1beta1/{name}'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_containeranalysis_projects_occurrences_get_iam_policy(client):
    """Test case for containeranalysis_projects_occurrences_get_iam_policy

    
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
        path='/v1beta1/{resourceget_iam_polic}'.format(resource='resource_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_containeranalysis_projects_occurrences_get_notes(client):
    """Test case for containeranalysis_projects_occurrences_get_notes

    
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
        path='/v1beta1/{name}/notes'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_containeranalysis_projects_occurrences_get_vulnerability_summary(client):
    """Test case for containeranalysis_projects_occurrences_get_vulnerability_summary

    
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
                    ('filter', 'filter_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1beta1/{parent}/occurrences:vulnerabilitySummary'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_containeranalysis_projects_occurrences_list(client):
    """Test case for containeranalysis_projects_occurrences_list

    
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
        path='/v1beta1/{parent}/occurrences'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_containeranalysis_projects_occurrences_patch(client):
    """Test case for containeranalysis_projects_occurrences_patch

    
    """
    body = {"discovered":{"discovered":{"lastScanTime":"lastScanTime","sbomStatus":{"sbomState":"SBOM_STATE_UNSPECIFIED","error":"error"},"analysisCompleted":{"analysisType":["analysisType","analysisType"]},"analysisError":[{"code":6,"details":[{"key":""},{"key":""}],"message":"message"},{"code":6,"details":[{"key":""},{"key":""}],"message":"message"}],"analysisStatusError":{"code":6,"details":[{"key":""},{"key":""}],"message":"message"},"continuousAnalysis":"CONTINUOUS_ANALYSIS_UNSPECIFIED","lastAnalysisTime":"lastAnalysisTime","analysisStatus":"ANALYSIS_STATUS_UNSPECIFIED"}},"attestation":{"attestation":{"genericSignedAttestation":{"serializedPayload":"serializedPayload","contentType":"CONTENT_TYPE_UNSPECIFIED","signatures":[{"signature":"signature","publicKeyId":"publicKeyId"},{"signature":"signature","publicKeyId":"publicKeyId"}]},"pgpSignedAttestation":{"pgpKeyId":"pgpKeyId","signature":"signature","contentType":"CONTENT_TYPE_UNSPECIFIED"}}},"resource":{"name":"name","uri":"uri","contentHash":{"type":"HASH_TYPE_UNSPECIFIED","value":"value"}},"kind":"NOTE_KIND_UNSPECIFIED","noteName":"noteName","sbomReference":{"payloadType":"payloadType","payload":{"predicate":{"referrerId":"referrerId","digest":{"key":"digest"},"location":"location","mimeType":"mimeType"},"predicateType":"predicateType","subject":[{"digest":{"key":"digest"},"name":"name"},{"digest":{"key":"digest"},"name":"name"}],"_type":"_type"},"signatures":[{"sig":"sig","keyid":"keyid"},{"sig":"sig","keyid":"keyid"}]},"intoto":{"signed":{"environment":{"customValues":{"key":"customValues"}},"materials":[{"hashes":{"sha256":"sha256"},"resourceUri":"resourceUri"},{"hashes":{"sha256":"sha256"},"resourceUri":"resourceUri"}],"byproducts":{"customValues":{"key":"customValues"}},"command":["command","command"],"products":[{"hashes":{"sha256":"sha256"},"resourceUri":"resourceUri"},{"hashes":{"sha256":"sha256"},"resourceUri":"resourceUri"}]},"signatures":[{"sig":"sig","keyid":"keyid"},{"sig":"sig","keyid":"keyid"}]},"updateTime":"updateTime","spdxRelationship":{"comment":"comment","source":"source","type":"RELATIONSHIP_TYPE_UNSPECIFIED","target":"target"},"vulnerability":{"longDescription":"longDescription","severity":"SEVERITY_UNSPECIFIED","cvssV2":{"exploitabilityScore":2.302136,"confidentialityImpact":"IMPACT_UNSPECIFIED","attackComplexity":"ATTACK_COMPLEXITY_UNSPECIFIED","scope":"SCOPE_UNSPECIFIED","attackVector":"ATTACK_VECTOR_UNSPECIFIED","availabilityImpact":"IMPACT_UNSPECIFIED","integrityImpact":"IMPACT_UNSPECIFIED","baseScore":5.637377,"privilegesRequired":"PRIVILEGES_REQUIRED_UNSPECIFIED","impactScore":7.0614014,"userInteraction":"USER_INTERACTION_UNSPECIFIED","authentication":"AUTHENTICATION_UNSPECIFIED"},"shortDescription":"shortDescription","type":"type","cvssScore":5.962134,"cvssV3":{"exploitabilityScore":2.302136,"confidentialityImpact":"IMPACT_UNSPECIFIED","attackComplexity":"ATTACK_COMPLEXITY_UNSPECIFIED","scope":"SCOPE_UNSPECIFIED","attackVector":"ATTACK_VECTOR_UNSPECIFIED","availabilityImpact":"IMPACT_UNSPECIFIED","integrityImpact":"IMPACT_UNSPECIFIED","baseScore":5.637377,"privilegesRequired":"PRIVILEGES_REQUIRED_UNSPECIFIED","impactScore":7.0614014,"userInteraction":"USER_INTERACTION_UNSPECIFIED","authentication":"AUTHENTICATION_UNSPECIFIED"},"cvssVersion":"CVSS_VERSION_UNSPECIFIED","relatedUrls":[{"label":"label","url":"url"},{"label":"label","url":"url"}],"packageIssue":[{"affectedLocation":{"package":"package","cpeUri":"cpeUri","version":{"inclusive":True,"kind":"VERSION_KIND_UNSPECIFIED","name":"name","epoch":1,"revision":"revision"}},"effectiveSeverity":"SEVERITY_UNSPECIFIED","fixedLocation":{"package":"package","cpeUri":"cpeUri","version":{"inclusive":True,"kind":"VERSION_KIND_UNSPECIFIED","name":"name","epoch":1,"revision":"revision"}},"packageType":"packageType","severityName":"severityName"},{"affectedLocation":{"package":"package","cpeUri":"cpeUri","version":{"inclusive":True,"kind":"VERSION_KIND_UNSPECIFIED","name":"name","epoch":1,"revision":"revision"}},"effectiveSeverity":"SEVERITY_UNSPECIFIED","fixedLocation":{"package":"package","cpeUri":"cpeUri","version":{"inclusive":True,"kind":"VERSION_KIND_UNSPECIFIED","name":"name","epoch":1,"revision":"revision"}},"packageType":"packageType","severityName":"severityName"}],"extraDetails":"extraDetails","effectiveSeverity":"SEVERITY_UNSPECIFIED","vexAssessment":{"cve":"cve","vulnerabilityId":"vulnerabilityId","relatedUris":[{"label":"label","url":"url"},{"label":"label","url":"url"}],"noteName":"noteName","remediations":[{"remediationType":"REMEDIATION_TYPE_UNSPECIFIED","remediationUri":{"label":"label","url":"url"},"details":"details"},{"remediationType":"REMEDIATION_TYPE_UNSPECIFIED","remediationUri":{"label":"label","url":"url"},"details":"details"}],"impacts":["impacts","impacts"],"justification":{"justificationType":"JUSTIFICATION_TYPE_UNSPECIFIED","details":"details"},"state":"STATE_UNSPECIFIED"}},"spdxFile":{"copyright":"copyright","filesLicenseInfo":["filesLicenseInfo","filesLicenseInfo"],"licenseConcluded":{"comments":"comments","expression":"expression"},"comment":"comment","contributors":["contributors","contributors"],"id":"id","attributions":["attributions","attributions"],"notice":"notice"},"remediation":"remediation","envelope":{"payloadType":"payloadType","payload":"payload","signatures":[{"sig":"sig","keyid":"keyid"},{"sig":"sig","keyid":"keyid"}]},"build":{"provenance":{"creator":"creator","triggerId":"triggerId","buildOptions":{"key":"buildOptions"},"sourceProvenance":{"additionalContexts":[{"git":{"revisionId":"revisionId","url":"url"},"gerrit":{"aliasContext":{"kind":"KIND_UNSPECIFIED","name":"name"},"revisionId":"revisionId","hostUri":"hostUri","gerritProject":"gerritProject"},"cloudRepo":{"aliasContext":{"kind":"KIND_UNSPECIFIED","name":"name"},"revisionId":"revisionId","repoId":{"uid":"uid","projectRepoId":{"repoName":"repoName","projectId":"projectId"}}},"labels":{"key":"labels"}},{"git":{"revisionId":"revisionId","url":"url"},"gerrit":{"aliasContext":{"kind":"KIND_UNSPECIFIED","name":"name"},"revisionId":"revisionId","hostUri":"hostUri","gerritProject":"gerritProject"},"cloudRepo":{"aliasContext":{"kind":"KIND_UNSPECIFIED","name":"name"},"revisionId":"revisionId","repoId":{"uid":"uid","projectRepoId":{"repoName":"repoName","projectId":"projectId"}}},"labels":{"key":"labels"}}],"artifactStorageSourceUri":"artifactStorageSourceUri","context":{"git":{"revisionId":"revisionId","url":"url"},"gerrit":{"aliasContext":{"kind":"KIND_UNSPECIFIED","name":"name"},"revisionId":"revisionId","hostUri":"hostUri","gerritProject":"gerritProject"},"cloudRepo":{"aliasContext":{"kind":"KIND_UNSPECIFIED","name":"name"},"revisionId":"revisionId","repoId":{"uid":"uid","projectRepoId":{"repoName":"repoName","projectId":"projectId"}}},"labels":{"key":"labels"}},"fileHashes":{"key":{"fileHash":[{"type":"HASH_TYPE_UNSPECIFIED","value":"value"},{"type":"HASH_TYPE_UNSPECIFIED","value":"value"}]}}},"createTime":"createTime","logsUri":"logsUri","builderVersion":"builderVersion","builtArtifacts":[{"names":["names","names"],"checksum":"checksum","id":"id"},{"names":["names","names"],"checksum":"checksum","id":"id"}],"startTime":"startTime","endTime":"endTime","id":"id","projectId":"projectId","commands":[{"args":["args","args"],"name":"name","id":"id","dir":"dir","env":["env","env"],"waitFor":["waitFor","waitFor"]},{"args":["args","args"],"name":"name","id":"id","dir":"dir","env":["env","env"],"waitFor":["waitFor","waitFor"]}]},"provenanceBytes":"provenanceBytes","inTotoSlsaProvenanceV1":{"predicate":{"runDetails":{"metadata":{"finishedOn":"finishedOn","invocationId":"invocationId","startedOn":"startedOn"},"builder":{"builderDependencies":[{"digest":{"key":"digest"},"name":"name","annotations":{"key":""},"downloadLocation":"downloadLocation","mediaType":"mediaType","uri":"uri","content":"content"},{"digest":{"key":"digest"},"name":"name","annotations":{"key":""},"downloadLocation":"downloadLocation","mediaType":"mediaType","uri":"uri","content":"content"}],"id":"id","version":{"key":"version"}},"byproducts":[{"digest":{"key":"digest"},"name":"name","annotations":{"key":""},"downloadLocation":"downloadLocation","mediaType":"mediaType","uri":"uri","content":"content"},{"digest":{"key":"digest"},"name":"name","annotations":{"key":""},"downloadLocation":"downloadLocation","mediaType":"mediaType","uri":"uri","content":"content"}]},"buildDefinition":{"buildType":"buildType","internalParameters":{"key":""},"resolvedDependencies":[{"digest":{"key":"digest"},"name":"name","annotations":{"key":""},"downloadLocation":"downloadLocation","mediaType":"mediaType","uri":"uri","content":"content"},{"digest":{"key":"digest"},"name":"name","annotations":{"key":""},"downloadLocation":"downloadLocation","mediaType":"mediaType","uri":"uri","content":"content"}],"externalParameters":{"key":""}}},"predicateType":"predicateType","subject":[{"digest":{"key":"digest"},"name":"name"},{"digest":{"key":"digest"},"name":"name"}],"_type":"_type"}},"createTime":"createTime","spdxPackage":{"sourceInfo":"sourceInfo","filename":"filename","licenseConcluded":{"comments":"comments","expression":"expression"},"comment":"comment","id":"id","title":"title","homePage":"homePage","packageType":"packageType","summaryDescription":"summaryDescription","version":"version"},"installation":{"installation":{"license":{"comments":"comments","expression":"expression"},"name":"name","location":[{"path":"path","cpeUri":"cpeUri","version":{"inclusive":True,"kind":"VERSION_KIND_UNSPECIFIED","name":"name","epoch":1,"revision":"revision"}},{"path":"path","cpeUri":"cpeUri","version":{"inclusive":True,"kind":"VERSION_KIND_UNSPECIFIED","name":"name","epoch":1,"revision":"revision"}}],"cpeUri":"cpeUri","packageType":"packageType","version":{"inclusive":True,"kind":"VERSION_KIND_UNSPECIFIED","name":"name","epoch":1,"revision":"revision"},"architecture":"ARCHITECTURE_UNSPECIFIED"}},"name":"name","sbom":{"creatorComment":"creatorComment","documentComment":"documentComment","licenseListVersion":"licenseListVersion","createTime":"createTime","creators":["creators","creators"],"namespace":"namespace","externalDocumentRefs":["externalDocumentRefs","externalDocumentRefs"],"id":"id","title":"title"},"deployment":{"deployment":{"address":"address","undeployTime":"undeployTime","userEmail":"userEmail","deployTime":"deployTime","resourceUri":["resourceUri","resourceUri"],"config":"config","platform":"PLATFORM_UNSPECIFIED"}},"derivedImage":{"derivedImage":{"distance":0,"fingerprint":{"v1Name":"v1Name","v2Blob":["v2Blob","v2Blob"],"v2Name":"v2Name"},"baseResourceUrl":"baseResourceUrl","layerInfo":[{"arguments":"arguments","directive":"DIRECTIVE_UNSPECIFIED"},{"arguments":"arguments","directive":"DIRECTIVE_UNSPECIFIED"}]}}}
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
        path='/v1beta1/{name}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_containeranalysis_projects_occurrences_set_iam_policy(client):
    """Test case for containeranalysis_projects_occurrences_set_iam_policy

    
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
        path='/v1beta1/{resourceset_iam_polic}'.format(resource='resource_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_containeranalysis_projects_occurrences_test_iam_permissions(client):
    """Test case for containeranalysis_projects_occurrences_test_iam_permissions

    
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
        path='/v1beta1/{resourcetest_iam_permission}'.format(resource='resource_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_containeranalysis_projects_resources_export_sbom(client):
    """Test case for containeranalysis_projects_resources_export_sbom

    
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
        path='/v1beta1/{nameexport_sbo}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_containeranalysis_projects_resources_generate_packages_summary(client):
    """Test case for containeranalysis_projects_resources_generate_packages_summary

    
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
        path='/v1beta1/{namegenerate_packages_summar}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

