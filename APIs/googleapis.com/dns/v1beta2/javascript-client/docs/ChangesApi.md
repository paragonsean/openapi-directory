# CloudDnsApi.ChangesApi

All URIs are relative to *https://dns.googleapis.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dnsChangesCreate**](ChangesApi.md#dnsChangesCreate) | **POST** /dns/v1beta2/projects/{project}/managedZones/{managedZone}/changes | 
[**dnsChangesGet**](ChangesApi.md#dnsChangesGet) | **GET** /dns/v1beta2/projects/{project}/managedZones/{managedZone}/changes/{changeId} | 
[**dnsChangesList**](ChangesApi.md#dnsChangesList) | **GET** /dns/v1beta2/projects/{project}/managedZones/{managedZone}/changes | 



## dnsChangesCreate

> Change dnsChangesCreate(project, managedZone, opts)



Atomically updates the ResourceRecordSet collection.

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

let apiInstance = new CloudDnsApi.ChangesApi();
let project = "project_example"; // String | Identifies the project addressed by this request.
let managedZone = "managedZone_example"; // String | Identifies the managed zone addressed by this request. Can be the managed zone name or ID.
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
  'clientOperationId': "clientOperationId_example", // String | For mutating operation requests only. An optional identifier specified by the client. Must be unique for operation resources in the Operations collection.
  'change': new CloudDnsApi.Change() // Change | 
};
apiInstance.dnsChangesCreate(project, managedZone, opts, (error, data, response) => {
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
 **managedZone** | **String**| Identifies the managed zone addressed by this request. Can be the managed zone name or ID. | 
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
 **change** | [**Change**](Change.md)|  | [optional] 

### Return type

[**Change**](Change.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## dnsChangesGet

> Change dnsChangesGet(project, managedZone, changeId, opts)



Fetches the representation of an existing Change.

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

let apiInstance = new CloudDnsApi.ChangesApi();
let project = "project_example"; // String | Identifies the project addressed by this request.
let managedZone = "managedZone_example"; // String | Identifies the managed zone addressed by this request. Can be the managed zone name or ID.
let changeId = "changeId_example"; // String | The identifier of the requested change, from a previous ResourceRecordSetsChangeResponse.
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
apiInstance.dnsChangesGet(project, managedZone, changeId, opts, (error, data, response) => {
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
 **managedZone** | **String**| Identifies the managed zone addressed by this request. Can be the managed zone name or ID. | 
 **changeId** | **String**| The identifier of the requested change, from a previous ResourceRecordSetsChangeResponse. | 
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

[**Change**](Change.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## dnsChangesList

> ChangesListResponse dnsChangesList(project, managedZone, opts)



Enumerates Changes to a ResourceRecordSet collection.

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

let apiInstance = new CloudDnsApi.ChangesApi();
let project = "project_example"; // String | Identifies the project addressed by this request.
let managedZone = "managedZone_example"; // String | Identifies the managed zone addressed by this request. Can be the managed zone name or ID.
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
  'sortBy': "sortBy_example", // String | Sorting criterion. The only supported value is change sequence.
  'sortOrder': "sortOrder_example" // String | Sorting order direction: 'ascending' or 'descending'.
};
apiInstance.dnsChangesList(project, managedZone, opts, (error, data, response) => {
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
 **managedZone** | **String**| Identifies the managed zone addressed by this request. Can be the managed zone name or ID. | 
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
 **sortBy** | **String**| Sorting criterion. The only supported value is change sequence. | [optional] 
 **sortOrder** | **String**| Sorting order direction: &#39;ascending&#39; or &#39;descending&#39;. | [optional] 

### Return type

[**ChangesListResponse**](ChangesListResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

