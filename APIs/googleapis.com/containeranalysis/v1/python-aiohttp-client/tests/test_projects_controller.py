# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.batch_create_notes_request import BatchCreateNotesRequest
from openapi_server.models.batch_create_notes_response import BatchCreateNotesResponse
from openapi_server.models.batch_create_occurrences_request import BatchCreateOccurrencesRequest
from openapi_server.models.batch_create_occurrences_response import BatchCreateOccurrencesResponse
from openapi_server.models.export_sbom_request import ExportSBOMRequest
from openapi_server.models.export_sbom_response import ExportSBOMResponse
from openapi_server.models.get_iam_policy_request import GetIamPolicyRequest
from openapi_server.models.list_note_occurrences_response import ListNoteOccurrencesResponse
from openapi_server.models.list_notes_response import ListNotesResponse
from openapi_server.models.list_occurrences_response import ListOccurrencesResponse
from openapi_server.models.note import Note
from openapi_server.models.occurrence import Occurrence
from openapi_server.models.policy import Policy
from openapi_server.models.set_iam_policy_request import SetIamPolicyRequest
from openapi_server.models.test_iam_permissions_request import TestIamPermissionsRequest
from openapi_server.models.test_iam_permissions_response import TestIamPermissionsResponse
from openapi_server.models.vulnerability_occurrences_summary import VulnerabilityOccurrencesSummary


pytestmark = pytest.mark.asyncio

