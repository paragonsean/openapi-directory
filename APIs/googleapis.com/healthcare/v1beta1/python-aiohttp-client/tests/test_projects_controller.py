# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.activate_consent_request import ActivateConsentRequest
from openapi_server.models.analyze_entities_request import AnalyzeEntitiesRequest
from openapi_server.models.analyze_entities_response import AnalyzeEntitiesResponse
from openapi_server.models.annotation import Annotation
from openapi_server.models.annotation_store import AnnotationStore
from openapi_server.models.apply_admin_consents_request import ApplyAdminConsentsRequest
from openapi_server.models.apply_consents_request import ApplyConsentsRequest
from openapi_server.models.attribute_definition import AttributeDefinition
from openapi_server.models.batch_get_messages_response import BatchGetMessagesResponse
from openapi_server.models.check_data_access_request import CheckDataAccessRequest
from openapi_server.models.check_data_access_response import CheckDataAccessResponse
from openapi_server.models.configure_search_request import ConfigureSearchRequest
from openapi_server.models.consent import Consent
from openapi_server.models.consent_artifact import ConsentArtifact
from openapi_server.models.consent_store import ConsentStore
from openapi_server.models.create_message_request import CreateMessageRequest
from openapi_server.models.dataset import Dataset
from openapi_server.models.deidentify_dataset_request import DeidentifyDatasetRequest
from openapi_server.models.deidentify_fhir_store_request import DeidentifyFhirStoreRequest
from openapi_server.models.dicom_store import DicomStore
from openapi_server.models.dicom_store_metrics import DicomStoreMetrics
from openapi_server.models.evaluate_annotation_store_request import EvaluateAnnotationStoreRequest
from openapi_server.models.evaluate_user_consents_request import EvaluateUserConsentsRequest
from openapi_server.models.evaluate_user_consents_response import EvaluateUserConsentsResponse
from openapi_server.models.explain_data_access_response import ExplainDataAccessResponse
from openapi_server.models.export_messages_request import ExportMessagesRequest
from openapi_server.models.fhir_store import FhirStore
from openapi_server.models.fhir_store_metrics import FhirStoreMetrics
from openapi_server.models.hl7_v2_store import Hl7V2Store
from openapi_server.models.hl7_v2_store_metrics import Hl7V2StoreMetrics
from openapi_server.models.http_body import HttpBody
from openapi_server.models.import_messages_request import ImportMessagesRequest
from openapi_server.models.ingest_message_request import IngestMessageRequest
from openapi_server.models.ingest_message_response import IngestMessageResponse
from openapi_server.models.list_annotation_stores_response import ListAnnotationStoresResponse
from openapi_server.models.list_annotations_response import ListAnnotationsResponse
from openapi_server.models.list_attribute_definitions_response import ListAttributeDefinitionsResponse
from openapi_server.models.list_consent_artifacts_response import ListConsentArtifactsResponse
from openapi_server.models.list_consent_revisions_response import ListConsentRevisionsResponse
from openapi_server.models.list_consent_stores_response import ListConsentStoresResponse
from openapi_server.models.list_consents_response import ListConsentsResponse
from openapi_server.models.list_datasets_response import ListDatasetsResponse
from openapi_server.models.list_dicom_stores_response import ListDicomStoresResponse
from openapi_server.models.list_fhir_stores_response import ListFhirStoresResponse
from openapi_server.models.list_hl7_v2_stores_response import ListHl7V2StoresResponse
from openapi_server.models.list_locations_response import ListLocationsResponse
from openapi_server.models.list_messages_response import ListMessagesResponse
from openapi_server.models.list_operations_response import ListOperationsResponse
from openapi_server.models.list_user_data_mappings_response import ListUserDataMappingsResponse
from openapi_server.models.message import Message
from openapi_server.models.operation import Operation
from openapi_server.models.policy import Policy
from openapi_server.models.query_accessible_data_request import QueryAccessibleDataRequest
from openapi_server.models.reject_consent_request import RejectConsentRequest
from openapi_server.models.revoke_consent_request import RevokeConsentRequest
from openapi_server.models.rollback_fhir_resources_request import RollbackFhirResourcesRequest
from openapi_server.models.search_resources_request import SearchResourcesRequest
from openapi_server.models.series_metrics import SeriesMetrics
from openapi_server.models.set_blob_storage_settings_request import SetBlobStorageSettingsRequest
from openapi_server.models.set_iam_policy_request import SetIamPolicyRequest
from openapi_server.models.storage_info import StorageInfo
from openapi_server.models.study_metrics import StudyMetrics
from openapi_server.models.test_iam_permissions_request import TestIamPermissionsRequest
from openapi_server.models.test_iam_permissions_response import TestIamPermissionsResponse
from openapi_server.models.user_data_mapping import UserDataMapping


pytestmark = pytest.mark.asyncio

