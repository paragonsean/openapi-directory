from typing import List, Dict
from aiohttp import web

from openapi_server.models.activate_consent_request import ActivateConsentRequest
from openapi_server.models.analyze_entities_request import AnalyzeEntitiesRequest
from openapi_server.models.analyze_entities_response import AnalyzeEntitiesResponse
from openapi_server.models.attribute_definition import AttributeDefinition
from openapi_server.models.check_data_access_request import CheckDataAccessRequest
from openapi_server.models.check_data_access_response import CheckDataAccessResponse
from openapi_server.models.consent import Consent
from openapi_server.models.consent_artifact import ConsentArtifact
from openapi_server.models.consent_store import ConsentStore
from openapi_server.models.create_message_request import CreateMessageRequest
from openapi_server.models.dataset import Dataset
from openapi_server.models.deidentify_dataset_request import DeidentifyDatasetRequest
from openapi_server.models.deidentify_fhir_store_request import DeidentifyFhirStoreRequest
from openapi_server.models.dicom_store import DicomStore
from openapi_server.models.dicom_store_metrics import DicomStoreMetrics
from openapi_server.models.evaluate_user_consents_request import EvaluateUserConsentsRequest
from openapi_server.models.evaluate_user_consents_response import EvaluateUserConsentsResponse
from openapi_server.models.export_messages_request import ExportMessagesRequest
from openapi_server.models.fhir_store import FhirStore
from openapi_server.models.fhir_store_metrics import FhirStoreMetrics
from openapi_server.models.hl7_v2_store import Hl7V2Store
from openapi_server.models.hl7_v2_store_metrics import Hl7V2StoreMetrics
from openapi_server.models.http_body import HttpBody
from openapi_server.models.import_messages_request import ImportMessagesRequest
from openapi_server.models.ingest_message_request import IngestMessageRequest
from openapi_server.models.ingest_message_response import IngestMessageResponse
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
from openapi_server.models.set_iam_policy_request import SetIamPolicyRequest
from openapi_server.models.study_metrics import StudyMetrics
from openapi_server.models.test_iam_permissions_request import TestIamPermissionsRequest
from openapi_server.models.test_iam_permissions_response import TestIamPermissionsResponse
from openapi_server.models.user_data_mapping import UserDataMapping
from openapi_server import util


async def healthcare_projects_locations_datasets_consent_stores_attribute_definitions_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, attribute_definition_id=None, body=None) -> web.Response:
    """healthcare_projects_locations_datasets_consent_stores_attribute_definitions_create

    Creates a new Attribute definition in the parent consent store.

    :param parent: Required. The name of the consent store that this Attribute definition belongs to.
    :type parent: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param attribute_definition_id: Required. The ID of the Attribute definition to create. The string must match the following regex: &#x60;_a-zA-Z{0,255}&#x60; and must not be a reserved keyword within the Common Expression Language as listed on https://github.com/google/cel-spec/blob/master/doc/langdef.md.
    :type attribute_definition_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = AttributeDefinition.from_dict(body)
    return web.Response(status=200)


async def healthcare_projects_locations_datasets_consent_stores_attribute_definitions_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, page_size=None, page_token=None) -> web.Response:
    """healthcare_projects_locations_datasets_consent_stores_attribute_definitions_list

    Lists the Attribute definitions in the specified consent store.

    :param parent: Required. Name of the consent store to retrieve Attribute definitions from.
    :type parent: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param filter: Optional. Restricts the attributes returned to those matching a filter. The only field available for filtering is &#x60;category&#x60;. For example, &#x60;filter&#x3D;category&#x3D;\\\&quot;REQUEST\\\&quot;&#x60;.
    :type filter: str
    :param page_size: Optional. Limit on the number of Attribute definitions to return in a single response. If not specified, 100 is used. May not be larger than 1000.
    :type page_size: int
    :param page_token: Optional. Token to retrieve the next page of results or empty to get the first page.
    :type page_token: str

    """
    return web.Response(status=200)


async def healthcare_projects_locations_datasets_consent_stores_check_data_access(request: web.Request, consent_store, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """healthcare_projects_locations_datasets_consent_stores_check_data_access

    Checks if a particular data_id of a User data mapping in the specified consent store is consented for the specified use.

    :param consent_store: Required. Name of the consent store where the requested data_id is stored, of the form &#x60;projects/{project_id}/locations/{location_id}/datasets/{dataset_id}/consentStores/{consent_store_id}&#x60;.
    :type consent_store: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = CheckDataAccessRequest.from_dict(body)
    return web.Response(status=200)


async def healthcare_projects_locations_datasets_consent_stores_consent_artifacts_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """healthcare_projects_locations_datasets_consent_stores_consent_artifacts_create

    Creates a new Consent artifact in the parent consent store.

    :param parent: Required. The name of the consent store this Consent artifact belongs to.
    :type parent: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = ConsentArtifact.from_dict(body)
    return web.Response(status=200)


async def healthcare_projects_locations_datasets_consent_stores_consent_artifacts_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, page_size=None, page_token=None) -> web.Response:
    """healthcare_projects_locations_datasets_consent_stores_consent_artifacts_list

    Lists the Consent artifacts in the specified consent store.

    :param parent: Required. Name of the consent store to retrieve consent artifacts from.
    :type parent: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param filter: Optional. Restricts the artifacts returned to those matching a filter. The following syntax is available: * A string field value can be written as text inside quotation marks, for example &#x60;\&quot;query text\&quot;&#x60;. The only valid relational operation for text fields is equality (&#x60;&#x3D;&#x60;), where text is searched within the field, rather than having the field be equal to the text. For example, &#x60;\&quot;Comment &#x3D; great\&quot;&#x60; returns messages with &#x60;great&#x60; in the comment field. * A number field value can be written as an integer, a decimal, or an exponential. The valid relational operators for number fields are the equality operator (&#x60;&#x3D;&#x60;), along with the less than/greater than operators (&#x60;&lt;&#x60;, &#x60;&lt;&#x3D;&#x60;, &#x60;&gt;&#x60;, &#x60;&gt;&#x3D;&#x60;). Note that there is no inequality (&#x60;!&#x3D;&#x60;) operator. You can prepend the &#x60;NOT&#x60; operator to an expression to negate it. * A date field value must be written in &#x60;yyyy-mm-dd&#x60; form. Fields with date and time use the RFC3339 time format. Leading zeros are required for one-digit months and days. The valid relational operators for date fields are the equality operator (&#x60;&#x3D;&#x60;) , along with the less than/greater than operators (&#x60;&lt;&#x60;, &#x60;&lt;&#x3D;&#x60;, &#x60;&gt;&#x60;, &#x60;&gt;&#x3D;&#x60;). Note that there is no inequality (&#x60;!&#x3D;&#x60;) operator. You can prepend the &#x60;NOT&#x60; operator to an expression to negate it. * Multiple field query expressions can be combined in one query by adding &#x60;AND&#x60; or &#x60;OR&#x60; operators between the expressions. If a boolean operator appears within a quoted string, it is not treated as special, it&#39;s just another part of the character string to be matched. You can prepend the &#x60;NOT&#x60; operator to an expression to negate it. The fields available for filtering are: - user_id. For example, &#x60;filter&#x3D;user_id&#x3D;\\\&quot;user123\\\&quot;&#x60;. - consent_content_version - metadata. For example, &#x60;filter&#x3D;Metadata(\\\&quot;testkey\\\&quot;)&#x3D;\\\&quot;value\\\&quot;&#x60; or &#x60;filter&#x3D;HasMetadata(\\\&quot;testkey\\\&quot;)&#x60;.
    :type filter: str
    :param page_size: Optional. Limit on the number of consent artifacts to return in a single response. If not specified, 100 is used. May not be larger than 1000.
    :type page_size: int
    :param page_token: Optional. The next_page_token value returned from the previous List request, if any.
    :type page_token: str

    """
    return web.Response(status=200)


async def healthcare_projects_locations_datasets_consent_stores_consents_activate(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """healthcare_projects_locations_datasets_consent_stores_consents_activate

    Activates the latest revision of the specified Consent by committing a new revision with &#x60;state&#x60; updated to &#x60;ACTIVE&#x60;. If the latest revision of the specified Consent is in the &#x60;ACTIVE&#x60; state, no new revision is committed. A FAILED_PRECONDITION error occurs if the latest revision of the specified Consent is in the &#x60;REJECTED&#x60; or &#x60;REVOKED&#x60; state.

    :param name: Required. The resource name of the Consent to activate, of the form &#x60;projects/{project_id}/locations/{location_id}/datasets/{dataset_id}/consentStores/{consent_store_id}/consents/{consent_id}&#x60;. An INVALID_ARGUMENT error occurs if &#x60;revision_id&#x60; is specified in the name.
    :type name: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = ActivateConsentRequest.from_dict(body)
    return web.Response(status=200)


