# CloudFirestoreApi.ProjectsApi

All URIs are relative to *https://firestore.googleapis.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**firestoreProjectsDatabasesCollectionGroupsFieldsList**](ProjectsApi.md#firestoreProjectsDatabasesCollectionGroupsFieldsList) | **GET** /v1beta2/{parent}/fields | 
[**firestoreProjectsDatabasesCollectionGroupsFieldsPatch**](ProjectsApi.md#firestoreProjectsDatabasesCollectionGroupsFieldsPatch) | **PATCH** /v1beta2/{name} | 
[**firestoreProjectsDatabasesCollectionGroupsIndexesCreate**](ProjectsApi.md#firestoreProjectsDatabasesCollectionGroupsIndexesCreate) | **POST** /v1beta2/{parent}/indexes | 
[**firestoreProjectsDatabasesCollectionGroupsIndexesDelete**](ProjectsApi.md#firestoreProjectsDatabasesCollectionGroupsIndexesDelete) | **DELETE** /v1beta2/{name} | 
[**firestoreProjectsDatabasesCollectionGroupsIndexesGet**](ProjectsApi.md#firestoreProjectsDatabasesCollectionGroupsIndexesGet) | **GET** /v1beta2/{name} | 
[**firestoreProjectsDatabasesCollectionGroupsIndexesList**](ProjectsApi.md#firestoreProjectsDatabasesCollectionGroupsIndexesList) | **GET** /v1beta2/{parent}/indexes | 
[**firestoreProjectsDatabasesExportDocuments**](ProjectsApi.md#firestoreProjectsDatabasesExportDocuments) | **POST** /v1beta2/{name}:exportDocuments | 
[**firestoreProjectsDatabasesImportDocuments**](ProjectsApi.md#firestoreProjectsDatabasesImportDocuments) | **POST** /v1beta2/{name}:importDocuments | 



## firestoreProjectsDatabasesCollectionGroupsFieldsList

> GoogleFirestoreAdminV1beta2ListFieldsResponse firestoreProjectsDatabasesCollectionGroupsFieldsList(parent, opts)



Lists the field configuration and metadata for this database. Currently, FirestoreAdmin.ListFields only supports listing fields that have been explicitly overridden. To issue this query, call FirestoreAdmin.ListFields with the filter set to &#x60;indexConfig.usesAncestorConfig:false&#x60;.

### Example

```javascript
import CloudFirestoreApi from 'cloud_firestore_api';
let defaultClient = CloudFirestoreApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CloudFirestoreApi.ProjectsApi();
let parent = "parent_example"; // String | A parent name of the form `projects/{project_id}/databases/{database_id}/collectionGroups/{collection_id}`
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'filter': "filter_example", // String | The filter to apply to list results. Currently, FirestoreAdmin.ListFields only supports listing fields that have been explicitly overridden. To issue this query, call FirestoreAdmin.ListFields with the filter set to `indexConfig.usesAncestorConfig:false`.
  'pageSize': 56, // Number | The number of results to return.
  'pageToken': "pageToken_example" // String | A page token, returned from a previous call to FirestoreAdmin.ListFields, that may be used to get the next page of results.
};
apiInstance.firestoreProjectsDatabasesCollectionGroupsFieldsList(parent, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent** | **String**| A parent name of the form &#x60;projects/{project_id}/databases/{database_id}/collectionGroups/{collection_id}&#x60; | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **filter** | **String**| The filter to apply to list results. Currently, FirestoreAdmin.ListFields only supports listing fields that have been explicitly overridden. To issue this query, call FirestoreAdmin.ListFields with the filter set to &#x60;indexConfig.usesAncestorConfig:false&#x60;. | [optional] 
 **pageSize** | **Number**| The number of results to return. | [optional] 
 **pageToken** | **String**| A page token, returned from a previous call to FirestoreAdmin.ListFields, that may be used to get the next page of results. | [optional] 

### Return type

[**GoogleFirestoreAdminV1beta2ListFieldsResponse**](GoogleFirestoreAdminV1beta2ListFieldsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## firestoreProjectsDatabasesCollectionGroupsFieldsPatch

> GoogleLongrunningOperation firestoreProjectsDatabasesCollectionGroupsFieldsPatch(name, opts)



Updates a field configuration. Currently, field updates apply only to single field index configuration. However, calls to FirestoreAdmin.UpdateField should provide a field mask to avoid changing any configuration that the caller isn&#39;t aware of. The field mask should be specified as: &#x60;{ paths: \&quot;index_config\&quot; }&#x60;. This call returns a google.longrunning.Operation which may be used to track the status of the field update. The metadata for the operation will be the type FieldOperationMetadata. To configure the default field settings for the database, use the special &#x60;Field&#x60; with resource name: &#x60;projects/{project_id}/databases/{database_id}/collectionGroups/__default__/fields/_*&#x60;.

### Example

```javascript
import CloudFirestoreApi from 'cloud_firestore_api';
let defaultClient = CloudFirestoreApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CloudFirestoreApi.ProjectsApi();
let name = "name_example"; // String | A field name of the form `projects/{project_id}/databases/{database_id}/collectionGroups/{collection_id}/fields/{field_path}` A field path may be a simple field name, e.g. `address` or a path to fields within map_value , e.g. `address.city`, or a special field path. The only valid special field is `*`, which represents any field. Field paths may be quoted using ` (backtick). The only character that needs to be escaped within a quoted field path is the backtick character itself, escaped using a backslash. Special characters in field paths that must be quoted include: `*`, `.`, ``` (backtick), `[`, `]`, as well as any ascii symbolic characters. Examples: (Note: Comments here are written in markdown syntax, so there is an additional layer of backticks to represent a code block) `\\`address.city\\`` represents a field named `address.city`, not the map key `city` in the field `address`. `\\`*\\`` represents a field named `*`, not any field. A special `Field` contains the default indexing settings for all fields. This field's resource name is: `projects/{project_id}/databases/{database_id}/collectionGroups/__default__/fields/_*` Indexes defined on this `Field` will be applied to all fields which do not have their own `Field` index configuration.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'updateMask': "updateMask_example", // String | A mask, relative to the field. If specified, only configuration specified by this field_mask will be updated in the field.
  'googleFirestoreAdminV1beta2Field': new CloudFirestoreApi.GoogleFirestoreAdminV1beta2Field() // GoogleFirestoreAdminV1beta2Field | 
};
apiInstance.firestoreProjectsDatabasesCollectionGroupsFieldsPatch(name, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **String**| A field name of the form &#x60;projects/{project_id}/databases/{database_id}/collectionGroups/{collection_id}/fields/{field_path}&#x60; A field path may be a simple field name, e.g. &#x60;address&#x60; or a path to fields within map_value , e.g. &#x60;address.city&#x60;, or a special field path. The only valid special field is &#x60;*&#x60;, which represents any field. Field paths may be quoted using &#x60; (backtick). The only character that needs to be escaped within a quoted field path is the backtick character itself, escaped using a backslash. Special characters in field paths that must be quoted include: &#x60;*&#x60;, &#x60;.&#x60;, &#x60;&#x60;&#x60; (backtick), &#x60;[&#x60;, &#x60;]&#x60;, as well as any ascii symbolic characters. Examples: (Note: Comments here are written in markdown syntax, so there is an additional layer of backticks to represent a code block) &#x60;\\&#x60;address.city\\&#x60;&#x60; represents a field named &#x60;address.city&#x60;, not the map key &#x60;city&#x60; in the field &#x60;address&#x60;. &#x60;\\&#x60;*\\&#x60;&#x60; represents a field named &#x60;*&#x60;, not any field. A special &#x60;Field&#x60; contains the default indexing settings for all fields. This field&#39;s resource name is: &#x60;projects/{project_id}/databases/{database_id}/collectionGroups/__default__/fields/_*&#x60; Indexes defined on this &#x60;Field&#x60; will be applied to all fields which do not have their own &#x60;Field&#x60; index configuration. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **updateMask** | **String**| A mask, relative to the field. If specified, only configuration specified by this field_mask will be updated in the field. | [optional] 
 **googleFirestoreAdminV1beta2Field** | [**GoogleFirestoreAdminV1beta2Field**](GoogleFirestoreAdminV1beta2Field.md)|  | [optional] 

### Return type

[**GoogleLongrunningOperation**](GoogleLongrunningOperation.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## firestoreProjectsDatabasesCollectionGroupsIndexesCreate

> GoogleLongrunningOperation firestoreProjectsDatabasesCollectionGroupsIndexesCreate(parent, opts)



Creates a composite index. This returns a google.longrunning.Operation which may be used to track the status of the creation. The metadata for the operation will be the type IndexOperationMetadata.

### Example

```javascript
import CloudFirestoreApi from 'cloud_firestore_api';
let defaultClient = CloudFirestoreApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CloudFirestoreApi.ProjectsApi();
let parent = "parent_example"; // String | A parent name of the form `projects/{project_id}/databases/{database_id}/collectionGroups/{collection_id}`
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'googleFirestoreAdminV1beta2Index': new CloudFirestoreApi.GoogleFirestoreAdminV1beta2Index() // GoogleFirestoreAdminV1beta2Index | 
};
apiInstance.firestoreProjectsDatabasesCollectionGroupsIndexesCreate(parent, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent** | **String**| A parent name of the form &#x60;projects/{project_id}/databases/{database_id}/collectionGroups/{collection_id}&#x60; | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **googleFirestoreAdminV1beta2Index** | [**GoogleFirestoreAdminV1beta2Index**](GoogleFirestoreAdminV1beta2Index.md)|  | [optional] 

### Return type

[**GoogleLongrunningOperation**](GoogleLongrunningOperation.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## firestoreProjectsDatabasesCollectionGroupsIndexesDelete

> Object firestoreProjectsDatabasesCollectionGroupsIndexesDelete(name, opts)



Deletes a composite index.

### Example

```javascript
import CloudFirestoreApi from 'cloud_firestore_api';
let defaultClient = CloudFirestoreApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CloudFirestoreApi.ProjectsApi();
let name = "name_example"; // String | A name of the form `projects/{project_id}/databases/{database_id}/collectionGroups/{collection_id}/indexes/{index_id}`
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example" // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
};
apiInstance.firestoreProjectsDatabasesCollectionGroupsIndexesDelete(name, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **String**| A name of the form &#x60;projects/{project_id}/databases/{database_id}/collectionGroups/{collection_id}/indexes/{index_id}&#x60; | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 

### Return type

**Object**

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## firestoreProjectsDatabasesCollectionGroupsIndexesGet

> GoogleFirestoreAdminV1beta2Index firestoreProjectsDatabasesCollectionGroupsIndexesGet(name, opts)



Gets a composite index.

### Example

```javascript
import CloudFirestoreApi from 'cloud_firestore_api';
let defaultClient = CloudFirestoreApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CloudFirestoreApi.ProjectsApi();
let name = "name_example"; // String | A name of the form `projects/{project_id}/databases/{database_id}/collectionGroups/{collection_id}/indexes/{index_id}`
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example" // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
};
apiInstance.firestoreProjectsDatabasesCollectionGroupsIndexesGet(name, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **String**| A name of the form &#x60;projects/{project_id}/databases/{database_id}/collectionGroups/{collection_id}/indexes/{index_id}&#x60; | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 

### Return type

[**GoogleFirestoreAdminV1beta2Index**](GoogleFirestoreAdminV1beta2Index.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## firestoreProjectsDatabasesCollectionGroupsIndexesList

> GoogleFirestoreAdminV1beta2ListIndexesResponse firestoreProjectsDatabasesCollectionGroupsIndexesList(parent, opts)



Lists composite indexes.

### Example

```javascript
import CloudFirestoreApi from 'cloud_firestore_api';
let defaultClient = CloudFirestoreApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CloudFirestoreApi.ProjectsApi();
let parent = "parent_example"; // String | A parent name of the form `projects/{project_id}/databases/{database_id}/collectionGroups/{collection_id}`
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'filter': "filter_example", // String | The filter to apply to list results.
  'pageSize': 56, // Number | The number of results to return.
  'pageToken': "pageToken_example" // String | A page token, returned from a previous call to FirestoreAdmin.ListIndexes, that may be used to get the next page of results.
};
apiInstance.firestoreProjectsDatabasesCollectionGroupsIndexesList(parent, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent** | **String**| A parent name of the form &#x60;projects/{project_id}/databases/{database_id}/collectionGroups/{collection_id}&#x60; | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **filter** | **String**| The filter to apply to list results. | [optional] 
 **pageSize** | **Number**| The number of results to return. | [optional] 
 **pageToken** | **String**| A page token, returned from a previous call to FirestoreAdmin.ListIndexes, that may be used to get the next page of results. | [optional] 

### Return type

[**GoogleFirestoreAdminV1beta2ListIndexesResponse**](GoogleFirestoreAdminV1beta2ListIndexesResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## firestoreProjectsDatabasesExportDocuments

> GoogleLongrunningOperation firestoreProjectsDatabasesExportDocuments(name, opts)



Exports a copy of all or a subset of documents from Google Cloud Firestore to another storage system, such as Google Cloud Storage. Recent updates to documents may not be reflected in the export. The export occurs in the background and its progress can be monitored and managed via the Operation resource that is created. The output of an export may only be used once the associated operation is done. If an export operation is cancelled before completion it may leave partial data behind in Google Cloud Storage.

### Example

```javascript
import CloudFirestoreApi from 'cloud_firestore_api';
let defaultClient = CloudFirestoreApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CloudFirestoreApi.ProjectsApi();
let name = "name_example"; // String | Database to export. Should be of the form: `projects/{project_id}/databases/{database_id}`.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'googleFirestoreAdminV1beta2ExportDocumentsRequest': new CloudFirestoreApi.GoogleFirestoreAdminV1beta2ExportDocumentsRequest() // GoogleFirestoreAdminV1beta2ExportDocumentsRequest | 
};
apiInstance.firestoreProjectsDatabasesExportDocuments(name, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **String**| Database to export. Should be of the form: &#x60;projects/{project_id}/databases/{database_id}&#x60;. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **googleFirestoreAdminV1beta2ExportDocumentsRequest** | [**GoogleFirestoreAdminV1beta2ExportDocumentsRequest**](GoogleFirestoreAdminV1beta2ExportDocumentsRequest.md)|  | [optional] 

### Return type

[**GoogleLongrunningOperation**](GoogleLongrunningOperation.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## firestoreProjectsDatabasesImportDocuments

> GoogleLongrunningOperation firestoreProjectsDatabasesImportDocuments(name, opts)



Imports documents into Google Cloud Firestore. Existing documents with the same name are overwritten. The import occurs in the background and its progress can be monitored and managed via the Operation resource that is created. If an ImportDocuments operation is cancelled, it is possible that a subset of the data has already been imported to Cloud Firestore.

### Example

```javascript
import CloudFirestoreApi from 'cloud_firestore_api';
let defaultClient = CloudFirestoreApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CloudFirestoreApi.ProjectsApi();
let name = "name_example"; // String | Database to import into. Should be of the form: `projects/{project_id}/databases/{database_id}`.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'googleFirestoreAdminV1beta2ImportDocumentsRequest': new CloudFirestoreApi.GoogleFirestoreAdminV1beta2ImportDocumentsRequest() // GoogleFirestoreAdminV1beta2ImportDocumentsRequest | 
};
apiInstance.firestoreProjectsDatabasesImportDocuments(name, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **String**| Database to import into. Should be of the form: &#x60;projects/{project_id}/databases/{database_id}&#x60;. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **googleFirestoreAdminV1beta2ImportDocumentsRequest** | [**GoogleFirestoreAdminV1beta2ImportDocumentsRequest**](GoogleFirestoreAdminV1beta2ImportDocumentsRequest.md)|  | [optional] 

### Return type

[**GoogleLongrunningOperation**](GoogleLongrunningOperation.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

