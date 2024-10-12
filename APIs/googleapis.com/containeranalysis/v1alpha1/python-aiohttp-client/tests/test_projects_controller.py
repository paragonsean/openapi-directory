# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_operation_request import CreateOperationRequest
from openapi_server.models.get_vulnz_occurrences_summary_response import GetVulnzOccurrencesSummaryResponse
from openapi_server.models.list_notes_response import ListNotesResponse
from openapi_server.models.list_occurrences_response import ListOccurrencesResponse
from openapi_server.models.list_scan_configs_response import ListScanConfigsResponse
from openapi_server.models.note import Note
from openapi_server.models.occurrence import Occurrence
from openapi_server.models.operation import Operation


pytestmark = pytest.mark.asyncio

async def test_containeranalysis_projects_notes_create(client):
    """Test case for containeranalysis_projects_notes_create

    
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
                    ('name', 'name_example'),
                    ('noteId', 'note_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1alpha1/{parent}/notes'.format(parent='parent_example'),
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
                    ('name', 'name_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1alpha1/{parent}/notes'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_containeranalysis_projects_occurrences_create(client):
    """Test case for containeranalysis_projects_occurrences_create

    
    """
    body = {"discovered":{"lastScanTime":"lastScanTime","archiveTime":"archiveTime","sbomStatus":{"sbomState":"SBOM_STATE_UNSPECIFIED","error":"error"},"analysisCompleted":{"analysisType":["analysisType","analysisType"]},"analysisError":[{"code":6,"details":[{"key":""},{"key":""}],"message":"message"},{"code":6,"details":[{"key":""},{"key":""}],"message":"message"}],"analysisStatusError":{"code":6,"details":[{"key":""},{"key":""}],"message":"message"},"continuousAnalysis":"CONTINUOUS_ANALYSIS_UNSPECIFIED","cpe":"cpe","operation":{"metadata":{"key":""},"response":{"key":""},"name":"name","error":{"code":6,"details":[{"key":""},{"key":""}],"message":"message"},"done":True},"analysisStatus":"ANALYSIS_STATUS_UNSPECIFIED"},"attestation":{"pgpSignedAttestation":{"pgpKeyId":"pgpKeyId","signature":"signature","contentType":"CONTENT_TYPE_UNSPECIFIED"}},"upgrade":{"package":"package","distribution":{"severity":"severity","cve":["cve","cve"],"classification":"classification","cpeUri":"cpeUri"},"parsedVersion":{"inclusive":True,"kind":"NORMAL","name":"name","epoch":6,"revision":"revision"}},"resource":{"name":"name","uri":"uri","contentHash":{"type":"NONE","value":"value"}},"kind":"KIND_UNSPECIFIED","noteName":"noteName","sbomReference":{"payloadType":"payloadType","payload":{"predicate":{"referrerId":"referrerId","digest":{"key":"digest"},"location":"location","mimeType":"mimeType"},"predicateType":"predicateType","subject":[{"digest":{"key":"digest"},"name":"name"},{"digest":{"key":"digest"},"name":"name"}],"_type":"_type"},"signatures":[{"sig":"sig","keyid":"keyid"},{"sig":"sig","keyid":"keyid"}]},"dsseAttestation":{"envelope":{"payloadType":"payloadType","payload":"payload","signatures":[{"sig":"sig","keyid":"keyid"},{"sig":"sig","keyid":"keyid"}]},"statement":{"provenance":{"metadata":{"buildFinishedOn":"buildFinishedOn","buildStartedOn":"buildStartedOn","reproducible":True,"buildInvocationId":"buildInvocationId","completeness":{"environment":True,"materials":True,"arguments":True}},"builderConfig":{"id":"id"},"materials":["materials","materials"],"recipe":{"environment":[{"key":""},{"key":""}],"arguments":[{"key":""},{"key":""}],"entryPoint":"entryPoint","type":"type","definedInMaterial":"definedInMaterial"}},"predicateType":"predicateType","subject":[{"digest":{"key":"digest"},"name":"name"},{"digest":{"key":"digest"},"name":"name"}],"_type":"_type","slsaProvenanceZeroTwo":{"buildConfig":{"key":""},"invocation":{"environment":{"key":""},"configSource":{"digest":{"key":"digest"},"entryPoint":"entryPoint","uri":"uri"},"parameters":{"key":""}},"metadata":{"buildFinishedOn":"buildFinishedOn","buildStartedOn":"buildStartedOn","reproducible":True,"buildInvocationId":"buildInvocationId","completeness":{"environment":True,"materials":True,"parameters":True}},"materials":[{"digest":{"key":"digest"},"uri":"uri"},{"digest":{"key":"digest"},"uri":"uri"}],"buildType":"buildType","builder":{"id":"id"}},"slsaProvenance":{"metadata":{"buildFinishedOn":"buildFinishedOn","buildStartedOn":"buildStartedOn","reproducible":True,"buildInvocationId":"buildInvocationId","completeness":{"environment":True,"materials":True,"arguments":True}},"materials":[{"digest":{"key":"digest"},"uri":"uri"},{"digest":{"key":"digest"},"uri":"uri"}],"builder":{"id":"id"},"recipe":{"environment":{"key":""},"arguments":{"key":""},"entryPoint":"entryPoint","type":"type","definedInMaterial":"definedInMaterial"}}}},"updateTime":"updateTime","spdxRelationship":{"comment":"comment","source":"source","type":"RELATIONSHIP_TYPE_UNSPECIFIED","target":"target"},"vulnerabilityDetails":{"severity":"SEVERITY_UNSPECIFIED","cvssScore":1.4658129,"cvssV3":{"exploitabilityScore":5.637377,"confidentialityImpact":"IMPACT_UNSPECIFIED","attackComplexity":"ATTACK_COMPLEXITY_UNSPECIFIED","scope":"SCOPE_UNSPECIFIED","attackVector":"ATTACK_VECTOR_UNSPECIFIED","availabilityImpact":"IMPACT_UNSPECIFIED","integrityImpact":"IMPACT_UNSPECIFIED","baseScore":5.962134,"privilegesRequired":"PRIVILEGES_REQUIRED_UNSPECIFIED","impactScore":2.302136,"userInteraction":"USER_INTERACTION_UNSPECIFIED","authentication":"AUTHENTICATION_UNSPECIFIED"},"cvssVersion":"CVSS_VERSION_UNSPECIFIED","packageIssue":[{"affectedLocation":{"package":"package","fileLocation":[{"filePath":"filePath"},{"filePath":"filePath"}],"cpeUri":"cpeUri","version":{"inclusive":True,"kind":"NORMAL","name":"name","epoch":6,"revision":"revision"}},"effectiveSeverity":"SEVERITY_UNSPECIFIED","fixedLocation":{"package":"package","fileLocation":[{"filePath":"filePath"},{"filePath":"filePath"}],"cpeUri":"cpeUri","version":{"inclusive":True,"kind":"NORMAL","name":"name","epoch":6,"revision":"revision"}},"packageType":"packageType","severityName":"severityName"},{"affectedLocation":{"package":"package","fileLocation":[{"filePath":"filePath"},{"filePath":"filePath"}],"cpeUri":"cpeUri","version":{"inclusive":True,"kind":"NORMAL","name":"name","epoch":6,"revision":"revision"}},"effectiveSeverity":"SEVERITY_UNSPECIFIED","fixedLocation":{"package":"package","fileLocation":[{"filePath":"filePath"},{"filePath":"filePath"}],"cpeUri":"cpeUri","version":{"inclusive":True,"kind":"NORMAL","name":"name","epoch":6,"revision":"revision"}},"packageType":"packageType","severityName":"severityName"}],"cvssV2":{"exploitabilityScore":5.637377,"confidentialityImpact":"IMPACT_UNSPECIFIED","attackComplexity":"ATTACK_COMPLEXITY_UNSPECIFIED","scope":"SCOPE_UNSPECIFIED","attackVector":"ATTACK_VECTOR_UNSPECIFIED","availabilityImpact":"IMPACT_UNSPECIFIED","integrityImpact":"IMPACT_UNSPECIFIED","baseScore":5.962134,"privilegesRequired":"PRIVILEGES_REQUIRED_UNSPECIFIED","impactScore":2.302136,"userInteraction":"USER_INTERACTION_UNSPECIFIED","authentication":"AUTHENTICATION_UNSPECIFIED"},"extraDetails":"extraDetails","type":"type","effectiveSeverity":"SEVERITY_UNSPECIFIED","vexAssessment":{"cve":"cve","vulnerabilityId":"vulnerabilityId","relatedUris":[{"label":"label","uri":"uri"},{"label":"label","uri":"uri"}],"noteName":"noteName","remediations":[{"remediationType":"REMEDIATION_TYPE_UNSPECIFIED","remediationUri":{"label":"label","uri":"uri"},"details":"details"},{"remediationType":"REMEDIATION_TYPE_UNSPECIFIED","remediationUri":{"label":"label","uri":"uri"},"details":"details"}],"impacts":["impacts","impacts"],"justification":{"justificationType":"JUSTIFICATION_TYPE_UNSPECIFIED","details":"details"},"state":"STATE_UNSPECIFIED"}},"spdxFile":{"copyright":"copyright","filesLicenseInfo":["filesLicenseInfo","filesLicenseInfo"],"licenseConcluded":{"comments":"comments","expression":"expression"},"comment":"comment","contributors":["contributors","contributors"],"id":"id","attributions":["attributions","attributions"],"notice":"notice"},"remediation":"remediation","envelope":{"payloadType":"payloadType","payload":"payload","signatures":[{"sig":"sig","keyid":"keyid"},{"sig":"sig","keyid":"keyid"}]},"resourceUrl":"resourceUrl","createTime":"createTime","compliance":{"nonCompliantFiles":[{"path":"path","reason":"reason","displayCommand":"displayCommand"},{"path":"path","reason":"reason","displayCommand":"displayCommand"}],"nonComplianceReason":"nonComplianceReason"},"spdxPackage":{"sourceInfo":"sourceInfo","filename":"filename","licenseConcluded":{"comments":"comments","expression":"expression"},"comment":"comment","id":"id","title":"title","homePage":"homePage","packageType":"packageType","summaryDescription":"summaryDescription","version":"version"},"installation":{"license":{"comments":"comments","expression":"expression"},"name":"name","location":[{"path":"path","cpeUri":"cpeUri","version":{"inclusive":True,"kind":"NORMAL","name":"name","epoch":6,"revision":"revision"}},{"path":"path","cpeUri":"cpeUri","version":{"inclusive":True,"kind":"NORMAL","name":"name","epoch":6,"revision":"revision"}}],"cpeUri":"cpeUri","packageType":"packageType","version":{"inclusive":True,"kind":"NORMAL","name":"name","epoch":6,"revision":"revision"},"architecture":"ARCHITECTURE_UNSPECIFIED"},"buildDetails":{"provenance":{"creator":"creator","finishTime":"finishTime","triggerId":"triggerId","buildOptions":{"key":"buildOptions"},"sourceProvenance":{"artifactStorageSource":{"bucket":"bucket","generation":"generation","object":"object"},"additionalContexts":[{"git":{"revisionId":"revisionId","url":"url"},"gerrit":{"aliasContext":{"kind":"KIND_UNSPECIFIED","name":"name"},"revisionId":"revisionId","hostUri":"hostUri","gerritProject":"gerritProject"},"cloudRepo":{"aliasContext":{"kind":"KIND_UNSPECIFIED","name":"name"},"revisionId":"revisionId","repoId":{"uid":"uid","projectRepoId":{"repoName":"repoName","projectId":"projectId"}}},"labels":{"key":"labels"}},{"git":{"revisionId":"revisionId","url":"url"},"gerrit":{"aliasContext":{"kind":"KIND_UNSPECIFIED","name":"name"},"revisionId":"revisionId","hostUri":"hostUri","gerritProject":"gerritProject"},"cloudRepo":{"aliasContext":{"kind":"KIND_UNSPECIFIED","name":"name"},"revisionId":"revisionId","repoId":{"uid":"uid","projectRepoId":{"repoName":"repoName","projectId":"projectId"}}},"labels":{"key":"labels"}}],"context":{"git":{"revisionId":"revisionId","url":"url"},"gerrit":{"aliasContext":{"kind":"KIND_UNSPECIFIED","name":"name"},"revisionId":"revisionId","hostUri":"hostUri","gerritProject":"gerritProject"},"cloudRepo":{"aliasContext":{"kind":"KIND_UNSPECIFIED","name":"name"},"revisionId":"revisionId","repoId":{"uid":"uid","projectRepoId":{"repoName":"repoName","projectId":"projectId"}}},"labels":{"key":"labels"}},"fileHashes":{"key":{"fileHash":[{"type":"NONE","value":"value"},{"type":"NONE","value":"value"}]}},"storageSource":{"bucket":"bucket","generation":"generation","object":"object"},"repoSource":{"repoName":"repoName","branchName":"branchName","commitSha":"commitSha","tagName":"tagName","projectId":"projectId"}},"createTime":"createTime","logsBucket":"logsBucket","builderVersion":"builderVersion","builtArtifacts":[{"names":["names","names"],"checksum":"checksum","name":"name","id":"id"},{"names":["names","names"],"checksum":"checksum","name":"name","id":"id"}],"startTime":"startTime","id":"id","projectId":"projectId","commands":[{"args":["args","args"],"name":"name","id":"id","dir":"dir","env":["env","env"],"waitFor":["waitFor","waitFor"]},{"args":["args","args"],"name":"name","id":"id","dir":"dir","env":["env","env"],"waitFor":["waitFor","waitFor"]}]},"provenanceBytes":"provenanceBytes","intotoStatement":{"provenance":{"metadata":{"buildFinishedOn":"buildFinishedOn","buildStartedOn":"buildStartedOn","reproducible":True,"buildInvocationId":"buildInvocationId","completeness":{"environment":True,"materials":True,"arguments":True}},"builderConfig":{"id":"id"},"materials":["materials","materials"],"recipe":{"environment":[{"key":""},{"key":""}],"arguments":[{"key":""},{"key":""}],"entryPoint":"entryPoint","type":"type","definedInMaterial":"definedInMaterial"}},"predicateType":"predicateType","subject":[{"digest":{"key":"digest"},"name":"name"},{"digest":{"key":"digest"},"name":"name"}],"_type":"_type","slsaProvenanceZeroTwo":{"buildConfig":{"key":""},"invocation":{"environment":{"key":""},"configSource":{"digest":{"key":"digest"},"entryPoint":"entryPoint","uri":"uri"},"parameters":{"key":""}},"metadata":{"buildFinishedOn":"buildFinishedOn","buildStartedOn":"buildStartedOn","reproducible":True,"buildInvocationId":"buildInvocationId","completeness":{"environment":True,"materials":True,"parameters":True}},"materials":[{"digest":{"key":"digest"},"uri":"uri"},{"digest":{"key":"digest"},"uri":"uri"}],"buildType":"buildType","builder":{"id":"id"}},"slsaProvenance":{"metadata":{"buildFinishedOn":"buildFinishedOn","buildStartedOn":"buildStartedOn","reproducible":True,"buildInvocationId":"buildInvocationId","completeness":{"environment":True,"materials":True,"arguments":True}},"materials":[{"digest":{"key":"digest"},"uri":"uri"},{"digest":{"key":"digest"},"uri":"uri"}],"builder":{"id":"id"},"recipe":{"environment":{"key":""},"arguments":{"key":""},"entryPoint":"entryPoint","type":"type","definedInMaterial":"definedInMaterial"}}},"inTotoSlsaProvenanceV1":{"predicate":{"runDetails":{"metadata":{"finishedOn":"finishedOn","invocationId":"invocationId","startedOn":"startedOn"},"builder":{"builderDependencies":[{"digest":{"key":"digest"},"name":"name","annotations":{"key":""},"downloadLocation":"downloadLocation","mediaType":"mediaType","uri":"uri","content":"content"},{"digest":{"key":"digest"},"name":"name","annotations":{"key":""},"downloadLocation":"downloadLocation","mediaType":"mediaType","uri":"uri","content":"content"}],"id":"id","version":{"key":"version"}},"byproducts":[{"digest":{"key":"digest"},"name":"name","annotations":{"key":""},"downloadLocation":"downloadLocation","mediaType":"mediaType","uri":"uri","content":"content"},{"digest":{"key":"digest"},"name":"name","annotations":{"key":""},"downloadLocation":"downloadLocation","mediaType":"mediaType","uri":"uri","content":"content"}]},"buildDefinition":{"buildType":"buildType","internalParameters":{"key":""},"resolvedDependencies":[{"digest":{"key":"digest"},"name":"name","annotations":{"key":""},"downloadLocation":"downloadLocation","mediaType":"mediaType","uri":"uri","content":"content"},{"digest":{"key":"digest"},"name":"name","annotations":{"key":""},"downloadLocation":"downloadLocation","mediaType":"mediaType","uri":"uri","content":"content"}],"externalParameters":{"key":""}}},"predicateType":"predicateType","subject":[{"digest":{"key":"digest"},"name":"name"},{"digest":{"key":"digest"},"name":"name"}],"_type":"_type"},"intotoProvenance":{"metadata":{"buildFinishedOn":"buildFinishedOn","buildStartedOn":"buildStartedOn","reproducible":True,"buildInvocationId":"buildInvocationId","completeness":{"environment":True,"materials":True,"arguments":True}},"builderConfig":{"id":"id"},"materials":["materials","materials"],"recipe":{"environment":[{"key":""},{"key":""}],"arguments":[{"key":""},{"key":""}],"entryPoint":"entryPoint","type":"type","definedInMaterial":"definedInMaterial"}}},"name":"name","sbom":{"creatorComment":"creatorComment","documentComment":"documentComment","licenseListVersion":"licenseListVersion","createTime":"createTime","creators":["creators","creators"],"namespace":"namespace","externalDocumentRefs":["externalDocumentRefs","externalDocumentRefs"],"id":"id","title":"title"},"deployment":{"address":"address","undeployTime":"undeployTime","userEmail":"userEmail","deployTime":"deployTime","resourceUri":["resourceUri","resourceUri"],"config":"config","platform":"PLATFORM_UNSPECIFIED"},"derivedImage":{"distance":0,"fingerprint":{"v1Name":"v1Name","v2Blob":["v2Blob","v2Blob"],"v2Name":"v2Name"},"baseResourceUrl":"baseResourceUrl","layerInfo":[{"arguments":"arguments","directive":"DIRECTIVE_UNSPECIFIED"},{"arguments":"arguments","directive":"DIRECTIVE_UNSPECIFIED"}]}}
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
                    ('name', 'name_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1alpha1/{parent}/occurrences'.format(parent='parent_example'),
        headers=headers,
        json=body,
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
        path='/v1alpha1/{parent}/occurrences:vulnerabilitySummary'.format(parent='parent_example'),
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
                    ('kind', 'kind_example'),
                    ('name', 'name_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1alpha1/{parent}/occurrences'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_containeranalysis_projects_operations_create(client):
    """Test case for containeranalysis_projects_operations_create

    
    """
    body = {"operationId":"operationId","operation":{"metadata":{"key":""},"response":{"key":""},"name":"name","error":{"code":6,"details":[{"key":""},{"key":""}],"message":"message"},"done":True}}
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
        path='/v1alpha1/{parent}/operations'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_containeranalysis_projects_scan_configs_list(client):
    """Test case for containeranalysis_projects_scan_configs_list

    
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
        path='/v1alpha1/{parent}/scanConfigs'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