async def healthcare_projects_locations_datasets_consent_stores_consents_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """healthcare_projects_locations_datasets_consent_stores_consents_create

    Creates a new Consent in the parent consent store.

    :param parent: Required. Name of the consent store.
    :type parent: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = Consent.from_dict(body)
    return web.Response(status=200)


async def healthcare_projects_locations_datasets_consent_stores_consents_delete_revision(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None) -> web.Response:
    """healthcare_projects_locations_datasets_consent_stores_consents_delete_revision

    Deletes the specified revision of a Consent. An INVALID_ARGUMENT error occurs if the specified revision is the latest revision.

    :param name: Required. The resource name of the Consent revision to delete, of the form &#x60;projects/{project_id}/locations/{location_id}/datasets/{dataset_id}/consentStores/{consent_store_id}/consents/{consent_id}@{revision_id}&#x60;. An INVALID_ARGUMENT error occurs if &#x60;revision_id&#x60; is not specified in the name.
    :type name: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str

    """
    return web.Response(status=200)


async def healthcare_projects_locations_datasets_consent_stores_consents_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, page_size=None, page_token=None) -> web.Response:
    """healthcare_projects_locations_datasets_consent_stores_consents_list

    Lists the Consent in the given consent store, returning each Consent&#39;s latest revision.

    :param parent: Required. Name of the consent store to retrieve Consents from.
    :type parent: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param filter: Optional. Restricts the Consents returned to those matching a filter. The following syntax is available: * A string field value can be written as text inside quotation marks, for example &#x60;\&quot;query text\&quot;&#x60;. The only valid relational operation for text fields is equality (&#x60;&#x3D;&#x60;), where text is searched within the field, rather than having the field be equal to the text. For example, &#x60;\&quot;Comment &#x3D; great\&quot;&#x60; returns messages with &#x60;great&#x60; in the comment field. * A number field value can be written as an integer, a decimal, or an exponential. The valid relational operators for number fields are the equality operator (&#x60;&#x3D;&#x60;), along with the less than/greater than operators (&#x60;&lt;&#x60;, &#x60;&lt;&#x3D;&#x60;, &#x60;&gt;&#x60;, &#x60;&gt;&#x3D;&#x60;). Note that there is no inequality (&#x60;!&#x3D;&#x60;) operator. You can prepend the &#x60;NOT&#x60; operator to an expression to negate it. * A date field value must be written in &#x60;yyyy-mm-dd&#x60; form. Fields with date and time use the RFC3339 time format. Leading zeros are required for one-digit months and days. The valid relational operators for date fields are the equality operator (&#x60;&#x3D;&#x60;) , along with the less than/greater than operators (&#x60;&lt;&#x60;, &#x60;&lt;&#x3D;&#x60;, &#x60;&gt;&#x60;, &#x60;&gt;&#x3D;&#x60;). Note that there is no inequality (&#x60;!&#x3D;&#x60;) operator. You can prepend the &#x60;NOT&#x60; operator to an expression to negate it. * Multiple field query expressions can be combined in one query by adding &#x60;AND&#x60; or &#x60;OR&#x60; operators between the expressions. If a boolean operator appears within a quoted string, it is not treated as special, it&#39;s just another part of the character string to be matched. You can prepend the &#x60;NOT&#x60; operator to an expression to negate it. The fields available for filtering are: - user_id. For example, &#x60;filter&#x3D;&#39;user_id&#x3D;\&quot;user123\&quot;&#39;&#x60;. - consent_artifact - state - revision_create_time - metadata. For example, &#x60;filter&#x3D;Metadata(\\\&quot;testkey\\\&quot;)&#x3D;\\\&quot;value\\\&quot;&#x60; or &#x60;filter&#x3D;HasMetadata(\\\&quot;testkey\\\&quot;)&#x60;.
    :type filter: str
    :param page_size: Optional. Limit on the number of Consents to return in a single response. If not specified, 100 is used. May not be larger than 1000.
    :type page_size: int
    :param page_token: Optional. The next_page_token value returned from the previous List request, if any.
    :type page_token: str

    """
    return web.Response(status=200)


async def healthcare_projects_locations_datasets_consent_stores_consents_list_revisions(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, page_size=None, page_token=None) -> web.Response:
    """healthcare_projects_locations_datasets_consent_stores_consents_list_revisions

    Lists the revisions of the specified Consent in reverse chronological order.

    :param name: Required. The resource name of the Consent to retrieve revisions for.
    :type name: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param filter: Optional. Restricts the revisions returned to those matching a filter. The following syntax is available: * A string field value can be written as text inside quotation marks, for example &#x60;\&quot;query text\&quot;&#x60;. The only valid relational operation for text fields is equality (&#x60;&#x3D;&#x60;), where text is searched within the field, rather than having the field be equal to the text. For example, &#x60;\&quot;Comment &#x3D; great\&quot;&#x60; returns messages with &#x60;great&#x60; in the comment field. * A number field value can be written as an integer, a decimal, or an exponential. The valid relational operators for number fields are the equality operator (&#x60;&#x3D;&#x60;), along with the less than/greater than operators (&#x60;&lt;&#x60;, &#x60;&lt;&#x3D;&#x60;, &#x60;&gt;&#x60;, &#x60;&gt;&#x3D;&#x60;). Note that there is no inequality (&#x60;!&#x3D;&#x60;) operator. You can prepend the &#x60;NOT&#x60; operator to an expression to negate it. * A date field value must be written in &#x60;yyyy-mm-dd&#x60; form. Fields with date and time use the RFC3339 time format. Leading zeros are required for one-digit months and days. The valid relational operators for date fields are the equality operator (&#x60;&#x3D;&#x60;) , along with the less than/greater than operators (&#x60;&lt;&#x60;, &#x60;&lt;&#x3D;&#x60;, &#x60;&gt;&#x60;, &#x60;&gt;&#x3D;&#x60;). Note that there is no inequality (&#x60;!&#x3D;&#x60;) operator. You can prepend the &#x60;NOT&#x60; operator to an expression to negate it. * Multiple field query expressions can be combined in one query by adding &#x60;AND&#x60; or &#x60;OR&#x60; operators between the expressions. If a boolean operator appears within a quoted string, it is not treated as special, it&#39;s just another part of the character string to be matched. You can prepend the &#x60;NOT&#x60; operator to an expression to negate it. Fields available for filtering are: - user_id. For example, &#x60;filter&#x3D;&#39;user_id&#x3D;\&quot;user123\&quot;&#39;&#x60;. - consent_artifact - state - revision_create_time - metadata. For example, &#x60;filter&#x3D;Metadata(\\\&quot;testkey\\\&quot;)&#x3D;\\\&quot;value\\\&quot;&#x60; or &#x60;filter&#x3D;HasMetadata(\\\&quot;testkey\\\&quot;)&#x60;.
    :type filter: str
    :param page_size: Optional. Limit on the number of revisions to return in a single response. If not specified, 100 is used. May not be larger than 1000.
    :type page_size: int
    :param page_token: Optional. Token to retrieve the next page of results or empty if there are no more results in the list.
    :type page_token: str

    """
    return web.Response(status=200)


async def healthcare_projects_locations_datasets_consent_stores_consents_reject(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """healthcare_projects_locations_datasets_consent_stores_consents_reject

    Rejects the latest revision of the specified Consent by committing a new revision with &#x60;state&#x60; updated to &#x60;REJECTED&#x60;. If the latest revision of the specified Consent is in the &#x60;REJECTED&#x60; state, no new revision is committed. A FAILED_PRECONDITION error occurs if the latest revision of the specified Consent is in the &#x60;ACTIVE&#x60; or &#x60;REVOKED&#x60; state.

    :param name: Required. The resource name of the Consent to reject, of the form &#x60;projects/{project_id}/locations/{location_id}/datasets/{dataset_id}/consentStores/{consent_store_id}/consents/{consent_id}&#x60;. An INVALID_ARGUMENT error occurs if &#x60;revision_id&#x60; is specified in the name.
    :type name: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = RejectConsentRequest.from_dict(body)
    return web.Response(status=200)


