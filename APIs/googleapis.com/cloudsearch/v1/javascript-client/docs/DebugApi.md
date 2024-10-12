# CloudSearchApi.DebugApi

All URIs are relative to *https://cloudsearch.googleapis.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cloudsearchDebugDatasourcesItemsCheckAccess**](DebugApi.md#cloudsearchDebugDatasourcesItemsCheckAccess) | **POST** /v1/debug/{name}:checkAccess | 
[**cloudsearchDebugDatasourcesItemsSearchByViewUrl**](DebugApi.md#cloudsearchDebugDatasourcesItemsSearchByViewUrl) | **POST** /v1/debug/{name}/items:searchByViewUrl | 
[**cloudsearchDebugIdentitysourcesItemsListForunmappedidentity**](DebugApi.md#cloudsearchDebugIdentitysourcesItemsListForunmappedidentity) | **GET** /v1/debug/{parent}/items:forunmappedidentity | 
[**cloudsearchDebugIdentitysourcesUnmappedidsList**](DebugApi.md#cloudsearchDebugIdentitysourcesUnmappedidsList) | **GET** /v1/debug/{parent}/unmappedids | 



## cloudsearchDebugDatasourcesItemsCheckAccess

> CheckAccessResponse cloudsearchDebugDatasourcesItemsCheckAccess(name, opts)



Checks whether an item is accessible by specified principal. Principal must be a user; groups and domain values aren&#39;t supported. **Note:** This API requires an admin account to execute.

### Example

```javascript
import CloudSearchApi from 'cloud_search_api';
let defaultClient = CloudSearchApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CloudSearchApi.DebugApi();
let name = "name_example"; // String | Item name, format: datasources/{source_id}/items/{item_id}
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
  'debugOptionsEnableDebugging': true, // Boolean | If you are asked by Google to help with debugging, set this field. Otherwise, ignore this field.
  'principal': new CloudSearchApi.Principal() // Principal | 
};
apiInstance.cloudsearchDebugDatasourcesItemsCheckAccess(name, opts, (error, data, response) => {
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
 **name** | **String**| Item name, format: datasources/{source_id}/items/{item_id} | 
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
 **debugOptionsEnableDebugging** | **Boolean**| If you are asked by Google to help with debugging, set this field. Otherwise, ignore this field. | [optional] 
 **principal** | [**Principal**](Principal.md)|  | [optional] 

### Return type

[**CheckAccessResponse**](CheckAccessResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## cloudsearchDebugDatasourcesItemsSearchByViewUrl

> SearchItemsByViewUrlResponse cloudsearchDebugDatasourcesItemsSearchByViewUrl(name, opts)



Fetches the item whose viewUrl exactly matches that of the URL provided in the request. **Note:** This API requires an admin account to execute.

### Example

```javascript
import CloudSearchApi from 'cloud_search_api';
let defaultClient = CloudSearchApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CloudSearchApi.DebugApi();
let name = "name_example"; // String | Source name, format: datasources/{source_id}
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
  'searchItemsByViewUrlRequest': new CloudSearchApi.SearchItemsByViewUrlRequest() // SearchItemsByViewUrlRequest | 
};
apiInstance.cloudsearchDebugDatasourcesItemsSearchByViewUrl(name, opts, (error, data, response) => {
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
 **name** | **String**| Source name, format: datasources/{source_id} | 
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
 **searchItemsByViewUrlRequest** | [**SearchItemsByViewUrlRequest**](SearchItemsByViewUrlRequest.md)|  | [optional] 

### Return type

[**SearchItemsByViewUrlResponse**](SearchItemsByViewUrlResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## cloudsearchDebugIdentitysourcesItemsListForunmappedidentity

> ListItemNamesForUnmappedIdentityResponse cloudsearchDebugIdentitysourcesItemsListForunmappedidentity(parent, opts)



Lists names of items associated with an unmapped identity. **Note:** This API requires an admin account to execute.

### Example

```javascript
import CloudSearchApi from 'cloud_search_api';
let defaultClient = CloudSearchApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CloudSearchApi.DebugApi();
let parent = "parent_example"; // String | The name of the identity source, in the following format: identitysources/{source_id}}
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
  'debugOptionsEnableDebugging': true, // Boolean | If you are asked by Google to help with debugging, set this field. Otherwise, ignore this field.
  'groupResourceName': "groupResourceName_example", // String | 
  'pageSize': 56, // Number | Maximum number of items to fetch in a request. Defaults to 100.
  'pageToken': "pageToken_example", // String | The next_page_token value returned from a previous List request, if any.
  'userResourceName': "userResourceName_example" // String | 
};
apiInstance.cloudsearchDebugIdentitysourcesItemsListForunmappedidentity(parent, opts, (error, data, response) => {
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
 **parent** | **String**| The name of the identity source, in the following format: identitysources/{source_id}} | 
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
 **debugOptionsEnableDebugging** | **Boolean**| If you are asked by Google to help with debugging, set this field. Otherwise, ignore this field. | [optional] 
 **groupResourceName** | **String**|  | [optional] 
 **pageSize** | **Number**| Maximum number of items to fetch in a request. Defaults to 100. | [optional] 
 **pageToken** | **String**| The next_page_token value returned from a previous List request, if any. | [optional] 
 **userResourceName** | **String**|  | [optional] 

### Return type

[**ListItemNamesForUnmappedIdentityResponse**](ListItemNamesForUnmappedIdentityResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## cloudsearchDebugIdentitysourcesUnmappedidsList

> ListUnmappedIdentitiesResponse cloudsearchDebugIdentitysourcesUnmappedidsList(parent, opts)



Lists unmapped user identities for an identity source. **Note:** This API requires an admin account to execute.

### Example

```javascript
import CloudSearchApi from 'cloud_search_api';
let defaultClient = CloudSearchApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CloudSearchApi.DebugApi();
let parent = "parent_example"; // String | The name of the identity source, in the following format: identitysources/{source_id}
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
  'debugOptionsEnableDebugging': true, // Boolean | If you are asked by Google to help with debugging, set this field. Otherwise, ignore this field.
  'pageSize': 56, // Number | Maximum number of items to fetch in a request. Defaults to 100.
  'pageToken': "pageToken_example", // String | The next_page_token value returned from a previous List request, if any.
  'resolutionStatusCode': "resolutionStatusCode_example" // String | Limit users selection to this status.
};
apiInstance.cloudsearchDebugIdentitysourcesUnmappedidsList(parent, opts, (error, data, response) => {
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
 **parent** | **String**| The name of the identity source, in the following format: identitysources/{source_id} | 
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
 **debugOptionsEnableDebugging** | **Boolean**| If you are asked by Google to help with debugging, set this field. Otherwise, ignore this field. | [optional] 
 **pageSize** | **Number**| Maximum number of items to fetch in a request. Defaults to 100. | [optional] 
 **pageToken** | **String**| The next_page_token value returned from a previous List request, if any. | [optional] 
 **resolutionStatusCode** | **String**| Limit users selection to this status. | [optional] 

### Return type

[**ListUnmappedIdentitiesResponse**](ListUnmappedIdentitiesResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

