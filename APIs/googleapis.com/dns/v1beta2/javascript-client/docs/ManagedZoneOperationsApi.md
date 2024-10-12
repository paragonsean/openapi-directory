# CloudDnsApi.ManagedZoneOperationsApi

All URIs are relative to *https://dns.googleapis.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dnsManagedZoneOperationsGet**](ManagedZoneOperationsApi.md#dnsManagedZoneOperationsGet) | **GET** /dns/v1beta2/projects/{project}/managedZones/{managedZone}/operations/{operation} | 
[**dnsManagedZoneOperationsList**](ManagedZoneOperationsApi.md#dnsManagedZoneOperationsList) | **GET** /dns/v1beta2/projects/{project}/managedZones/{managedZone}/operations | 



## dnsManagedZoneOperationsGet

> Operation dnsManagedZoneOperationsGet(project, managedZone, operation, opts)



Fetches the representation of an existing Operation.

### Example

```javascript
import CloudDnsApi from 'cloud_dns_api';
let defaultClient = CloudDnsApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CloudDnsApi.ManagedZoneOperationsApi();
let project = "project_example"; // String | Identifies the project addressed by this request.
let managedZone = "managedZone_example"; // String | Identifies the managed zone addressed by this request.
let operation = "operation_example"; // String | Identifies the operation addressed by this request (ID of the operation).
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
  'clientOperationId': "clientOperationId_example" // String | For mutating operation requests only. An optional identifier specified by the client. Must be unique for operation resources in the Operations collection.
};
apiInstance.dnsManagedZoneOperationsGet(project, managedZone, operation, opts, (error, data, response) => {
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
 **project** | **String**| Identifies the project addressed by this request. | 
 **managedZone** | **String**| Identifies the managed zone addressed by this request. | 
 **operation** | **String**| Identifies the operation addressed by this request (ID of the operation). | 
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
 **clientOperationId** | **String**| For mutating operation requests only. An optional identifier specified by the client. Must be unique for operation resources in the Operations collection. | [optional] 

### Return type

[**Operation**](Operation.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## dnsManagedZoneOperationsList

> ManagedZoneOperationsListResponse dnsManagedZoneOperationsList(project, managedZone, opts)



Enumerates Operations for the given ManagedZone.

### Example

```javascript
import CloudDnsApi from 'cloud_dns_api';
let defaultClient = CloudDnsApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CloudDnsApi.ManagedZoneOperationsApi();
let project = "project_example"; // String | Identifies the project addressed by this request.
let managedZone = "managedZone_example"; // String | Identifies the managed zone addressed by this request.
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
  'maxResults': 56, // Number | Optional. Maximum number of results to be returned. If unspecified, the server decides how many results to return.
  'pageToken': "pageToken_example", // String | Optional. A tag returned by a previous list request that was truncated. Use this parameter to continue a previous list request.
  'sortBy': "sortBy_example" // String | Sorting criterion. The only supported values are START_TIME and ID.
};
apiInstance.dnsManagedZoneOperationsList(project, managedZone, opts, (error, data, response) => {
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
 **project** | **String**| Identifies the project addressed by this request. | 
 **managedZone** | **String**| Identifies the managed zone addressed by this request. | 
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
 **maxResults** | **Number**| Optional. Maximum number of results to be returned. If unspecified, the server decides how many results to return. | [optional] 
 **pageToken** | **String**| Optional. A tag returned by a previous list request that was truncated. Use this parameter to continue a previous list request. | [optional] 
 **sortBy** | **String**| Sorting criterion. The only supported values are START_TIME and ID. | [optional] 

### Return type

[**ManagedZoneOperationsListResponse**](ManagedZoneOperationsListResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