async def healthcare_projects_locations_datasets_consent_stores_consents_revoke(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """healthcare_projects_locations_datasets_consent_stores_consents_revoke

    Revokes the latest revision of the specified Consent by committing a new revision with &#x60;state&#x60; updated to &#x60;REVOKED&#x60;. If the latest revision of the specified Consent is in the &#x60;REVOKED&#x60; state, no new revision is committed. A FAILED_PRECONDITION error occurs if the latest revision of the given consent is in &#x60;DRAFT&#x60; or &#x60;REJECTED&#x60; state.

    :param name: Required. The resource name of the Consent to revoke, of the form &#x60;projects/{project_id}/locations/{location_id}/datasets/{dataset_id}/consentStores/{consent_store_id}/consents/{consent_id}&#x60;. An INVALID_ARGUMENT error occurs if &#x60;revision_id&#x60; is specified in the name.
    :type name: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = RevokeConsentRequest.from_dict(body)
    return web.Response(status=200)


async def healthcare_projects_locations_datasets_consent_stores_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, consent_store_id=None, body=None) -> web.Response:
    """healthcare_projects_locations_datasets_consent_stores_create

    Creates a new consent store in the parent dataset. Attempting to create a consent store with the same ID as an existing store fails with an ALREADY_EXISTS error.

    :param parent: Required. The name of the dataset this consent store belongs to.
    :type parent: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param consent_store_id: Required. The ID of the consent store to create. The string must match the following regex: &#x60;[\\p{L}\\p{N}_\\-\\.]{1,256}&#x60;. Cannot be changed after creation.
    :type consent_store_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = ConsentStore.from_dict(body)
    return web.Response(status=200)


async def healthcare_projects_locations_datasets_consent_stores_evaluate_user_consents(request: web.Request, consent_store, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """healthcare_projects_locations_datasets_consent_stores_evaluate_user_consents

    Evaluates the user&#39;s Consents for all matching User data mappings. Note: User data mappings are indexed asynchronously, which can cause a slight delay between the time mappings are created or updated and when they are included in EvaluateUserConsents results.

    :param consent_store: Required. Name of the consent store to retrieve User data mappings from.
    :type consent_store: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = EvaluateUserConsentsRequest.from_dict(body)
    return web.Response(status=200)


async def healthcare_projects_locations_datasets_consent_stores_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, page_size=None, page_token=None) -> web.Response:
    """healthcare_projects_locations_datasets_consent_stores_list

    Lists the consent stores in the specified dataset.

    :param parent: Required. Name of the dataset.
    :type parent: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param filter: Optional. Restricts the stores returned to those matching a filter. Only filtering on labels is supported. For example, &#x60;filter&#x3D;labels.key&#x3D;value&#x60;.
    :type filter: str
    :param page_size: Optional. Limit on the number of consent stores to return in a single response. If not specified, 100 is used. May not be larger than 1000.
    :type page_size: int
    :param page_token: Optional. Token to retrieve the next page of results, or empty to get the first page.
    :type page_token: str

    """
    return web.Response(status=200)


async def healthcare_projects_locations_datasets_consent_stores_query_accessible_data(request: web.Request, consent_store, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """healthcare_projects_locations_datasets_consent_stores_query_accessible_data

    Queries all data_ids that are consented for a specified use in the given consent store and writes them to a specified destination. The returned Operation includes a progress counter for the number of User data mappings processed. If the request is successful, a detailed response is returned of type QueryAccessibleDataResponse, contained in the response field when the operation finishes. The metadata field type is OperationMetadata. Errors are logged to Cloud Logging (see [Viewing error logs in Cloud Logging](https://cloud.google.com/healthcare/docs/how-tos/logging)). For example, the following sample log entry shows a &#x60;failed to evaluate consent policy&#x60; error that occurred during a QueryAccessibleData call to consent store &#x60;projects/{project_id}/locations/{location_id}/datasets/{dataset_id}/consentStores/{consent_store_id}&#x60;. &#x60;&#x60;&#x60;json jsonPayload: { @type: \&quot;type.googleapis.com/google.cloud.healthcare.logging.QueryAccessibleDataLogEntry\&quot; error: { code: 9 message: \&quot;failed to evaluate consent policy\&quot; } resourceName: \&quot;projects/{project_id}/locations/{location_id}/datasets/{dataset_id}/consentStores/{consent_store_id}/consents/{consent_id}\&quot; } logName: \&quot;projects/{project_id}/logs/healthcare.googleapis.com%2Fquery_accessible_data\&quot; operation: { id: \&quot;projects/{project_id}/locations/{location_id}/datasets/{dataset_id}/operations/{operation_id}\&quot; producer: \&quot;healthcare.googleapis.com/QueryAccessibleData\&quot; } receiveTimestamp: \&quot;TIMESTAMP\&quot; resource: { labels: { consent_store_id: \&quot;{consent_store_id}\&quot; dataset_id: \&quot;{dataset_id}\&quot; location: \&quot;{location_id}\&quot; project_id: \&quot;{project_id}\&quot; } type: \&quot;healthcare_consent_store\&quot; } severity: \&quot;ERROR\&quot; timestamp: \&quot;TIMESTAMP\&quot; &#x60;&#x60;&#x60;

    :param consent_store: Required. Name of the consent store to retrieve User data mappings from.
    :type consent_store: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = QueryAccessibleDataRequest.from_dict(body)
    return web.Response(status=200)


async def healthcare_projects_locations_datasets_consent_stores_user_data_mappings_archive(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """healthcare_projects_locations_datasets_consent_stores_user_data_mappings_archive

    Archives the specified User data mapping.

    :param name: Required. The resource name of the User data mapping to archive.
    :type name: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param body: 
    :type body: 

    """
    return web.Response(status=200)


async def healthcare_projects_locations_datasets_consent_stores_user_data_mappings_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """healthcare_projects_locations_datasets_consent_stores_user_data_mappings_create

    Creates a new User data mapping in the parent consent store.

    :param parent: Required. Name of the consent store.
    :type parent: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = UserDataMapping.from_dict(body)
    return web.Response(status=200)


async def healthcare_projects_locations_datasets_consent_stores_user_data_mappings_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, page_size=None, page_token=None) -> web.Response:
    """healthcare_projects_locations_datasets_consent_stores_user_data_mappings_list

    Lists the User data mappings in the specified consent store.

    :param parent: Required. Name of the consent store to retrieve User data mappings from.
    :type parent: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param filter: Optional. Restricts the User data mappings returned to those matching a filter. The following syntax is available: * A string field value can be written as text inside quotation marks, for example &#x60;\&quot;query text\&quot;&#x60;. The only valid relational operation for text fields is equality (&#x60;&#x3D;&#x60;), where text is searched within the field, rather than having the field be equal to the text. For example, &#x60;\&quot;Comment &#x3D; great\&quot;&#x60; returns messages with &#x60;great&#x60; in the comment field. * A number field value can be written as an integer, a decimal, or an exponential. The valid relational operators for number fields are the equality operator (&#x60;&#x3D;&#x60;), along with the less than/greater than operators (&#x60;&lt;&#x60;, &#x60;&lt;&#x3D;&#x60;, &#x60;&gt;&#x60;, &#x60;&gt;&#x3D;&#x60;). Note that there is no inequality (&#x60;!&#x3D;&#x60;) operator. You can prepend the &#x60;NOT&#x60; operator to an expression to negate it. * A date field value must be written in &#x60;yyyy-mm-dd&#x60; form. Fields with date and time use the RFC3339 time format. Leading zeros are required for one-digit months and days. The valid relational operators for date fields are the equality operator (&#x60;&#x3D;&#x60;) , along with the less than/greater than operators (&#x60;&lt;&#x60;, &#x60;&lt;&#x3D;&#x60;, &#x60;&gt;&#x60;, &#x60;&gt;&#x3D;&#x60;). Note that there is no inequality (&#x60;!&#x3D;&#x60;) operator. You can prepend the &#x60;NOT&#x60; operator to an expression to negate it. * Multiple field query expressions can be combined in one query by adding &#x60;AND&#x60; or &#x60;OR&#x60; operators between the expressions. If a boolean operator appears within a quoted string, it is not treated as special, it&#39;s just another part of the character string to be matched. You can prepend the &#x60;NOT&#x60; operator to an expression to negate it. The fields available for filtering are: - data_id - user_id. For example, &#x60;filter&#x3D;user_id&#x3D;\\\&quot;user123\\\&quot;&#x60;. - archived - archive_time
    :type filter: str
    :param page_size: Optional. Limit on the number of User data mappings to return in a single response. If not specified, 100 is used. May not be larger than 1000.
    :type page_size: int
    :param page_token: Optional. Token to retrieve the next page of results, or empty to get the first page.
    :type page_token: str

    """
    return web.Response(status=200)


async def healthcare_projects_locations_datasets_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, dataset_id=None, body=None) -> web.Response:
    """healthcare_projects_locations_datasets_create

    Creates a new health dataset. Results are returned through the Operation interface which returns either an &#x60;Operation.response&#x60; which contains a Dataset or &#x60;Operation.error&#x60;. The metadata field type is OperationMetadata.

    :param parent: Required. The name of the project where the server creates the dataset. For example, &#x60;projects/{project_id}/locations/{location_id}&#x60;.
    :type parent: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param dataset_id: Required. The ID of the dataset that is being created. The string must match the following regex: &#x60;[\\p{L}\\p{N}_\\-\\.]{1,256}&#x60;.
    :type dataset_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = Dataset.from_dict(body)
    return web.Response(status=200)


async def healthcare_projects_locations_datasets_deidentify(request: web.Request, source_dataset, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """healthcare_projects_locations_datasets_deidentify

    Creates a new dataset containing de-identified data from the source dataset. The metadata field type is OperationMetadata. If the request is successful, the response field type is DeidentifySummary. If errors occur, error is set. The LRO result may still be successful if de-identification fails for some DICOM instances. The new de-identified dataset will not contain these failed resources. Failed resource totals are tracked in Operation.metadata. Error details are also logged to Cloud Logging. For more information, see [Viewing error logs in Cloud Logging](https://cloud.google.com/healthcare/docs/how-tos/logging).

    :param source_dataset: Required. Source dataset resource name. For example, &#x60;projects/{project_id}/locations/{location_id}/datasets/{dataset_id}&#x60;.
    :type source_dataset: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = DeidentifyDatasetRequest.from_dict(body)
    return web.Response(status=200)


async def healthcare_projects_locations_datasets_dicom_stores_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, dicom_store_id=None, body=None) -> web.Response:
    """healthcare_projects_locations_datasets_dicom_stores_create

    Creates a new DICOM store within the parent dataset.

    :param parent: Required. The name of the dataset this DICOM store belongs to.
    :type parent: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param dicom_store_id: Required. The ID of the DICOM store that is being created. Any string value up to 256 characters in length.
    :type dicom_store_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = DicomStore.from_dict(body)
    return web.Response(status=200)


async def healthcare_projects_locations_datasets_dicom_stores_dicom_web_studies_get_study_metrics(request: web.Request, study, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None) -> web.Response:
    """healthcare_projects_locations_datasets_dicom_stores_dicom_web_studies_get_study_metrics

    GetStudyMetrics returns metrics for a study.

    :param study: Required. The study resource path. For example, &#x60;projects/{project_id}/locations/{location_id}/datasets/{dataset_id}/dicomStores/{dicom_store_id}/dicomWeb/studies/{study_uid}&#x60;.
    :type study: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str

    """
    return web.Response(status=200)


async def healthcare_projects_locations_datasets_dicom_stores_dicom_web_studies_series_get_series_metrics(request: web.Request, series, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None) -> web.Response:
    """healthcare_projects_locations_datasets_dicom_stores_dicom_web_studies_series_get_series_metrics

    GetSeriesMetrics returns metrics for a series.

    :param series: Required. The series resource path. For example, &#x60;projects/{project_id}/locations/{location_id}/datasets/{dataset_id}/dicomStores/{dicom_store_id}/dicomWeb/studies/{study_uid}/series/{series_uid}&#x60;.
    :type series: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str

    """
    return web.Response(status=200)


async def healthcare_projects_locations_datasets_dicom_stores_get_dicom_store_metrics(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None) -> web.Response:
    """healthcare_projects_locations_datasets_dicom_stores_get_dicom_store_metrics

    Gets metrics associated with the DICOM store.

    :param name: Required. The resource name of the DICOM store to get metrics for.
    :type name: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str

    """
    return web.Response(status=200)


async def healthcare_projects_locations_datasets_dicom_stores_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, page_size=None, page_token=None) -> web.Response:
    """healthcare_projects_locations_datasets_dicom_stores_list

    Lists the DICOM stores in the given dataset.

    :param parent: Required. Name of the dataset.
    :type parent: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param filter: Restricts stores returned to those matching a filter. The following syntax is available: * A string field value can be written as text inside quotation marks, for example &#x60;\&quot;query text\&quot;&#x60;. The only valid relational operation for text fields is equality (&#x60;&#x3D;&#x60;), where text is searched within the field, rather than having the field be equal to the text. For example, &#x60;\&quot;Comment &#x3D; great\&quot;&#x60; returns messages with &#x60;great&#x60; in the comment field. * A number field value can be written as an integer, a decimal, or an exponential. The valid relational operators for number fields are the equality operator (&#x60;&#x3D;&#x60;), along with the less than/greater than operators (&#x60;&lt;&#x60;, &#x60;&lt;&#x3D;&#x60;, &#x60;&gt;&#x60;, &#x60;&gt;&#x3D;&#x60;). Note that there is no inequality (&#x60;!&#x3D;&#x60;) operator. You can prepend the &#x60;NOT&#x60; operator to an expression to negate it. * A date field value must be written in &#x60;yyyy-mm-dd&#x60; form. Fields with date and time use the RFC3339 time format. Leading zeros are required for one-digit months and days. The valid relational operators for date fields are the equality operator (&#x60;&#x3D;&#x60;) , along with the less than/greater than operators (&#x60;&lt;&#x60;, &#x60;&lt;&#x3D;&#x60;, &#x60;&gt;&#x60;, &#x60;&gt;&#x3D;&#x60;). Note that there is no inequality (&#x60;!&#x3D;&#x60;) operator. You can prepend the &#x60;NOT&#x60; operator to an expression to negate it. * Multiple field query expressions can be combined in one query by adding &#x60;AND&#x60; or &#x60;OR&#x60; operators between the expressions. If a boolean operator appears within a quoted string, it is not treated as special, it&#39;s just another part of the character string to be matched. You can prepend the &#x60;NOT&#x60; operator to an expression to negate it. Only filtering on labels is supported. For example, &#x60;labels.key&#x3D;value&#x60;.
    :type filter: str
    :param page_size: Limit on the number of DICOM stores to return in a single response. If not specified, 100 is used. May not be larger than 1000.
    :type page_size: int
    :param page_token: The next_page_token value returned from the previous List request, if any.
    :type page_token: str

    """
    return web.Response(status=200)


async def healthcare_projects_locations_datasets_dicom_stores_studies_series_instances_delete(request: web.Request, parent, dicom_web_path, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None) -> web.Response:
    """healthcare_projects_locations_datasets_dicom_stores_studies_series_instances_delete

    DeleteInstance deletes an instance associated with the given study, series, and SOP Instance UID. Delete requests are equivalent to the GET requests specified in the Retrieve transaction. Study and series search results can take a few seconds to be updated after an instance is deleted using DeleteInstance. For samples that show how to call DeleteInstance, see [Delete a study, series, or instance](https://cloud.google.com/healthcare/docs/how-tos/dicomweb#delete-dicom).

    :param parent: Required. The name of the DICOM store that is being accessed. For example, &#x60;projects/{project_id}/locations/{location_id}/datasets/{dataset_id}/dicomStores/{dicom_store_id}&#x60;.
    :type parent: str
    :param dicom_web_path: Required. The path of the DeleteInstance request. For example, &#x60;studies/{study_uid}/series/{series_uid}/instances/{instance_uid}&#x60;.
    :type dicom_web_path: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str

    """
    return web.Response(status=200)


async def healthcare_projects_locations_datasets_dicom_stores_studies_series_instances_frames_retrieve_rendered(request: web.Request, parent, dicom_web_path, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None) -> web.Response:
    """healthcare_projects_locations_datasets_dicom_stores_studies_series_instances_frames_retrieve_rendered

    RetrieveRenderedFrames returns instances associated with the given study, series, SOP Instance UID and frame numbers in an acceptable Rendered Media Type. See [RetrieveTransaction] (http://dicom.nema.org/medical/dicom/current/output/html/part18.html#sect_10.4). For details on the implementation of RetrieveRenderedFrames, see [Rendered resources](https://cloud.google.com/healthcare/docs/dicom#rendered_resources) in the Cloud Healthcare API conformance statement. For samples that show how to call RetrieveRenderedFrames, see [Retrieve consumer image formats](https://cloud.google.com/healthcare/docs/how-tos/dicomweb#retrieve-consumer).

    :param parent: Required. The name of the DICOM store that is being accessed. For example, &#x60;projects/{project_id}/locations/{location_id}/datasets/{dataset_id}/dicomStores/{dicom_store_id}&#x60;.
    :type parent: str
    :param dicom_web_path: Required. The path of the RetrieveRenderedFrames DICOMweb request. For example, &#x60;studies/{study_uid}/series/{series_uid}/instances/{instance_uid}/frames/{frame_list}/rendered&#x60;.
    :type dicom_web_path: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str

    """
    return web.Response(status=200)


async def healthcare_projects_locations_datasets_dicom_stores_studies_store_instances(request: web.Request, parent, dicom_web_path, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """healthcare_projects_locations_datasets_dicom_stores_studies_store_instances

    StoreInstances stores DICOM instances associated with study instance unique identifiers (SUID). See [Store Transaction] (http://dicom.nema.org/medical/dicom/current/output/html/part18.html#sect_10.5). For details on the implementation of StoreInstances, see [Store transaction](https://cloud.google.com/healthcare/docs/dicom#store_transaction) in the Cloud Healthcare API conformance statement. For samples that show how to call StoreInstances, see [Store DICOM data](https://cloud.google.com/healthcare/docs/how-tos/dicomweb#store-dicom).

    :param parent: Required. The name of the DICOM store that is being accessed. For example, &#x60;projects/{project_id}/locations/{location_id}/datasets/{dataset_id}/dicomStores/{dicom_store_id}&#x60;.
    :type parent: str
    :param dicom_web_path: Required. The path of the StoreInstances DICOMweb request. For example, &#x60;studies/[{study_uid}]&#x60;. Note that the &#x60;study_uid&#x60; is optional.
    :type dicom_web_path: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = HttpBody.from_dict(body)
    return web.Response(status=200)


async def healthcare_projects_locations_datasets_fhir_stores_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, fhir_store_id=None, body=None) -> web.Response:
    """healthcare_projects_locations_datasets_fhir_stores_create

    Creates a new FHIR store within the parent dataset.

    :param parent: Required. The name of the dataset this FHIR store belongs to.
    :type parent: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param fhir_store_id: Required. The ID of the FHIR store that is being created. The string must match the following regex: &#x60;[\\p{L}\\p{N}_\\-\\.]{1,256}&#x60;.
    :type fhir_store_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = FhirStore.from_dict(body)
    return web.Response(status=200)


async def healthcare_projects_locations_datasets_fhir_stores_deidentify(request: web.Request, source_store, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """healthcare_projects_locations_datasets_fhir_stores_deidentify

    De-identifies data from the source store and writes it to the destination store. The metadata field type is OperationMetadata. If the request is successful, the response field type is DeidentifyFhirStoreSummary. If errors occur, error is set. Error details are also logged to Cloud Logging (see [Viewing error logs in Cloud Logging](https://cloud.google.com/healthcare/docs/how-tos/logging)).

    :param source_store: Required. Source FHIR store resource name. For example, &#x60;projects/{project_id}/locations/{location_id}/datasets/{dataset_id}/fhirStores/{fhir_store_id}&#x60;.
    :type source_store: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = DeidentifyFhirStoreRequest.from_dict(body)
    return web.Response(status=200)


async def healthcare_projects_locations_datasets_fhir_stores_fhir_capabilities(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None) -> web.Response:
    """healthcare_projects_locations_datasets_fhir_stores_fhir_capabilities

    Gets the FHIR capability statement ([STU3](http://hl7.org/implement/standards/fhir/STU3/capabilitystatement.html), [R4](http://hl7.org/implement/standards/fhir/R4/capabilitystatement.html)), or the [conformance statement](http://hl7.org/implement/standards/fhir/DSTU2/conformance.html) in the DSTU2 case for the store, which contains a description of functionality supported by the server. Implements the FHIR standard capabilities interaction ([STU3](http://hl7.org/implement/standards/fhir/STU3/http.html#capabilities), [R4](http://hl7.org/implement/standards/fhir/R4/http.html#capabilities)), or the [conformance interaction](http://hl7.org/implement/standards/fhir/DSTU2/http.html#conformance) in the DSTU2 case. On success, the response body contains a JSON-encoded representation of a &#x60;CapabilityStatement&#x60; resource.

    :param name: Required. Name of the FHIR store to retrieve the capabilities for.
    :type name: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str

    """
    return web.Response(status=200)


async def healthcare_projects_locations_datasets_fhir_stores_fhir_conditional_delete(request: web.Request, parent, type, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None) -> web.Response:
    """healthcare_projects_locations_datasets_fhir_stores_fhir_conditional_delete

    Deletes a FHIR resource that match an identifier search query. Implements the FHIR standard conditional delete interaction, limited to searching by resource identifier. If multiple resources match, 412 Precondition Failed error will be returned. Search term for identifier should be in the pattern &#x60;identifier&#x3D;system|value&#x60; or &#x60;identifier&#x3D;value&#x60; - similar to the &#x60;search&#x60; method on resources with a specific identifier. Note: Unless resource versioning is disabled by setting the disable_resource_versioning flag on the FHIR store, the deleted resource is moved to a history repository that can still be retrieved through vread and related methods, unless they are removed by the purge method. For samples that show how to call &#x60;conditionalDelete&#x60;, see [Conditionally deleting a FHIR resource](https://cloud.google.com/healthcare/docs/how-tos/fhir-resources#conditionally_deleting_a_fhir_resource).

    :param parent: Required. The name of the FHIR store this resource belongs to.
    :type parent: str
    :param type: Required. The FHIR resource type to delete, such as Patient or Observation. For a complete list, see the FHIR Resource Index ([DSTU2](https://hl7.org/implement/standards/fhir/DSTU2/resourcelist.html), [STU3](https://hl7.org/implement/standards/fhir/STU3/resourcelist.html), [R4](https://hl7.org/implement/standards/fhir/R4/resourcelist.html)).
    :type type: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str

    """
    return web.Response(status=200)


async def healthcare_projects_locations_datasets_fhir_stores_fhir_conditional_patch(request: web.Request, parent, type, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """healthcare_projects_locations_datasets_fhir_stores_fhir_conditional_patch

    If a resource is found with the identifier specified in the query parameters, updates part of that resource by applying the operations specified in a [JSON Patch](http://jsonpatch.com/) document. Implements the FHIR standard conditional patch interaction, limited to searching by resource identifier. DSTU2 doesn&#39;t define a conditional patch method, but the server supports it in the same way it supports STU3. Search term for identifier should be in the pattern &#x60;identifier&#x3D;system|value&#x60; or &#x60;identifier&#x3D;value&#x60; - similar to the &#x60;search&#x60; method on resources with a specific identifier. If the search criteria identify more than one match, the request returns a &#x60;412 Precondition Failed&#x60; error. The request body must contain a JSON Patch document, and the request headers must contain &#x60;Content-Type: application/json-patch+json&#x60;. On success, the response body contains a JSON-encoded representation of the updated resource, including the server-assigned version ID. Errors generated by the FHIR store contain a JSON-encoded &#x60;OperationOutcome&#x60; resource describing the reason for the error. If the request cannot be mapped to a valid API method on a FHIR store, a generic GCP error might be returned instead. For samples that show how to call &#x60;conditionalPatch&#x60;, see [Conditionally patching a FHIR resource](https://cloud.google.com/healthcare/docs/how-tos/fhir-resources#conditionally_patching_a_fhir_resource).

    :param parent: Required. The name of the FHIR store this resource belongs to.
    :type parent: str
    :param type: Required. The FHIR resource type to update, such as Patient or Observation. For a complete list, see the FHIR Resource Index ([DSTU2](https://hl7.org/implement/standards/fhir/DSTU2/resourcelist.html), [STU3](https://hl7.org/implement/standards/fhir/STU3/resourcelist.html), [R4](https://hl7.org/implement/standards/fhir/R4/resourcelist.html)).
    :type type: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = HttpBody.from_dict(body)
    return web.Response(status=200)


async def healthcare_projects_locations_datasets_fhir_stores_fhir_conditional_update(request: web.Request, parent, type, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """healthcare_projects_locations_datasets_fhir_stores_fhir_conditional_update

    If a resource is found with the identifier specified in the query parameters, updates the entire contents of that resource. Implements the FHIR standard conditional update interaction, limited to searching by resource identifier. Search term for identifier should be in the pattern &#x60;identifier&#x3D;system|value&#x60; or &#x60;identifier&#x3D;value&#x60; - similar to the &#x60;search&#x60; method on resources with a specific identifier. If the search criteria identify more than one match, the request returns a &#x60;412 Precondition Failed&#x60; error. If the search criteria identify zero matches, and the supplied resource body contains an &#x60;id&#x60;, and the FHIR store has enable_update_create set, creates the resource with the client-specified ID. It is strongly advised not to include or encode any sensitive data such as patient identifiers in client-specified resource IDs. Those IDs are part of the FHIR resource path recorded in Cloud Audit Logs and Pub/Sub notifications. Those IDs can also be contained in reference fields within other resources. If the search criteria identify zero matches, and the supplied resource body does not contain an &#x60;id&#x60;, the resource is created with a server-assigned ID as per the create method. The request body must contain a JSON-encoded FHIR resource, and the request headers must contain &#x60;Content-Type: application/fhir+json&#x60;. On success, the response body contains a JSON-encoded representation of the updated resource, including the server-assigned version ID. Errors generated by the FHIR store contain a JSON-encoded &#x60;OperationOutcome&#x60; resource describing the reason for the error. If the request cannot be mapped to a valid API method on a FHIR store, a generic GCP error might be returned instead. For samples that show how to call &#x60;conditionalUpdate&#x60;, see [Conditionally updating a FHIR resource](https://cloud.google.com/healthcare/docs/how-tos/fhir-resources#conditionally_updating_a_fhir_resource).

    :param parent: Required. The name of the FHIR store this resource belongs to.
    :type parent: str
    :param type: Required. The FHIR resource type to update, such as Patient or Observation. For a complete list, see the FHIR Resource Index ([DSTU2](https://hl7.org/implement/standards/fhir/DSTU2/resourcelist.html), [STU3](https://hl7.org/implement/standards/fhir/STU3/resourcelist.html), [R4](https://hl7.org/implement/standards/fhir/R4/resourcelist.html)). Must match the resource type in the provided content.
    :type type: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = HttpBody.from_dict(body)
    return web.Response(status=200)


async def healthcare_projects_locations_datasets_fhir_stores_fhir_create(request: web.Request, parent, type, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """healthcare_projects_locations_datasets_fhir_stores_fhir_create

    Creates a FHIR resource. Implements the FHIR standard create interaction ([DSTU2](http://hl7.org/implement/standards/fhir/DSTU2/http.html#create), [STU3](http://hl7.org/implement/standards/fhir/STU3/http.html#create), [R4](http://hl7.org/implement/standards/fhir/R4/http.html#create)), which creates a new resource with a server-assigned resource ID. Also supports the FHIR standard conditional create interaction ([DSTU2](https://hl7.org/implement/standards/fhir/DSTU2/http.html#ccreate), [STU3](https://hl7.org/implement/standards/fhir/STU3/http.html#ccreate), [R4](https://hl7.org/implement/standards/fhir/R4/http.html#ccreate)), specified by supplying an &#x60;If-None-Exist&#x60; header containing a FHIR search query, limited to searching by resource identifier. If no resources match this search query, the server processes the create operation as normal. When using conditional create, the search term for identifier should be in the pattern &#x60;identifier&#x3D;system|value&#x60; or &#x60;identifier&#x3D;value&#x60; - similar to the &#x60;search&#x60; method on resources with a specific identifier. The request body must contain a JSON-encoded FHIR resource, and the request headers must contain &#x60;Content-Type: application/fhir+json&#x60;. On success, the response body contains a JSON-encoded representation of the resource as it was created on the server, including the server-assigned resource ID and version ID. Errors generated by the FHIR store contain a JSON-encoded &#x60;OperationOutcome&#x60; resource describing the reason for the error. If the request cannot be mapped to a valid API method on a FHIR store, a generic GCP error might be returned instead. For samples that show how to call &#x60;create&#x60;, see [Creating a FHIR resource](https://cloud.google.com/healthcare/docs/how-tos/fhir-resources#creating_a_fhir_resource).

    :param parent: Required. The name of the FHIR store this resource belongs to.
    :type parent: str
    :param type: Required. The FHIR resource type to create, such as Patient or Observation. For a complete list, see the FHIR Resource Index ([DSTU2](http://hl7.org/implement/standards/fhir/DSTU2/resourcelist.html), [STU3](http://hl7.org/implement/standards/fhir/STU3/resourcelist.html), [R4](http://hl7.org/implement/standards/fhir/R4/resourcelist.html)). Must match the resource type in the provided content.
    :type type: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = HttpBody.from_dict(body)
    return web.Response(status=200)


async def healthcare_projects_locations_datasets_fhir_stores_fhir_execute_bundle(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """healthcare_projects_locations_datasets_fhir_stores_fhir_execute_bundle

    Executes all the requests in the given Bundle. Implements the FHIR standard batch/transaction interaction ([DSTU2](https://hl7.org/implement/standards/fhir/DSTU2/http.html#transaction), [STU3](https://hl7.org/implement/standards/fhir/STU3/http.html#transaction), [R4](https://hl7.org/implement/standards/fhir/R4/http.html#transaction)). Supports all interactions within a bundle, except search. This method accepts Bundles of type &#x60;batch&#x60; and &#x60;transaction&#x60;, processing them according to the batch processing rules ([DSTU2](https://hl7.org/implement/standards/fhir/DSTU2/http.html#2.1.0.16.1), [STU3](https://hl7.org/implement/standards/fhir/STU3/http.html#2.21.0.17.1), [R4](https://hl7.org/implement/standards/fhir/R4/http.html#brules)) and transaction processing rules ([DSTU2](https://hl7.org/implement/standards/fhir/DSTU2/http.html#2.1.0.16.2), [STU3](https://hl7.org/implement/standards/fhir/STU3/http.html#2.21.0.17.2), [R4](https://hl7.org/implement/standards/fhir/R4/http.html#trules)). The request body must contain a JSON-encoded FHIR &#x60;Bundle&#x60; resource, and the request headers must contain &#x60;Content-Type: application/fhir+json&#x60;. For a batch bundle or a successful transaction, the response body contains a JSON-encoded representation of a &#x60;Bundle&#x60; resource of type &#x60;batch-response&#x60; or &#x60;transaction-response&#x60; containing one entry for each entry in the request, with the outcome of processing the entry. In the case of an error for a transaction bundle, the response body contains a JSON-encoded &#x60;OperationOutcome&#x60; resource describing the reason for the error. If the request cannot be mapped to a valid API method on a FHIR store, a generic GCP error might be returned instead. This method checks permissions for each request in the bundle. The &#x60;executeBundle&#x60; permission is required to call this method, but you must also grant sufficient permissions to execute the individual requests in the bundle. For example, if the bundle contains a request to create a FHIR resource, the caller must also have been granted the &#x60;healthcare.fhirResources.create&#x60; permission. You can use audit logs to view the permissions for &#x60;executeBundle&#x60; and each request in the bundle. For more information, see [Viewing Cloud Audit logs](https://cloud.google.com/healthcare-api/docs/how-tos/audit-logging). For samples that show how to call &#x60;executeBundle&#x60;, see [Managing FHIR resources using FHIR bundles](https://cloud.google.com/healthcare/docs/how-tos/fhir-bundles).

    :param parent: Required. Name of the FHIR store in which this bundle will be executed.
    :type parent: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = HttpBody.from_dict(body)
    return web.Response(status=200)


async def healthcare_projects_locations_datasets_fhir_stores_fhir_history(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, at=None, count=None, page_token=None, since=None) -> web.Response:
    """healthcare_projects_locations_datasets_fhir_stores_fhir_history

    Lists all the versions of a resource (including the current version and deleted versions) from the FHIR store. Implements the per-resource form of the FHIR standard history interaction ([DSTU2](http://hl7.org/implement/standards/fhir/DSTU2/http.html#history), [STU3](http://hl7.org/implement/standards/fhir/STU3/http.html#history), [R4](http://hl7.org/implement/standards/fhir/R4/http.html#history)). On success, the response body contains a JSON-encoded representation of a &#x60;Bundle&#x60; resource of type &#x60;history&#x60;, containing the version history sorted from most recent to oldest versions. Errors generated by the FHIR store contain a JSON-encoded &#x60;OperationOutcome&#x60; resource describing the reason for the error. If the request cannot be mapped to a valid API method on a FHIR store, a generic GCP error might be returned instead. For samples that show how to call &#x60;history&#x60;, see [Listing FHIR resource versions](https://cloud.google.com/healthcare/docs/how-tos/fhir-resources#listing_fhir_resource_versions).

    :param name: Required. The name of the resource to retrieve.
    :type name: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param at: Only include resource versions that were current at some point during the time period specified in the date time value. The date parameter format is yyyy-mm-ddThh:mm:ss[Z|(+|-)hh:mm] Clients may specify any of the following: * An entire year: &#x60;_at&#x3D;2019&#x60; * An entire month: &#x60;_at&#x3D;2019-01&#x60; * A specific day: &#x60;_at&#x3D;2019-01-20&#x60; * A specific second: &#x60;_at&#x3D;2018-12-31T23:59:58Z&#x60;
    :type at: str
    :param count: The maximum number of search results on a page. If not specified, 100 is used. May not be larger than 1000.
    :type count: int
    :param page_token: Used to retrieve the first, previous, next, or last page of resource versions when using pagination. Value should be set to the value of &#x60;_page_token&#x60; set in next or previous page links&#39; URLs. Next and previous page are returned in the response bundle&#39;s links field, where &#x60;link.relation&#x60; is \&quot;previous\&quot; or \&quot;next\&quot;. Omit &#x60;_page_token&#x60; if no previous request has been made.
    :type page_token: str
    :param since: Only include resource versions that were created at or after the given instant in time. The instant in time uses the format YYYY-MM-DDThh:mm:ss.sss+zz:zz (for example 2015-02-07T13:28:17.239+02:00 or 2017-01-01T00:00:00Z). The time must be specified to the second and include a time zone.
    :type since: str

    """
    return web.Response(status=200)


async def healthcare_projects_locations_datasets_fhir_stores_fhir_patient_everything(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, count=None, page_token=None, since=None, type=None, end=None, start=None) -> web.Response:
    """healthcare_projects_locations_datasets_fhir_stores_fhir_patient_everything

    Retrieves a Patient resource and resources related to that patient. Implements the FHIR extended operation Patient-everything ([DSTU2](http://hl7.org/implement/standards/fhir/DSTU2/patient-operations.html#everything), [STU3](http://hl7.org/implement/standards/fhir/STU3/patient-operations.html#everything), [R4](http://hl7.org/implement/standards/fhir/R4/patient-operations.html#everything)). On success, the response body contains a JSON-encoded representation of a &#x60;Bundle&#x60; resource of type &#x60;searchset&#x60;, containing the results of the operation. Errors generated by the FHIR store contain a JSON-encoded &#x60;OperationOutcome&#x60; resource describing the reason for the error. If the request cannot be mapped to a valid API method on a FHIR store, a generic GCP error might be returned instead. The resources in scope for the response are: * The patient resource itself. * All the resources directly referenced by the patient resource. * Resources directly referencing the patient resource that meet the inclusion criteria. The inclusion criteria are based on the membership rules in the patient compartment definition ([DSTU2](http://hl7.org/fhir/DSTU2/compartment-patient.html), [STU3](http://www.hl7.org/fhir/stu3/compartmentdefinition-patient.html), [R4](http://hl7.org/fhir/R4/compartmentdefinition-patient.html)), which details the eligible resource types and referencing search parameters. For samples that show how to call &#x60;Patient-everything&#x60;, see [Getting all patient compartment resources](https://cloud.google.com/healthcare/docs/how-tos/fhir-resources#getting_all_patient_compartment_resources).

    :param name: Required. Name of the &#x60;Patient&#x60; resource for which the information is required.
    :type name: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param count: Optional. Maximum number of resources in a page. If not specified, 100 is used. May not be larger than 1000.
    :type count: int
    :param page_token: Used to retrieve the next or previous page of results when using pagination. Set &#x60;_page_token&#x60; to the value of _page_token set in next or previous page links&#39; url. Next and previous page are returned in the response bundle&#39;s links field, where &#x60;link.relation&#x60; is \&quot;previous\&quot; or \&quot;next\&quot;. Omit &#x60;_page_token&#x60; if no previous request has been made.
    :type page_token: str
    :param since: Optional. If provided, only resources updated after this time are returned. The time uses the format YYYY-MM-DDThh:mm:ss.sss+zz:zz. For example, &#x60;2015-02-07T13:28:17.239+02:00&#x60; or &#x60;2017-01-01T00:00:00Z&#x60;. The time must be specified to the second and include a time zone.
    :type since: str
    :param type: Optional. String of comma-delimited FHIR resource types. If provided, only resources of the specified resource type(s) are returned. Specifying multiple &#x60;_type&#x60; parameters isn&#39;t supported. For example, the result of &#x60;_type&#x3D;Observation&amp;_type&#x3D;Encounter&#x60; is undefined. Use &#x60;_type&#x3D;Observation,Encounter&#x60; instead.
    :type type: str
    :param end: Optional. The response includes records prior to the end date. The date uses the format YYYY-MM-DD. If no end date is provided, all records subsequent to the start date are in scope.
    :type end: str
    :param start: Optional. The response includes records subsequent to the start date. The date uses the format YYYY-MM-DD. If no start date is provided, all records prior to the end date are in scope.
    :type start: str

    """
    return web.Response(status=200)


async def healthcare_projects_locations_datasets_fhir_stores_fhir_resource_purge(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None) -> web.Response:
    """healthcare_projects_locations_datasets_fhir_stores_fhir_resource_purge

    Deletes all the historical versions of a resource (excluding the current version) from the FHIR store. To remove all versions of a resource, first delete the current version and then call this method. This is not a FHIR standard operation. For samples that show how to call &#x60;Resource-purge&#x60;, see [Deleting historical versions of a FHIR resource](https://cloud.google.com/healthcare/docs/how-tos/fhir-resources#deleting_historical_versions_of_a_fhir_resource).

    :param name: Required. The name of the resource to purge.
    :type name: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str

    """
    return web.Response(status=200)


async def healthcare_projects_locations_datasets_fhir_stores_fhir_resource_validate(request: web.Request, parent, type, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, profile=None, body=None) -> web.Response:
    """healthcare_projects_locations_datasets_fhir_stores_fhir_resource_validate

    Validates an input FHIR resource&#39;s conformance to its profiles and the profiles configured on the FHIR store. Implements the FHIR extended operation $validate ([DSTU2](http://hl7.org/implement/standards/fhir/DSTU2/resource-operations.html#validate), [STU3](http://hl7.org/implement/standards/fhir/STU3/resource-operations.html#validate), or [R4](http://hl7.org/implement/standards/fhir/R4/resource-operation-validate.html)). The request body must contain a JSON-encoded FHIR resource, and the request headers must contain &#x60;Content-Type: application/fhir+json&#x60;. The &#x60;Parameters&#x60; input syntax is not supported. The &#x60;profile&#x60; query parameter can be used to request that the resource only be validated against a specific profile. If a profile with the given URL cannot be found in the FHIR store then an error is returned. Errors generated by validation contain a JSON-encoded &#x60;OperationOutcome&#x60; resource describing the reason for the error. If the request cannot be mapped to a valid API method on a FHIR store, a generic GCP error might be returned instead.

    :param parent: Required. The name of the FHIR store that holds the profiles being used for validation.
    :type parent: str
    :param type: Required. The FHIR resource type of the resource being validated. For a complete list, see the FHIR Resource Index ([DSTU2](http://hl7.org/implement/standards/fhir/DSTU2/resourcelist.html), [STU3](http://hl7.org/implement/standards/fhir/STU3/resourcelist.html), or [R4](http://hl7.org/implement/standards/fhir/R4/resourcelist.html)). Must match the resource type in the provided content.
    :type type: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param profile: Required. The canonical URL of a profile that this resource should be validated against. For example, to validate a Patient resource against the US Core Patient profile this parameter would be &#x60;http://hl7.org/fhir/us/core/StructureDefinition/us-core-patient&#x60;. A StructureDefinition with this canonical URL must exist in the FHIR store.
    :type profile: str
    :param body: 
    :type body: dict | bytes

    """
    body = HttpBody.from_dict(body)
    return web.Response(status=200)


async def healthcare_projects_locations_datasets_fhir_stores_fhir_search(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """healthcare_projects_locations_datasets_fhir_stores_fhir_search

    Searches for resources in the given FHIR store according to criteria specified as query parameters. Implements the FHIR standard search interaction ([DSTU2](http://hl7.org/implement/standards/fhir/DSTU2/http.html#search), [STU3](http://hl7.org/implement/standards/fhir/STU3/http.html#search), [R4](http://hl7.org/implement/standards/fhir/R4/http.html#search)) using the search semantics described in the FHIR Search specification ([DSTU2](http://hl7.org/implement/standards/fhir/DSTU2/search.html), [STU3](http://hl7.org/implement/standards/fhir/STU3/search.html), [R4](http://hl7.org/implement/standards/fhir/R4/search.html)). Supports four methods of search defined by the specification: * &#x60;GET [base]?[parameters]&#x60; to search across all resources. * &#x60;GET [base]/[type]?[parameters]&#x60; to search resources of a specified type. * &#x60;POST [base]/_search?[parameters]&#x60; as an alternate form having the same semantics as the &#x60;GET&#x60; method across all resources. * &#x60;POST [base]/[type]/_search?[parameters]&#x60; as an alternate form having the same semantics as the &#x60;GET&#x60; method for the specified type. The &#x60;GET&#x60; and &#x60;POST&#x60; methods do not support compartment searches. The &#x60;POST&#x60; method does not support &#x60;application/x-www-form-urlencoded&#x60; search parameters. On success, the response body contains a JSON-encoded representation of a &#x60;Bundle&#x60; resource of type &#x60;searchset&#x60;, containing the results of the search. Errors generated by the FHIR store contain a JSON-encoded &#x60;OperationOutcome&#x60; resource describing the reason for the error. If the request cannot be mapped to a valid API method on a FHIR store, a generic GCP error might be returned instead. The server&#39;s capability statement, retrieved through capabilities, indicates what search parameters are supported on each FHIR resource. A list of all search parameters defined by the specification can be found in the FHIR Search Parameter Registry ([STU3](http://hl7.org/implement/standards/fhir/STU3/searchparameter-registry.html), [R4](http://hl7.org/implement/standards/fhir/R4/searchparameter-registry.html)). FHIR search parameters for DSTU2 can be found on each resource&#39;s definition page. Supported search modifiers: &#x60;:missing&#x60;, &#x60;:exact&#x60;, &#x60;:contains&#x60;, &#x60;:text&#x60;, &#x60;:in&#x60;, &#x60;:not-in&#x60;, &#x60;:above&#x60;, &#x60;:below&#x60;, &#x60;:[type]&#x60;, &#x60;:not&#x60;, and &#x60;recurse&#x60; (DSTU2 and STU3) or &#x60;:iterate&#x60; (R4). Supported search result parameters: &#x60;_sort&#x60;, &#x60;_count&#x60;, &#x60;_include&#x60;, &#x60;_revinclude&#x60;, &#x60;_summary&#x3D;text&#x60;, &#x60;_summary&#x3D;data&#x60;, and &#x60;_elements&#x60;. The maximum number of search results returned defaults to 100, which can be overridden by the &#x60;_count&#x60; parameter up to a maximum limit of 1000. The server might return fewer resources than requested to prevent excessively large responses. If there are additional results, the returned &#x60;Bundle&#x60; contains a link of &#x60;relation&#x60; \&quot;next\&quot;, which has a &#x60;_page_token&#x60; parameter for an opaque pagination token that can be used to retrieve the next page. Resources with a total size larger than 5MB or a field count larger than 50,000 might not be fully searchable as the server might trim its generated search index in those cases. Note: FHIR resources are indexed asynchronously, so there might be a slight delay between the time a resource is created or changed, and the time when the change reflects in search results. The only exception is resource identifier data, which is indexed synchronously as a special index. As a result, searching using resource identifier is not subject to indexing delay. To use the special synchronous index, the search term for identifier should be in the pattern &#x60;identifier&#x3D;[system]|[value]&#x60; or &#x60;identifier&#x3D;[value]&#x60;, and any of the following search result parameters can be used: * &#x60;_count&#x60; * &#x60;_include&#x60; * &#x60;_revinclude&#x60; * &#x60;_summary&#x60; * &#x60;_elements&#x60; If your query contains any other search parameters, the standard asynchronous index will be used instead. Note that searching against the special index is optimized for resolving a small number of matches. The search isn&#39;t optimized if your identifier search criteria matches a large number (i.e. more than 2,000) of resources. For a search query that will match a large number of resources, you can avoiding using the special synchronous index by including an additional &#x60;_sort&#x60; parameter in your query. Use &#x60;_sort&#x3D;-_lastUpdated&#x60; if you want to keep the default sorting order. Note: The special synchronous identifier index are currently disabled for DocumentReference and DocumentManifest searches. For samples and detailed information, see [Searching for FHIR resources](https://cloud.google.com/healthcare/docs/how-tos/fhir-search) and [Advanced FHIR search features](https://cloud.google.com/healthcare/docs/how-tos/fhir-advanced-search).

    :param parent: Required. Name of the FHIR store to retrieve resources from.
    :type parent: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = SearchResourcesRequest.from_dict(body)
    return web.Response(status=200)


async def healthcare_projects_locations_datasets_fhir_stores_fhir_search_type(request: web.Request, parent, resource_type, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """healthcare_projects_locations_datasets_fhir_stores_fhir_search_type

    Searches for resources in the given FHIR store according to criteria specified as query parameters. Implements the FHIR standard search interaction ([DSTU2](http://hl7.org/implement/standards/fhir/DSTU2/http.html#search), [STU3](http://hl7.org/implement/standards/fhir/STU3/http.html#search), [R4](http://hl7.org/implement/standards/fhir/R4/http.html#search)) using the search semantics described in the FHIR Search specification ([DSTU2](http://hl7.org/implement/standards/fhir/DSTU2/search.html), [STU3](http://hl7.org/implement/standards/fhir/STU3/search.html), [R4](http://hl7.org/implement/standards/fhir/R4/search.html)). Supports four methods of search defined by the specification: * &#x60;GET [base]?[parameters]&#x60; to search across all resources. * &#x60;GET [base]/[type]?[parameters]&#x60; to search resources of a specified type. * &#x60;POST [base]/_search?[parameters]&#x60; as an alternate form having the same semantics as the &#x60;GET&#x60; method across all resources. * &#x60;POST [base]/[type]/_search?[parameters]&#x60; as an alternate form having the same semantics as the &#x60;GET&#x60; method for the specified type. The &#x60;GET&#x60; and &#x60;POST&#x60; methods do not support compartment searches. The &#x60;POST&#x60; method does not support &#x60;application/x-www-form-urlencoded&#x60; search parameters. On success, the response body contains a JSON-encoded representation of a &#x60;Bundle&#x60; resource of type &#x60;searchset&#x60;, containing the results of the search. Errors generated by the FHIR store contain a JSON-encoded &#x60;OperationOutcome&#x60; resource describing the reason for the error. If the request cannot be mapped to a valid API method on a FHIR store, a generic GCP error might be returned instead. The server&#39;s capability statement, retrieved through capabilities, indicates what search parameters are supported on each FHIR resource. A list of all search parameters defined by the specification can be found in the FHIR Search Parameter Registry ([STU3](http://hl7.org/implement/standards/fhir/STU3/searchparameter-registry.html), [R4](http://hl7.org/implement/standards/fhir/R4/searchparameter-registry.html)). FHIR search parameters for DSTU2 can be found on each resource&#39;s definition page. Supported search modifiers: &#x60;:missing&#x60;, &#x60;:exact&#x60;, &#x60;:contains&#x60;, &#x60;:text&#x60;, &#x60;:in&#x60;, &#x60;:not-in&#x60;, &#x60;:above&#x60;, &#x60;:below&#x60;, &#x60;:[type]&#x60;, &#x60;:not&#x60;, and &#x60;recurse&#x60; (DSTU2 and STU3) or &#x60;:iterate&#x60; (R4). Supported search result parameters: &#x60;_sort&#x60;, &#x60;_count&#x60;, &#x60;_include&#x60;, &#x60;_revinclude&#x60;, &#x60;_summary&#x3D;text&#x60;, &#x60;_summary&#x3D;data&#x60;, and &#x60;_elements&#x60;. The maximum number of search results returned defaults to 100, which can be overridden by the &#x60;_count&#x60; parameter up to a maximum limit of 1000. The server might return fewer resources than requested to prevent excessively large responses. If there are additional results, the returned &#x60;Bundle&#x60; contains a link of &#x60;relation&#x60; \&quot;next\&quot;, which has a &#x60;_page_token&#x60; parameter for an opaque pagination token that can be used to retrieve the next page. Resources with a total size larger than 5MB or a field count larger than 50,000 might not be fully searchable as the server might trim its generated search index in those cases. Note: FHIR resources are indexed asynchronously, so there might be a slight delay between the time a resource is created or changed, and the time when the change reflects in search results. The only exception is resource identifier data, which is indexed synchronously as a special index. As a result, searching using resource identifier is not subject to indexing delay. To use the special synchronous index, the search term for identifier should be in the pattern &#x60;identifier&#x3D;[system]|[value]&#x60; or &#x60;identifier&#x3D;[value]&#x60;, and any of the following search result parameters can be used: * &#x60;_count&#x60; * &#x60;_include&#x60; * &#x60;_revinclude&#x60; * &#x60;_summary&#x60; * &#x60;_elements&#x60; If your query contains any other search parameters, the standard asynchronous index will be used instead. Note that searching against the special index is optimized for resolving a small number of matches. The search isn&#39;t optimized if your identifier search criteria matches a large number (i.e. more than 2,000) of resources. For a search query that will match a large number of resources, you can avoiding using the special synchronous index by including an additional &#x60;_sort&#x60; parameter in your query. Use &#x60;_sort&#x3D;-_lastUpdated&#x60; if you want to keep the default sorting order. Note: The special synchronous identifier index are currently disabled for DocumentReference and DocumentManifest searches. For samples and detailed information, see [Searching for FHIR resources](https://cloud.google.com/healthcare/docs/how-tos/fhir-search) and [Advanced FHIR search features](https://cloud.google.com/healthcare/docs/how-tos/fhir-advanced-search).

    :param parent: Required. Name of the FHIR store to retrieve resources from.
    :type parent: str
    :param resource_type: Required. The FHIR resource type to search, such as Patient or Observation. For a complete list, see the FHIR Resource Index ([DSTU2](http://hl7.org/implement/standards/fhir/DSTU2/resourcelist.html), [STU3](http://hl7.org/implement/standards/fhir/STU3/resourcelist.html), [R4](http://hl7.org/implement/standards/fhir/R4/resourcelist.html)).
    :type resource_type: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = SearchResourcesRequest.from_dict(body)
    return web.Response(status=200)


async def healthcare_projects_locations_datasets_fhir_stores_fhir_update(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """healthcare_projects_locations_datasets_fhir_stores_fhir_update

    Updates the entire contents of a resource. Implements the FHIR standard update interaction ([DSTU2](http://hl7.org/implement/standards/fhir/DSTU2/http.html#update), [STU3](http://hl7.org/implement/standards/fhir/STU3/http.html#update), [R4](http://hl7.org/implement/standards/fhir/R4/http.html#update)). If the specified resource does not exist and the FHIR store has enable_update_create set, creates the resource with the client-specified ID. It is strongly advised not to include or encode any sensitive data such as patient identifiers in client-specified resource IDs. Those IDs are part of the FHIR resource path recorded in Cloud Audit Logs and Pub/Sub notifications. Those IDs can also be contained in reference fields within other resources. The request body must contain a JSON-encoded FHIR resource, and the request headers must contain &#x60;Content-Type: application/fhir+json&#x60;. The resource must contain an &#x60;id&#x60; element having an identical value to the ID in the REST path of the request. On success, the response body contains a JSON-encoded representation of the updated resource, including the server-assigned version ID. Errors generated by the FHIR store contain a JSON-encoded &#x60;OperationOutcome&#x60; resource describing the reason for the error. If the request cannot be mapped to a valid API method on a FHIR store, a generic GCP error might be returned instead. For samples that show how to call &#x60;update&#x60;, see [Updating a FHIR resource](https://cloud.google.com/healthcare/docs/how-tos/fhir-resources#updating_a_fhir_resource).

    :param name: Required. The name of the resource to update.
    :type name: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = HttpBody.from_dict(body)
    return web.Response(status=200)


async def healthcare_projects_locations_datasets_fhir_stores_get_fhir_store_metrics(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None) -> web.Response:
    """healthcare_projects_locations_datasets_fhir_stores_get_fhir_store_metrics

    Gets metrics associated with the FHIR store.

    :param name: Required. The resource name of the FHIR store to get metrics for.
    :type name: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str

    """
    return web.Response(status=200)


async def healthcare_projects_locations_datasets_fhir_stores_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, page_size=None, page_token=None) -> web.Response:
    """healthcare_projects_locations_datasets_fhir_stores_list

    Lists the FHIR stores in the given dataset.

    :param parent: Required. Name of the dataset.
    :type parent: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param filter: Restricts stores returned to those matching a filter. The following syntax is available: * A string field value can be written as text inside quotation marks, for example &#x60;\&quot;query text\&quot;&#x60;. The only valid relational operation for text fields is equality (&#x60;&#x3D;&#x60;), where text is searched within the field, rather than having the field be equal to the text. For example, &#x60;\&quot;Comment &#x3D; great\&quot;&#x60; returns messages with &#x60;great&#x60; in the comment field. * A number field value can be written as an integer, a decimal, or an exponential. The valid relational operators for number fields are the equality operator (&#x60;&#x3D;&#x60;), along with the less than/greater than operators (&#x60;&lt;&#x60;, &#x60;&lt;&#x3D;&#x60;, &#x60;&gt;&#x60;, &#x60;&gt;&#x3D;&#x60;). Note that there is no inequality (&#x60;!&#x3D;&#x60;) operator. You can prepend the &#x60;NOT&#x60; operator to an expression to negate it. * A date field value must be written in &#x60;yyyy-mm-dd&#x60; form. Fields with date and time use the RFC3339 time format. Leading zeros are required for one-digit months and days. The valid relational operators for date fields are the equality operator (&#x60;&#x3D;&#x60;) , along with the less than/greater than operators (&#x60;&lt;&#x60;, &#x60;&lt;&#x3D;&#x60;, &#x60;&gt;&#x60;, &#x60;&gt;&#x3D;&#x60;). Note that there is no inequality (&#x60;!&#x3D;&#x60;) operator. You can prepend the &#x60;NOT&#x60; operator to an expression to negate it. * Multiple field query expressions can be combined in one query by adding &#x60;AND&#x60; or &#x60;OR&#x60; operators between the expressions. If a boolean operator appears within a quoted string, it is not treated as special, it&#39;s just another part of the character string to be matched. You can prepend the &#x60;NOT&#x60; operator to an expression to negate it. Only filtering on labels is supported, for example &#x60;labels.key&#x3D;value&#x60;.
    :type filter: str
    :param page_size: Limit on the number of FHIR stores to return in a single response. If not specified, 100 is used. May not be larger than 1000.
    :type page_size: int
    :param page_token: The next_page_token value returned from the previous List request, if any.
    :type page_token: str

    """
    return web.Response(status=200)


async def healthcare_projects_locations_datasets_fhir_stores_rollback(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """healthcare_projects_locations_datasets_fhir_stores_rollback

    Rolls back resources from the FHIR store to the specified time. This method returns an Operation that can be used to track the status of the rollback by calling GetOperation. Immediate fatal errors appear in the error field, errors are also logged to Cloud Logging (see [Viewing error logs in Cloud Logging](https://cloud.google.com/healthcare/docs/how-tos/logging)). Otherwise, when the operation finishes, a detailed response of type RollbackFhirResourcesResponse is returned in the response field. The metadata field type for this operation is OperationMetadata.

    :param name: Required. The name of the FHIR store to rollback, in the format of \&quot;projects/{project_id}/locations/{location_id}/datasets/{dataset_id} /fhirStores/{fhir_store_id}\&quot;.
    :type name: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = RollbackFhirResourcesRequest.from_dict(body)
    return web.Response(status=200)


async def healthcare_projects_locations_datasets_hl7_v2_stores_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, hl7_v2_store_id=None, body=None) -> web.Response:
    """healthcare_projects_locations_datasets_hl7_v2_stores_create

    Creates a new HL7v2 store within the parent dataset.

    :param parent: Required. The name of the dataset this HL7v2 store belongs to.
    :type parent: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param hl7_v2_store_id: Required. The ID of the HL7v2 store that is being created. The string must match the following regex: &#x60;[\\p{L}\\p{N}_\\-\\.]{1,256}&#x60;.
    :type hl7_v2_store_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = Hl7V2Store.from_dict(body)
    return web.Response(status=200)


async def healthcare_projects_locations_datasets_hl7_v2_stores_export(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """healthcare_projects_locations_datasets_hl7_v2_stores_export

    Exports the messages to a destination. To filter messages to be exported, define a filter using the start and end time, relative to the message generation time (MSH.7). This API returns an Operation that can be used to track the status of the job by calling GetOperation. Immediate fatal errors appear in the error field. Otherwise, when the operation finishes, a detailed response of type ExportMessagesResponse is returned in the response field. The metadata field type for this operation is OperationMetadata.

    :param name: Required. The name of the source HL7v2 store, in the format &#x60;projects/{project_id}/locations/{location_id}/datasets/{dataset_id}/hl7v2Stores/{hl7v2_store_id}&#x60;
    :type name: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = ExportMessagesRequest.from_dict(body)
    return web.Response(status=200)


async def healthcare_projects_locations_datasets_hl7_v2_stores_get_hl7v2_store_metrics(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None) -> web.Response:
    """healthcare_projects_locations_datasets_hl7_v2_stores_get_hl7v2_store_metrics

    Gets metrics associated with the HL7v2 store.

    :param name: Required. The resource name of the HL7v2 store to get metrics for, in the format &#x60;projects/{project_id}/locations/{location_id}/datasets/{dataset_id}/hl7V2Stores/{hl7v2_store_id}&#x60;.
    :type name: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str

    """
    return web.Response(status=200)


async def healthcare_projects_locations_datasets_hl7_v2_stores_get_iam_policy(request: web.Request, resource, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, options_requested_policy_version=None) -> web.Response:
    """healthcare_projects_locations_datasets_hl7_v2_stores_get_iam_policy

    Gets the access control policy for a resource. Returns an empty policy if the resource exists and does not have a policy set.

    :param resource: REQUIRED: The resource for which the policy is being requested. See [Resource names](https://cloud.google.com/apis/design/resource_names) for the appropriate value for this field.
    :type resource: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param options_requested_policy_version: Optional. The maximum policy version that will be used to format the policy. Valid values are 0, 1, and 3. Requests specifying an invalid value will be rejected. Requests for policies with any conditional role bindings must specify version 3. Policies with no conditional role bindings may specify any valid value or leave the field unset. The policy in the response might use the policy version that you specified, or it might use a lower policy version. For example, if you specify version 3, but the policy has no conditional role bindings, the response uses version 1. To learn which resources support conditions in their IAM policies, see the [IAM documentation](https://cloud.google.com/iam/help/conditions/resource-policies).
    :type options_requested_policy_version: int

    """
    return web.Response(status=200)


async def healthcare_projects_locations_datasets_hl7_v2_stores_import(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """healthcare_projects_locations_datasets_hl7_v2_stores_import

    Import messages to the HL7v2 store by loading data from the specified sources. This method is optimized to load large quantities of data using import semantics that ignore some HL7v2 store configuration options and are not suitable for all use cases. It is primarily intended to load data into an empty HL7v2 store that is not being used by other clients. An existing message will be overwritten if a duplicate message is imported. A duplicate message is a message with the same raw bytes as a message that already exists in this HL7v2 store. When a message is overwritten, its labels will also be overwritten. The import operation is idempotent unless the input data contains multiple valid messages with the same raw bytes but different labels. In that case, after the import completes, the store contains exactly one message with those raw bytes but there is no ordering guarantee on which version of the labels it has. The operation result counters do not count duplicated raw bytes as an error and count one success for each message in the input, which might result in a success count larger than the number of messages in the HL7v2 store. If some messages fail to import, for example due to parsing errors, successfully imported messages are not rolled back. This method returns an Operation that can be used to track the status of the import by calling GetOperation. Immediate fatal errors appear in the error field, errors are also logged to Cloud Logging (see [Viewing error logs in Cloud Logging](https://cloud.google.com/healthcare/docs/how-tos/logging)). Otherwise, when the operation finishes, a response of type ImportMessagesResponse is returned in the response field. The metadata field type for this operation is OperationMetadata.

    :param name: Required. The name of the target HL7v2 store, in the format &#x60;projects/{project_id}/locations/{location_id}/datasets/{dataset_id}/hl7v2Stores/{hl7v2_store_id}&#x60;
    :type name: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = ImportMessagesRequest.from_dict(body)
    return web.Response(status=200)


async def healthcare_projects_locations_datasets_hl7_v2_stores_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, page_size=None, page_token=None) -> web.Response:
    """healthcare_projects_locations_datasets_hl7_v2_stores_list

    Lists the HL7v2 stores in the given dataset.

    :param parent: Required. Name of the dataset.
    :type parent: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param filter: Restricts stores returned to those matching a filter. The following syntax is available: * A string field value can be written as text inside quotation marks, for example &#x60;\&quot;query text\&quot;&#x60;. The only valid relational operation for text fields is equality (&#x60;&#x3D;&#x60;), where text is searched within the field, rather than having the field be equal to the text. For example, &#x60;\&quot;Comment &#x3D; great\&quot;&#x60; returns messages with &#x60;great&#x60; in the comment field. * A number field value can be written as an integer, a decimal, or an exponential. The valid relational operators for number fields are the equality operator (&#x60;&#x3D;&#x60;), along with the less than/greater than operators (&#x60;&lt;&#x60;, &#x60;&lt;&#x3D;&#x60;, &#x60;&gt;&#x60;, &#x60;&gt;&#x3D;&#x60;). Note that there is no inequality (&#x60;!&#x3D;&#x60;) operator. You can prepend the &#x60;NOT&#x60; operator to an expression to negate it. * A date field value must be written in &#x60;yyyy-mm-dd&#x60; form. Fields with date and time use the RFC3339 time format. Leading zeros are required for one-digit months and days. The valid relational operators for date fields are the equality operator (&#x60;&#x3D;&#x60;) , along with the less than/greater than operators (&#x60;&lt;&#x60;, &#x60;&lt;&#x3D;&#x60;, &#x60;&gt;&#x60;, &#x60;&gt;&#x3D;&#x60;). Note that there is no inequality (&#x60;!&#x3D;&#x60;) operator. You can prepend the &#x60;NOT&#x60; operator to an expression to negate it. * Multiple field query expressions can be combined in one query by adding &#x60;AND&#x60; or &#x60;OR&#x60; operators between the expressions. If a boolean operator appears within a quoted string, it is not treated as special, it&#39;s just another part of the character string to be matched. You can prepend the &#x60;NOT&#x60; operator to an expression to negate it. Only filtering on labels is supported. For example, &#x60;labels.key&#x3D;value&#x60;.
    :type filter: str
    :param page_size: Limit on the number of HL7v2 stores to return in a single response. If not specified, 100 is used. May not be larger than 1000.
    :type page_size: int
    :param page_token: The next_page_token value returned from the previous List request, if any.
    :type page_token: str

    """
    return web.Response(status=200)


async def healthcare_projects_locations_datasets_hl7_v2_stores_messages_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """healthcare_projects_locations_datasets_hl7_v2_stores_messages_create

    Parses and stores an HL7v2 message. This method triggers an asynchronous notification to any Pub/Sub topic configured in Hl7V2Store.Hl7V2NotificationConfig, if the filtering matches the message. If an MLLP adapter is configured to listen to a Pub/Sub topic, the adapter transmits the message when a notification is received.

    :param parent: Required. The name of the HL7v2 store this message belongs to.
    :type parent: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateMessageRequest.from_dict(body)
    return web.Response(status=200)


async def healthcare_projects_locations_datasets_hl7_v2_stores_messages_delete(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None) -> web.Response:
    """healthcare_projects_locations_datasets_hl7_v2_stores_messages_delete

    Deletes an HL7v2 message.

    :param name: Required. The resource name of the HL7v2 message to delete.
    :type name: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str

    """
    return web.Response(status=200)


async def healthcare_projects_locations_datasets_hl7_v2_stores_messages_ingest(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """healthcare_projects_locations_datasets_hl7_v2_stores_messages_ingest

    Parses and stores an HL7v2 message. This method triggers an asynchronous notification to any Pub/Sub topic configured in Hl7V2Store.Hl7V2NotificationConfig, if the filtering matches the message. If an MLLP adapter is configured to listen to a Pub/Sub topic, the adapter transmits the message when a notification is received. If the method is successful, it generates a response containing an HL7v2 acknowledgment (&#x60;ACK&#x60;) message. If the method encounters an error, it returns a negative acknowledgment (&#x60;NACK&#x60;) message. This behavior is suitable for replying to HL7v2 interface systems that expect these acknowledgments.

    :param parent: Required. The name of the HL7v2 store this message belongs to.
    :type parent: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = IngestMessageRequest.from_dict(body)
    return web.Response(status=200)


async def healthcare_projects_locations_datasets_hl7_v2_stores_messages_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, order_by=None, page_size=None, page_token=None, view=None) -> web.Response:
    """healthcare_projects_locations_datasets_hl7_v2_stores_messages_list

    Lists all the messages in the given HL7v2 store with support for filtering. Note: HL7v2 messages are indexed asynchronously, so there might be a slight delay between the time a message is created and when it can be found through a filter.

    :param parent: Required. Name of the HL7v2 store to retrieve messages from.
    :type parent: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param filter: Restricts messages returned to those matching a filter. The following syntax is available: * A string field value can be written as text inside quotation marks, for example &#x60;\&quot;query text\&quot;&#x60;. The only valid relational operation for text fields is equality (&#x60;&#x3D;&#x60;), where text is searched within the field, rather than having the field be equal to the text. For example, &#x60;\&quot;Comment &#x3D; great\&quot;&#x60; returns messages with &#x60;great&#x60; in the comment field. * A number field value can be written as an integer, a decimal, or an exponential. The valid relational operators for number fields are the equality operator (&#x60;&#x3D;&#x60;), along with the less than/greater than operators (&#x60;&lt;&#x60;, &#x60;&lt;&#x3D;&#x60;, &#x60;&gt;&#x60;, &#x60;&gt;&#x3D;&#x60;). Note that there is no inequality (&#x60;!&#x3D;&#x60;) operator. You can prepend the &#x60;NOT&#x60; operator to an expression to negate it. * A date field value must be written in &#x60;yyyy-mm-dd&#x60; form. Fields with date and time use the RFC3339 time format. Leading zeros are required for one-digit months and days. The valid relational operators for date fields are the equality operator (&#x60;&#x3D;&#x60;) , along with the less than/greater than operators (&#x60;&lt;&#x60;, &#x60;&lt;&#x3D;&#x60;, &#x60;&gt;&#x60;, &#x60;&gt;&#x3D;&#x60;). Note that there is no inequality (&#x60;!&#x3D;&#x60;) operator. You can prepend the &#x60;NOT&#x60; operator to an expression to negate it. * Multiple field query expressions can be combined in one query by adding &#x60;AND&#x60; or &#x60;OR&#x60; operators between the expressions. If a boolean operator appears within a quoted string, it is not treated as special, it&#39;s just another part of the character string to be matched. You can prepend the &#x60;NOT&#x60; operator to an expression to negate it. Fields/functions available for filtering are: * &#x60;message_type&#x60;, from the MSH-9.1 field. For example, &#x60;NOT message_type &#x3D; \&quot;ADT\&quot;&#x60;. * &#x60;send_date&#x60; or &#x60;sendDate&#x60;, the YYYY-MM-DD date the message was sent in the dataset&#39;s time_zone, from the MSH-7 segment. For example, &#x60;send_date &lt; \&quot;2017-01-02\&quot;&#x60;. * &#x60;send_time&#x60;, the timestamp when the message was sent, using the RFC3339 time format for comparisons, from the MSH-7 segment. For example, &#x60;send_time &lt; \&quot;2017-01-02T00:00:00-05:00\&quot;&#x60;. * &#x60;create_time&#x60;, the timestamp when the message was created in the HL7v2 store. Use the RFC3339 time format for comparisons. For example, &#x60;create_time &lt; \&quot;2017-01-02T00:00:00-05:00\&quot;&#x60;. * &#x60;send_facility&#x60;, the care center that the message came from, from the MSH-4 segment. For example, &#x60;send_facility &#x3D; \&quot;ABC\&quot;&#x60;. * &#x60;PatientId(value, type)&#x60;, which matches if the message lists a patient having an ID of the given value and type in the PID-2, PID-3, or PID-4 segments. For example, &#x60;PatientId(\&quot;123456\&quot;, \&quot;MRN\&quot;)&#x60;. * &#x60;labels.x&#x60;, a string value of the label with key &#x60;x&#x60; as set using the Message.labels map. For example, &#x60;labels.\&quot;priority\&quot;&#x3D;\&quot;high\&quot;&#x60;. The operator &#x60;:*&#x60; can be used to assert the existence of a label. For example, &#x60;labels.\&quot;priority\&quot;:*&#x60;.
    :type filter: str
    :param order_by: Orders messages returned by the specified order_by clause. Syntax: https://cloud.google.com/apis/design/design_patterns#sorting_order Fields available for ordering are: * &#x60;send_time&#x60;
    :type order_by: str
    :param page_size: Limit on the number of messages to return in a single response. If not specified, 100 is used. May not be larger than 1000.
    :type page_size: int
    :param page_token: The next_page_token value returned from the previous List request, if any.
    :type page_token: str
    :param view: Specifies the parts of the Message to return in the response. When unspecified, equivalent to BASIC. Setting this to anything other than BASIC with a &#x60;page_size&#x60; larger than the default can generate a large response, which impacts the performance of this method.
    :type view: str

    """
    return web.Response(status=200)


async def healthcare_projects_locations_datasets_hl7_v2_stores_messages_patch(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, update_mask=None, body=None) -> web.Response:
    """healthcare_projects_locations_datasets_hl7_v2_stores_messages_patch

    Update the message. The contents of the message in Message.data and data extracted from the contents such as Message.create_time cannot be altered. Only the Message.labels field is allowed to be updated. The labels in the request are merged with the existing set of labels. Existing labels with the same keys are updated.

    :param name: Output only. Resource name of the Message, of the form &#x60;projects/{project_id}/locations/{location_id}/datasets/{dataset_id}/hl7V2Stores/{hl7_v2_store_id}/messages/{message_id}&#x60;. Assigned by the server.
    :type name: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param update_mask: Required. The update mask applies to the resource. For the &#x60;FieldMask&#x60; definition, see https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#fieldmask
    :type update_mask: str
    :param body: 
    :type body: dict | bytes

    """
    body = Message.from_dict(body)
    return web.Response(status=200)


async def healthcare_projects_locations_datasets_hl7_v2_stores_set_iam_policy(request: web.Request, resource, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """healthcare_projects_locations_datasets_hl7_v2_stores_set_iam_policy

    Sets the access control policy on the specified resource. Replaces any existing policy. Can return &#x60;NOT_FOUND&#x60;, &#x60;INVALID_ARGUMENT&#x60;, and &#x60;PERMISSION_DENIED&#x60; errors.

    :param resource: REQUIRED: The resource for which the policy is being specified. See [Resource names](https://cloud.google.com/apis/design/resource_names) for the appropriate value for this field.
    :type resource: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = SetIamPolicyRequest.from_dict(body)
    return web.Response(status=200)


async def healthcare_projects_locations_datasets_hl7_v2_stores_test_iam_permissions(request: web.Request, resource, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """healthcare_projects_locations_datasets_hl7_v2_stores_test_iam_permissions

    Returns permissions that a caller has on the specified resource. If the resource does not exist, this will return an empty set of permissions, not a &#x60;NOT_FOUND&#x60; error. Note: This operation is designed to be used for building permission-aware UIs and command-line tools, not for authorization checking. This operation may \&quot;fail open\&quot; without warning.

    :param resource: REQUIRED: The resource for which the policy detail is being requested. See [Resource names](https://cloud.google.com/apis/design/resource_names) for the appropriate value for this field.
    :type resource: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = TestIamPermissionsRequest.from_dict(body)
    return web.Response(status=200)


async def healthcare_projects_locations_datasets_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, page_size=None, page_token=None) -> web.Response:
    """healthcare_projects_locations_datasets_list

    Lists the health datasets in the current project.

    :param parent: Required. The name of the project whose datasets should be listed. For example, &#x60;projects/{project_id}/locations/{location_id}&#x60;.
    :type parent: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param page_size: The maximum number of items to return. If not specified, 100 is used. May not be larger than 1000.
    :type page_size: int
    :param page_token: The next_page_token value returned from a previous List request, if any.
    :type page_token: str

    """
    return web.Response(status=200)


async def healthcare_projects_locations_datasets_operations_cancel(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """healthcare_projects_locations_datasets_operations_cancel

    Starts asynchronous cancellation on a long-running operation. The server makes a best effort to cancel the operation, but success is not guaranteed. If the server doesn&#39;t support this method, it returns &#x60;google.rpc.Code.UNIMPLEMENTED&#x60;. Clients can use Operations.GetOperation or other methods to check whether the cancellation succeeded or whether the operation completed despite cancellation. On successful cancellation, the operation is not deleted; instead, it becomes an operation with an Operation.error value with a google.rpc.Status.code of 1, corresponding to &#x60;Code.CANCELLED&#x60;.

    :param name: The name of the operation resource to be cancelled.
    :type name: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param body: 
    :type body: 

    """
    return web.Response(status=200)


async def healthcare_projects_locations_datasets_operations_get(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, view=None) -> web.Response:
    """healthcare_projects_locations_datasets_operations_get

    Gets the latest state of a long-running operation. Clients can use this method to poll the operation result at intervals as recommended by the API service.

    :param name: The name of the operation resource.
    :type name: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param view: Specifies which parts of the Message resource to return in the response. When unspecified, equivalent to FULL.
    :type view: str

    """
    return web.Response(status=200)


async def healthcare_projects_locations_datasets_operations_list(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, page_size=None, page_token=None) -> web.Response:
    """healthcare_projects_locations_datasets_operations_list

    Lists operations that match the specified filter in the request. If the server doesn&#39;t support this method, it returns &#x60;UNIMPLEMENTED&#x60;.

    :param name: The name of the operation&#39;s parent resource.
    :type name: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param filter: The standard list filter.
    :type filter: str
    :param page_size: The standard list page size.
    :type page_size: int
    :param page_token: The standard list page token.
    :type page_token: str

    """
    return web.Response(status=200)


async def healthcare_projects_locations_list(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, page_size=None, page_token=None) -> web.Response:
    """healthcare_projects_locations_list

    Lists information about the supported locations for this service.

    :param name: The resource that owns the locations collection, if applicable.
    :type name: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param filter: A filter to narrow down results to a preferred subset. The filtering language accepts strings like &#x60;\&quot;displayName&#x3D;tokyo\&quot;&#x60;, and is documented in more detail in [AIP-160](https://google.aip.dev/160).
    :type filter: str
    :param page_size: The maximum number of results to return. If not set, the service selects a default.
    :type page_size: int
    :param page_token: A page token received from the &#x60;next_page_token&#x60; field in the response. Send that page token to receive the subsequent page.
    :type page_token: str

    """
    return web.Response(status=200)


async def healthcare_projects_locations_services_nlp_analyze_entities(request: web.Request, nlp_service, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """healthcare_projects_locations_services_nlp_analyze_entities

    Analyze heathcare entity in a document. Its response includes the recognized entity mentions and the relationships between them. AnalyzeEntities uses context aware models to detect entities.

    :param nlp_service: The resource name of the service of the form: \&quot;projects/{project_id}/locations/{location_id}/services/nlp\&quot;.
    :type nlp_service: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = AnalyzeEntitiesRequest.from_dict(body)
    return web.Response(status=200)