async def test_healthcare_projects_locations_datasets_annotation_stores_annotations_create(client):
    """Test case for healthcare_projects_locations_datasets_annotation_stores_annotations_create

    
    """
    body = {"imageAnnotation":{"frameIndex":1,"boundingPolys":[{"vertices":[{"x":0.8008282,"y":6.0274563},{"x":0.8008282,"y":6.0274563}],"label":"label"},{"vertices":[{"x":0.8008282,"y":6.0274563},{"x":0.8008282,"y":6.0274563}],"label":"label"}]},"textAnnotation":{"details":{"key":{"findings":[{"infoType":"infoType","quote":"quote","start":"start","end":"end"},{"infoType":"infoType","quote":"quote","start":"start","end":"end"}]}}},"annotationSource":{"cloudHealthcareSource":{"name":"name"}},"resourceAnnotation":{"label":"label"},"name":"name","customData":{"key":"customData"}}
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
        path='/v1beta1/{parent}/annotations'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_healthcare_projects_locations_datasets_annotation_stores_annotations_list(client):
    """Test case for healthcare_projects_locations_datasets_annotation_stores_annotations_list

    
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
                    ('view', 'view_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1beta1/{parent}/annotations'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_healthcare_projects_locations_datasets_annotation_stores_create(client):
    """Test case for healthcare_projects_locations_datasets_annotation_stores_create

    
    """
    body = {"name":"name","labels":{"key":"labels"}}
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
                    ('annotationStoreId', 'annotation_store_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta1/{parent}/annotationStores'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_healthcare_projects_locations_datasets_annotation_stores_evaluate(client):
    """Test case for healthcare_projects_locations_datasets_annotation_stores_evaluate

    
    """
    body = {"goldenInfoTypeMapping":{"key":"goldenInfoTypeMapping"},"bigqueryDestination":{"writeDisposition":"WRITE_DISPOSITION_UNSPECIFIED","schemaType":"SCHEMA_TYPE_UNSPECIFIED","force":True,"tableUri":"tableUri"},"evalInfoTypeMapping":{"key":"evalInfoTypeMapping"},"goldenStore":"goldenStore","infoTypeConfig":{"ignoreList":{"infoTypes":["infoTypes","infoTypes"]},"evaluateList":{"infoTypes":["infoTypes","infoTypes"]},"strictMatching":True}}
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
        path='/v1beta1/{nameevaluat}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_healthcare_projects_locations_datasets_annotation_stores_list(client):
    """Test case for healthcare_projects_locations_datasets_annotation_stores_list

    
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
        path='/v1beta1/{parent}/annotationStores'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_healthcare_projects_locations_datasets_consent_stores_attribute_definitions_create(client):
    """Test case for healthcare_projects_locations_datasets_consent_stores_attribute_definitions_create

    
    """
    body = {"allowedValues":["allowedValues","allowedValues"],"consentDefaultValues":["consentDefaultValues","consentDefaultValues"],"name":"name","description":"description","category":"CATEGORY_UNSPECIFIED","dataMappingDefaultValue":"dataMappingDefaultValue"}
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
                    ('attributeDefinitionId', 'attribute_definition_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta1/{parent}/attributeDefinitions'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_healthcare_projects_locations_datasets_consent_stores_attribute_definitions_list(client):
    """Test case for healthcare_projects_locations_datasets_consent_stores_attribute_definitions_list

    
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
        path='/v1beta1/{parent}/attributeDefinitions'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_healthcare_projects_locations_datasets_consent_stores_check_data_access(client):
    """Test case for healthcare_projects_locations_datasets_consent_stores_check_data_access

    
    """
    body = {"consentList":{"consents":["consents","consents"]},"requestAttributes":{"key":"requestAttributes"},"dataId":"dataId","responseView":"RESPONSE_VIEW_UNSPECIFIED"}
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
        path='/v1beta1/{consent_storecheck_data_acces}'.format(consent_store='consent_store_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_healthcare_projects_locations_datasets_consent_stores_consent_artifacts_create(client):
    """Test case for healthcare_projects_locations_datasets_consent_stores_consent_artifacts_create

    
    """
    body = {"userSignature":{"image":{"gcsUri":"gcsUri","rawBytes":"rawBytes"},"metadata":{"key":"metadata"},"userId":"userId","signatureTime":"signatureTime"},"consentContentVersion":"consentContentVersion","consentContentScreenshots":[{"gcsUri":"gcsUri","rawBytes":"rawBytes"},{"gcsUri":"gcsUri","rawBytes":"rawBytes"}],"metadata":{"key":"metadata"},"witnessSignature":{"image":{"gcsUri":"gcsUri","rawBytes":"rawBytes"},"metadata":{"key":"metadata"},"userId":"userId","signatureTime":"signatureTime"},"name":"name","guardianSignature":{"image":{"gcsUri":"gcsUri","rawBytes":"rawBytes"},"metadata":{"key":"metadata"},"userId":"userId","signatureTime":"signatureTime"},"userId":"userId"}
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
        path='/v1beta1/{parent}/consentArtifacts'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_healthcare_projects_locations_datasets_consent_stores_consent_artifacts_list(client):
    """Test case for healthcare_projects_locations_datasets_consent_stores_consent_artifacts_list

    
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
        path='/v1beta1/{parent}/consentArtifacts'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_healthcare_projects_locations_datasets_consent_stores_consents_activate(client):
    """Test case for healthcare_projects_locations_datasets_consent_stores_consents_activate

    
    """
    body = {"expireTime":"expireTime","consentArtifact":"consentArtifact","ttl":"ttl"}
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
        path='/v1beta1/{nameactivat}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_healthcare_projects_locations_datasets_consent_stores_consents_create(client):
    """Test case for healthcare_projects_locations_datasets_consent_stores_consents_create

    
    """
    body = {"revisionId":"revisionId","metadata":{"key":"metadata"},"expireTime":"expireTime","name":"name","policies":[{"resourceAttributes":[{"attributeDefinitionId":"attributeDefinitionId","values":["values","values"]},{"attributeDefinitionId":"attributeDefinitionId","values":["values","values"]}],"authorizationRule":{"expression":"expression","description":"description","location":"location","title":"title"}},{"resourceAttributes":[{"attributeDefinitionId":"attributeDefinitionId","values":["values","values"]},{"attributeDefinitionId":"attributeDefinitionId","values":["values","values"]}],"authorizationRule":{"expression":"expression","description":"description","location":"location","title":"title"}}],"consentArtifact":"consentArtifact","revisionCreateTime":"revisionCreateTime","state":"STATE_UNSPECIFIED","ttl":"ttl","userId":"userId"}
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
        path='/v1beta1/{parent}/consents'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_healthcare_projects_locations_datasets_consent_stores_consents_delete_revision(client):
    """Test case for healthcare_projects_locations_datasets_consent_stores_consents_delete_revision

    
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
        path='/v1beta1/{namedelete_revisio}'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_healthcare_projects_locations_datasets_consent_stores_consents_list(client):
    """Test case for healthcare_projects_locations_datasets_consent_stores_consents_list

    
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
        path='/v1beta1/{parent}/consents'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_healthcare_projects_locations_datasets_consent_stores_consents_list_revisions(client):
    """Test case for healthcare_projects_locations_datasets_consent_stores_consents_list_revisions

    
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
        path='/v1beta1/{namelist_revision}'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_healthcare_projects_locations_datasets_consent_stores_consents_reject(client):
    """Test case for healthcare_projects_locations_datasets_consent_stores_consents_reject

    
    """
    body = {"consentArtifact":"consentArtifact"}
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
        path='/v1beta1/{namerejec}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_healthcare_projects_locations_datasets_consent_stores_consents_revoke(client):
    """Test case for healthcare_projects_locations_datasets_consent_stores_consents_revoke

    
    """
    body = {"consentArtifact":"consentArtifact"}
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
        path='/v1beta1/{namerevok}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_healthcare_projects_locations_datasets_consent_stores_create(client):
    """Test case for healthcare_projects_locations_datasets_consent_stores_create

    
    """
    body = {"defaultConsentTtl":"defaultConsentTtl","enableConsentCreateOnUpdate":True,"name":"name","labels":{"key":"labels"}}
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
                    ('consentStoreId', 'consent_store_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta1/{parent}/consentStores'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_healthcare_projects_locations_datasets_consent_stores_evaluate_user_consents(client):
    """Test case for healthcare_projects_locations_datasets_consent_stores_evaluate_user_consents

    
    """
    body = {"consentList":{"consents":["consents","consents"]},"requestAttributes":{"key":"requestAttributes"},"pageSize":0,"pageToken":"pageToken","resourceAttributes":{"key":"resourceAttributes"},"userId":"userId","responseView":"RESPONSE_VIEW_UNSPECIFIED"}
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
        path='/v1beta1/{consent_storeevaluate_user_consent}'.format(consent_store='consent_store_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_healthcare_projects_locations_datasets_consent_stores_list(client):
    """Test case for healthcare_projects_locations_datasets_consent_stores_list

    
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
        path='/v1beta1/{parent}/consentStores'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_healthcare_projects_locations_datasets_consent_stores_query_accessible_data(client):
    """Test case for healthcare_projects_locations_datasets_consent_stores_query_accessible_data

    
    """
    body = {"requestAttributes":{"key":"requestAttributes"},"gcsDestination":{"uriPrefix":"uriPrefix"},"resourceAttributes":{"key":"resourceAttributes"}}
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
        path='/v1beta1/{consent_storequery_accessible_dat}'.format(consent_store='consent_store_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_healthcare_projects_locations_datasets_consent_stores_user_data_mappings_archive(client):
    """Test case for healthcare_projects_locations_datasets_consent_stores_user_data_mappings_archive

    
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
        path='/v1beta1/{namearchiv}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_healthcare_projects_locations_datasets_consent_stores_user_data_mappings_create(client):
    """Test case for healthcare_projects_locations_datasets_consent_stores_user_data_mappings_create

    
    """
    body = {"archiveTime":"archiveTime","archived":True,"dataId":"dataId","name":"name","resourceAttributes":[{"attributeDefinitionId":"attributeDefinitionId","values":["values","values"]},{"attributeDefinitionId":"attributeDefinitionId","values":["values","values"]}],"userId":"userId"}
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
        path='/v1beta1/{parent}/userDataMappings'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_healthcare_projects_locations_datasets_consent_stores_user_data_mappings_list(client):
    """Test case for healthcare_projects_locations_datasets_consent_stores_user_data_mappings_list

    
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
        path='/v1beta1/{parent}/userDataMappings'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_healthcare_projects_locations_datasets_create(client):
    """Test case for healthcare_projects_locations_datasets_create

    
    """
    body = {"name":"name","timeZone":"timeZone"}
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
                    ('datasetId', 'dataset_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta1/{parent}/datasets'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_healthcare_projects_locations_datasets_deidentify(client):
    """Test case for healthcare_projects_locations_datasets_deidentify

    
    """
    body = {"gcsConfigUri":"gcsConfigUri","destinationDataset":"destinationDataset","config":{"annotation":{"annotationStoreName":"annotationStoreName","storeQuote":True},"operationMetadata":{"fhirOutput":{"fhirStore":"fhirStore"}},"image":{"excludeInfoTypes":["excludeInfoTypes","excludeInfoTypes"],"additionalInfoTypes":["additionalInfoTypes","additionalInfoTypes"],"textRedactionMode":"TEXT_REDACTION_MODE_UNSPECIFIED"},"fhir":{"fieldMetadataList":[{"paths":["paths","paths"],"action":"ACTION_UNSPECIFIED"},{"paths":["paths","paths"],"action":"ACTION_UNSPECIFIED"}],"defaultKeepExtensions":True},"useRegionalDataProcessing":True,"fhirFieldConfig":{"profileType":"PROFILE_TYPE_UNSPECIFIED","fieldMetadataList":[{"characterMaskField":"{}","cryptoHashField":"{}","dateShiftField":"{}","keepField":"{}","paths":["paths","paths"],"cleanTextField":"{}","removeField":"{}"},{"characterMaskField":"{}","cryptoHashField":"{}","dateShiftField":"{}","keepField":"{}","paths":["paths","paths"],"cleanTextField":"{}","removeField":"{}"}],"options":{"cryptoHashConfig":{"kmsWrapped":{"cryptoKey":"cryptoKey","wrappedKey":"wrappedKey"},"cryptoKey":"cryptoKey"},"dateShiftConfig":{"kmsWrapped":{"cryptoKey":"cryptoKey","wrappedKey":"wrappedKey"},"cryptoKey":"cryptoKey"},"keepExtensions":"{}","characterMaskConfig":{"maskingCharacter":"maskingCharacter"},"contextualDeid":"{}"}},"text":{"profileType":"PROFILE_TYPE_UNSPECIFIED","excludeInfoTypes":["excludeInfoTypes","excludeInfoTypes"],"transformations":[{"redactConfig":"{}","cryptoHashConfig":{"kmsWrapped":{"cryptoKey":"cryptoKey","wrappedKey":"wrappedKey"},"cryptoKey":"cryptoKey"},"dateShiftConfig":{"kmsWrapped":{"cryptoKey":"cryptoKey","wrappedKey":"wrappedKey"},"cryptoKey":"cryptoKey"},"infoTypes":["infoTypes","infoTypes"],"replaceWithInfoTypeConfig":"{}","characterMaskConfig":{"maskingCharacter":"maskingCharacter"}},{"redactConfig":"{}","cryptoHashConfig":{"kmsWrapped":{"cryptoKey":"cryptoKey","wrappedKey":"wrappedKey"},"cryptoKey":"cryptoKey"},"dateShiftConfig":{"kmsWrapped":{"cryptoKey":"cryptoKey","wrappedKey":"wrappedKey"},"cryptoKey":"cryptoKey"},"infoTypes":["infoTypes","infoTypes"],"replaceWithInfoTypeConfig":"{}","characterMaskConfig":{"maskingCharacter":"maskingCharacter"}}],"additionalTransformations":[{"redactConfig":"{}","cryptoHashConfig":{"kmsWrapped":{"cryptoKey":"cryptoKey","wrappedKey":"wrappedKey"},"cryptoKey":"cryptoKey"},"dateShiftConfig":{"kmsWrapped":{"cryptoKey":"cryptoKey","wrappedKey":"wrappedKey"},"cryptoKey":"cryptoKey"},"infoTypes":["infoTypes","infoTypes"],"replaceWithInfoTypeConfig":"{}","characterMaskConfig":{"maskingCharacter":"maskingCharacter"}},{"redactConfig":"{}","cryptoHashConfig":{"kmsWrapped":{"cryptoKey":"cryptoKey","wrappedKey":"wrappedKey"},"cryptoKey":"cryptoKey"},"dateShiftConfig":{"kmsWrapped":{"cryptoKey":"cryptoKey","wrappedKey":"wrappedKey"},"cryptoKey":"cryptoKey"},"infoTypes":["infoTypes","infoTypes"],"replaceWithInfoTypeConfig":"{}","characterMaskConfig":{"maskingCharacter":"maskingCharacter"}}]},"dicom":{"filterProfile":"TAG_FILTER_PROFILE_UNSPECIFIED","removeList":{"tags":["tags","tags"]},"keepList":{"tags":["tags","tags"]},"skipIdRedaction":True},"dicomTagConfig":{"profileType":"PROFILE_TYPE_UNSPECIFIED","options":{"primaryIds":"PRIMARY_IDS_OPTION_UNSPECIFIED","cleanImage":{"excludeInfoTypes":["excludeInfoTypes","excludeInfoTypes"],"additionalInfoTypes":["additionalInfoTypes","additionalInfoTypes"],"textRedactionMode":"TEXT_REDACTION_MODE_UNSPECIFIED"},"cleanDescriptors":"{}"},"actions":[{"deleteTag":"{}","keepTag":"{}","recurseTag":"{}","resetTag":"{}","regenUidTag":"{}","cleanImageTag":{"excludeInfoTypes":["excludeInfoTypes","excludeInfoTypes"],"additionalInfoTypes":["additionalInfoTypes","additionalInfoTypes"],"textRedactionMode":"TEXT_REDACTION_MODE_UNSPECIFIED"},"cleanTextTag":"{}","removeTag":"{}","queries":["queries","queries"]},{"deleteTag":"{}","keepTag":"{}","recurseTag":"{}","resetTag":"{}","regenUidTag":"{}","cleanImageTag":{"excludeInfoTypes":["excludeInfoTypes","excludeInfoTypes"],"additionalInfoTypes":["additionalInfoTypes","additionalInfoTypes"],"textRedactionMode":"TEXT_REDACTION_MODE_UNSPECIFIED"},"cleanTextTag":"{}","removeTag":"{}","queries":["queries","queries"]}]}}}
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
        path='/v1beta1/{source_datasetdeidentif}'.format(source_dataset='source_dataset_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_healthcare_projects_locations_datasets_dicom_stores_create(client):
    """Test case for healthcare_projects_locations_datasets_dicom_stores_create

    
    """
    body = {"streamConfigs":[{"bigqueryDestination":{"writeDisposition":"WRITE_DISPOSITION_UNSPECIFIED","force":True,"tableUri":"tableUri"}},{"bigqueryDestination":{"writeDisposition":"WRITE_DISPOSITION_UNSPECIFIED","force":True,"tableUri":"tableUri"}}],"name":"name","notificationConfig":{"sendForBulkImport":True,"pubsubTopic":"pubsubTopic"},"labels":{"key":"labels"}}
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
                    ('dicomStoreId', 'dicom_store_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta1/{parent}/dicomStores'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_healthcare_projects_locations_datasets_dicom_stores_dicom_web_studies_get_study_metrics(client):
    """Test case for healthcare_projects_locations_datasets_dicom_stores_dicom_web_studies_get_study_metrics

    
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
        path='/v1beta1/{studyget_study_metric}'.format(study='study_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_healthcare_projects_locations_datasets_dicom_stores_dicom_web_studies_series_get_series_metrics(client):
    """Test case for healthcare_projects_locations_datasets_dicom_stores_dicom_web_studies_series_get_series_metrics

    
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
        path='/v1beta1/{seriesget_series_metric}'.format(series='series_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_healthcare_projects_locations_datasets_dicom_stores_dicom_web_studies_series_instances_get_storage_info(client):
    """Test case for healthcare_projects_locations_datasets_dicom_stores_dicom_web_studies_series_instances_get_storage_info

    
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
        path='/v1beta1/{resourceget_storage_inf}'.format(resource='resource_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_healthcare_projects_locations_datasets_dicom_stores_dicom_web_studies_set_blob_storage_settings(client):
    """Test case for healthcare_projects_locations_datasets_dicom_stores_dicom_web_studies_set_blob_storage_settings

    
    """
    body = {"blobStorageSettings":{"blobStorageClass":"BLOB_STORAGE_CLASS_UNSPECIFIED"},"filterConfig":{"resourcePathsGcsUri":"resourcePathsGcsUri"}}
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
        path='/v1beta1/{resourceset_blob_storage_setting}'.format(resource='resource_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_healthcare_projects_locations_datasets_dicom_stores_get_dicom_store_metrics(client):
    """Test case for healthcare_projects_locations_datasets_dicom_stores_get_dicom_store_metrics

    
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
        path='/v1beta1/{nameget_dicom_store_metric}'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_healthcare_projects_locations_datasets_dicom_stores_list(client):
    """Test case for healthcare_projects_locations_datasets_dicom_stores_list

    
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
        path='/v1beta1/{parent}/dicomStores'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_healthcare_projects_locations_datasets_dicom_stores_studies_series_instances_delete(client):
    """Test case for healthcare_projects_locations_datasets_dicom_stores_studies_series_instances_delete

    
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
        path='/v1beta1/{parent}/dicomWeb/{dicom_web_path}'.format(parent='parent_example', dicom_web_path='dicom_web_path_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_healthcare_projects_locations_datasets_dicom_stores_studies_series_instances_frames_retrieve_rendered(client):
    """Test case for healthcare_projects_locations_datasets_dicom_stores_studies_series_instances_frames_retrieve_rendered

    
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
        path='/v1beta1/{parent}/dicomWeb/{dicom_web_path}'.format(parent='parent_example', dicom_web_path='dicom_web_path_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_healthcare_projects_locations_datasets_dicom_stores_studies_store_instances(client):
    """Test case for healthcare_projects_locations_datasets_dicom_stores_studies_store_instances

    
    """
    body = {"extensions":[{"key":""},{"key":""}],"data":"data","contentType":"contentType"}
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
        path='/v1beta1/{parent}/dicomWeb/{dicom_web_path}'.format(parent='parent_example', dicom_web_path='dicom_web_path_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_healthcare_projects_locations_datasets_fhir_stores_apply_admin_consents(client):
    """Test case for healthcare_projects_locations_datasets_fhir_stores_apply_admin_consents

    
    """
    body = {"validateOnly":True,"newConsentsList":{"names":["names","names"]}}
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
        path='/v1beta1/{nameapply_admin_consent}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_healthcare_projects_locations_datasets_fhir_stores_apply_consents(client):
    """Test case for healthcare_projects_locations_datasets_fhir_stores_apply_consents

    
    """
    body = {"patientScope":{"patientIds":["patientIds","patientIds"]},"validateOnly":True,"timeRange":{"start":"start","end":"end"}}
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
        path='/v1beta1/{nameapply_consent}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_healthcare_projects_locations_datasets_fhir_stores_configure_search(client):
    """Test case for healthcare_projects_locations_datasets_fhir_stores_configure_search

    
    """
    body = {"validateOnly":True,"canonicalUrls":["canonicalUrls","canonicalUrls"]}
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
        path='/v1beta1/{nameconfigure_searc}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_healthcare_projects_locations_datasets_fhir_stores_create(client):
    """Test case for healthcare_projects_locations_datasets_fhir_stores_create

    
    """
    body = {"disableReferentialIntegrity":True,"enableHistoryModifications":True,"disableResourceVersioning":True,"enableUpdateCreate":True,"version":"VERSION_UNSPECIFIED","labels":{"key":"labels"},"defaultSearchHandlingStrict":True,"consentConfig":{"enforcedAdminConsents":["enforcedAdminConsents","enforcedAdminConsents"],"consentHeaderHandling":{"profile":"SCOPE_PROFILE_UNSPECIFIED"},"accessEnforced":True,"accessDeterminationLogConfig":{"logLevel":"LOG_LEVEL_UNSPECIFIED"},"version":"CONSENT_ENFORCEMENT_VERSION_UNSPECIFIED"},"streamConfigs":[{"resourceTypes":["resourceTypes","resourceTypes"],"bigqueryDestination":{"datasetUri":"datasetUri","schemaConfig":{"recursiveStructureDepth":"recursiveStructureDepth","schemaType":"SCHEMA_TYPE_UNSPECIFIED","lastUpdatedPartitionConfig":{"expirationMs":"expirationMs","type":"PARTITION_TYPE_UNSPECIFIED"}},"writeDisposition":"WRITE_DISPOSITION_UNSPECIFIED","force":True},"deidentifiedStoreDestination":{"store":"store","config":{"annotation":{"annotationStoreName":"annotationStoreName","storeQuote":True},"operationMetadata":{"fhirOutput":{"fhirStore":"fhirStore"}},"image":{"excludeInfoTypes":["excludeInfoTypes","excludeInfoTypes"],"additionalInfoTypes":["additionalInfoTypes","additionalInfoTypes"],"textRedactionMode":"TEXT_REDACTION_MODE_UNSPECIFIED"},"fhir":{"fieldMetadataList":[{"paths":["paths","paths"],"action":"ACTION_UNSPECIFIED"},{"paths":["paths","paths"],"action":"ACTION_UNSPECIFIED"}],"defaultKeepExtensions":True},"useRegionalDataProcessing":True,"fhirFieldConfig":{"profileType":"PROFILE_TYPE_UNSPECIFIED","fieldMetadataList":[{"characterMaskField":"{}","cryptoHashField":"{}","dateShiftField":"{}","keepField":"{}","paths":["paths","paths"],"cleanTextField":"{}","removeField":"{}"},{"characterMaskField":"{}","cryptoHashField":"{}","dateShiftField":"{}","keepField":"{}","paths":["paths","paths"],"cleanTextField":"{}","removeField":"{}"}],"options":{"cryptoHashConfig":{"kmsWrapped":{"cryptoKey":"cryptoKey","wrappedKey":"wrappedKey"},"cryptoKey":"cryptoKey"},"dateShiftConfig":{"kmsWrapped":{"cryptoKey":"cryptoKey","wrappedKey":"wrappedKey"},"cryptoKey":"cryptoKey"},"keepExtensions":"{}","characterMaskConfig":{"maskingCharacter":"maskingCharacter"},"contextualDeid":"{}"}},"text":{"profileType":"PROFILE_TYPE_UNSPECIFIED","excludeInfoTypes":["excludeInfoTypes","excludeInfoTypes"],"transformations":[{"redactConfig":"{}","cryptoHashConfig":{"kmsWrapped":{"cryptoKey":"cryptoKey","wrappedKey":"wrappedKey"},"cryptoKey":"cryptoKey"},"dateShiftConfig":{"kmsWrapped":{"cryptoKey":"cryptoKey","wrappedKey":"wrappedKey"},"cryptoKey":"cryptoKey"},"infoTypes":["infoTypes","infoTypes"],"replaceWithInfoTypeConfig":"{}","characterMaskConfig":{"maskingCharacter":"maskingCharacter"}},{"redactConfig":"{}","cryptoHashConfig":{"kmsWrapped":{"cryptoKey":"cryptoKey","wrappedKey":"wrappedKey"},"cryptoKey":"cryptoKey"},"dateShiftConfig":{"kmsWrapped":{"cryptoKey":"cryptoKey","wrappedKey":"wrappedKey"},"cryptoKey":"cryptoKey"},"infoTypes":["infoTypes","infoTypes"],"replaceWithInfoTypeConfig":"{}","characterMaskConfig":{"maskingCharacter":"maskingCharacter"}}],"additionalTransformations":[{"redactConfig":"{}","cryptoHashConfig":{"kmsWrapped":{"cryptoKey":"cryptoKey","wrappedKey":"wrappedKey"},"cryptoKey":"cryptoKey"},"dateShiftConfig":{"kmsWrapped":{"cryptoKey":"cryptoKey","wrappedKey":"wrappedKey"},"cryptoKey":"cryptoKey"},"infoTypes":["infoTypes","infoTypes"],"replaceWithInfoTypeConfig":"{}","characterMaskConfig":{"maskingCharacter":"maskingCharacter"}},{"redactConfig":"{}","cryptoHashConfig":{"kmsWrapped":{"cryptoKey":"cryptoKey","wrappedKey":"wrappedKey"},"cryptoKey":"cryptoKey"},"dateShiftConfig":{"kmsWrapped":{"cryptoKey":"cryptoKey","wrappedKey":"wrappedKey"},"cryptoKey":"cryptoKey"},"infoTypes":["infoTypes","infoTypes"],"replaceWithInfoTypeConfig":"{}","characterMaskConfig":{"maskingCharacter":"maskingCharacter"}}]},"dicom":{"filterProfile":"TAG_FILTER_PROFILE_UNSPECIFIED","removeList":{"tags":["tags","tags"]},"keepList":{"tags":["tags","tags"]},"skipIdRedaction":True},"dicomTagConfig":{"profileType":"PROFILE_TYPE_UNSPECIFIED","options":{"primaryIds":"PRIMARY_IDS_OPTION_UNSPECIFIED","cleanImage":{"excludeInfoTypes":["excludeInfoTypes","excludeInfoTypes"],"additionalInfoTypes":["additionalInfoTypes","additionalInfoTypes"],"textRedactionMode":"TEXT_REDACTION_MODE_UNSPECIFIED"},"cleanDescriptors":"{}"},"actions":[{"deleteTag":"{}","keepTag":"{}","recurseTag":"{}","resetTag":"{}","regenUidTag":"{}","cleanImageTag":{"excludeInfoTypes":["excludeInfoTypes","excludeInfoTypes"],"additionalInfoTypes":["additionalInfoTypes","additionalInfoTypes"],"textRedactionMode":"TEXT_REDACTION_MODE_UNSPECIFIED"},"cleanTextTag":"{}","removeTag":"{}","queries":["queries","queries"]},{"deleteTag":"{}","keepTag":"{}","recurseTag":"{}","resetTag":"{}","regenUidTag":"{}","cleanImageTag":{"excludeInfoTypes":["excludeInfoTypes","excludeInfoTypes"],"additionalInfoTypes":["additionalInfoTypes","additionalInfoTypes"],"textRedactionMode":"TEXT_REDACTION_MODE_UNSPECIFIED"},"cleanTextTag":"{}","removeTag":"{}","queries":["queries","queries"]}]}}}},{"resourceTypes":["resourceTypes","resourceTypes"],"bigqueryDestination":{"datasetUri":"datasetUri","schemaConfig":{"recursiveStructureDepth":"recursiveStructureDepth","schemaType":"SCHEMA_TYPE_UNSPECIFIED","lastUpdatedPartitionConfig":{"expirationMs":"expirationMs","type":"PARTITION_TYPE_UNSPECIFIED"}},"writeDisposition":"WRITE_DISPOSITION_UNSPECIFIED","force":True},"deidentifiedStoreDestination":{"store":"store","config":{"annotation":{"annotationStoreName":"annotationStoreName","storeQuote":True},"operationMetadata":{"fhirOutput":{"fhirStore":"fhirStore"}},"image":{"excludeInfoTypes":["excludeInfoTypes","excludeInfoTypes"],"additionalInfoTypes":["additionalInfoTypes","additionalInfoTypes"],"textRedactionMode":"TEXT_REDACTION_MODE_UNSPECIFIED"},"fhir":{"fieldMetadataList":[{"paths":["paths","paths"],"action":"ACTION_UNSPECIFIED"},{"paths":["paths","paths"],"action":"ACTION_UNSPECIFIED"}],"defaultKeepExtensions":True},"useRegionalDataProcessing":True,"fhirFieldConfig":{"profileType":"PROFILE_TYPE_UNSPECIFIED","fieldMetadataList":[{"characterMaskField":"{}","cryptoHashField":"{}","dateShiftField":"{}","keepField":"{}","paths":["paths","paths"],"cleanTextField":"{}","removeField":"{}"},{"characterMaskField":"{}","cryptoHashField":"{}","dateShiftField":"{}","keepField":"{}","paths":["paths","paths"],"cleanTextField":"{}","removeField":"{}"}],"options":{"cryptoHashConfig":{"kmsWrapped":{"cryptoKey":"cryptoKey","wrappedKey":"wrappedKey"},"cryptoKey":"cryptoKey"},"dateShiftConfig":{"kmsWrapped":{"cryptoKey":"cryptoKey","wrappedKey":"wrappedKey"},"cryptoKey":"cryptoKey"},"keepExtensions":"{}","characterMaskConfig":{"maskingCharacter":"maskingCharacter"},"contextualDeid":"{}"}},"text":{"profileType":"PROFILE_TYPE_UNSPECIFIED","excludeInfoTypes":["excludeInfoTypes","excludeInfoTypes"],"transformations":[{"redactConfig":"{}","cryptoHashConfig":{"kmsWrapped":{"cryptoKey":"cryptoKey","wrappedKey":"wrappedKey"},"cryptoKey":"cryptoKey"},"dateShiftConfig":{"kmsWrapped":{"cryptoKey":"cryptoKey","wrappedKey":"wrappedKey"},"cryptoKey":"cryptoKey"},"infoTypes":["infoTypes","infoTypes"],"replaceWithInfoTypeConfig":"{}","characterMaskConfig":{"maskingCharacter":"maskingCharacter"}},{"redactConfig":"{}","cryptoHashConfig":{"kmsWrapped":{"cryptoKey":"cryptoKey","wrappedKey":"wrappedKey"},"cryptoKey":"cryptoKey"},"dateShiftConfig":{"kmsWrapped":{"cryptoKey":"cryptoKey","wrappedKey":"wrappedKey"},"cryptoKey":"cryptoKey"},"infoTypes":["infoTypes","infoTypes"],"replaceWithInfoTypeConfig":"{}","characterMaskConfig":{"maskingCharacter":"maskingCharacter"}}],"additionalTransformations":[{"redactConfig":"{}","cryptoHashConfig":{"kmsWrapped":{"cryptoKey":"cryptoKey","wrappedKey":"wrappedKey"},"cryptoKey":"cryptoKey"},"dateShiftConfig":{"kmsWrapped":{"cryptoKey":"cryptoKey","wrappedKey":"wrappedKey"},"cryptoKey":"cryptoKey"},"infoTypes":["infoTypes","infoTypes"],"replaceWithInfoTypeConfig":"{}","characterMaskConfig":{"maskingCharacter":"maskingCharacter"}},{"redactConfig":"{}","cryptoHashConfig":{"kmsWrapped":{"cryptoKey":"cryptoKey","wrappedKey":"wrappedKey"},"cryptoKey":"cryptoKey"},"dateShiftConfig":{"kmsWrapped":{"cryptoKey":"cryptoKey","wrappedKey":"wrappedKey"},"cryptoKey":"cryptoKey"},"infoTypes":["infoTypes","infoTypes"],"replaceWithInfoTypeConfig":"{}","characterMaskConfig":{"maskingCharacter":"maskingCharacter"}}]},"dicom":{"filterProfile":"TAG_FILTER_PROFILE_UNSPECIFIED","removeList":{"tags":["tags","tags"]},"keepList":{"tags":["tags","tags"]},"skipIdRedaction":True},"dicomTagConfig":{"profileType":"PROFILE_TYPE_UNSPECIFIED","options":{"primaryIds":"PRIMARY_IDS_OPTION_UNSPECIFIED","cleanImage":{"excludeInfoTypes":["excludeInfoTypes","excludeInfoTypes"],"additionalInfoTypes":["additionalInfoTypes","additionalInfoTypes"],"textRedactionMode":"TEXT_REDACTION_MODE_UNSPECIFIED"},"cleanDescriptors":"{}"},"actions":[{"deleteTag":"{}","keepTag":"{}","recurseTag":"{}","resetTag":"{}","regenUidTag":"{}","cleanImageTag":{"excludeInfoTypes":["excludeInfoTypes","excludeInfoTypes"],"additionalInfoTypes":["additionalInfoTypes","additionalInfoTypes"],"textRedactionMode":"TEXT_REDACTION_MODE_UNSPECIFIED"},"cleanTextTag":"{}","removeTag":"{}","queries":["queries","queries"]},{"deleteTag":"{}","keepTag":"{}","recurseTag":"{}","resetTag":"{}","regenUidTag":"{}","cleanImageTag":{"excludeInfoTypes":["excludeInfoTypes","excludeInfoTypes"],"additionalInfoTypes":["additionalInfoTypes","additionalInfoTypes"],"textRedactionMode":"TEXT_REDACTION_MODE_UNSPECIFIED"},"cleanTextTag":"{}","removeTag":"{}","queries":["queries","queries"]}]}}}}],"complexDataTypeReferenceParsing":"COMPLEX_DATA_TYPE_REFERENCE_PARSING_UNSPECIFIED","name":"name","notificationConfig":{"sendForBulkImport":True,"pubsubTopic":"pubsubTopic"},"notificationConfigs":[{"sendPreviousResourceOnDelete":True,"sendFullResource":True,"pubsubTopic":"pubsubTopic"},{"sendPreviousResourceOnDelete":True,"sendFullResource":True,"pubsubTopic":"pubsubTopic"}],"validationConfig":{"disableProfileValidation":True,"enabledImplementationGuides":["enabledImplementationGuides","enabledImplementationGuides"],"disableRequiredFieldValidation":True,"disableReferenceTypeValidation":True,"disableFhirpathValidation":True},"searchConfig":{"searchParameters":[{"canonicalUrl":"canonicalUrl","parameter":"parameter"},{"canonicalUrl":"canonicalUrl","parameter":"parameter"}]}}
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
                    ('fhirStoreId', 'fhir_store_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta1/{parent}/fhirStores'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_healthcare_projects_locations_datasets_fhir_stores_deidentify(client):
    """Test case for healthcare_projects_locations_datasets_fhir_stores_deidentify

    
    """
    body = {"skipModifiedResources":True,"destinationStore":"destinationStore","gcsConfigUri":"gcsConfigUri","resourceFilter":{"resources":{"resources":["resources","resources"]}},"config":{"annotation":{"annotationStoreName":"annotationStoreName","storeQuote":True},"operationMetadata":{"fhirOutput":{"fhirStore":"fhirStore"}},"image":{"excludeInfoTypes":["excludeInfoTypes","excludeInfoTypes"],"additionalInfoTypes":["additionalInfoTypes","additionalInfoTypes"],"textRedactionMode":"TEXT_REDACTION_MODE_UNSPECIFIED"},"fhir":{"fieldMetadataList":[{"paths":["paths","paths"],"action":"ACTION_UNSPECIFIED"},{"paths":["paths","paths"],"action":"ACTION_UNSPECIFIED"}],"defaultKeepExtensions":True},"useRegionalDataProcessing":True,"fhirFieldConfig":{"profileType":"PROFILE_TYPE_UNSPECIFIED","fieldMetadataList":[{"characterMaskField":"{}","cryptoHashField":"{}","dateShiftField":"{}","keepField":"{}","paths":["paths","paths"],"cleanTextField":"{}","removeField":"{}"},{"characterMaskField":"{}","cryptoHashField":"{}","dateShiftField":"{}","keepField":"{}","paths":["paths","paths"],"cleanTextField":"{}","removeField":"{}"}],"options":{"cryptoHashConfig":{"kmsWrapped":{"cryptoKey":"cryptoKey","wrappedKey":"wrappedKey"},"cryptoKey":"cryptoKey"},"dateShiftConfig":{"kmsWrapped":{"cryptoKey":"cryptoKey","wrappedKey":"wrappedKey"},"cryptoKey":"cryptoKey"},"keepExtensions":"{}","characterMaskConfig":{"maskingCharacter":"maskingCharacter"},"contextualDeid":"{}"}},"text":{"profileType":"PROFILE_TYPE_UNSPECIFIED","excludeInfoTypes":["excludeInfoTypes","excludeInfoTypes"],"transformations":[{"redactConfig":"{}","cryptoHashConfig":{"kmsWrapped":{"cryptoKey":"cryptoKey","wrappedKey":"wrappedKey"},"cryptoKey":"cryptoKey"},"dateShiftConfig":{"kmsWrapped":{"cryptoKey":"cryptoKey","wrappedKey":"wrappedKey"},"cryptoKey":"cryptoKey"},"infoTypes":["infoTypes","infoTypes"],"replaceWithInfoTypeConfig":"{}","characterMaskConfig":{"maskingCharacter":"maskingCharacter"}},{"redactConfig":"{}","cryptoHashConfig":{"kmsWrapped":{"cryptoKey":"cryptoKey","wrappedKey":"wrappedKey"},"cryptoKey":"cryptoKey"},"dateShiftConfig":{"kmsWrapped":{"cryptoKey":"cryptoKey","wrappedKey":"wrappedKey"},"cryptoKey":"cryptoKey"},"infoTypes":["infoTypes","infoTypes"],"replaceWithInfoTypeConfig":"{}","characterMaskConfig":{"maskingCharacter":"maskingCharacter"}}],"additionalTransformations":[{"redactConfig":"{}","cryptoHashConfig":{"kmsWrapped":{"cryptoKey":"cryptoKey","wrappedKey":"wrappedKey"},"cryptoKey":"cryptoKey"},"dateShiftConfig":{"kmsWrapped":{"cryptoKey":"cryptoKey","wrappedKey":"wrappedKey"},"cryptoKey":"cryptoKey"},"infoTypes":["infoTypes","infoTypes"],"replaceWithInfoTypeConfig":"{}","characterMaskConfig":{"maskingCharacter":"maskingCharacter"}},{"redactConfig":"{}","cryptoHashConfig":{"kmsWrapped":{"cryptoKey":"cryptoKey","wrappedKey":"wrappedKey"},"cryptoKey":"cryptoKey"},"dateShiftConfig":{"kmsWrapped":{"cryptoKey":"cryptoKey","wrappedKey":"wrappedKey"},"cryptoKey":"cryptoKey"},"infoTypes":["infoTypes","infoTypes"],"replaceWithInfoTypeConfig":"{}","characterMaskConfig":{"maskingCharacter":"maskingCharacter"}}]},"dicom":{"filterProfile":"TAG_FILTER_PROFILE_UNSPECIFIED","removeList":{"tags":["tags","tags"]},"keepList":{"tags":["tags","tags"]},"skipIdRedaction":True},"dicomTagConfig":{"profileType":"PROFILE_TYPE_UNSPECIFIED","options":{"primaryIds":"PRIMARY_IDS_OPTION_UNSPECIFIED","cleanImage":{"excludeInfoTypes":["excludeInfoTypes","excludeInfoTypes"],"additionalInfoTypes":["additionalInfoTypes","additionalInfoTypes"],"textRedactionMode":"TEXT_REDACTION_MODE_UNSPECIFIED"},"cleanDescriptors":"{}"},"actions":[{"deleteTag":"{}","keepTag":"{}","recurseTag":"{}","resetTag":"{}","regenUidTag":"{}","cleanImageTag":{"excludeInfoTypes":["excludeInfoTypes","excludeInfoTypes"],"additionalInfoTypes":["additionalInfoTypes","additionalInfoTypes"],"textRedactionMode":"TEXT_REDACTION_MODE_UNSPECIFIED"},"cleanTextTag":"{}","removeTag":"{}","queries":["queries","queries"]},{"deleteTag":"{}","keepTag":"{}","recurseTag":"{}","resetTag":"{}","regenUidTag":"{}","cleanImageTag":{"excludeInfoTypes":["excludeInfoTypes","excludeInfoTypes"],"additionalInfoTypes":["additionalInfoTypes","additionalInfoTypes"],"textRedactionMode":"TEXT_REDACTION_MODE_UNSPECIFIED"},"cleanTextTag":"{}","removeTag":"{}","queries":["queries","queries"]}]}}}
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
        path='/v1beta1/{source_storedeidentif}'.format(source_store='source_store_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_healthcare_projects_locations_datasets_fhir_stores_explain_data_access(client):
    """Test case for healthcare_projects_locations_datasets_fhir_stores_explain_data_access

    
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
                    ('resourceId', 'resource_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1beta1/{nameexplain_data_acces}'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_healthcare_projects_locations_datasets_fhir_stores_fhir_capabilities(client):
    """Test case for healthcare_projects_locations_datasets_fhir_stores_fhir_capabilities

    
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
        path='/v1beta1/{name}/fhir/metadata'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_healthcare_projects_locations_datasets_fhir_stores_fhir_concept_map_search_translate(client):
    """Test case for healthcare_projects_locations_datasets_fhir_stores_fhir_concept_map_search_translate

    
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
                    ('code', 'code_example'),
                    ('conceptMapVersion', 'concept_map_version_example'),
                    ('source', 'source_example'),
                    ('system', 'system_example'),
                    ('target', 'target_example'),
                    ('url', 'url_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1beta1/{parent}/fhir/ConceptMap/$translate'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_healthcare_projects_locations_datasets_fhir_stores_fhir_concept_map_translate(client):
    """Test case for healthcare_projects_locations_datasets_fhir_stores_fhir_concept_map_translate

    
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
                    ('code', 'code_example'),
                    ('conceptMapVersion', 'concept_map_version_example'),
                    ('system', 'system_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1beta1/{name}/$translate'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_healthcare_projects_locations_datasets_fhir_stores_fhir_conditional_delete(client):
    """Test case for healthcare_projects_locations_datasets_fhir_stores_fhir_conditional_delete

    
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
        path='/v1beta1/{parent}/fhir/{type}'.format(parent='parent_example', type='type_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_healthcare_projects_locations_datasets_fhir_stores_fhir_conditional_patch(client):
    """Test case for healthcare_projects_locations_datasets_fhir_stores_fhir_conditional_patch

    
    """
    body = {"extensions":[{"key":""},{"key":""}],"data":"data","contentType":"contentType"}
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
        method='PATCH',
        path='/v1beta1/{parent}/fhir/{type}'.format(parent='parent_example', type='type_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_healthcare_projects_locations_datasets_fhir_stores_fhir_conditional_update(client):
    """Test case for healthcare_projects_locations_datasets_fhir_stores_fhir_conditional_update

    
    """
    body = {"extensions":[{"key":""},{"key":""}],"data":"data","contentType":"contentType"}
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
        path='/v1beta1/{parent}/fhir/{type}'.format(parent='parent_example', type='type_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_healthcare_projects_locations_datasets_fhir_stores_fhir_create(client):
    """Test case for healthcare_projects_locations_datasets_fhir_stores_fhir_create

    
    """
    body = {"extensions":[{"key":""},{"key":""}],"data":"data","contentType":"contentType"}
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
        path='/v1beta1/{parent}/fhir/{type}'.format(parent='parent_example', type='type_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_healthcare_projects_locations_datasets_fhir_stores_fhir_execute_bundle(client):
    """Test case for healthcare_projects_locations_datasets_fhir_stores_fhir_execute_bundle

    
    """
    body = {"extensions":[{"key":""},{"key":""}],"data":"data","contentType":"contentType"}
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
        path='/v1beta1/{parent}/fhir'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_healthcare_projects_locations_datasets_fhir_stores_fhir_history(client):
    """Test case for healthcare_projects_locations_datasets_fhir_stores_fhir_history

    
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
                    ('_at', 'at_example'),
                    ('_count', 56),
                    ('_page_token', 'page_token_example'),
                    ('_since', 'since_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1beta1/{name}/_history'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_healthcare_projects_locations_datasets_fhir_stores_fhir_observation_lastn(client):
    """Test case for healthcare_projects_locations_datasets_fhir_stores_fhir_observation_lastn

    
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
        path='/v1beta1/{parent}/fhir/Observation/$lastn'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_healthcare_projects_locations_datasets_fhir_stores_fhir_patient_consent_enforcement_status(client):
    """Test case for healthcare_projects_locations_datasets_fhir_stores_fhir_patient_consent_enforcement_status

    
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
                    ('_count', 56),
                    ('_page_token', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1beta1/{name}/$consent-enforcement-status'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_healthcare_projects_locations_datasets_fhir_stores_fhir_patient_everything(client):
    """Test case for healthcare_projects_locations_datasets_fhir_stores_fhir_patient_everything

    
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
                    ('_count', 56),
                    ('_page_token', 'page_token_example'),
                    ('_since', 'since_example'),
                    ('_type', 'type_example'),
                    ('end', 'end_example'),
                    ('start', 'start_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1beta1/{name}/$everything'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_healthcare_projects_locations_datasets_fhir_stores_fhir_resource_incoming_references(client):
    """Test case for healthcare_projects_locations_datasets_fhir_stores_fhir_resource_incoming_references

    
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
                    ('_count', 56),
                    ('_page_token', 'page_token_example'),
                    ('_summary', 'summary_example'),
                    ('_type', 'type_example'),
                    ('target', 'target_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1beta1/{parent}/fhir/$references'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_healthcare_projects_locations_datasets_fhir_stores_fhir_resource_purge(client):
    """Test case for healthcare_projects_locations_datasets_fhir_stores_fhir_resource_purge

    
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
        path='/v1beta1/{name}/$purge'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_healthcare_projects_locations_datasets_fhir_stores_fhir_resource_validate(client):
    """Test case for healthcare_projects_locations_datasets_fhir_stores_fhir_resource_validate

    
    """
    body = {"extensions":[{"key":""},{"key":""}],"data":"data","contentType":"contentType"}
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
                    ('profile', 'profile_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta1/{parent}/fhir/{type}/$validate'.format(parent='parent_example', type='type_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_healthcare_projects_locations_datasets_fhir_stores_fhir_search(client):
    """Test case for healthcare_projects_locations_datasets_fhir_stores_fhir_search

    
    """
    body = {"resourceType":"resourceType"}
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
        path='/v1beta1/{parent}/fhir/_search'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_healthcare_projects_locations_datasets_fhir_stores_fhir_search_type(client):
    """Test case for healthcare_projects_locations_datasets_fhir_stores_fhir_search_type

    
    """
    body = {"resourceType":"resourceType"}
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
        path='/v1beta1/{parent}/fhir/{resource_type}/_search'.format(parent='parent_example', resource_type='resource_type_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_healthcare_projects_locations_datasets_fhir_stores_fhir_update(client):
    """Test case for healthcare_projects_locations_datasets_fhir_stores_fhir_update

    
    """
    body = {"extensions":[{"key":""},{"key":""}],"data":"data","contentType":"contentType"}
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
        path='/v1beta1/{name}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_healthcare_projects_locations_datasets_fhir_stores_get_fhir_store_metrics(client):
    """Test case for healthcare_projects_locations_datasets_fhir_stores_get_fhir_store_metrics

    
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
        path='/v1beta1/{nameget_fhir_store_metric}'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_healthcare_projects_locations_datasets_fhir_stores_list(client):
    """Test case for healthcare_projects_locations_datasets_fhir_stores_list

    
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
        path='/v1beta1/{parent}/fhirStores'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_healthcare_projects_locations_datasets_fhir_stores_rollback(client):
    """Test case for healthcare_projects_locations_datasets_fhir_stores_rollback

    
    """
    body = {"filteringFields":{"metadataFilter":"metadataFilter","operationIds":["operationIds","operationIds"]},"resultGcsBucket":"resultGcsBucket","changeType":"CHANGE_TYPE_UNSPECIFIED","inputGcsObject":"inputGcsObject","excludeRollbacks":True,"force":True,"rollbackTime":"rollbackTime","type":["type","type"]}
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
        path='/v1beta1/{namerollbac}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_healthcare_projects_locations_datasets_hl7_v2_stores_create(client):
    """Test case for healthcare_projects_locations_datasets_hl7_v2_stores_create

    
    """
    body = {"parserConfig":{"schema":{"unexpectedSegmentHandling":"UNEXPECTED_SEGMENT_HANDLING_MODE_UNSPECIFIED","types":[{"type":[{"primitive":"PRIMITIVE_UNSPECIFIED","name":"name","fields":[{"minOccurs":2,"name":"name","maxOccurs":5,"type":"type","table":"table"},{"minOccurs":2,"name":"name","maxOccurs":5,"type":"type","table":"table"}]},{"primitive":"PRIMITIVE_UNSPECIFIED","name":"name","fields":[{"minOccurs":2,"name":"name","maxOccurs":5,"type":"type","table":"table"},{"minOccurs":2,"name":"name","maxOccurs":5,"type":"type","table":"table"}]}],"version":[{"mshField":"mshField","value":"value"},{"mshField":"mshField","value":"value"}]},{"type":[{"primitive":"PRIMITIVE_UNSPECIFIED","name":"name","fields":[{"minOccurs":2,"name":"name","maxOccurs":5,"type":"type","table":"table"},{"minOccurs":2,"name":"name","maxOccurs":5,"type":"type","table":"table"}]},{"primitive":"PRIMITIVE_UNSPECIFIED","name":"name","fields":[{"minOccurs":2,"name":"name","maxOccurs":5,"type":"type","table":"table"},{"minOccurs":2,"name":"name","maxOccurs":5,"type":"type","table":"table"}]}],"version":[{"mshField":"mshField","value":"value"},{"mshField":"mshField","value":"value"}]}],"schemas":[{"messageSchemaConfigs":{"key":{"minOccurs":5,"members":[{"segment":{"minOccurs":1,"maxOccurs":6,"type":"type"}},{"segment":{"minOccurs":1,"maxOccurs":6,"type":"type"}}],"name":"name","maxOccurs":0,"choice":True}},"version":[{"mshField":"mshField","value":"value"},{"mshField":"mshField","value":"value"}]},{"messageSchemaConfigs":{"key":{"minOccurs":5,"members":[{"segment":{"minOccurs":1,"maxOccurs":6,"type":"type"}},{"segment":{"minOccurs":1,"maxOccurs":6,"type":"type"}}],"name":"name","maxOccurs":0,"choice":True}},"version":[{"mshField":"mshField","value":"value"},{"mshField":"mshField","value":"value"}]}],"ignoreMinOccurs":True,"schematizedParsingType":"SCHEMATIZED_PARSING_TYPE_UNSPECIFIED"},"segmentTerminator":"segmentTerminator","allowNullHeader":True,"version":"PARSER_VERSION_UNSPECIFIED"},"rejectDuplicateMessage":True,"name":"name","notificationConfig":{"sendForBulkImport":True,"pubsubTopic":"pubsubTopic"},"notificationConfigs":[{"filter":"filter","pubsubTopic":"pubsubTopic"},{"filter":"filter","pubsubTopic":"pubsubTopic"}],"labels":{"key":"labels"}}
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
                    ('hl7V2StoreId', 'hl7_v2_store_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta1/{parent}/hl7V2Stores'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_healthcare_projects_locations_datasets_hl7_v2_stores_export(client):
    """Test case for healthcare_projects_locations_datasets_hl7_v2_stores_export

    
    """
    body = {"filter":"filter","gcsDestination":{"contentStructure":"CONTENT_STRUCTURE_UNSPECIFIED","messageView":"MESSAGE_VIEW_UNSPECIFIED","uriPrefix":"uriPrefix"},"pubsubDestination":{"pubsubTopic":"pubsubTopic"},"startTime":"startTime","endTime":"endTime"}
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
        path='/v1beta1/{nameexpor}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_healthcare_projects_locations_datasets_hl7_v2_stores_get_hl7v2_store_metrics(client):
    """Test case for healthcare_projects_locations_datasets_hl7_v2_stores_get_hl7v2_store_metrics

    
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
        path='/v1beta1/{nameget_hl7v2_store_metric}'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_healthcare_projects_locations_datasets_hl7_v2_stores_get_iam_policy(client):
    """Test case for healthcare_projects_locations_datasets_hl7_v2_stores_get_iam_policy

    
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
        path='/v1beta1/{resourceget_iam_polic}'.format(resource='resource_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_healthcare_projects_locations_datasets_hl7_v2_stores_import(client):
    """Test case for healthcare_projects_locations_datasets_hl7_v2_stores_import

    
    """
    body = {"gcsSource":{"uri":"uri"}}
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
        path='/v1beta1/{nameimpor}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_healthcare_projects_locations_datasets_hl7_v2_stores_list(client):
    """Test case for healthcare_projects_locations_datasets_hl7_v2_stores_list

    
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
        path='/v1beta1/{parent}/hl7V2Stores'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_healthcare_projects_locations_datasets_hl7_v2_stores_messages_batch_get(client):
    """Test case for healthcare_projects_locations_datasets_hl7_v2_stores_messages_batch_get

    
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
                    ('ids', ['ids_example']),
                    ('view', 'view_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1beta1/{parent}/messages:batchGet'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_healthcare_projects_locations_datasets_hl7_v2_stores_messages_create(client):
    """Test case for healthcare_projects_locations_datasets_hl7_v2_stores_messages_create

    
    """
    body = {"message":{"patientIds":[{"type":"type","value":"value"},{"type":"type","value":"value"}],"sendFacility":"sendFacility","data":"data","messageType":"messageType","createTime":"createTime","parsedData":{"segments":[{"segmentId":"segmentId","setId":"setId","fields":{"key":"fields"}},{"segmentId":"segmentId","setId":"setId","fields":{"key":"fields"}}]},"schematizedData":{"data":"data","error":"error"},"name":"name","labels":{"key":"labels"},"sendTime":"sendTime"}}
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
        path='/v1beta1/{parent}/messages'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_healthcare_projects_locations_datasets_hl7_v2_stores_messages_delete(client):
    """Test case for healthcare_projects_locations_datasets_hl7_v2_stores_messages_delete

    
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

async def test_healthcare_projects_locations_datasets_hl7_v2_stores_messages_ingest(client):
    """Test case for healthcare_projects_locations_datasets_hl7_v2_stores_messages_ingest

    
    """
    body = {"message":{"patientIds":[{"type":"type","value":"value"},{"type":"type","value":"value"}],"sendFacility":"sendFacility","data":"data","messageType":"messageType","createTime":"createTime","parsedData":{"segments":[{"segmentId":"segmentId","setId":"setId","fields":{"key":"fields"}},{"segmentId":"segmentId","setId":"setId","fields":{"key":"fields"}}]},"schematizedData":{"data":"data","error":"error"},"name":"name","labels":{"key":"labels"},"sendTime":"sendTime"}}
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
        path='/v1beta1/{parent}/messages:ingest'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_healthcare_projects_locations_datasets_hl7_v2_stores_messages_list(client):
    """Test case for healthcare_projects_locations_datasets_hl7_v2_stores_messages_list

    
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
                    ('pageToken', 'page_token_example'),
                    ('view', 'view_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1beta1/{parent}/messages'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_healthcare_projects_locations_datasets_hl7_v2_stores_messages_patch(client):
    """Test case for healthcare_projects_locations_datasets_hl7_v2_stores_messages_patch

    
    """
    body = {"patientIds":[{"type":"type","value":"value"},{"type":"type","value":"value"}],"sendFacility":"sendFacility","data":"data","messageType":"messageType","createTime":"createTime","parsedData":{"segments":[{"segmentId":"segmentId","setId":"setId","fields":{"key":"fields"}},{"segmentId":"segmentId","setId":"setId","fields":{"key":"fields"}}]},"schematizedData":{"data":"data","error":"error"},"name":"name","labels":{"key":"labels"},"sendTime":"sendTime"}
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

async def test_healthcare_projects_locations_datasets_hl7_v2_stores_set_iam_policy(client):
    """Test case for healthcare_projects_locations_datasets_hl7_v2_stores_set_iam_policy

    
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
        path='/v1beta1/{resourceset_iam_polic}'.format(resource='resource_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_healthcare_projects_locations_datasets_hl7_v2_stores_test_iam_permissions(client):
    """Test case for healthcare_projects_locations_datasets_hl7_v2_stores_test_iam_permissions

    
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

async def test_healthcare_projects_locations_datasets_list(client):
    """Test case for healthcare_projects_locations_datasets_list

    
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
        path='/v1beta1/{parent}/datasets'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_healthcare_projects_locations_datasets_operations_cancel(client):
    """Test case for healthcare_projects_locations_datasets_operations_cancel

    
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
        path='/v1beta1/{namecance}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_healthcare_projects_locations_datasets_operations_get(client):
    """Test case for healthcare_projects_locations_datasets_operations_get

    
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
        path='/v1beta1/{name}'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_healthcare_projects_locations_datasets_operations_list(client):
    """Test case for healthcare_projects_locations_datasets_operations_list

    
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
        path='/v1beta1/{name}/operations'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_healthcare_projects_locations_list(client):
    """Test case for healthcare_projects_locations_list

    
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
        path='/v1beta1/{name}/locations'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_healthcare_projects_locations_services_nlp_analyze_entities(client):
    """Test case for healthcare_projects_locations_services_nlp_analyze_entities

    
    """
    body = {"licensedVocabularies":["LICENSED_VOCABULARY_UNSPECIFIED","LICENSED_VOCABULARY_UNSPECIFIED"],"alternativeOutputFormat":"ALTERNATIVE_OUTPUT_FORMAT_UNSPECIFIED","documentContent":"documentContent"}
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
        path='/v1beta1/{nlp_serviceanalyze_entitie}'.format(nlp_service='nlp_service_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

