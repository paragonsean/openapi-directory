from typing import List, Dict
from aiohttp import web

from openapi_server.models.google_firestore_admin_v1beta2_export_documents_request import GoogleFirestoreAdminV1beta2ExportDocumentsRequest
from openapi_server.models.google_firestore_admin_v1beta2_field import GoogleFirestoreAdminV1beta2Field
from openapi_server.models.google_firestore_admin_v1beta2_import_documents_request import GoogleFirestoreAdminV1beta2ImportDocumentsRequest
from openapi_server.models.google_firestore_admin_v1beta2_index import GoogleFirestoreAdminV1beta2Index
from openapi_server.models.google_firestore_admin_v1beta2_list_fields_response import GoogleFirestoreAdminV1beta2ListFieldsResponse
from openapi_server.models.google_firestore_admin_v1beta2_list_indexes_response import GoogleFirestoreAdminV1beta2ListIndexesResponse
from openapi_server.models.google_longrunning_operation import GoogleLongrunningOperation
from openapi_server import util


async def firestore_projects_databases_collection_groups_fields_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, page_size=None, page_token=None) -> web.Response:
    """firestore_projects_databases_collection_groups_fields_list

    Lists the field configuration and metadata for this database. Currently, FirestoreAdmin.ListFields only supports listing fields that have been explicitly overridden. To issue this query, call FirestoreAdmin.ListFields with the filter set to &#x60;indexConfig.usesAncestorConfig:false&#x60;.

    :param parent: A parent name of the form &#x60;projects/{project_id}/databases/{database_id}/collectionGroups/{collection_id}&#x60;
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
    :param filter: The filter to apply to list results. Currently, FirestoreAdmin.ListFields only supports listing fields that have been explicitly overridden. To issue this query, call FirestoreAdmin.ListFields with the filter set to &#x60;indexConfig.usesAncestorConfig:false&#x60;.
    :type filter: str
    :param page_size: The number of results to return.
    :type page_size: int
    :param page_token: A page token, returned from a previous call to FirestoreAdmin.ListFields, that may be used to get the next page of results.
    :type page_token: str

    """
    return web.Response(status=200)


async def firestore_projects_databases_collection_groups_fields_patch(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, update_mask=None, body=None) -> web.Response:
    """firestore_projects_databases_collection_groups_fields_patch

    Updates a field configuration. Currently, field updates apply only to single field index configuration. However, calls to FirestoreAdmin.UpdateField should provide a field mask to avoid changing any configuration that the caller isn&#39;t aware of. The field mask should be specified as: &#x60;{ paths: \&quot;index_config\&quot; }&#x60;. This call returns a google.longrunning.Operation which may be used to track the status of the field update. The metadata for the operation will be the type FieldOperationMetadata. To configure the default field settings for the database, use the special &#x60;Field&#x60; with resource name: &#x60;projects/{project_id}/databases/{database_id}/collectionGroups/__default__/fields/*&#x60;.

    :param name: A field name of the form &#x60;projects/{project_id}/databases/{database_id}/collectionGroups/{collection_id}/fields/{field_path}&#x60; A field path may be a simple field name, e.g. &#x60;address&#x60; or a path to fields within map_value , e.g. &#x60;address.city&#x60;, or a special field path. The only valid special field is &#x60;*&#x60;, which represents any field. Field paths may be quoted using &#x60; (backtick). The only character that needs to be escaped within a quoted field path is the backtick character itself, escaped using a backslash. Special characters in field paths that must be quoted include: &#x60;*&#x60;, &#x60;.&#x60;, &#x60;&#x60;&#x60; (backtick), &#x60;[&#x60;, &#x60;]&#x60;, as well as any ascii symbolic characters. Examples: (Note: Comments here are written in markdown syntax, so there is an additional layer of backticks to represent a code block) &#x60;\\&#x60;address.city\\&#x60;&#x60; represents a field named &#x60;address.city&#x60;, not the map key &#x60;city&#x60; in the field &#x60;address&#x60;. &#x60;\\&#x60;*\\&#x60;&#x60; represents a field named &#x60;*&#x60;, not any field. A special &#x60;Field&#x60; contains the default indexing settings for all fields. This field&#39;s resource name is: &#x60;projects/{project_id}/databases/{database_id}/collectionGroups/__default__/fields/*&#x60; Indexes defined on this &#x60;Field&#x60; will be applied to all fields which do not have their own &#x60;Field&#x60; index configuration.
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
    :param update_mask: A mask, relative to the field. If specified, only configuration specified by this field_mask will be updated in the field.
    :type update_mask: str
    :param body: 
    :type body: dict | bytes

    """
    body = GoogleFirestoreAdminV1beta2Field.from_dict(body)
    return web.Response(status=200)