async def test_containeranalysis_projects_notes_batch_create(client):
    """Test case for containeranalysis_projects_notes_batch_create

    
    """
    body = {"notes":{"key":{"longDescription":"longDescription","image":{"resourceUrl":"resourceUrl","fingerprint":{"v1Name":"v1Name","v2Blob":["v2Blob","v2Blob"],"v2Name":"v2Name"}},"attestation":{"hint":{"humanReadableName":"humanReadableName"}},"package":{"license":{"comments":"comments","expression":"expression"},"digest":[{"digestBytes":"digestBytes","algo":"algo"},{"digestBytes":"digestBytes","algo":"algo"}],"name":"name","description":"description","distribution":[{"latestVersion":{"inclusive":True,"kind":"VERSION_KIND_UNSPECIFIED","name":"name","fullName":"fullName","epoch":1,"revision":"revision"},"description":"description","cpeUri":"cpeUri","maintainer":"maintainer","url":"url","architecture":"ARCHITECTURE_UNSPECIFIED"},{"latestVersion":{"inclusive":True,"kind":"VERSION_KIND_UNSPECIFIED","name":"name","fullName":"fullName","epoch":1,"revision":"revision"},"description":"description","cpeUri":"cpeUri","maintainer":"maintainer","url":"url","architecture":"ARCHITECTURE_UNSPECIFIED"}],"cpeUri":"cpeUri","packageType":"packageType","version":{"inclusive":True,"kind":"VERSION_KIND_UNSPECIFIED","name":"name","fullName":"fullName","epoch":1,"revision":"revision"},"maintainer":"maintainer","url":"url","architecture":"ARCHITECTURE_UNSPECIFIED"},"upgrade":{"package":"package","version":{"inclusive":True,"kind":"VERSION_KIND_UNSPECIFIED","name":"name","fullName":"fullName","epoch":1,"revision":"revision"},"distributions":[{"severity":"severity","cve":["cve","cve"],"classification":"classification","cpeUri":"cpeUri"},{"severity":"severity","cve":["cve","cve"],"classification":"classification","cpeUri":"cpeUri"}],"windowsUpdate":{"lastPublishedTimestamp":"lastPublishedTimestamp","identity":{"updateId":"updateId","revision":5},"supportUrl":"supportUrl","description":"description","kbArticleIds":["kbArticleIds","kbArticleIds"],"categories":[{"name":"name","categoryId":"categoryId"},{"name":"name","categoryId":"categoryId"}],"title":"title"}},"kind":"NOTE_KIND_UNSPECIFIED","sbomReference":{"format":"format","version":"version"},"vulnerabilityAssessment":{"longDescription":"longDescription","assessment":{"longDescription":"longDescription","cve":"cve","vulnerabilityId":"vulnerabilityId","relatedUris":[{"label":"label","url":"url"},{"label":"label","url":"url"}],"remediations":[{"remediationType":"REMEDIATION_TYPE_UNSPECIFIED","remediationUri":{"label":"label","url":"url"},"details":"details"},{"remediationType":"REMEDIATION_TYPE_UNSPECIFIED","remediationUri":{"label":"label","url":"url"},"details":"details"}],"impacts":["impacts","impacts"],"justification":{"justificationType":"JUSTIFICATION_TYPE_UNSPECIFIED","details":"details"},"shortDescription":"shortDescription","state":"STATE_UNSPECIFIED"},"product":{"genericUri":"genericUri","name":"name","id":"id"},"publisher":{"issuingAuthority":"issuingAuthority","name":"name","publisherNamespace":"publisherNamespace"},"shortDescription":"shortDescription","languageCode":"languageCode","title":"title"},"dsseAttestation":{"hint":{"humanReadableName":"humanReadableName"}},"updateTime":"updateTime","shortDescription":"shortDescription","vulnerability":{"severity":"SEVERITY_UNSPECIFIED","cvssScore":6.0274563,"cvssV3":{"exploitabilityScore":5.962134,"confidentialityImpact":"IMPACT_UNSPECIFIED","attackComplexity":"ATTACK_COMPLEXITY_UNSPECIFIED","scope":"SCOPE_UNSPECIFIED","attackVector":"ATTACK_VECTOR_UNSPECIFIED","availabilityImpact":"IMPACT_UNSPECIFIED","integrityImpact":"IMPACT_UNSPECIFIED","baseScore":1.4658129,"privilegesRequired":"PRIVILEGES_REQUIRED_UNSPECIFIED","impactScore":5.637377,"userInteraction":"USER_INTERACTION_UNSPECIFIED"},"cvssVersion":"CVSS_VERSION_UNSPECIFIED","details":[{"fixedVersion":{"inclusive":True,"kind":"VERSION_KIND_UNSPECIFIED","name":"name","fullName":"fullName","epoch":1,"revision":"revision"},"affectedPackage":"affectedPackage","fixedPackage":"fixedPackage","description":"description","sourceUpdateTime":"sourceUpdateTime","isObsolete":True,"source":"source","packageType":"packageType","fixedCpeUri":"fixedCpeUri","affectedCpeUri":"affectedCpeUri","vendor":"vendor","affectedVersionEnd":{"inclusive":True,"kind":"VERSION_KIND_UNSPECIFIED","name":"name","fullName":"fullName","epoch":1,"revision":"revision"},"affectedVersionStart":{"inclusive":True,"kind":"VERSION_KIND_UNSPECIFIED","name":"name","fullName":"fullName","epoch":1,"revision":"revision"},"severityName":"severityName"},{"fixedVersion":{"inclusive":True,"kind":"VERSION_KIND_UNSPECIFIED","name":"name","fullName":"fullName","epoch":1,"revision":"revision"},"affectedPackage":"affectedPackage","fixedPackage":"fixedPackage","description":"description","sourceUpdateTime":"sourceUpdateTime","isObsolete":True,"source":"source","packageType":"packageType","fixedCpeUri":"fixedCpeUri","affectedCpeUri":"affectedCpeUri","vendor":"vendor","affectedVersionEnd":{"inclusive":True,"kind":"VERSION_KIND_UNSPECIFIED","name":"name","fullName":"fullName","epoch":1,"revision":"revision"},"affectedVersionStart":{"inclusive":True,"kind":"VERSION_KIND_UNSPECIFIED","name":"name","fullName":"fullName","epoch":1,"revision":"revision"},"severityName":"severityName"}],"sourceUpdateTime":"sourceUpdateTime","cvssV2":{"exploitabilityScore":7.0614014,"confidentialityImpact":"IMPACT_UNSPECIFIED","attackComplexity":"ATTACK_COMPLEXITY_UNSPECIFIED","scope":"SCOPE_UNSPECIFIED","attackVector":"ATTACK_VECTOR_UNSPECIFIED","availabilityImpact":"IMPACT_UNSPECIFIED","integrityImpact":"IMPACT_UNSPECIFIED","baseScore":2.302136,"privilegesRequired":"PRIVILEGES_REQUIRED_UNSPECIFIED","impactScore":9.301444,"userInteraction":"USER_INTERACTION_UNSPECIFIED","authentication":"AUTHENTICATION_UNSPECIFIED"},"windowsDetails":[{"name":"name","description":"description","fixingKbs":[{"name":"name","url":"url"},{"name":"name","url":"url"}],"cpeUri":"cpeUri"},{"name":"name","description":"description","fixingKbs":[{"name":"name","url":"url"},{"name":"name","url":"url"}],"cpeUri":"cpeUri"}]},"relatedNoteNames":["relatedNoteNames","relatedNoteNames"],"build":{"builderVersion":"builderVersion"},"createTime":"createTime","compliance":{"remediation":"remediation","cisBenchmark":{"severity":"SEVERITY_UNSPECIFIED","profileLevel":0},"scanInstructions":"scanInstructions","description":"description","title":"title","rationale":"rationale","version":[{"benchmarkDocument":"benchmarkDocument","cpeUri":"cpeUri","version":"version"},{"benchmarkDocument":"benchmarkDocument","cpeUri":"cpeUri","version":"version"}]},"discovery":{"analysisKind":"NOTE_KIND_UNSPECIFIED"},"expirationTime":"expirationTime","name":"name","relatedUrl":[{"label":"label","url":"url"},{"label":"label","url":"url"}],"deployment":{"resourceUri":["resourceUri","resourceUri"]}}}}
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
        path='/v1/{parent}/notes:batchCreate'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_containeranalysis_projects_notes_create(client):
    """Test case for containeranalysis_projects_notes_create

    
    """
    body = {"longDescription":"longDescription","image":{"resourceUrl":"resourceUrl","fingerprint":{"v1Name":"v1Name","v2Blob":["v2Blob","v2Blob"],"v2Name":"v2Name"}},"attestation":{"hint":{"humanReadableName":"humanReadableName"}},"package":{"license":{"comments":"comments","expression":"expression"},"digest":[{"digestBytes":"digestBytes","algo":"algo"},{"digestBytes":"digestBytes","algo":"algo"}],"name":"name","description":"description","distribution":[{"latestVersion":{"inclusive":True,"kind":"VERSION_KIND_UNSPECIFIED","name":"name","fullName":"fullName","epoch":1,"revision":"revision"},"description":"description","cpeUri":"cpeUri","maintainer":"maintainer","url":"url","architecture":"ARCHITECTURE_UNSPECIFIED"},{"latestVersion":{"inclusive":True,"kind":"VERSION_KIND_UNSPECIFIED","name":"name","fullName":"fullName","epoch":1,"revision":"revision"},"description":"description","cpeUri":"cpeUri","maintainer":"maintainer","url":"url","architecture":"ARCHITECTURE_UNSPECIFIED"}],"cpeUri":"cpeUri","packageType":"packageType","version":{"inclusive":True,"kind":"VERSION_KIND_UNSPECIFIED","name":"name","fullName":"fullName","epoch":1,"revision":"revision"},"maintainer":"maintainer","url":"url","architecture":"ARCHITECTURE_UNSPECIFIED"},"upgrade":{"package":"package","version":{"inclusive":True,"kind":"VERSION_KIND_UNSPECIFIED","name":"name","fullName":"fullName","epoch":1,"revision":"revision"},"distributions":[{"severity":"severity","cve":["cve","cve"],"classification":"classification","cpeUri":"cpeUri"},{"severity":"severity","cve":["cve","cve"],"classification":"classification","cpeUri":"cpeUri"}],"windowsUpdate":{"lastPublishedTimestamp":"lastPublishedTimestamp","identity":{"updateId":"updateId","revision":5},"supportUrl":"supportUrl","description":"description","kbArticleIds":["kbArticleIds","kbArticleIds"],"categories":[{"name":"name","categoryId":"categoryId"},{"name":"name","categoryId":"categoryId"}],"title":"title"}},"kind":"NOTE_KIND_UNSPECIFIED","sbomReference":{"format":"format","version":"version"},"vulnerabilityAssessment":{"longDescription":"longDescription","assessment":{"longDescription":"longDescription","cve":"cve","vulnerabilityId":"vulnerabilityId","relatedUris":[{"label":"label","url":"url"},{"label":"label","url":"url"}],"remediations":[{"remediationType":"REMEDIATION_TYPE_UNSPECIFIED","remediationUri":{"label":"label","url":"url"},"details":"details"},{"remediationType":"REMEDIATION_TYPE_UNSPECIFIED","remediationUri":{"label":"label","url":"url"},"details":"details"}],"impacts":["impacts","impacts"],"justification":{"justificationType":"JUSTIFICATION_TYPE_UNSPECIFIED","details":"details"},"shortDescription":"shortDescription","state":"STATE_UNSPECIFIED"},"product":{"genericUri":"genericUri","name":"name","id":"id"},"publisher":{"issuingAuthority":"issuingAuthority","name":"name","publisherNamespace":"publisherNamespace"},"shortDescription":"shortDescription","languageCode":"languageCode","title":"title"},"dsseAttestation":{"hint":{"humanReadableName":"humanReadableName"}},"updateTime":"updateTime","shortDescription":"shortDescription","vulnerability":{"severity":"SEVERITY_UNSPECIFIED","cvssScore":6.0274563,"cvssV3":{"exploitabilityScore":5.962134,"confidentialityImpact":"IMPACT_UNSPECIFIED","attackComplexity":"ATTACK_COMPLEXITY_UNSPECIFIED","scope":"SCOPE_UNSPECIFIED","attackVector":"ATTACK_VECTOR_UNSPECIFIED","availabilityImpact":"IMPACT_UNSPECIFIED","integrityImpact":"IMPACT_UNSPECIFIED","baseScore":1.4658129,"privilegesRequired":"PRIVILEGES_REQUIRED_UNSPECIFIED","impactScore":5.637377,"userInteraction":"USER_INTERACTION_UNSPECIFIED"},"cvssVersion":"CVSS_VERSION_UNSPECIFIED","details":[{"fixedVersion":{"inclusive":True,"kind":"VERSION_KIND_UNSPECIFIED","name":"name","fullName":"fullName","epoch":1,"revision":"revision"},"affectedPackage":"affectedPackage","fixedPackage":"fixedPackage","description":"description","sourceUpdateTime":"sourceUpdateTime","isObsolete":True,"source":"source","packageType":"packageType","fixedCpeUri":"fixedCpeUri","affectedCpeUri":"affectedCpeUri","vendor":"vendor","affectedVersionEnd":{"inclusive":True,"kind":"VERSION_KIND_UNSPECIFIED","name":"name","fullName":"fullName","epoch":1,"revision":"revision"},"affectedVersionStart":{"inclusive":True,"kind":"VERSION_KIND_UNSPECIFIED","name":"name","fullName":"fullName","epoch":1,"revision":"revision"},"severityName":"severityName"},{"fixedVersion":{"inclusive":True,"kind":"VERSION_KIND_UNSPECIFIED","name":"name","fullName":"fullName","epoch":1,"revision":"revision"},"affectedPackage":"affectedPackage","fixedPackage":"fixedPackage","description":"description","sourceUpdateTime":"sourceUpdateTime","isObsolete":True,"source":"source","packageType":"packageType","fixedCpeUri":"fixedCpeUri","affectedCpeUri":"affectedCpeUri","vendor":"vendor","affectedVersionEnd":{"inclusive":True,"kind":"VERSION_KIND_UNSPECIFIED","name":"name","fullName":"fullName","epoch":1,"revision":"revision"},"affectedVersionStart":{"inclusive":True,"kind":"VERSION_KIND_UNSPECIFIED","name":"name","fullName":"fullName","epoch":1,"revision":"revision"},"severityName":"severityName"}],"sourceUpdateTime":"sourceUpdateTime","cvssV2":{"exploitabilityScore":7.0614014,"confidentialityImpact":"IMPACT_UNSPECIFIED","attackComplexity":"ATTACK_COMPLEXITY_UNSPECIFIED","scope":"SCOPE_UNSPECIFIED","attackVector":"ATTACK_VECTOR_UNSPECIFIED","availabilityImpact":"IMPACT_UNSPECIFIED","integrityImpact":"IMPACT_UNSPECIFIED","baseScore":2.302136,"privilegesRequired":"PRIVILEGES_REQUIRED_UNSPECIFIED","impactScore":9.301444,"userInteraction":"USER_INTERACTION_UNSPECIFIED","authentication":"AUTHENTICATION_UNSPECIFIED"},"windowsDetails":[{"name":"name","description":"description","fixingKbs":[{"name":"name","url":"url"},{"name":"name","url":"url"}],"cpeUri":"cpeUri"},{"name":"name","description":"description","fixingKbs":[{"name":"name","url":"url"},{"name":"name","url":"url"}],"cpeUri":"cpeUri"}]},"relatedNoteNames":["relatedNoteNames","relatedNoteNames"],"build":{"builderVersion":"builderVersion"},"createTime":"createTime","compliance":{"remediation":"remediation","cisBenchmark":{"severity":"SEVERITY_UNSPECIFIED","profileLevel":0},"scanInstructions":"scanInstructions","description":"description","title":"title","rationale":"rationale","version":[{"benchmarkDocument":"benchmarkDocument","cpeUri":"cpeUri","version":"version"},{"benchmarkDocument":"benchmarkDocument","cpeUri":"cpeUri","version":"version"}]},"discovery":{"analysisKind":"NOTE_KIND_UNSPECIFIED"},"expirationTime":"expirationTime","name":"name","relatedUrl":[{"label":"label","url":"url"},{"label":"label","url":"url"}],"deployment":{"resourceUri":["resourceUri","resourceUri"]}}
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
        path='/v1/{parent}/notes'.format(parent='parent_example'),
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
        path='/v1/{parent}/notes'.format(parent='parent_example'),
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
        path='/v1/{name}/occurrences'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_containeranalysis_projects_occurrences_batch_create(client):
    """Test case for containeranalysis_projects_occurrences_batch_create

    
    """
    body = {"occurrences":[{"image":{"distance":6,"fingerprint":{"v1Name":"v1Name","v2Blob":["v2Blob","v2Blob"],"v2Name":"v2Name"},"baseResourceUrl":"baseResourceUrl","layerInfo":[{"arguments":"arguments","directive":"directive"},{"arguments":"arguments","directive":"directive"}]},"attestation":{"serializedPayload":"serializedPayload","jwts":[{"compactJwt":"compactJwt"},{"compactJwt":"compactJwt"}],"signatures":[{"signature":"signature","publicKeyId":"publicKeyId"},{"signature":"signature","publicKeyId":"publicKeyId"}]},"package":{"license":{"comments":"comments","expression":"expression"},"name":"name","location":[{"path":"path","cpeUri":"cpeUri","version":{"inclusive":True,"kind":"VERSION_KIND_UNSPECIFIED","name":"name","fullName":"fullName","epoch":1,"revision":"revision"}},{"path":"path","cpeUri":"cpeUri","version":{"inclusive":True,"kind":"VERSION_KIND_UNSPECIFIED","name":"name","fullName":"fullName","epoch":1,"revision":"revision"}}],"cpeUri":"cpeUri","packageType":"packageType","version":{"inclusive":True,"kind":"VERSION_KIND_UNSPECIFIED","name":"name","fullName":"fullName","epoch":1,"revision":"revision"},"architecture":"ARCHITECTURE_UNSPECIFIED"},"upgrade":{"package":"package","distribution":{"severity":"severity","cve":["cve","cve"],"classification":"classification","cpeUri":"cpeUri"},"parsedVersion":{"inclusive":True,"kind":"VERSION_KIND_UNSPECIFIED","name":"name","fullName":"fullName","epoch":1,"revision":"revision"},"windowsUpdate":{"lastPublishedTimestamp":"lastPublishedTimestamp","identity":{"updateId":"updateId","revision":5},"supportUrl":"supportUrl","description":"description","kbArticleIds":["kbArticleIds","kbArticleIds"],"categories":[{"name":"name","categoryId":"categoryId"},{"name":"name","categoryId":"categoryId"}],"title":"title"}},"kind":"NOTE_KIND_UNSPECIFIED","noteName":"noteName","sbomReference":{"payloadType":"payloadType","payload":{"predicate":{"referrerId":"referrerId","digest":{"key":"digest"},"location":"location","mimeType":"mimeType"},"predicateType":"predicateType","subject":[{"digest":{"key":"digest"},"name":"name"},{"digest":{"key":"digest"},"name":"name"}],"_type":"_type"},"signatures":[{"sig":"sig","keyid":"keyid"},{"sig":"sig","keyid":"keyid"}]},"dsseAttestation":{"envelope":{"payloadType":"payloadType","payload":"payload","signatures":[{"sig":"sig","keyid":"keyid"},{"sig":"sig","keyid":"keyid"}]},"statement":{"provenance":{"metadata":{"buildFinishedOn":"buildFinishedOn","buildStartedOn":"buildStartedOn","reproducible":True,"buildInvocationId":"buildInvocationId","completeness":{"environment":True,"materials":True,"arguments":True}},"builderConfig":{"id":"id"},"materials":["materials","materials"],"recipe":{"environment":[{"key":""},{"key":""}],"arguments":[{"key":""},{"key":""}],"entryPoint":"entryPoint","type":"type","definedInMaterial":"definedInMaterial"}},"predicateType":"predicateType","subject":[{"digest":{"key":"digest"},"name":"name"},{"digest":{"key":"digest"},"name":"name"}],"_type":"_type","slsaProvenanceZeroTwo":{"buildConfig":{"key":""},"invocation":{"environment":{"key":""},"configSource":{"digest":{"key":"digest"},"entryPoint":"entryPoint","uri":"uri"},"parameters":{"key":""}},"metadata":{"buildFinishedOn":"buildFinishedOn","buildStartedOn":"buildStartedOn","reproducible":True,"buildInvocationId":"buildInvocationId","completeness":{"environment":True,"materials":True,"parameters":True}},"materials":[{"digest":{"key":"digest"},"uri":"uri"},{"digest":{"key":"digest"},"uri":"uri"}],"buildType":"buildType","builder":{"id":"id"}},"slsaProvenance":{"metadata":{"buildFinishedOn":"buildFinishedOn","buildStartedOn":"buildStartedOn","reproducible":True,"buildInvocationId":"buildInvocationId","completeness":{"environment":True,"materials":True,"arguments":True}},"materials":[{"digest":{"key":"digest"},"uri":"uri"},{"digest":{"key":"digest"},"uri":"uri"}],"builder":{"id":"id"},"recipe":{"environment":{"key":""},"arguments":{"key":""},"entryPoint":"entryPoint","type":"type","definedInMaterial":"definedInMaterial"}}}},"updateTime":"updateTime","resourceUri":"resourceUri","vulnerability":{"longDescription":"longDescription","severity":"SEVERITY_UNSPECIFIED","fixAvailable":True,"cvssV2":{"exploitabilityScore":7.0614014,"confidentialityImpact":"IMPACT_UNSPECIFIED","attackComplexity":"ATTACK_COMPLEXITY_UNSPECIFIED","scope":"SCOPE_UNSPECIFIED","attackVector":"ATTACK_VECTOR_UNSPECIFIED","availabilityImpact":"IMPACT_UNSPECIFIED","integrityImpact":"IMPACT_UNSPECIFIED","baseScore":2.302136,"privilegesRequired":"PRIVILEGES_REQUIRED_UNSPECIFIED","impactScore":9.301444,"userInteraction":"USER_INTERACTION_UNSPECIFIED","authentication":"AUTHENTICATION_UNSPECIFIED"},"shortDescription":"shortDescription","type":"type","cvssScore":5.637377,"cvssv3":{"exploitabilityScore":7.0614014,"confidentialityImpact":"IMPACT_UNSPECIFIED","attackComplexity":"ATTACK_COMPLEXITY_UNSPECIFIED","scope":"SCOPE_UNSPECIFIED","attackVector":"ATTACK_VECTOR_UNSPECIFIED","availabilityImpact":"IMPACT_UNSPECIFIED","integrityImpact":"IMPACT_UNSPECIFIED","baseScore":2.302136,"privilegesRequired":"PRIVILEGES_REQUIRED_UNSPECIFIED","impactScore":9.301444,"userInteraction":"USER_INTERACTION_UNSPECIFIED","authentication":"AUTHENTICATION_UNSPECIFIED"},"cvssVersion":"CVSS_VERSION_UNSPECIFIED","relatedUrls":[{"label":"label","url":"url"},{"label":"label","url":"url"}],"packageIssue":[{"fixAvailable":True,"fixedVersion":{"inclusive":True,"kind":"VERSION_KIND_UNSPECIFIED","name":"name","fullName":"fullName","epoch":1,"revision":"revision"},"affectedVersion":{"inclusive":True,"kind":"VERSION_KIND_UNSPECIFIED","name":"name","fullName":"fullName","epoch":1,"revision":"revision"},"affectedCpeUri":"affectedCpeUri","affectedPackage":"affectedPackage","fixedPackage":"fixedPackage","fileLocation":[{"filePath":"filePath"},{"filePath":"filePath"}],"effectiveSeverity":"SEVERITY_UNSPECIFIED","packageType":"packageType","fixedCpeUri":"fixedCpeUri"},{"fixAvailable":True,"fixedVersion":{"inclusive":True,"kind":"VERSION_KIND_UNSPECIFIED","name":"name","fullName":"fullName","epoch":1,"revision":"revision"},"affectedVersion":{"inclusive":True,"kind":"VERSION_KIND_UNSPECIFIED","name":"name","fullName":"fullName","epoch":1,"revision":"revision"},"affectedCpeUri":"affectedCpeUri","affectedPackage":"affectedPackage","fixedPackage":"fixedPackage","fileLocation":[{"filePath":"filePath"},{"filePath":"filePath"}],"effectiveSeverity":"SEVERITY_UNSPECIFIED","packageType":"packageType","fixedCpeUri":"fixedCpeUri"}],"extraDetails":"extraDetails","effectiveSeverity":"SEVERITY_UNSPECIFIED","vexAssessment":{"cve":"cve","vulnerabilityId":"vulnerabilityId","relatedUris":[{"label":"label","url":"url"},{"label":"label","url":"url"}],"noteName":"noteName","remediations":[{"remediationType":"REMEDIATION_TYPE_UNSPECIFIED","remediationUri":{"label":"label","url":"url"},"details":"details"},{"remediationType":"REMEDIATION_TYPE_UNSPECIFIED","remediationUri":{"label":"label","url":"url"},"details":"details"}],"impacts":["impacts","impacts"],"justification":{"justificationType":"JUSTIFICATION_TYPE_UNSPECIFIED","details":"details"},"state":"STATE_UNSPECIFIED"}},"remediation":"remediation","envelope":{"payloadType":"payloadType","payload":"payload","signatures":[{"sig":"sig","keyid":"keyid"},{"sig":"sig","keyid":"keyid"}]},"build":{"provenance":{"creator":"creator","triggerId":"triggerId","buildOptions":{"key":"buildOptions"},"sourceProvenance":{"additionalContexts":[{"git":{"revisionId":"revisionId","url":"url"},"gerrit":{"aliasContext":{"kind":"KIND_UNSPECIFIED","name":"name"},"revisionId":"revisionId","hostUri":"hostUri","gerritProject":"gerritProject"},"cloudRepo":{"aliasContext":{"kind":"KIND_UNSPECIFIED","name":"name"},"revisionId":"revisionId","repoId":{"uid":"uid","projectRepoId":{"repoName":"repoName","projectId":"projectId"}}},"labels":{"key":"labels"}},{"git":{"revisionId":"revisionId","url":"url"},"gerrit":{"aliasContext":{"kind":"KIND_UNSPECIFIED","name":"name"},"revisionId":"revisionId","hostUri":"hostUri","gerritProject":"gerritProject"},"cloudRepo":{"aliasContext":{"kind":"KIND_UNSPECIFIED","name":"name"},"revisionId":"revisionId","repoId":{"uid":"uid","projectRepoId":{"repoName":"repoName","projectId":"projectId"}}},"labels":{"key":"labels"}}],"artifactStorageSourceUri":"artifactStorageSourceUri","context":{"git":{"revisionId":"revisionId","url":"url"},"gerrit":{"aliasContext":{"kind":"KIND_UNSPECIFIED","name":"name"},"revisionId":"revisionId","hostUri":"hostUri","gerritProject":"gerritProject"},"cloudRepo":{"aliasContext":{"kind":"KIND_UNSPECIFIED","name":"name"},"revisionId":"revisionId","repoId":{"uid":"uid","projectRepoId":{"repoName":"repoName","projectId":"projectId"}}},"labels":{"key":"labels"}},"fileHashes":{"key":{"fileHash":[{"type":"type","value":"value"},{"type":"type","value":"value"}]}}},"createTime":"createTime","logsUri":"logsUri","builderVersion":"builderVersion","builtArtifacts":[{"names":["names","names"],"checksum":"checksum","id":"id"},{"names":["names","names"],"checksum":"checksum","id":"id"}],"startTime":"startTime","endTime":"endTime","id":"id","projectId":"projectId","commands":[{"args":["args","args"],"name":"name","id":"id","dir":"dir","env":["env","env"],"waitFor":["waitFor","waitFor"]},{"args":["args","args"],"name":"name","id":"id","dir":"dir","env":["env","env"],"waitFor":["waitFor","waitFor"]}]},"provenanceBytes":"provenanceBytes","intotoStatement":{"provenance":{"metadata":{"buildFinishedOn":"buildFinishedOn","buildStartedOn":"buildStartedOn","reproducible":True,"buildInvocationId":"buildInvocationId","completeness":{"environment":True,"materials":True,"arguments":True}},"builderConfig":{"id":"id"},"materials":["materials","materials"],"recipe":{"environment":[{"key":""},{"key":""}],"arguments":[{"key":""},{"key":""}],"entryPoint":"entryPoint","type":"type","definedInMaterial":"definedInMaterial"}},"predicateType":"predicateType","subject":[{"digest":{"key":"digest"},"name":"name"},{"digest":{"key":"digest"},"name":"name"}],"_type":"_type","slsaProvenanceZeroTwo":{"buildConfig":{"key":""},"invocation":{"environment":{"key":""},"configSource":{"digest":{"key":"digest"},"entryPoint":"entryPoint","uri":"uri"},"parameters":{"key":""}},"metadata":{"buildFinishedOn":"buildFinishedOn","buildStartedOn":"buildStartedOn","reproducible":True,"buildInvocationId":"buildInvocationId","completeness":{"environment":True,"materials":True,"parameters":True}},"materials":[{"digest":{"key":"digest"},"uri":"uri"},{"digest":{"key":"digest"},"uri":"uri"}],"buildType":"buildType","builder":{"id":"id"}},"slsaProvenance":{"metadata":{"buildFinishedOn":"buildFinishedOn","buildStartedOn":"buildStartedOn","reproducible":True,"buildInvocationId":"buildInvocationId","completeness":{"environment":True,"materials":True,"arguments":True}},"materials":[{"digest":{"key":"digest"},"uri":"uri"},{"digest":{"key":"digest"},"uri":"uri"}],"builder":{"id":"id"},"recipe":{"environment":{"key":""},"arguments":{"key":""},"entryPoint":"entryPoint","type":"type","definedInMaterial":"definedInMaterial"}}},"inTotoSlsaProvenanceV1":{"predicate":{"runDetails":{"metadata":{"finishedOn":"finishedOn","invocationId":"invocationId","startedOn":"startedOn"},"builder":{"builderDependencies":[{"digest":{"key":"digest"},"name":"name","annotations":{"key":""},"downloadLocation":"downloadLocation","mediaType":"mediaType","uri":"uri","content":"content"},{"digest":{"key":"digest"},"name":"name","annotations":{"key":""},"downloadLocation":"downloadLocation","mediaType":"mediaType","uri":"uri","content":"content"}],"id":"id","version":{"key":"version"}},"byproducts":[{"digest":{"key":"digest"},"name":"name","annotations":{"key":""},"downloadLocation":"downloadLocation","mediaType":"mediaType","uri":"uri","content":"content"},{"digest":{"key":"digest"},"name":"name","annotations":{"key":""},"downloadLocation":"downloadLocation","mediaType":"mediaType","uri":"uri","content":"content"}]},"buildDefinition":{"buildType":"buildType","internalParameters":{"key":""},"resolvedDependencies":[{"digest":{"key":"digest"},"name":"name","annotations":{"key":""},"downloadLocation":"downloadLocation","mediaType":"mediaType","uri":"uri","content":"content"},{"digest":{"key":"digest"},"name":"name","annotations":{"key":""},"downloadLocation":"downloadLocation","mediaType":"mediaType","uri":"uri","content":"content"}],"externalParameters":{"key":""}}},"predicateType":"predicateType","subject":[{"digest":{"key":"digest"},"name":"name"},{"digest":{"key":"digest"},"name":"name"}],"_type":"_type"},"intotoProvenance":{"metadata":{"buildFinishedOn":"buildFinishedOn","buildStartedOn":"buildStartedOn","reproducible":True,"buildInvocationId":"buildInvocationId","completeness":{"environment":True,"materials":True,"arguments":True}},"builderConfig":{"id":"id"},"materials":["materials","materials"],"recipe":{"environment":[{"key":""},{"key":""}],"arguments":[{"key":""},{"key":""}],"entryPoint":"entryPoint","type":"type","definedInMaterial":"definedInMaterial"}}},"createTime":"createTime","compliance":{"nonCompliantFiles":[{"path":"path","reason":"reason","displayCommand":"displayCommand"},{"path":"path","reason":"reason","displayCommand":"displayCommand"}],"nonComplianceReason":"nonComplianceReason"},"discovery":{"lastScanTime":"lastScanTime","archiveTime":"archiveTime","sbomStatus":{"sbomState":"SBOM_STATE_UNSPECIFIED","error":"error"},"analysisCompleted":{"analysisType":["analysisType","analysisType"]},"analysisError":[{"code":0,"details":[{"key":""},{"key":""}],"message":"message"},{"code":0,"details":[{"key":""},{"key":""}],"message":"message"}],"analysisStatusError":{"code":0,"details":[{"key":""},{"key":""}],"message":"message"},"continuousAnalysis":"CONTINUOUS_ANALYSIS_UNSPECIFIED","cpe":"cpe","analysisStatus":"ANALYSIS_STATUS_UNSPECIFIED"},"name":"name","deployment":{"address":"address","undeployTime":"undeployTime","userEmail":"userEmail","deployTime":"deployTime","resourceUri":["resourceUri","resourceUri"],"config":"config","platform":"PLATFORM_UNSPECIFIED"}},{"image":{"distance":6,"fingerprint":{"v1Name":"v1Name","v2Blob":["v2Blob","v2Blob"],"v2Name":"v2Name"},"baseResourceUrl":"baseResourceUrl","layerInfo":[{"arguments":"arguments","directive":"directive"},{"arguments":"arguments","directive":"directive"}]},"attestation":{"serializedPayload":"serializedPayload","jwts":[{"compactJwt":"compactJwt"},{"compactJwt":"compactJwt"}],"signatures":[{"signature":"signature","publicKeyId":"publicKeyId"},{"signature":"signature","publicKeyId":"publicKeyId"}]},"package":{"license":{"comments":"comments","expression":"expression"},"name":"name","location":[{"path":"path","cpeUri":"cpeUri","version":{"inclusive":True,"kind":"VERSION_KIND_UNSPECIFIED","name":"name","fullName":"fullName","epoch":1,"revision":"revision"}},{"path":"path","cpeUri":"cpeUri","version":{"inclusive":True,"kind":"VERSION_KIND_UNSPECIFIED","name":"name","fullName":"fullName","epoch":1,"revision":"revision"}}],"cpeUri":"cpeUri","packageType":"packageType","version":{"inclusive":True,"kind":"VERSION_KIND_UNSPECIFIED","name":"name","fullName":"fullName","epoch":1,"revision":"revision"},"architecture":"ARCHITECTURE_UNSPECIFIED"},"upgrade":{"package":"package","distribution":{"severity":"severity","cve":["cve","cve"],"classification":"classification","cpeUri":"cpeUri"},"parsedVersion":{"inclusive":True,"kind":"VERSION_KIND_UNSPECIFIED","name":"name","fullName":"fullName","epoch":1,"revision":"revision"},"windowsUpdate":{"lastPublishedTimestamp":"lastPublishedTimestamp","identity":{"updateId":"updateId","revision":5},"supportUrl":"supportUrl","description":"description","kbArticleIds":["kbArticleIds","kbArticleIds"],"categories":[{"name":"name","categoryId":"categoryId"},{"name":"name","categoryId":"categoryId"}],"title":"title"}},"kind":"NOTE_KIND_UNSPECIFIED","noteName":"noteName","sbomReference":{"payloadType":"payloadType","payload":{"predicate":{"referrerId":"referrerId","digest":{"key":"digest"},"location":"location","mimeType":"mimeType"},"predicateType":"predicateType","subject":[{"digest":{"key":"digest"},"name":"name"},{"digest":{"key":"digest"},"name":"name"}],"_type":"_type"},"signatures":[{"sig":"sig","keyid":"keyid"},{"sig":"sig","keyid":"keyid"}]},"dsseAttestation":{"envelope":{"payloadType":"payloadType","payload":"payload","signatures":[{"sig":"sig","keyid":"keyid"},{"sig":"sig","keyid":"keyid"}]},"statement":{"provenance":{"metadata":{"buildFinishedOn":"buildFinishedOn","buildStartedOn":"buildStartedOn","reproducible":True,"buildInvocationId":"buildInvocationId","completeness":{"environment":True,"materials":True,"arguments":True}},"builderConfig":{"id":"id"},"materials":["materials","materials"],"recipe":{"environment":[{"key":""},{"key":""}],"arguments":[{"key":""},{"key":""}],"entryPoint":"entryPoint","type":"type","definedInMaterial":"definedInMaterial"}},"predicateType":"predicateType","subject":[{"digest":{"key":"digest"},"name":"name"},{"digest":{"key":"digest"},"name":"name"}],"_type":"_type","slsaProvenanceZeroTwo":{"buildConfig":{"key":""},"invocation":{"environment":{"key":""},"configSource":{"digest":{"key":"digest"},"entryPoint":"entryPoint","uri":"uri"},"parameters":{"key":""}},"metadata":{"buildFinishedOn":"buildFinishedOn","buildStartedOn":"buildStartedOn","reproducible":True,"buildInvocationId":"buildInvocationId","completeness":{"environment":True,"materials":True,"parameters":True}},"materials":[{"digest":{"key":"digest"},"uri":"uri"},{"digest":{"key":"digest"},"uri":"uri"}],"buildType":"buildType","builder":{"id":"id"}},"slsaProvenance":{"metadata":{"buildFinishedOn":"buildFinishedOn","buildStartedOn":"buildStartedOn","reproducible":True,"buildInvocationId":"buildInvocationId","completeness":{"environment":True,"materials":True,"arguments":True}},"materials":[{"digest":{"key":"digest"},"uri":"uri"},{"digest":{"key":"digest"},"uri":"uri"}],"builder":{"id":"id"},"recipe":{"environment":{"key":""},"arguments":{"key":""},"entryPoint":"entryPoint","type":"type","definedInMaterial":"definedInMaterial"}}}},"updateTime":"updateTime","resourceUri":"resourceUri","vulnerability":{"longDescription":"longDescription","severity":"SEVERITY_UNSPECIFIED","fixAvailable":True,"cvssV2":{"exploitabilityScore":7.0614014,"confidentialityImpact":"IMPACT_UNSPECIFIED","attackComplexity":"ATTACK_COMPLEXITY_UNSPECIFIED","scope":"SCOPE_UNSPECIFIED","attackVector":"ATTACK_VECTOR_UNSPECIFIED","availabilityImpact":"IMPACT_UNSPECIFIED","integrityImpact":"IMPACT_UNSPECIFIED","baseScore":2.302136,"privilegesRequired":"PRIVILEGES_REQUIRED_UNSPECIFIED","impactScore":9.301444,"userInteraction":"USER_INTERACTION_UNSPECIFIED","authentication":"AUTHENTICATION_UNSPECIFIED"},"shortDescription":"shortDescription","type":"type","cvssScore":5.637377,"cvssv3":{"exploitabilityScore":7.0614014,"confidentialityImpact":"IMPACT_UNSPECIFIED","attackComplexity":"ATTACK_COMPLEXITY_UNSPECIFIED","scope":"SCOPE_UNSPECIFIED","attackVector":"ATTACK_VECTOR_UNSPECIFIED","availabilityImpact":"IMPACT_UNSPECIFIED","integrityImpact":"IMPACT_UNSPECIFIED","baseScore":2.302136,"privilegesRequired":"PRIVILEGES_REQUIRED_UNSPECIFIED","impactScore":9.301444,"userInteraction":"USER_INTERACTION_UNSPECIFIED","authentication":"AUTHENTICATION_UNSPECIFIED"},"cvssVersion":"CVSS_VERSION_UNSPECIFIED","relatedUrls":[{"label":"label","url":"url"},{"label":"label","url":"url"}],"packageIssue":[{"fixAvailable":True,"fixedVersion":{"inclusive":True,"kind":"VERSION_KIND_UNSPECIFIED","name":"name","fullName":"fullName","epoch":1,"revision":"revision"},"affectedVersion":{"inclusive":True,"kind":"VERSION_KIND_UNSPECIFIED","name":"name","fullName":"fullName","epoch":1,"revision":"revision"},"affectedCpeUri":"affectedCpeUri","affectedPackage":"affectedPackage","fixedPackage":"fixedPackage","fileLocation":[{"filePath":"filePath"},{"filePath":"filePath"}],"effectiveSeverity":"SEVERITY_UNSPECIFIED","packageType":"packageType","fixedCpeUri":"fixedCpeUri"},{"fixAvailable":True,"fixedVersion":{"inclusive":True,"kind":"VERSION_KIND_UNSPECIFIED","name":"name","fullName":"fullName","epoch":1,"revision":"revision"},"affectedVersion":{"inclusive":True,"kind":"VERSION_KIND_UNSPECIFIED","name":"name","fullName":"fullName","epoch":1,"revision":"revision"},"affectedCpeUri":"affectedCpeUri","affectedPackage":"affectedPackage","fixedPackage":"fixedPackage","fileLocation":[{"filePath":"filePath"},{"filePath":"filePath"}],"effectiveSeverity":"SEVERITY_UNSPECIFIED","packageType":"packageType","fixedCpeUri":"fixedCpeUri"}],"extraDetails":"extraDetails","effectiveSeverity":"SEVERITY_UNSPECIFIED","vexAssessment":{"cve":"cve","vulnerabilityId":"vulnerabilityId","relatedUris":[{"label":"label","url":"url"},{"label":"label","url":"url"}],"noteName":"noteName","remediations":[{"remediationType":"REMEDIATION_TYPE_UNSPECIFIED","remediationUri":{"label":"label","url":"url"},"details":"details"},{"remediationType":"REMEDIATION_TYPE_UNSPECIFIED","remediationUri":{"label":"label","url":"url"},"details":"details"}],"impacts":["impacts","impacts"],"justification":{"justificationType":"JUSTIFICATION_TYPE_UNSPECIFIED","details":"details"},"state":"STATE_UNSPECIFIED"}},"remediation":"remediation","envelope":{"payloadType":"payloadType","payload":"payload","signatures":[{"sig":"sig","keyid":"keyid"},{"sig":"sig","keyid":"keyid"}]},"build":{"provenance":{"creator":"creator","triggerId":"triggerId","buildOptions":{"key":"buildOptions"},"sourceProvenance":{"additionalContexts":[{"git":{"revisionId":"revisionId","url":"url"},"gerrit":{"aliasContext":{"kind":"KIND_UNSPECIFIED","name":"name"},"revisionId":"revisionId","hostUri":"hostUri","gerritProject":"gerritProject"},"cloudRepo":{"aliasContext":{"kind":"KIND_UNSPECIFIED","name":"name"},"revisionId":"revisionId","repoId":{"uid":"uid","projectRepoId":{"repoName":"repoName","projectId":"projectId"}}},"labels":{"key":"labels"}},{"git":{"revisionId":"revisionId","url":"url"},"gerrit":{"aliasContext":{"kind":"KIND_UNSPECIFIED","name":"name"},"revisionId":"revisionId","hostUri":"hostUri","gerritProject":"gerritProject"},"cloudRepo":{"aliasContext":{"kind":"KIND_UNSPECIFIED","name":"name"},"revisionId":"revisionId","repoId":{"uid":"uid","projectRepoId":{"repoName":"repoName","projectId":"projectId"}}},"labels":{"key":"labels"}}],"artifactStorageSourceUri":"artifactStorageSourceUri","context":{"git":{"revisionId":"revisionId","url":"url"},"gerrit":{"aliasContext":{"kind":"KIND_UNSPECIFIED","name":"name"},"revisionId":"revisionId","hostUri":"hostUri","gerritProject":"gerritProject"},"cloudRepo":{"aliasContext":{"kind":"KIND_UNSPECIFIED","name":"name"},"revisionId":"revisionId","repoId":{"uid":"uid","projectRepoId":{"repoName":"repoName","projectId":"projectId"}}},"labels":{"key":"labels"}},"fileHashes":{"key":{"fileHash":[{"type":"type","value":"value"},{"type":"type","value":"value"}]}}},"createTime":"createTime","logsUri":"logsUri","builderVersion":"builderVersion","builtArtifacts":[{"names":["names","names"],"checksum":"checksum","id":"id"},{"names":["names","names"],"checksum":"checksum","id":"id"}],"startTime":"startTime","endTime":"endTime","id":"id","projectId":"projectId","commands":[{"args":["args","args"],"name":"name","id":"id","dir":"dir","env":["env","env"],"waitFor":["waitFor","waitFor"]},{"args":["args","args"],"name":"name","id":"id","dir":"dir","env":["env","env"],"waitFor":["waitFor","waitFor"]}]},"provenanceBytes":"provenanceBytes","intotoStatement":{"provenance":{"metadata":{"buildFinishedOn":"buildFinishedOn","buildStartedOn":"buildStartedOn","reproducible":True,"buildInvocationId":"buildInvocationId","completeness":{"environment":True,"materials":True,"arguments":True}},"builderConfig":{"id":"id"},"materials":["materials","materials"],"recipe":{"environment":[{"key":""},{"key":""}],"arguments":[{"key":""},{"key":""}],"entryPoint":"entryPoint","type":"type","definedInMaterial":"definedInMaterial"}},"predicateType":"predicateType","subject":[{"digest":{"key":"digest"},"name":"name"},{"digest":{"key":"digest"},"name":"name"}],"_type":"_type","slsaProvenanceZeroTwo":{"buildConfig":{"key":""},"invocation":{"environment":{"key":""},"configSource":{"digest":{"key":"digest"},"entryPoint":"entryPoint","uri":"uri"},"parameters":{"key":""}},"metadata":{"buildFinishedOn":"buildFinishedOn","buildStartedOn":"buildStartedOn","reproducible":True,"buildInvocationId":"buildInvocationId","completeness":{"environment":True,"materials":True,"parameters":True}},"materials":[{"digest":{"key":"digest"},"uri":"uri"},{"digest":{"key":"digest"},"uri":"uri"}],"buildType":"buildType","builder":{"id":"id"}},"slsaProvenance":{"metadata":{"buildFinishedOn":"buildFinishedOn","buildStartedOn":"buildStartedOn","reproducible":True,"buildInvocationId":"buildInvocationId","completeness":{"environment":True,"materials":True,"arguments":True}},"materials":[{"digest":{"key":"digest"},"uri":"uri"},{"digest":{"key":"digest"},"uri":"uri"}],"builder":{"id":"id"},"recipe":{"environment":{"key":""},"arguments":{"key":""},"entryPoint":"entryPoint","type":"type","definedInMaterial":"definedInMaterial"}}},"inTotoSlsaProvenanceV1":{"predicate":{"runDetails":{"metadata":{"finishedOn":"finishedOn","invocationId":"invocationId","startedOn":"startedOn"},"builder":{"builderDependencies":[{"digest":{"key":"digest"},"name":"name","annotations":{"key":""},"downloadLocation":"downloadLocation","mediaType":"mediaType","uri":"uri","content":"content"},{"digest":{"key":"digest"},"name":"name","annotations":{"key":""},"downloadLocation":"downloadLocation","mediaType":"mediaType","uri":"uri","content":"content"}],"id":"id","version":{"key":"version"}},"byproducts":[{"digest":{"key":"digest"},"name":"name","annotations":{"key":""},"downloadLocation":"downloadLocation","mediaType":"mediaType","uri":"uri","content":"content"},{"digest":{"key":"digest"},"name":"name","annotations":{"key":""},"downloadLocation":"downloadLocation","mediaType":"mediaType","uri":"uri","content":"content"}]},"buildDefinition":{"buildType":"buildType","internalParameters":{"key":""},"resolvedDependencies":[{"digest":{"key":"digest"},"name":"name","annotations":{"key":""},"downloadLocation":"downloadLocation","mediaType":"mediaType","uri":"uri","content":"content"},{"digest":{"key":"digest"},"name":"name","annotations":{"key":""},"downloadLocation":"downloadLocation","mediaType":"mediaType","uri":"uri","content":"content"}],"externalParameters":{"key":""}}},"predicateType":"predicateType","subject":[{"digest":{"key":"digest"},"name":"name"},{"digest":{"key":"digest"},"name":"name"}],"_type":"_type"},"intotoProvenance":{"metadata":{"buildFinishedOn":"buildFinishedOn","buildStartedOn":"buildStartedOn","reproducible":True,"buildInvocationId":"buildInvocationId","completeness":{"environment":True,"materials":True,"arguments":True}},"builderConfig":{"id":"id"},"materials":["materials","materials"],"recipe":{"environment":[{"key":""},{"key":""}],"arguments":[{"key":""},{"key":""}],"entryPoint":"entryPoint","type":"type","definedInMaterial":"definedInMaterial"}}},"createTime":"createTime","compliance":{"nonCompliantFiles":[{"path":"path","reason":"reason","displayCommand":"displayCommand"},{"path":"path","reason":"reason","displayCommand":"displayCommand"}],"nonComplianceReason":"nonComplianceReason"},"discovery":{"lastScanTime":"lastScanTime","archiveTime":"archiveTime","sbomStatus":{"sbomState":"SBOM_STATE_UNSPECIFIED","error":"error"},"analysisCompleted":{"analysisType":["analysisType","analysisType"]},"analysisError":[{"code":0,"details":[{"key":""},{"key":""}],"message":"message"},{"code":0,"details":[{"key":""},{"key":""}],"message":"message"}],"analysisStatusError":{"code":0,"details":[{"key":""},{"key":""}],"message":"message"},"continuousAnalysis":"CONTINUOUS_ANALYSIS_UNSPECIFIED","cpe":"cpe","analysisStatus":"ANALYSIS_STATUS_UNSPECIFIED"},"name":"name","deployment":{"address":"address","undeployTime":"undeployTime","userEmail":"userEmail","deployTime":"deployTime","resourceUri":["resourceUri","resourceUri"],"config":"config","platform":"PLATFORM_UNSPECIFIED"}}]}
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
        path='/v1/{parent}/occurrences:batchCreate'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_containeranalysis_projects_occurrences_create(client):
    """Test case for containeranalysis_projects_occurrences_create

    
    """
    body = {"image":{"distance":6,"fingerprint":{"v1Name":"v1Name","v2Blob":["v2Blob","v2Blob"],"v2Name":"v2Name"},"baseResourceUrl":"baseResourceUrl","layerInfo":[{"arguments":"arguments","directive":"directive"},{"arguments":"arguments","directive":"directive"}]},"attestation":{"serializedPayload":"serializedPayload","jwts":[{"compactJwt":"compactJwt"},{"compactJwt":"compactJwt"}],"signatures":[{"signature":"signature","publicKeyId":"publicKeyId"},{"signature":"signature","publicKeyId":"publicKeyId"}]},"package":{"license":{"comments":"comments","expression":"expression"},"name":"name","location":[{"path":"path","cpeUri":"cpeUri","version":{"inclusive":True,"kind":"VERSION_KIND_UNSPECIFIED","name":"name","fullName":"fullName","epoch":1,"revision":"revision"}},{"path":"path","cpeUri":"cpeUri","version":{"inclusive":True,"kind":"VERSION_KIND_UNSPECIFIED","name":"name","fullName":"fullName","epoch":1,"revision":"revision"}}],"cpeUri":"cpeUri","packageType":"packageType","version":{"inclusive":True,"kind":"VERSION_KIND_UNSPECIFIED","name":"name","fullName":"fullName","epoch":1,"revision":"revision"},"architecture":"ARCHITECTURE_UNSPECIFIED"},"upgrade":{"package":"package","distribution":{"severity":"severity","cve":["cve","cve"],"classification":"classification","cpeUri":"cpeUri"},"parsedVersion":{"inclusive":True,"kind":"VERSION_KIND_UNSPECIFIED","name":"name","fullName":"fullName","epoch":1,"revision":"revision"},"windowsUpdate":{"lastPublishedTimestamp":"lastPublishedTimestamp","identity":{"updateId":"updateId","revision":5},"supportUrl":"supportUrl","description":"description","kbArticleIds":["kbArticleIds","kbArticleIds"],"categories":[{"name":"name","categoryId":"categoryId"},{"name":"name","categoryId":"categoryId"}],"title":"title"}},"kind":"NOTE_KIND_UNSPECIFIED","noteName":"noteName","sbomReference":{"payloadType":"payloadType","payload":{"predicate":{"referrerId":"referrerId","digest":{"key":"digest"},"location":"location","mimeType":"mimeType"},"predicateType":"predicateType","subject":[{"digest":{"key":"digest"},"name":"name"},{"digest":{"key":"digest"},"name":"name"}],"_type":"_type"},"signatures":[{"sig":"sig","keyid":"keyid"},{"sig":"sig","keyid":"keyid"}]},"dsseAttestation":{"envelope":{"payloadType":"payloadType","payload":"payload","signatures":[{"sig":"sig","keyid":"keyid"},{"sig":"sig","keyid":"keyid"}]},"statement":{"provenance":{"metadata":{"buildFinishedOn":"buildFinishedOn","buildStartedOn":"buildStartedOn","reproducible":True,"buildInvocationId":"buildInvocationId","completeness":{"environment":True,"materials":True,"arguments":True}},"builderConfig":{"id":"id"},"materials":["materials","materials"],"recipe":{"environment":[{"key":""},{"key":""}],"arguments":[{"key":""},{"key":""}],"entryPoint":"entryPoint","type":"type","definedInMaterial":"definedInMaterial"}},"predicateType":"predicateType","subject":[{"digest":{"key":"digest"},"name":"name"},{"digest":{"key":"digest"},"name":"name"}],"_type":"_type","slsaProvenanceZeroTwo":{"buildConfig":{"key":""},"invocation":{"environment":{"key":""},"configSource":{"digest":{"key":"digest"},"entryPoint":"entryPoint","uri":"uri"},"parameters":{"key":""}},"metadata":{"buildFinishedOn":"buildFinishedOn","buildStartedOn":"buildStartedOn","reproducible":True,"buildInvocationId":"buildInvocationId","completeness":{"environment":True,"materials":True,"parameters":True}},"materials":[{"digest":{"key":"digest"},"uri":"uri"},{"digest":{"key":"digest"},"uri":"uri"}],"buildType":"buildType","builder":{"id":"id"}},"slsaProvenance":{"metadata":{"buildFinishedOn":"buildFinishedOn","buildStartedOn":"buildStartedOn","reproducible":True,"buildInvocationId":"buildInvocationId","completeness":{"environment":True,"materials":True,"arguments":True}},"materials":[{"digest":{"key":"digest"},"uri":"uri"},{"digest":{"key":"digest"},"uri":"uri"}],"builder":{"id":"id"},"recipe":{"environment":{"key":""},"arguments":{"key":""},"entryPoint":"entryPoint","type":"type","definedInMaterial":"definedInMaterial"}}}},"updateTime":"updateTime","resourceUri":"resourceUri","vulnerability":{"longDescription":"longDescription","severity":"SEVERITY_UNSPECIFIED","fixAvailable":True,"cvssV2":{"exploitabilityScore":7.0614014,"confidentialityImpact":"IMPACT_UNSPECIFIED","attackComplexity":"ATTACK_COMPLEXITY_UNSPECIFIED","scope":"SCOPE_UNSPECIFIED","attackVector":"ATTACK_VECTOR_UNSPECIFIED","availabilityImpact":"IMPACT_UNSPECIFIED","integrityImpact":"IMPACT_UNSPECIFIED","baseScore":2.302136,"privilegesRequired":"PRIVILEGES_REQUIRED_UNSPECIFIED","impactScore":9.301444,"userInteraction":"USER_INTERACTION_UNSPECIFIED","authentication":"AUTHENTICATION_UNSPECIFIED"},"shortDescription":"shortDescription","type":"type","cvssScore":5.637377,"cvssv3":{"exploitabilityScore":7.0614014,"confidentialityImpact":"IMPACT_UNSPECIFIED","attackComplexity":"ATTACK_COMPLEXITY_UNSPECIFIED","scope":"SCOPE_UNSPECIFIED","attackVector":"ATTACK_VECTOR_UNSPECIFIED","availabilityImpact":"IMPACT_UNSPECIFIED","integrityImpact":"IMPACT_UNSPECIFIED","baseScore":2.302136,"privilegesRequired":"PRIVILEGES_REQUIRED_UNSPECIFIED","impactScore":9.301444,"userInteraction":"USER_INTERACTION_UNSPECIFIED","authentication":"AUTHENTICATION_UNSPECIFIED"},"cvssVersion":"CVSS_VERSION_UNSPECIFIED","relatedUrls":[{"label":"label","url":"url"},{"label":"label","url":"url"}],"packageIssue":[{"fixAvailable":True,"fixedVersion":{"inclusive":True,"kind":"VERSION_KIND_UNSPECIFIED","name":"name","fullName":"fullName","epoch":1,"revision":"revision"},"affectedVersion":{"inclusive":True,"kind":"VERSION_KIND_UNSPECIFIED","name":"name","fullName":"fullName","epoch":1,"revision":"revision"},"affectedCpeUri":"affectedCpeUri","affectedPackage":"affectedPackage","fixedPackage":"fixedPackage","fileLocation":[{"filePath":"filePath"},{"filePath":"filePath"}],"effectiveSeverity":"SEVERITY_UNSPECIFIED","packageType":"packageType","fixedCpeUri":"fixedCpeUri"},{"fixAvailable":True,"fixedVersion":{"inclusive":True,"kind":"VERSION_KIND_UNSPECIFIED","name":"name","fullName":"fullName","epoch":1,"revision":"revision"},"affectedVersion":{"inclusive":True,"kind":"VERSION_KIND_UNSPECIFIED","name":"name","fullName":"fullName","epoch":1,"revision":"revision"},"affectedCpeUri":"affectedCpeUri","affectedPackage":"affectedPackage","fixedPackage":"fixedPackage","fileLocation":[{"filePath":"filePath"},{"filePath":"filePath"}],"effectiveSeverity":"SEVERITY_UNSPECIFIED","packageType":"packageType","fixedCpeUri":"fixedCpeUri"}],"extraDetails":"extraDetails","effectiveSeverity":"SEVERITY_UNSPECIFIED","vexAssessment":{"cve":"cve","vulnerabilityId":"vulnerabilityId","relatedUris":[{"label":"label","url":"url"},{"label":"label","url":"url"}],"noteName":"noteName","remediations":[{"remediationType":"REMEDIATION_TYPE_UNSPECIFIED","remediationUri":{"label":"label","url":"url"},"details":"details"},{"remediationType":"REMEDIATION_TYPE_UNSPECIFIED","remediationUri":{"label":"label","url":"url"},"details":"details"}],"impacts":["impacts","impacts"],"justification":{"justificationType":"JUSTIFICATION_TYPE_UNSPECIFIED","details":"details"},"state":"STATE_UNSPECIFIED"}},"remediation":"remediation","envelope":{"payloadType":"payloadType","payload":"payload","signatures":[{"sig":"sig","keyid":"keyid"},{"sig":"sig","keyid":"keyid"}]},"build":{"provenance":{"creator":"creator","triggerId":"triggerId","buildOptions":{"key":"buildOptions"},"sourceProvenance":{"additionalContexts":[{"git":{"revisionId":"revisionId","url":"url"},"gerrit":{"aliasContext":{"kind":"KIND_UNSPECIFIED","name":"name"},"revisionId":"revisionId","hostUri":"hostUri","gerritProject":"gerritProject"},"cloudRepo":{"aliasContext":{"kind":"KIND_UNSPECIFIED","name":"name"},"revisionId":"revisionId","repoId":{"uid":"uid","projectRepoId":{"repoName":"repoName","projectId":"projectId"}}},"labels":{"key":"labels"}},{"git":{"revisionId":"revisionId","url":"url"},"gerrit":{"aliasContext":{"kind":"KIND_UNSPECIFIED","name":"name"},"revisionId":"revisionId","hostUri":"hostUri","gerritProject":"gerritProject"},"cloudRepo":{"aliasContext":{"kind":"KIND_UNSPECIFIED","name":"name"},"revisionId":"revisionId","repoId":{"uid":"uid","projectRepoId":{"repoName":"repoName","projectId":"projectId"}}},"labels":{"key":"labels"}}],"artifactStorageSourceUri":"artifactStorageSourceUri","context":{"git":{"revisionId":"revisionId","url":"url"},"gerrit":{"aliasContext":{"kind":"KIND_UNSPECIFIED","name":"name"},"revisionId":"revisionId","hostUri":"hostUri","gerritProject":"gerritProject"},"cloudRepo":{"aliasContext":{"kind":"KIND_UNSPECIFIED","name":"name"},"revisionId":"revisionId","repoId":{"uid":"uid","projectRepoId":{"repoName":"repoName","projectId":"projectId"}}},"labels":{"key":"labels"}},"fileHashes":{"key":{"fileHash":[{"type":"type","value":"value"},{"type":"type","value":"value"}]}}},"createTime":"createTime","logsUri":"logsUri","builderVersion":"builderVersion","builtArtifacts":[{"names":["names","names"],"checksum":"checksum","id":"id"},{"names":["names","names"],"checksum":"checksum","id":"id"}],"startTime":"startTime","endTime":"endTime","id":"id","projectId":"projectId","commands":[{"args":["args","args"],"name":"name","id":"id","dir":"dir","env":["env","env"],"waitFor":["waitFor","waitFor"]},{"args":["args","args"],"name":"name","id":"id","dir":"dir","env":["env","env"],"waitFor":["waitFor","waitFor"]}]},"provenanceBytes":"provenanceBytes","intotoStatement":{"provenance":{"metadata":{"buildFinishedOn":"buildFinishedOn","buildStartedOn":"buildStartedOn","reproducible":True,"buildInvocationId":"buildInvocationId","completeness":{"environment":True,"materials":True,"arguments":True}},"builderConfig":{"id":"id"},"materials":["materials","materials"],"recipe":{"environment":[{"key":""},{"key":""}],"arguments":[{"key":""},{"key":""}],"entryPoint":"entryPoint","type":"type","definedInMaterial":"definedInMaterial"}},"predicateType":"predicateType","subject":[{"digest":{"key":"digest"},"name":"name"},{"digest":{"key":"digest"},"name":"name"}],"_type":"_type","slsaProvenanceZeroTwo":{"buildConfig":{"key":""},"invocation":{"environment":{"key":""},"configSource":{"digest":{"key":"digest"},"entryPoint":"entryPoint","uri":"uri"},"parameters":{"key":""}},"metadata":{"buildFinishedOn":"buildFinishedOn","buildStartedOn":"buildStartedOn","reproducible":True,"buildInvocationId":"buildInvocationId","completeness":{"environment":True,"materials":True,"parameters":True}},"materials":[{"digest":{"key":"digest"},"uri":"uri"},{"digest":{"key":"digest"},"uri":"uri"}],"buildType":"buildType","builder":{"id":"id"}},"slsaProvenance":{"metadata":{"buildFinishedOn":"buildFinishedOn","buildStartedOn":"buildStartedOn","reproducible":True,"buildInvocationId":"buildInvocationId","completeness":{"environment":True,"materials":True,"arguments":True}},"materials":[{"digest":{"key":"digest"},"uri":"uri"},{"digest":{"key":"digest"},"uri":"uri"}],"builder":{"id":"id"},"recipe":{"environment":{"key":""},"arguments":{"key":""},"entryPoint":"entryPoint","type":"type","definedInMaterial":"definedInMaterial"}}},"inTotoSlsaProvenanceV1":{"predicate":{"runDetails":{"metadata":{"finishedOn":"finishedOn","invocationId":"invocationId","startedOn":"startedOn"},"builder":{"builderDependencies":[{"digest":{"key":"digest"},"name":"name","annotations":{"key":""},"downloadLocation":"downloadLocation","mediaType":"mediaType","uri":"uri","content":"content"},{"digest":{"key":"digest"},"name":"name","annotations":{"key":""},"downloadLocation":"downloadLocation","mediaType":"mediaType","uri":"uri","content":"content"}],"id":"id","version":{"key":"version"}},"byproducts":[{"digest":{"key":"digest"},"name":"name","annotations":{"key":""},"downloadLocation":"downloadLocation","mediaType":"mediaType","uri":"uri","content":"content"},{"digest":{"key":"digest"},"name":"name","annotations":{"key":""},"downloadLocation":"downloadLocation","mediaType":"mediaType","uri":"uri","content":"content"}]},"buildDefinition":{"buildType":"buildType","internalParameters":{"key":""},"resolvedDependencies":[{"digest":{"key":"digest"},"name":"name","annotations":{"key":""},"downloadLocation":"downloadLocation","mediaType":"mediaType","uri":"uri","content":"content"},{"digest":{"key":"digest"},"name":"name","annotations":{"key":""},"downloadLocation":"downloadLocation","mediaType":"mediaType","uri":"uri","content":"content"}],"externalParameters":{"key":""}}},"predicateType":"predicateType","subject":[{"digest":{"key":"digest"},"name":"name"},{"digest":{"key":"digest"},"name":"name"}],"_type":"_type"},"intotoProvenance":{"metadata":{"buildFinishedOn":"buildFinishedOn","buildStartedOn":"buildStartedOn","reproducible":True,"buildInvocationId":"buildInvocationId","completeness":{"environment":True,"materials":True,"arguments":True}},"builderConfig":{"id":"id"},"materials":["materials","materials"],"recipe":{"environment":[{"key":""},{"key":""}],"arguments":[{"key":""},{"key":""}],"entryPoint":"entryPoint","type":"type","definedInMaterial":"definedInMaterial"}}},"createTime":"createTime","compliance":{"nonCompliantFiles":[{"path":"path","reason":"reason","displayCommand":"displayCommand"},{"path":"path","reason":"reason","displayCommand":"displayCommand"}],"nonComplianceReason":"nonComplianceReason"},"discovery":{"lastScanTime":"lastScanTime","archiveTime":"archiveTime","sbomStatus":{"sbomState":"SBOM_STATE_UNSPECIFIED","error":"error"},"analysisCompleted":{"analysisType":["analysisType","analysisType"]},"analysisError":[{"code":0,"details":[{"key":""},{"key":""}],"message":"message"},{"code":0,"details":[{"key":""},{"key":""}],"message":"message"}],"analysisStatusError":{"code":0,"details":[{"key":""},{"key":""}],"message":"message"},"continuousAnalysis":"CONTINUOUS_ANALYSIS_UNSPECIFIED","cpe":"cpe","analysisStatus":"ANALYSIS_STATUS_UNSPECIFIED"},"name":"name","deployment":{"address":"address","undeployTime":"undeployTime","userEmail":"userEmail","deployTime":"deployTime","resourceUri":["resourceUri","resourceUri"],"config":"config","platform":"PLATFORM_UNSPECIFIED"}}
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
        path='/v1/{parent}/occurrences'.format(parent='parent_example'),
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
        path='/v1/{name}'.format(name='name_example'),
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
        path='/v1/{name}'.format(name='name_example'),
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
        path='/v1/{resourceget_iam_polic}'.format(resource='resource_example'),
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
        path='/v1/{name}/notes'.format(name='name_example'),
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
        path='/v1/{parent}/occurrences:vulnerabilitySummary'.format(parent='parent_example'),
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
        path='/v1/{parent}/occurrences'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_containeranalysis_projects_occurrences_patch(client):
    """Test case for containeranalysis_projects_occurrences_patch

    
    """
    body = {"image":{"distance":6,"fingerprint":{"v1Name":"v1Name","v2Blob":["v2Blob","v2Blob"],"v2Name":"v2Name"},"baseResourceUrl":"baseResourceUrl","layerInfo":[{"arguments":"arguments","directive":"directive"},{"arguments":"arguments","directive":"directive"}]},"attestation":{"serializedPayload":"serializedPayload","jwts":[{"compactJwt":"compactJwt"},{"compactJwt":"compactJwt"}],"signatures":[{"signature":"signature","publicKeyId":"publicKeyId"},{"signature":"signature","publicKeyId":"publicKeyId"}]},"package":{"license":{"comments":"comments","expression":"expression"},"name":"name","location":[{"path":"path","cpeUri":"cpeUri","version":{"inclusive":True,"kind":"VERSION_KIND_UNSPECIFIED","name":"name","fullName":"fullName","epoch":1,"revision":"revision"}},{"path":"path","cpeUri":"cpeUri","version":{"inclusive":True,"kind":"VERSION_KIND_UNSPECIFIED","name":"name","fullName":"fullName","epoch":1,"revision":"revision"}}],"cpeUri":"cpeUri","packageType":"packageType","version":{"inclusive":True,"kind":"VERSION_KIND_UNSPECIFIED","name":"name","fullName":"fullName","epoch":1,"revision":"revision"},"architecture":"ARCHITECTURE_UNSPECIFIED"},"upgrade":{"package":"package","distribution":{"severity":"severity","cve":["cve","cve"],"classification":"classification","cpeUri":"cpeUri"},"parsedVersion":{"inclusive":True,"kind":"VERSION_KIND_UNSPECIFIED","name":"name","fullName":"fullName","epoch":1,"revision":"revision"},"windowsUpdate":{"lastPublishedTimestamp":"lastPublishedTimestamp","identity":{"updateId":"updateId","revision":5},"supportUrl":"supportUrl","description":"description","kbArticleIds":["kbArticleIds","kbArticleIds"],"categories":[{"name":"name","categoryId":"categoryId"},{"name":"name","categoryId":"categoryId"}],"title":"title"}},"kind":"NOTE_KIND_UNSPECIFIED","noteName":"noteName","sbomReference":{"payloadType":"payloadType","payload":{"predicate":{"referrerId":"referrerId","digest":{"key":"digest"},"location":"location","mimeType":"mimeType"},"predicateType":"predicateType","subject":[{"digest":{"key":"digest"},"name":"name"},{"digest":{"key":"digest"},"name":"name"}],"_type":"_type"},"signatures":[{"sig":"sig","keyid":"keyid"},{"sig":"sig","keyid":"keyid"}]},"dsseAttestation":{"envelope":{"payloadType":"payloadType","payload":"payload","signatures":[{"sig":"sig","keyid":"keyid"},{"sig":"sig","keyid":"keyid"}]},"statement":{"provenance":{"metadata":{"buildFinishedOn":"buildFinishedOn","buildStartedOn":"buildStartedOn","reproducible":True,"buildInvocationId":"buildInvocationId","completeness":{"environment":True,"materials":True,"arguments":True}},"builderConfig":{"id":"id"},"materials":["materials","materials"],"recipe":{"environment":[{"key":""},{"key":""}],"arguments":[{"key":""},{"key":""}],"entryPoint":"entryPoint","type":"type","definedInMaterial":"definedInMaterial"}},"predicateType":"predicateType","subject":[{"digest":{"key":"digest"},"name":"name"},{"digest":{"key":"digest"},"name":"name"}],"_type":"_type","slsaProvenanceZeroTwo":{"buildConfig":{"key":""},"invocation":{"environment":{"key":""},"configSource":{"digest":{"key":"digest"},"entryPoint":"entryPoint","uri":"uri"},"parameters":{"key":""}},"metadata":{"buildFinishedOn":"buildFinishedOn","buildStartedOn":"buildStartedOn","reproducible":True,"buildInvocationId":"buildInvocationId","completeness":{"environment":True,"materials":True,"parameters":True}},"materials":[{"digest":{"key":"digest"},"uri":"uri"},{"digest":{"key":"digest"},"uri":"uri"}],"buildType":"buildType","builder":{"id":"id"}},"slsaProvenance":{"metadata":{"buildFinishedOn":"buildFinishedOn","buildStartedOn":"buildStartedOn","reproducible":True,"buildInvocationId":"buildInvocationId","completeness":{"environment":True,"materials":True,"arguments":True}},"materials":[{"digest":{"key":"digest"},"uri":"uri"},{"digest":{"key":"digest"},"uri":"uri"}],"builder":{"id":"id"},"recipe":{"environment":{"key":""},"arguments":{"key":""},"entryPoint":"entryPoint","type":"type","definedInMaterial":"definedInMaterial"}}}},"updateTime":"updateTime","resourceUri":"resourceUri","vulnerability":{"longDescription":"longDescription","severity":"SEVERITY_UNSPECIFIED","fixAvailable":True,"cvssV2":{"exploitabilityScore":7.0614014,"confidentialityImpact":"IMPACT_UNSPECIFIED","attackComplexity":"ATTACK_COMPLEXITY_UNSPECIFIED","scope":"SCOPE_UNSPECIFIED","attackVector":"ATTACK_VECTOR_UNSPECIFIED","availabilityImpact":"IMPACT_UNSPECIFIED","integrityImpact":"IMPACT_UNSPECIFIED","baseScore":2.302136,"privilegesRequired":"PRIVILEGES_REQUIRED_UNSPECIFIED","impactScore":9.301444,"userInteraction":"USER_INTERACTION_UNSPECIFIED","authentication":"AUTHENTICATION_UNSPECIFIED"},"shortDescription":"shortDescription","type":"type","cvssScore":5.637377,"cvssv3":{"exploitabilityScore":7.0614014,"confidentialityImpact":"IMPACT_UNSPECIFIED","attackComplexity":"ATTACK_COMPLEXITY_UNSPECIFIED","scope":"SCOPE_UNSPECIFIED","attackVector":"ATTACK_VECTOR_UNSPECIFIED","availabilityImpact":"IMPACT_UNSPECIFIED","integrityImpact":"IMPACT_UNSPECIFIED","baseScore":2.302136,"privilegesRequired":"PRIVILEGES_REQUIRED_UNSPECIFIED","impactScore":9.301444,"userInteraction":"USER_INTERACTION_UNSPECIFIED","authentication":"AUTHENTICATION_UNSPECIFIED"},"cvssVersion":"CVSS_VERSION_UNSPECIFIED","relatedUrls":[{"label":"label","url":"url"},{"label":"label","url":"url"}],"packageIssue":[{"fixAvailable":True,"fixedVersion":{"inclusive":True,"kind":"VERSION_KIND_UNSPECIFIED","name":"name","fullName":"fullName","epoch":1,"revision":"revision"},"affectedVersion":{"inclusive":True,"kind":"VERSION_KIND_UNSPECIFIED","name":"name","fullName":"fullName","epoch":1,"revision":"revision"},"affectedCpeUri":"affectedCpeUri","affectedPackage":"affectedPackage","fixedPackage":"fixedPackage","fileLocation":[{"filePath":"filePath"},{"filePath":"filePath"}],"effectiveSeverity":"SEVERITY_UNSPECIFIED","packageType":"packageType","fixedCpeUri":"fixedCpeUri"},{"fixAvailable":True,"fixedVersion":{"inclusive":True,"kind":"VERSION_KIND_UNSPECIFIED","name":"name","fullName":"fullName","epoch":1,"revision":"revision"},"affectedVersion":{"inclusive":True,"kind":"VERSION_KIND_UNSPECIFIED","name":"name","fullName":"fullName","epoch":1,"revision":"revision"},"affectedCpeUri":"affectedCpeUri","affectedPackage":"affectedPackage","fixedPackage":"fixedPackage","fileLocation":[{"filePath":"filePath"},{"filePath":"filePath"}],"effectiveSeverity":"SEVERITY_UNSPECIFIED","packageType":"packageType","fixedCpeUri":"fixedCpeUri"}],"extraDetails":"extraDetails","effectiveSeverity":"SEVERITY_UNSPECIFIED","vexAssessment":{"cve":"cve","vulnerabilityId":"vulnerabilityId","relatedUris":[{"label":"label","url":"url"},{"label":"label","url":"url"}],"noteName":"noteName","remediations":[{"remediationType":"REMEDIATION_TYPE_UNSPECIFIED","remediationUri":{"label":"label","url":"url"},"details":"details"},{"remediationType":"REMEDIATION_TYPE_UNSPECIFIED","remediationUri":{"label":"label","url":"url"},"details":"details"}],"impacts":["impacts","impacts"],"justification":{"justificationType":"JUSTIFICATION_TYPE_UNSPECIFIED","details":"details"},"state":"STATE_UNSPECIFIED"}},"remediation":"remediation","envelope":{"payloadType":"payloadType","payload":"payload","signatures":[{"sig":"sig","keyid":"keyid"},{"sig":"sig","keyid":"keyid"}]},"build":{"provenance":{"creator":"creator","triggerId":"triggerId","buildOptions":{"key":"buildOptions"},"sourceProvenance":{"additionalContexts":[{"git":{"revisionId":"revisionId","url":"url"},"gerrit":{"aliasContext":{"kind":"KIND_UNSPECIFIED","name":"name"},"revisionId":"revisionId","hostUri":"hostUri","gerritProject":"gerritProject"},"cloudRepo":{"aliasContext":{"kind":"KIND_UNSPECIFIED","name":"name"},"revisionId":"revisionId","repoId":{"uid":"uid","projectRepoId":{"repoName":"repoName","projectId":"projectId"}}},"labels":{"key":"labels"}},{"git":{"revisionId":"revisionId","url":"url"},"gerrit":{"aliasContext":{"kind":"KIND_UNSPECIFIED","name":"name"},"revisionId":"revisionId","hostUri":"hostUri","gerritProject":"gerritProject"},"cloudRepo":{"aliasContext":{"kind":"KIND_UNSPECIFIED","name":"name"},"revisionId":"revisionId","repoId":{"uid":"uid","projectRepoId":{"repoName":"repoName","projectId":"projectId"}}},"labels":{"key":"labels"}}],"artifactStorageSourceUri":"artifactStorageSourceUri","context":{"git":{"revisionId":"revisionId","url":"url"},"gerrit":{"aliasContext":{"kind":"KIND_UNSPECIFIED","name":"name"},"revisionId":"revisionId","hostUri":"hostUri","gerritProject":"gerritProject"},"cloudRepo":{"aliasContext":{"kind":"KIND_UNSPECIFIED","name":"name"},"revisionId":"revisionId","repoId":{"uid":"uid","projectRepoId":{"repoName":"repoName","projectId":"projectId"}}},"labels":{"key":"labels"}},"fileHashes":{"key":{"fileHash":[{"type":"type","value":"value"},{"type":"type","value":"value"}]}}},"createTime":"createTime","logsUri":"logsUri","builderVersion":"builderVersion","builtArtifacts":[{"names":["names","names"],"checksum":"checksum","id":"id"},{"names":["names","names"],"checksum":"checksum","id":"id"}],"startTime":"startTime","endTime":"endTime","id":"id","projectId":"projectId","commands":[{"args":["args","args"],"name":"name","id":"id","dir":"dir","env":["env","env"],"waitFor":["waitFor","waitFor"]},{"args":["args","args"],"name":"name","id":"id","dir":"dir","env":["env","env"],"waitFor":["waitFor","waitFor"]}]},"provenanceBytes":"provenanceBytes","intotoStatement":{"provenance":{"metadata":{"buildFinishedOn":"buildFinishedOn","buildStartedOn":"buildStartedOn","reproducible":True,"buildInvocationId":"buildInvocationId","completeness":{"environment":True,"materials":True,"arguments":True}},"builderConfig":{"id":"id"},"materials":["materials","materials"],"recipe":{"environment":[{"key":""},{"key":""}],"arguments":[{"key":""},{"key":""}],"entryPoint":"entryPoint","type":"type","definedInMaterial":"definedInMaterial"}},"predicateType":"predicateType","subject":[{"digest":{"key":"digest"},"name":"name"},{"digest":{"key":"digest"},"name":"name"}],"_type":"_type","slsaProvenanceZeroTwo":{"buildConfig":{"key":""},"invocation":{"environment":{"key":""},"configSource":{"digest":{"key":"digest"},"entryPoint":"entryPoint","uri":"uri"},"parameters":{"key":""}},"metadata":{"buildFinishedOn":"buildFinishedOn","buildStartedOn":"buildStartedOn","reproducible":True,"buildInvocationId":"buildInvocationId","completeness":{"environment":True,"materials":True,"parameters":True}},"materials":[{"digest":{"key":"digest"},"uri":"uri"},{"digest":{"key":"digest"},"uri":"uri"}],"buildType":"buildType","builder":{"id":"id"}},"slsaProvenance":{"metadata":{"buildFinishedOn":"buildFinishedOn","buildStartedOn":"buildStartedOn","reproducible":True,"buildInvocationId":"buildInvocationId","completeness":{"environment":True,"materials":True,"arguments":True}},"materials":[{"digest":{"key":"digest"},"uri":"uri"},{"digest":{"key":"digest"},"uri":"uri"}],"builder":{"id":"id"},"recipe":{"environment":{"key":""},"arguments":{"key":""},"entryPoint":"entryPoint","type":"type","definedInMaterial":"definedInMaterial"}}},"inTotoSlsaProvenanceV1":{"predicate":{"runDetails":{"metadata":{"finishedOn":"finishedOn","invocationId":"invocationId","startedOn":"startedOn"},"builder":{"builderDependencies":[{"digest":{"key":"digest"},"name":"name","annotations":{"key":""},"downloadLocation":"downloadLocation","mediaType":"mediaType","uri":"uri","content":"content"},{"digest":{"key":"digest"},"name":"name","annotations":{"key":""},"downloadLocation":"downloadLocation","mediaType":"mediaType","uri":"uri","content":"content"}],"id":"id","version":{"key":"version"}},"byproducts":[{"digest":{"key":"digest"},"name":"name","annotations":{"key":""},"downloadLocation":"downloadLocation","mediaType":"mediaType","uri":"uri","content":"content"},{"digest":{"key":"digest"},"name":"name","annotations":{"key":""},"downloadLocation":"downloadLocation","mediaType":"mediaType","uri":"uri","content":"content"}]},"buildDefinition":{"buildType":"buildType","internalParameters":{"key":""},"resolvedDependencies":[{"digest":{"key":"digest"},"name":"name","annotations":{"key":""},"downloadLocation":"downloadLocation","mediaType":"mediaType","uri":"uri","content":"content"},{"digest":{"key":"digest"},"name":"name","annotations":{"key":""},"downloadLocation":"downloadLocation","mediaType":"mediaType","uri":"uri","content":"content"}],"externalParameters":{"key":""}}},"predicateType":"predicateType","subject":[{"digest":{"key":"digest"},"name":"name"},{"digest":{"key":"digest"},"name":"name"}],"_type":"_type"},"intotoProvenance":{"metadata":{"buildFinishedOn":"buildFinishedOn","buildStartedOn":"buildStartedOn","reproducible":True,"buildInvocationId":"buildInvocationId","completeness":{"environment":True,"materials":True,"arguments":True}},"builderConfig":{"id":"id"},"materials":["materials","materials"],"recipe":{"environment":[{"key":""},{"key":""}],"arguments":[{"key":""},{"key":""}],"entryPoint":"entryPoint","type":"type","definedInMaterial":"definedInMaterial"}}},"createTime":"createTime","compliance":{"nonCompliantFiles":[{"path":"path","reason":"reason","displayCommand":"displayCommand"},{"path":"path","reason":"reason","displayCommand":"displayCommand"}],"nonComplianceReason":"nonComplianceReason"},"discovery":{"lastScanTime":"lastScanTime","archiveTime":"archiveTime","sbomStatus":{"sbomState":"SBOM_STATE_UNSPECIFIED","error":"error"},"analysisCompleted":{"analysisType":["analysisType","analysisType"]},"analysisError":[{"code":0,"details":[{"key":""},{"key":""}],"message":"message"},{"code":0,"details":[{"key":""},{"key":""}],"message":"message"}],"analysisStatusError":{"code":0,"details":[{"key":""},{"key":""}],"message":"message"},"continuousAnalysis":"CONTINUOUS_ANALYSIS_UNSPECIFIED","cpe":"cpe","analysisStatus":"ANALYSIS_STATUS_UNSPECIFIED"},"name":"name","deployment":{"address":"address","undeployTime":"undeployTime","userEmail":"userEmail","deployTime":"deployTime","resourceUri":["resourceUri","resourceUri"],"config":"config","platform":"PLATFORM_UNSPECIFIED"}}
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
        path='/v1/{resourceset_iam_polic}'.format(resource='resource_example'),
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
        path='/v1/{resourcetest_iam_permission}'.format(resource='resource_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_containeranalysis_projects_resources_export_sbom(client):
    """Test case for containeranalysis_projects_resources_export_sbom

    
    """
    body = {"cloudStorageLocation":"{}"}
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
        path='/v1/{nameexport_sbo}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

