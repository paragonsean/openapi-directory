# CloudResourceManagerApi.FoldersApi

All URIs are relative to *https://cloudresourcemanager.googleapis.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cloudresourcemanagerFoldersCreate**](FoldersApi.md#cloudresourcemanagerFoldersCreate) | **POST** /v3/folders | 
[**cloudresourcemanagerFoldersList**](FoldersApi.md#cloudresourcemanagerFoldersList) | **GET** /v3/folders | 
[**cloudresourcemanagerFoldersSearch**](FoldersApi.md#cloudresourcemanagerFoldersSearch) | **GET** /v3/folders:search | 



## cloudresourcemanagerFoldersCreate

> Operation cloudresourcemanagerFoldersCreate(opts)



Creates a folder in the resource hierarchy. Returns an &#x60;Operation&#x60; which can be used to track the progress of the folder creation workflow. Upon success, the &#x60;Operation.response&#x60; field will be populated with the created Folder. In order to succeed, the addition of this new folder must not violate the folder naming, height, or fanout constraints. + The folder&#39;s &#x60;display_name&#x60; must be distinct from all other folders that share its parent. + The addition of the folder must not cause the active folder hierarchy to exceed a height of 10. Note, the full active + deleted folder hierarchy is allowed to reach a height of 20; this provides additional headroom when moving folders that contain deleted folders. + The addition of the folder must not cause the total number of folders under its parent to exceed 300. If the operation fails due to a folder constraint violation, some errors may be returned by the &#x60;CreateFolder&#x60; request, with status code &#x60;FAILED_PRECONDITION&#x60; and an error description. Other folder constraint violations will be communicated in the &#x60;Operation&#x60;, with the specific &#x60;PreconditionFailure&#x60; returned in the details list in the &#x60;Operation.error&#x60; field. The caller must have &#x60;resourcemanager.folders.create&#x60; permission on the identified parent.

### Example

```javascript
import CloudResourceManagerApi from 'cloud_resource_manager_api';
let defaultClient = CloudResourceManagerApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CloudResourceManagerApi.FoldersApi();
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
  'folder': new CloudResourceManagerApi.Folder() // Folder | 
};
apiInstance.cloudresourcemanagerFoldersCreate(opts, (error, data, response) => {
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
 **folder** | [**Folder**](Folder.md)|  | [optional] 

### Return type

[**Operation**](Operation.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## cloudresourcemanagerFoldersList

> ListFoldersResponse cloudresourcemanagerFoldersList(opts)



Lists the folders that are direct descendants of supplied parent resource. &#x60;list()&#x60; provides a strongly consistent view of the folders underneath the specified parent resource. &#x60;list()&#x60; returns folders sorted based upon the (ascending) lexical ordering of their display_name. The caller must have &#x60;resourcemanager.folders.list&#x60; permission on the identified parent.

### Example

```javascript
import CloudResourceManagerApi from 'cloud_resource_manager_api';
let defaultClient = CloudResourceManagerApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CloudResourceManagerApi.FoldersApi();
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
  'pageSize': 56, // Number | Optional. The maximum number of folders to return in the response. The server can return fewer folders than requested. If unspecified, server picks an appropriate default.
  'pageToken': "pageToken_example", // String | Optional. A pagination token returned from a previous call to `ListFolders` that indicates where this listing should continue from.
  'parent': "parent_example", // String | Required. The name of the parent resource whose folders are being listed. Only children of this parent resource are listed; descendants are not listed. If the parent is a folder, use the value `folders/{folder_id}`. If the parent is an organization, use the value `organizations/{org_id}`. Access to this method is controlled by checking the `resourcemanager.folders.list` permission on the `parent`.
  'showDeleted': true // Boolean | Optional. Controls whether folders in the DELETE_REQUESTED state should be returned. Defaults to false.
};
apiInstance.cloudresourcemanagerFoldersList(opts, (error, data, response) => {
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
 **pageSize** | **Number**| Optional. The maximum number of folders to return in the response. The server can return fewer folders than requested. If unspecified, server picks an appropriate default. | [optional] 
 **pageToken** | **String**| Optional. A pagination token returned from a previous call to &#x60;ListFolders&#x60; that indicates where this listing should continue from. | [optional] 
 **parent** | **String**| Required. The name of the parent resource whose folders are being listed. Only children of this parent resource are listed; descendants are not listed. If the parent is a folder, use the value &#x60;folders/{folder_id}&#x60;. If the parent is an organization, use the value &#x60;organizations/{org_id}&#x60;. Access to this method is controlled by checking the &#x60;resourcemanager.folders.list&#x60; permission on the &#x60;parent&#x60;. | [optional] 
 **showDeleted** | **Boolean**| Optional. Controls whether folders in the DELETE_REQUESTED state should be returned. Defaults to false. | [optional] 

### Return type

[**ListFoldersResponse**](ListFoldersResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## cloudresourcemanagerFoldersSearch

> SearchFoldersResponse cloudresourcemanagerFoldersSearch(opts)



Search for folders that match specific filter criteria. &#x60;search()&#x60; provides an eventually consistent view of the folders a user has access to which meet the specified filter criteria. This will only return folders on which the caller has the permission &#x60;resourcemanager.folders.get&#x60;.

### Example

```javascript
import CloudResourceManagerApi from 'cloud_resource_manager_api';
let defaultClient = CloudResourceManagerApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CloudResourceManagerApi.FoldersApi();
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
  'pageSize': 56, // Number | Optional. The maximum number of folders to return in the response. The server can return fewer folders than requested. If unspecified, server picks an appropriate default.
  'pageToken': "pageToken_example", // String | Optional. A pagination token returned from a previous call to `SearchFolders` that indicates from where search should continue.
  'query': "query_example" // String | Optional. Search criteria used to select the folders to return. If no search criteria is specified then all accessible folders will be returned. Query expressions can be used to restrict results based upon displayName, state and parent, where the operators `=` (`:`) `NOT`, `AND` and `OR` can be used along with the suffix wildcard symbol `*`. The `displayName` field in a query expression should use escaped quotes for values that include whitespace to prevent unexpected behavior. ``` | Field | Description | |-------------------------|----------------------------------------| | displayName | Filters by displayName. | | parent | Filters by parent (for example: folders/123). | | state, lifecycleState | Filters by state. | ``` Some example queries are: * Query `displayName=Test*` returns Folder resources whose display name starts with \"Test\". * Query `state=ACTIVE` returns Folder resources with `state` set to `ACTIVE`. * Query `parent=folders/123` returns Folder resources that have `folders/123` as a parent resource. * Query `parent=folders/123 AND state=ACTIVE` returns active Folder resources that have `folders/123` as a parent resource. * Query `displayName=\\\\\"Test String\\\\\"` returns Folder resources with display names that include both \"Test\" and \"String\".
};
apiInstance.cloudresourcemanagerFoldersSearch(opts, (error, data, response) => {
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
 **pageSize** | **Number**| Optional. The maximum number of folders to return in the response. The server can return fewer folders than requested. If unspecified, server picks an appropriate default. | [optional] 
 **pageToken** | **String**| Optional. A pagination token returned from a previous call to &#x60;SearchFolders&#x60; that indicates from where search should continue. | [optional] 
 **query** | **String**| Optional. Search criteria used to select the folders to return. If no search criteria is specified then all accessible folders will be returned. Query expressions can be used to restrict results based upon displayName, state and parent, where the operators &#x60;&#x3D;&#x60; (&#x60;:&#x60;) &#x60;NOT&#x60;, &#x60;AND&#x60; and &#x60;OR&#x60; can be used along with the suffix wildcard symbol &#x60;*&#x60;. The &#x60;displayName&#x60; field in a query expression should use escaped quotes for values that include whitespace to prevent unexpected behavior. &#x60;&#x60;&#x60; | Field | Description | |-------------------------|----------------------------------------| | displayName | Filters by displayName. | | parent | Filters by parent (for example: folders/123). | | state, lifecycleState | Filters by state. | &#x60;&#x60;&#x60; Some example queries are: * Query &#x60;displayName&#x3D;Test*&#x60; returns Folder resources whose display name starts with \&quot;Test\&quot;. * Query &#x60;state&#x3D;ACTIVE&#x60; returns Folder resources with &#x60;state&#x60; set to &#x60;ACTIVE&#x60;. * Query &#x60;parent&#x3D;folders/123&#x60; returns Folder resources that have &#x60;folders/123&#x60; as a parent resource. * Query &#x60;parent&#x3D;folders/123 AND state&#x3D;ACTIVE&#x60; returns active Folder resources that have &#x60;folders/123&#x60; as a parent resource. * Query &#x60;displayName&#x3D;\\\\\&quot;Test String\\\\\&quot;&#x60; returns Folder resources with display names that include both \&quot;Test\&quot; and \&quot;String\&quot;. | [optional] 

### Return type

[**SearchFoldersResponse**](SearchFoldersResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