async def firestore_projects_databases_collection_groups_indexes_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """firestore_projects_databases_collection_groups_indexes_create

    Creates a composite index. This returns a google.longrunning.Operation which may be used to track the status of the creation. The metadata for the operation will be the type IndexOperationMetadata.

    :param parent: A parent name of the form &#x60;projects/{project_id}/databases/{database_id}/collectionGroups/{collection_id}&#x60;
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
    body = GoogleFirestoreAdminV1beta2Index.from_dict(body)
    return web.Response(status=200)


async def firestore_projects_databases_collection_groups_indexes_delete(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None) -> web.Response:
    """firestore_projects_databases_collection_groups_indexes_delete

    Deletes a composite index.

    :param name: A name of the form &#x60;projects/{project_id}/databases/{database_id}/collectionGroups/{collection_id}/indexes/{index_id}&#x60;
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


async def firestore_projects_databases_collection_groups_indexes_get(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None) -> web.Response:
    """firestore_projects_databases_collection_groups_indexes_get

    Gets a composite index.

    :param name: A name of the form &#x60;projects/{project_id}/databases/{database_id}/collectionGroups/{collection_id}/indexes/{index_id}&#x60;
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


async def firestore_projects_databases_collection_groups_indexes_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, page_size=None, page_token=None) -> web.Response:
    """firestore_projects_databases_collection_groups_indexes_list

    Lists composite indexes.

    :param parent: A parent name of the form &#x60;projects/{project_id}/databases/{database_id}/collectionGroups/{collection_id}&#x60;
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
    :param filter: The filter to apply to list results.
    :type filter: str
    :param page_size: The number of results to return.
    :type page_size: int
    :param page_token: A page token, returned from a previous call to FirestoreAdmin.ListIndexes, that may be used to get the next page of results.
    :type page_token: str

    """
    return web.Response(status=200)


async def firestore_projects_databases_export_documents(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """firestore_projects_databases_export_documents

    Exports a copy of all or a subset of documents from Google Cloud Firestore to another storage system, such as Google Cloud Storage. Recent updates to documents may not be reflected in the export. The export occurs in the background and its progress can be monitored and managed via the Operation resource that is created. The output of an export may only be used once the associated operation is done. If an export operation is cancelled before completion it may leave partial data behind in Google Cloud Storage.

    :param name: Database to export. Should be of the form: &#x60;projects/{project_id}/databases/{database_id}&#x60;.
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
    body = GoogleFirestoreAdminV1beta2ExportDocumentsRequest.from_dict(body)
    return web.Response(status=200)


async def firestore_projects_databases_import_documents(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """firestore_projects_databases_import_documents

    Imports documents into Google Cloud Firestore. Existing documents with the same name are overwritten. The import occurs in the background and its progress can be monitored and managed via the Operation resource that is created. If an ImportDocuments operation is cancelled, it is possible that a subset of the data has already been imported to Cloud Firestore.

    :param name: Database to import into. Should be of the form: &#x60;projects/{project_id}/databases/{database_id}&#x60;.
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
    body = GoogleFirestoreAdminV1beta2ImportDocumentsRequest.from_dict(body)
    return web.Response(status=200)
